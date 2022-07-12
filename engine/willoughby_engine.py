from abc import ABC

from abstract_classes import Engine


class WilloughbyEngine(Engine, ABC):
    """Creates an instance of the Willoughby Engine"""

    def __init__(self, last_service_milage: int, current_milage: int):
        self.last_service_milage: int = last_service_milage
        self.current_milage: int = current_milage

    def needs_service(self) -> bool:
        return self.current_milage >= self.last_service_milage + 60000
