# Methods

## /get
### Description:
Retrieve all information about user. Register user if his id does not exist in the database.

Returns amount of user\`s money in each currency, number of new transactions and whether user is new in app.
### In:
- `id`: *int* - VK id of the user
### Out:
- `balances`: *dict* - amount of currencies. Get by currency name
    - `vkcoin`: *float* - amount of vkcoin 
    - ...
- `newTransactions`: *int* - number of unseen transactions
- `isNew`: *bool* - whether user is new in Maddle


## /settings
### Description:
Get all settings of a user.
### In:
- `id`: *int* - id of user, which settings you want to get
### Out:
- `settings`: *Settings* - settings 


## /save_settings
### Description:
Save settings to a certain section.
### In:
- `id`: *int* - VK id of the user
- `...`: *SettingsSection* - one of the parts of settings structure


## /remittance
### Description:
Returns a configured url to payment and fixes in the database pending transaction.
### In:
- `sender`: *int* - id of a sender
- `destination`: *int* - id of an addressee
- `amount`: *float* - amount of money
- `currency`: *str* - being transfered currency
- `message`: *str* - sender\`s comment
### Out:
- `url`: *str* - payment url


## /friends
### Description:
Returns list of all friends of a user updated by their balances.
### In:
- `id`: *int* - VK id of the user
- `currency`: *str* - name of currency
### Out:
- `friends`: *list* - list of user friends
    - `id`: *int* - id of a friend
    - `firstName`: *str* - first name of a user
    - `lastName`: *str* - last name of a user
    - `photo`: *str* - url of user's photo
    - `money`: *float* - amount of money that a friend has
    

## /history
### Description:
Get history of all transactions related to given user. Transactions are from user, to user and interaction with bank. In addition, returns information about related users.

Also, you can specify count and offset or filter by currency.  

If `amount` is negative and `destination` is 0, transaction means withdrawal.

Reset to zero counter of unseen transactions.
### In:
- `id`: *int* - VK id of the user
- `size` [optional] = 20: *int* - number of transactions
- `skip` [optional] = 0: *int* - number of transactions to skip (offset)
- `currency` [optional]: *str* - filter by currency
### Out:
- `transactions`: *list* - transaction history
    - `sender`: *int* - user that send money
    - `destination`: *int* - user that got money. 0 means bank account
    - `time`: *int* - time when the transaction was committed
    - `currency`: *str* - currency of transfered money
    - `amount`: *float* - amount of transferred money
    - `message`: *str* - sender\`s comment
- `users`: *dict* - users mentioned in transactions. Get by id
    - `360092594`: *dict* - a user
        - `firstName`: *str* - first name of a user
        - `lastName`: *str* - last name of a user
        - `photo`: *str* - url of user's photo
    - ...


## /favourites
### Description:
Get list of saved favourite users.
### In:
- `id`: *int* - VK id of the user
### Out:
- `favourites`: *list* - list of favourite users
    - `id`: *int* - id of a user
    - `firstName`: *str* - first name of a user
    - `lastName`: *str* - last name of a user
    - `photo`: *str* - url of user's photo


## /save_favourites
### Description:
Save given ids to favourites. You can save up to 10 user ids. They can be retrieved with `/favourites` method.
### In:
- `id`: *int* - VK id of the user
- `favourites`: *int[]* - list of ids to be saved in favourites


## /bank
### Description:
If `amount` is positive, it will return a payment url and wait for incoming transaction from user.

If `amount` is negative, it will send `-amount` money to user. If user has on account less money than requested, it will send as much as user has.

If `amount` is zero, API will return the current amount of currency on an account.
### In:
- `id`: *int* - VK id of the bank account owner
- `amount`: *int* | *float* - amount of currency user wants to withdraw / deposit
- `currency`: *str* - name of currency to work with
### Out:
- `data`: *str* | *int* | *float* - payment url or current amount or amount of withdrawn money.



# Structures
Dicts of dicts

## Settings

- `notifications`: *SettingSection*
    - `transactions`: *bool*
    - `market_news`: *bool*
    - `requests`: *bool*
    - `mailing`: *bool*
- `general`: *SettingSection*
    - `reset_filters`: *bool*
    - `confirmation`: *bool*
