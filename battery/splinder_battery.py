from abc import ABC
from datetime import date, datetime

from abstract_classes import Battery


class SplinderBattery(Battery, ABC):
    """Used to create an instance of the Splinder battery"""

    def needs_service(self, current_date: date = datetime.now().date()):
        return self.last_service_date.year + 2 <= current_date.year
