import pymysql


# # # config bot
# # WEBHOOK_PORT = 5002
# # TELEGRAM_TOKEN ='1217952102:AAHiIKy8gXqS-1ypbPxRamOadGDdBOxyQxY'
# # WEBHOOK_URL = 'https://2cd0e0e20b39.ngrok.io'
# # TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url={}/message'.format(TELEGRAM_TOKEN,
#                                                                                               WEBHOOK_URL)

WEBHOOK_PORT = 5002
TELEGRAM_TOKEN ='1438436987:AAG5n5E1h9sXKeoT7zrbcWOBO__dkvuqfCg'
WEBHOOK_URL = 'https://376675d57d7f.ngrok.io'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url={}/message'.format(TELEGRAM_TOKEN,
                                                                                              WEBHOOK_URL)


# config database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="covidbotdb",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

if connection.open:
    print("the connection is opened")
