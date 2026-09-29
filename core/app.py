from ai.client import AIClient
from ai.server import AIServer
from ai.prompt import build_system_prompt

from core.config import Config
from core.database import Database
from core.logger import get_logger


class SavierApp:

    def __init__(self):

        self.config = Config()

        self.db = Database()

        self.logger = get_logger("Savier")

        self.client = None

        self.server = None

    def initialize(self):

        self.logger.info("Initializing Savier...")

        print("Savier initialized.")

    def run(self):

        self.initialize()

        while True:

            text = input("You > ")

            if text.lower() in (
                "exit",
                "quit"
            ):

                break

            print("AI >", text)
