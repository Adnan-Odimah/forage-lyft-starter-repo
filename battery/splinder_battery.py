from abc import ABC
from datetime import datetime

from abstract_classes import Battery


class SplinderBattery(Battery, ABC):
    """Used to create an instance of the Splinder battery"""

    def needs_service(self):
        return self.last_service_date.year + 2 <= datetime.now().date().year
