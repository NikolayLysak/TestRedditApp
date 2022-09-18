import configparser
import os


class ConfigReader:
    def __init__(self, path=None):
        self.config = configparser.ConfigParser()
        if path is None:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.cfg")
        self.config.read(path)

    def get_desired_caps(self) -> dict[str, str]:
        desired_caps = {
            "platformName": self.config.get("Android", "platformName"),
            "platformVersion": self.config.get("Android", "platformVersion"),
            "udid": self.config.get("Android", "udid"),
            "deviceName": self.config.get("Android", "deviceName"),
            "app": self.get_app_path()
        }
        return desired_caps

    @staticmethod
    def get_app_path() -> str:
        if "tests" in f'{os.popen("pwd").read()}':
            return f'{os.popen("pwd").read().rstrip()}/../../app/Reddit.apk'
        else:
            return f'{os.popen("pwd").read().rstrip()}/app/Reddit.apk'

    def get_url(self) -> str:
        return self.config.get("Android", "url")
