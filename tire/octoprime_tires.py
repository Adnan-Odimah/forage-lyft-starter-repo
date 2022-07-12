from abc import ABC

from abstract_classes import Tires


class OctoprimeTires(Tires, ABC):
    """Class to initiate Carrigan Tires"""

    def needs_service(self) -> bool:
        """Checks if the sum of the wear list is greater than or equal to 3"""
        return sum(self.tire_list) >= 3.0
