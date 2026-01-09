from pycraft import Client
import time
import threading

SERVER = "Mega_Martin.aternos.me"
PORT = 25565
USERNAME = "Martin-AFK-BOT"
PASSWORD = "chatgpt.chadgpt"

def run_bot():
    client = Client()

    def on_join():
        print("Bot joined")

        def login_and_afk():
            time.sleep(3)
            client.chat(f"/register {PASSWORD}")
            client.chat(f"/login {PASSWORD}")

            while True:
                time.sleep(60)
                client.chat(" ")

        threading.Thread(target=login_and_afk).start()

    def on_disconnect(reason):
        print("Disconnected:", reason)
        time.sleep(5)
        run_bot()

    client.on_join = on_join
    client.on_disconnect = on_disconnect

    client.connect(
        SERVER,
        PORT,
        USERNAME,
        auth=False  # cracked server
    )

run_bot()

