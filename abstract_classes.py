from abc import ABC, abstractmethod
from datetime import date


class Engine(ABC):
    """
    Abstract class for the engines.
    """

    @abstractmethod
    def needs_service(self):
        """Checks if the engine needs service

        Returns:
            bool: true for yes, false for no
        """


class Battery(ABC):
    """
    Abstract class for the batteries.
    """

    def __init__(self, last_service_date: date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        """Checks if the battery needs service

        Returns:
            bool: true for yes, false for no
        """
