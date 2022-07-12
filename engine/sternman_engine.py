from abc import ABC

from abstract_classes import Engine


class SternmanEngine(Engine, ABC):
    """Creates an instance of the Sternman Engine"""

    def __init__(self, warning_light_is_on: bool):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        return self.warning_light_is_on
