from hugchat import hugchat
from hugchat.login import Login
from ..config import settings


def init_hugchat():
    # Log in to huggingface and grant authorization to huggingchat
    sign = Login(settings.hugchat_email, settings.hugchat_pwd)
    cookies = sign.login()

    # Save cookies to the local directory
    cookie_path_dir = str(settings.cookie_path)+"/"
    sign.saveCookiesToDir(cookie_path_dir)

    # Create a ChatBot
    chatbot = hugchat.ChatBot(
        cookies=cookies.get_dict()
    )  # or cookie_path="usercookies/<email>.json"
    settings.chatbot = chatbot


def call_api(value: str) -> str:
    chatbot: hugchat.ChatBot = settings.chatbot
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    resp = chatbot.chat(value)
    chatbot.delete_conversation(id)
    return resp
