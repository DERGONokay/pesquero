import threading
import time
import pyautogui
import logging
import datetime
from PIL import ImageGrab


def init_logging():
    logging.basicConfig(
        filename="C:/dergon-studios/pesquero/logs/fish-" + str(
            datetime.datetime.today().strftime('%Y%m%d%H%M%S')) + ".log",
        encoding="utf-8",
        level=logging.DEBUG
    )


class Fish(threading.Thread):

    should_fish: bool
    key: str

    def __init__(self):
        super().__init__()
        init_logging()

    def run(self):
        logging.debug("Starting to fish")
        self.should_fish = True
        self.press_fish_key()
        while self.should_fish:
            logging.debug("Waiting for the fish to bite...")
            self.wait(0.5)
            frame = ImageGrab.grab()
            pixel = frame.getpixel((960, 480))
            if pixel[0] > 200:
                logging.debug("GOT CHA! Pulling...")
                self.press_fish_key()
                self.wait(7)
                logging.debug("Throwing the bite")
                self.press_fish_key()

    def wait(self, seconds: float):
        if self.should_fish:
            logging.debug("Waiting " + str(seconds) + "s")
            time.sleep(seconds)

    def press_fish_key(self):
        if self.should_fish:
            logging.debug("Pressing '" + self.key + "' key")
            pyautogui.press(self.key)

    def stop(self):
        logging.debug("Stopping...")
        self.should_fish = False
