from abc import ABC

from abstract_classes import Tires


class CarriganTires(Tires, ABC):
    """Class to initiate Carrigan Tires"""

    def needs_service(self) -> bool:
        """Checks if the maximum wear tire is greater than or equal to 0.9"""
        return max(self.tire_list) >= 0.9
