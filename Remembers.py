import atexit
from typing import Dict, Tuple


class RememberDumper:
    """
    This class for dump virtual data, to real base.
    """

    def save(self, data: Dict):
        """
        Save information in .txt database, like date_time: "something does"
        """
        pass

    def get(self) -> Dict | None:
        """
        Get dictionary from a database, with my remembers
        """
        pass


class AssistantRemembers:
    """
    This class for working with virtual data
    """

    def __init__(self):
        self.data = RememberDumper().get() or {}
        atexit.register(self.exiting)

    def add(self, date_time, text: str):
        """
        adding remembers in my virtual database

        :param date_time: time when should tell me
        :param text: data for remember
        """
        self.data[date_time] = text

    def get(self, date_time) -> Tuple:
        """
        Get tuple: (key, remember)
        :param date_time: this is an object of date time
        """
        return date_time, self.data[date_time]

    def exiting(self):
        """
        Dump data in database
        """

        RememberDumper().save(self.data)