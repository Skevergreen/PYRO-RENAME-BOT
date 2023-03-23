import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "7184257")

API_HASH = os.environ.get("API_HASH", "00db684ac4ab37587f5395581ae3a9c8")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5398153171:AAGz21acZSwOs-rLoSKy2n4RG0-Ii_jFB5I") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Oxyver") 

DB_NAME = os.environ.get("DB_NAME","rename789")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Unlimited:Unlimited@cluster0.hrtvz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/41aec9a65ae32979a9453.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1412758888').split()]

PORT = os.environ.get('PORT', '8080')

WEBHOOK = bool(os.environ.get("WEBHOOK", True))
