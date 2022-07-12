from abc import ABC

from abstract_classes import Engine


class WilloughbyEngine(Engine, ABC):
    """Creates an instance of the Willoughby Engine"""

    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage: int = last_service_mileage
        self.current_mileage: int = current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage >= self.last_service_mileage + 60000

    def set_mileage(self, current_mileage: int) -> None:
        """Sets the current Mileage of the car"""
        self.current_mileage = current_mileage
