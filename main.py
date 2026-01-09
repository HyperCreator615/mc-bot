from minecraft.networking.connection import Connection
from minecraft.networking.packets import clientbound, serverbound
import time
import threading

SERVER = "Mega_Martin.aternos.me"
PORT = 25565
USERNAME = "Martin-AFK-BOT"
PASSWORD = "chatgpt.chadgpt"

def start_bot():
    print("Starting bot...")
    connection = Connection(
        SERVER,
        PORT,
        username=USERNAME,
        auth_token=None  # cracked server
    )

    @connection.listener(clientbound.play.JoinGamePacket)
    def on_join_game(packet):
        print("Bot joined the server")

        def login_and_afk():
            time.sleep(3)
            connection.write_packet(
                serverbound.play.ChatPacket(f"/register {PASSWORD}")
            )
            connection.write_packet(
                serverbound.play.ChatPacket(f"/login {PASSWORD}")
            )

            # anti-AFK loop
            while True:
                time.sleep(60)
                connection.write_packet(
                    serverbound.play.ChatPacket("/jump")
                )

        threading.Thread(target=login_and_afk).start()

    @connection.listener(clientbound.login.DisconnectPacket)
    def on_disconnect(packet):
        print("Disconnected, reconnecting in 5s...")
        time.sleep(5)
        start_bot()

    connection.connect()

start_bot()
