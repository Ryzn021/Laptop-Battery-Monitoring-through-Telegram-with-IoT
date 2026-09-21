import psutil 
import requests
import time

token = "PLACE_TOKEN_BOT_HERE"
chat_id = "YOUR_CHAT_ID"

def telegram_send(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)

print("Battery Monitoring is Succesfully Activated!")

#Main Loop
while True:
    try:
        battery = psutil.sensors_battery()
        
        if battery:
            if battery.percent >= 80 and battery.power_plugged:
                telegram_send(f"⚠️ The battery is {battery.percent}%. Unplug the charger immediately!")
                # Sleep fot 5 min. You dont want to get distracted by non-stop notification, do you?
                time.sleep(5)
        time.sleep(60)# updates every 60 seconds
    except:
        time.sleep(60)