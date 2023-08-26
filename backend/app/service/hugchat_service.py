from ..hugchat.api import call_api


class HugChatSevice:
    def call_api_hugchat(self, value: str) -> str:
        return call_api(value)
