import telebot
import requests
from telebot import types
#--------------------------------------------------------------------------
TOKEN = input("[•]Ingresa El Token: ")
#-------------------------------------------------------------------------
bot = telebot.TeleBot(TOKEN)
#------------------------------------------------------------------------#
#    • Telegram:                                                      #
#                                                                              #
# • Canal : @BoxPrey                                           #
#                                                                             #
# • By : @PreBoyx                                                #
#----------------------------------------------------------------------#

def obtener_info_ip(ip):
    
    info_ipinfo = requests.get(
        f'https://ipinfo.io/{ip}/json',
        headers={'User-Agent': 'Mozilla/5.0'}
    ).json()

  
    info_ip_api = requests.get(
        f'http://ip-api.com/json/{ip}',
        headers={'User-Agent': 'Mozilla/5.0'}
    ).json()

   
    info_ipapi = requests.get(
        f'https://ipapi.co/{ip}/json/',
        headers={'User-Agent': 'Mozilla/5.0'}
    ).json()

   
    info = {
        'ip': ip,
        'city': info_ipinfo.get('city', info_ip_api.get('city', info_ipapi.get('city'))),
        'region': info_ipinfo.get('region', info_ip_api.get('region', info_ipapi.get('region'))),
        'country': info_ipinfo.get('country', info_ip_api.get('country', info_ipapi.get('country'))),
        'org': info_ipinfo.get('org', info_ip_api.get('org', info_ipapi.get('org'))),
        'timezone': info_ipinfo.get('timezone', info_ip_api.get('timezone', info_ipapi.get('timezone'))),
        'lat': info_ipinfo.get('loc', info_ip_api.get('lat', info_ipapi.get('latitude'))),
        'lon': info_ipinfo.get('loc', info_ip_api.get('lon', info_ipapi.get('longitude'))),
        'asn': info_ipinfo.get('org', info_ip_api.get('as', info_ipapi.get('asn'))), 
        'isp': info_ipinfo.get('org', info_ip_api.get('isp', info_ipapi.get('isp'))), 
        'postal': info_ipinfo.get('postal', info_ip_api.get('zip', info_ipapi.get('postal'))), 
        'proxy': info_ip_api.get('proxy'), 
        'vpn': info_ip_api.get('vpn'), 
        
    }

    return info

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button_creador = types.InlineKeyboardButton("𝗣𝗿𝗲𝗕𝗼𝘆𝘅 • 👨‍💻", url="https://t.me/preboyx") 
    button_canal = types.InlineKeyboardButton(" 𝗖𝗮𝗻𝗮𝗹 • 🪐", url="https://t.me/BoxPrey") 
    markup.add(button_creador, button_canal)
    photo_url = 'https://telegra.ph/file/9530e9c427fffd1c5b507.jpg' 
    bot.send_photo(message.chat.id, photo=photo_url, caption='''


¡𝐇𝐨𝐥𝐚! 🗺️ ¿𝐍𝐞𝐜𝐞𝐬𝐢𝐭𝐚𝐬 𝐬𝐚𝐛𝐞𝐫 𝐝𝐨́𝐧𝐝𝐞 𝐬𝐞 𝐞𝐧𝐜𝐮𝐞𝐧𝐭𝐫𝐚 𝐮𝐧𝐚 𝐝𝐢𝐫𝐞𝐜𝐜𝐢𝐨́𝐧 𝐈𝐏?

𝐄𝐬𝐭𝐞 𝐛𝐨𝐭 𝐭𝐞 𝐚𝐲𝐮𝐝𝐚 𝐚 𝐠𝐞𝐨𝐥𝐨𝐜𝐚𝐥𝐢𝐳𝐚𝐫 𝐈𝐏𝐬 𝐲 𝐨𝐛𝐭𝐞𝐧𝐞𝐫 𝐢𝐧𝐟𝐨𝐫𝐦𝐚𝐜𝐢𝐨́𝐧 𝐝𝐞𝐭𝐚𝐥𝐥𝐚𝐝𝐚, ¡𝐢𝐧𝐜𝐥𝐮𝐬𝐨 𝐥𝐚𝐬 𝐜𝐨𝐨𝐫𝐝𝐞𝐧𝐚𝐝𝐚𝐬 𝐆𝐏𝐒!

𝐔𝐬𝐨 /𝐢𝐩 𝐲 𝐥𝐚 𝐢𝐩

''', reply_markup=markup)

@bot.message_handler(commands=['ip'])
def ip_handler(message):
    try:
        
        ip = message.text.split()[1]
        info = obtener_info_ip(ip)

       
        bot.send_location(message.chat.id, latitude=info['lat'], longitude=info['lon'])

        
        info_str = f"""
         ⌬ 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝗰𝗶𝗼́𝗻 𝗱𝗲 𝗹𝗮 𝗜𝗣:
         	
‣ 𝗜𝗣: {info['ip']}
‣ 𝗖𝗶𝘂𝗱𝗮𝗱:  {info['city']}
‣ 𝗥𝗲𝗴𝗶𝗼‌𝗻:  {info['region']}
‣ 𝗣𝗮𝗶‌𝘀:  {info['country']}
‣ 𝗢𝗿𝗴𝗮𝗻𝗶𝘇𝗮𝗰𝗶𝗼‌𝗻:  {info['org']}
‣ 𝗭𝗼𝗻𝗮 𝗛𝗼𝗿𝗮𝗿𝗶𝗮:  {info['timezone']}
‣ 𝗡𝘂‌𝗺𝗲𝗿𝗼 𝗱𝗲 𝗨𝗯𝗶𝗰𝗮𝗰𝗶𝗼‌𝗻:  {info['lat']},{info['lon']}
‣ 𝗔𝗦𝗡:  {info['asn']}
‣ 𝗣𝗿𝗼𝘃𝗲𝗲𝗱𝗼𝗿 𝗱𝗲 𝗜𝗻𝘁𝗲𝗿𝗻𝗲𝘁: {info['isp']}
‣ 𝗖𝗼‌𝗱𝗶𝗴𝗼 𝗣𝗼𝘀𝘁𝗮𝗹:  {info['postal']}
‣ 𝗣𝗿𝗼𝘅𝘆:  {info['proxy']}
‣ 𝗩𝗣𝗡: {info['vpn']}
        """       
        markup = types.InlineKeyboardMarkup()
        button_github = types.InlineKeyboardButton("𝗚𝗶𝘁𝗛𝘂𝗯 • 🌑", url="https://github.com/preboyx") 
        button_info = types.InlineKeyboardButton("𝗪𝗲𝗯 • 🌕", url="https://preboyx.github.io/Web")
        markup.add(button_github, button_info)

        bot.send_message(message.chat.id, info_str, reply_markup=markup)

    except IndexError:
        bot.send_message(message.chat.id, "💢𝗣𝗼𝗿 𝗳𝗮𝘃𝗼𝗿, 𝗶𝗻𝗴𝗿𝗲𝘀𝗮 𝘂𝗻𝗮 𝗜𝗣 𝘃𝗮́𝗹𝗶𝗱𝗮. 𝗘𝗷𝗲𝗺𝗽𝗹𝗼: /𝗶𝗽 𝟴.𝟴.𝟴.𝟴")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_message(message.chat.id, "🪄𝗨𝘁𝗶𝗹𝗶𝘇𝗮 𝗲𝗹 𝗰𝗼𝗺𝗮𝗻𝗱𝗼 /𝗶𝗽 𝗽𝗮𝗿𝗮 𝗯𝘂𝘀𝗰𝗮𝗿 𝗶𝗻𝗳𝗼𝗿𝗺𝗮𝗰𝗶𝗼́𝗻 𝘀𝗼𝗯𝗿𝗲 𝘂𝗻𝗮 𝗜𝗣.")
bot.infinity_polling()
