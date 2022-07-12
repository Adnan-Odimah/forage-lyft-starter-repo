from abc import ABC
from datetime import datetime

from abstract_classes import Battery


class NubbinBattery(Battery, ABC):
    """Used to create an instance of the Nubbin battery"""

    def needs_service(self):
        return self.last_service_date.year + 4 <= datetime.now().date().year
