import discord
import os
from dotenv import load_dotenv
from flask import Flask
from threading import Thread

app = Flask(__name__)

app = Flask('')

@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=True)

def keep_alive():
    t = Thread(target=run)
    t.start()
    print("Bot is still running!")


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    print("❌ ERROR: No token found. Make sure it's in the .env file!")
    exit()

intents = discord.Intents.default()  # No 'message_content' in v1.7.3
bot = discord.Client(intents=intents)


item_data = {
         "Boxer": {"speed": 160, "price": 55000, "duped_value": 0, "demand_status": "Low"},
    "Challenger": {"speed": 170, "price": 59000, "duped_value": 0, "demand_status": "Low"},
    "Camper": {"speed": 140, "price": 79000, "duped_value": 0, "demand_status": "Low"},
    "Tow truck": {"speed": 130, "price": 80000, "duped_value": 0, "demand_status": "Low"},
    "Pickup": {"speed": 130, "price": 9000, "duped_value": 0, "demand_status": "Low"},
    "Deja": {"speed": 145, "price": 10000, "duped_value": 0, "demand_status": "Low"},
    "Model-3": {"speed": 145, "price": 16000, "duped_value": 0, "demand_status": "Low"},
    "Ray": {"speed": 150, "price": 25000, "duped_value": 0, "demand_status": "Low"},
    "Interrogator": {"speed": 160, "price": 30000, "duped_value": 0, "demand_status": "Low"},
    "Dirt bike": {"speed": 115, "price": 35000, "duped_value": 0, "demand_status": "Low"},
    "Patrol bike": {"speed": 145, "price": 45000, "duped_value": 0, "demand_status": "Low"},
    "Dune buggy": {"speed": 130, "price": 45000, "duped_value": 0, "demand_status": "Low"},
    "Badger": {"speed": 145, "price": 45000, "duped_value": 0, "demand_status": "Low"},
    "Jetski": {"speed": 400, "price": 45000, "duped_value": 0, "demand_status": "Low"},
    "ATV": {"speed": 100, "price": 50000, "duped_value": 0, "demand_status": "Low"},
  "Tanker": {"speed": 215, "price": 80000, "duped_value": 0, "demand_status": "Low"},
  "Ambulance": {"speed": 160, "price": 90000, "duped_value": 0, "demand_status": "Low"},
  "Shell mark-5": {"speed": 190, "price": 92000, "duped_value": 0, "demand_status": "Low"},
  "Lamatador": {"speed": 180, "price": 100000, "duped_value": 0, "demand_status": "Low"},
  "Fiasco": {"speed": 130, "price": 100000, "duped_value": 0, "demand_status": "Low"},
  "Escape bot": {"speed": 100, "price": 100000, "duped_value": 0, "demand_status": "Low"},
  "Cyber truck": {"speed": 160, "price": 100000, "duped_value": 0, "demand_status": "Low"},
  "Surus": {"speed": 180, "price": 109000, "duped_value": 0, "demand_status": "Low"},
  "Prison bus": {"speed": 175, "price": 150000, "duped_value": 0, "demand_status": "Low"},
  "Falcon-s": {"speed": 180, "price": 150000, "duped_value": 0, "demand_status": "Low"},
  "Firetruck": {"speed": 215, "price": 175000, "duped_value": 0, "demand_status": "Low"},
  "Delorean": {"speed": 190, "price": 175000, "duped_value": 0, "demand_status": "Low"},
  "Little-bird": {"speed": 110, "price": 190000, "duped_value": 0, "demand_status": "Low"},
  "Ray-9": {"speed": 215, "price": 199000, "duped_value": 0, "demand_status": "Low"},
  "Stallion": {"speed": 250 , "price": 200000, "duped_value": 0, "demand_status": "Low"},
    "Stallion": {"speed": 250 , "price": 200000, "duped_value": 0, "demand_status": "Low"},
"Shell-classic": {"speed": 185, "price": 1500000, "duped_value": 1250000, "demand_status": "Below average"},
"Manta": {"speed": 230, "price": 1500000, "duped_value": 1250000, "demand_status": "Below average"},
"Longhorn": {"speed": 190, "price": 1500000, "duped_value": 1250000, "demand_status": "Below average"},
"Jackrabbit": {"speed": 170, "price": 1750000, "duped_value": 1500000, "demand_status": "Average"},
"Iceborn": {"speed": 330, "price": 2000000, "duped_value": 1500000, "demand_status": "Average"},
"Bloxy": {"speed": 205, "price": 2000000, "duped_value": 1500000, "demand_status": "Below Average"},
"Airtail": {"speed": 250, "price": 2000000, "duped_value": 1500000, "demand_status": "Average"},
"Poseidon": {"speed": 235, "price": 2000000, "duped_value": 1750000, "demand_status": "Below Average"},
"Concept": {"speed": 315, "price": 2500000, "duped_value": 0, "demand_status": "Below Average"},
"Tinytoy": {"speed": 130, "price": 2500000, "duped_value": 2000000, "demand_status": "Above Average"},
"Agent": {"speed": 200, "price": 2500000, "duped_value": 2000000, "demand_status": "Average"},
"Wedge": {"speed": 300, "price": 3000000, "duped_value": 2500000, "demand_status": "Average"},
"Snake": {"speed": 240, "price": 3000000, "duped_value": 2500000, "demand_status": "Average"}
}
    
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
     
    item_name = message.content.title()
    if item_name in item_data:
        item = item_data[item_name]
        response = (f"**{item_name}** -\n"
                    f"🏎 **Top Speed:** {item['speed']} km/h\n"
                    f"💰 **Price:** ${item['price']}\n"
                    f"📉 **Duped Value:** ${item['duped_value']}\n"
                    f"📈 **Demand Status:** {item['demand_status']}")
        await message.channel.send(response)
        await bot.process_commands(message)
keep_alive()
bot.run(TOKEN)
