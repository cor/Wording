from database import *


db_manager = DatabaseManager()

# Create users
db_manager.create_user('cor', 'cor@pruijs.nl', True, 'Hunter2')
db_manager.create_user('leon', 'leon@grasmeijer.nl', False, 'all_i_see_is_*****')
db_manager.create_user('philip', 'philip@debruijn.nl', False, '***hunter***')

# Create lists
db_manager.create_list('cor', 'duitse_woorden', 'NL_nl', 'DE_de')
db_manager.create_list('cor', 'engelse_woorden', 'NL_nl', 'EN_en')

db_manager.create_list('leon', 'latijn_woorden', 'NL_nl', 'LAT_ijn')

# Create translations
db_manager.create_translation('cor', 'engelse_woorden', 'auto', 'car')
db_manager.create_translation('cor', 'engelse_woorden', 'boom', 'tree')
db_manager.create_translation('cor', 'engelse_woorden', 'moeder', 'mother')
db_manager.create_translation('cor', 'engelse_woorden', 'vader', 'father')
db_manager.create_translation('cor', 'engelse_woorden', 'broer', 'bro')
db_manager.create_translation('cor', 'engelse_woorden', 'muis', 'mouse')
db_manager.create_translation('cor', 'engelse_woorden', 'toetsenbord', 'keyboard')

db_manager.create_translation('cor', 'duitse_woorden', 'auto', 'das Auto')
db_manager.create_translation('cor', 'duitse_woorden', 'kamp', 'kampf')
db_manager.create_translation('cor', 'duitse_woorden', 'geodriehoek', 'geometrie dreieick')

db_manager.create_translation('leon', 'latijn_woorden', 'rust', 'requiescat')
db_manager.create_translation('leon', 'latijn_woorden', 'in', 'im')
db_manager.create_translation('leon', 'latijn_woorden', 'vrede', 'pace')


# Get a list of all usernames
print(db_manager.get_username_list())

# Check if a username exists
print(db_manager.username_exists('cor'))  # True
print(db_manager.username_exists('henk')) # False


# Get user info by name
print(db_manager.get_user('cor'))
print(db_manager.get_user('leon'))
print(db_manager.get_user('philip'))

# Trying to get user info of a user that doesn't exist returns an error
db_manager.get_user('henk')

# Get allt he lists for a user
print(db_manager.get_lists_for_user('cor'))

print(db_manager.get_list('cor', 'engelse_woorden'))

print(db_manager.get_translations_for_list('cor', 'engelse_woorden'))


