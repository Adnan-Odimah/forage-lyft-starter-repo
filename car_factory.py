from datetime import date, datetime

from abstract_classes import Battery, Engine
from battery import NubbinBattery, SplinderBattery
from car import Car
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine


class CarFactory:
    """
    Car Factory Class

    I have assumed that all engines and batteries are new (because they have just been created in the factory) unless a specified value has been entered
    """

    def create_calliope(
        self,
        last_service_date: date = datetime.now().date(),
        last_service_mileage: int = 0,
    ) -> Car:
        """Creates a Calliope car

        Returns:
            Car instance with the Capulet Engine and Splidner Battery
        """
        engine: Engine = CapuletEngine(
            last_service_mileage=last_service_mileage, current_mileage=0
        )
        battery: Battery = SplinderBattery(last_service_date=last_service_date)

        return Car(engine=engine, battery=battery)

    def create_glissade(
        self,
        last_service_mileage: int = 0,
        last_service_date: date = datetime.now().date(),
    ) -> Car:
        """Creates a Glissade Car

        Returns:
            Car instance wth the Willoughby Engine and Splinder Battery
        """
        engine: Engine = WilloughbyEngine(
            last_service_mileage=last_service_mileage, current_mileage=0
        )
        battery: Battery = SplinderBattery(last_service_date=last_service_date)

        return Car(engine=engine, battery=battery)

    def create_palindrome(self, last_service_date: date = datetime.now().date()) -> Car:
        """Creates the Palindrome Car

        Returns:
            Car instance with the Sternman Engine and Splinder Battery
        """
        engine: Engine = SternmanEngine(warning_light_is_on=False)
        battery: Battery = SplinderBattery(last_service_date=last_service_date)

        return Car(engine=engine, battery=battery)

    def create_rorschach(
        self,
        last_service_mileage: int = 0,
        last_service_date: date = datetime.now().date(),
    ) -> Car:
        """Creates the Rorschach car

        Returns:
            Car instance with the Willoughby Engine and Nubbing Battery
        """
        engine: Engine = WilloughbyEngine(
            last_service_mileage=last_service_mileage, current_mileage=0
        )
        battery: Battery = NubbinBattery(last_service_date=last_service_date)

        return Car(engine=engine, battery=battery)

    def create_thovex(
        self,
        last_service_mileage: int = 0,
        last_service_date: date = datetime.now().date(),
    ) -> Car:
        """Creates the Thovex car

        Returns:
            Car instance with the Capulet Engine and Nubbin Battery
        """
        engine: Engine = CapuletEngine(
            last_service_mileage=last_service_mileage, current_mileage=0
        )
        battery: Battery = NubbinBattery(last_service_date=last_service_date)

        return Car(engine=engine, battery=battery)
