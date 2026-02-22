from _secrets import user_aliases
from telegram.ext import CallbackContext
import logging
import random
import redis_db
import re

logger = logging.getLogger(__name__)

# Don't include apostrophe
PUNCTUATION_REGEX = re.compile(r'[\s{}]+'.format(re.escape(r'!"#$%&()*+, -./:;<=>?@[\]^_`{|}~')))


def parse_userid(username: str, context: CallbackContext):
    username = username.strip()
    shuffled_alias_keys = list(user_aliases.keys())
    random.shuffle(shuffled_alias_keys)
    for alias_key in shuffled_alias_keys:
        for alias in user_aliases[alias_key]:
            if (alias.lower() == username.lower()):
                return alias_key
    
    if(username == context.bot.username or username == f"@{context.bot.username}"):
        return context.bot.id

    return redis_db.reverse_lookup_id(username)
