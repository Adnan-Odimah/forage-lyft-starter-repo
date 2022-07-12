from datetime import datetime

from abstract_classes import Battery, Engine
from battery import NubbinBattery, SplinderBattery
from car import Car
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine


class CarFactory:
    """
    Car Factory Class

    I have assumed that all engines and batteries are new (because they have just been created in the factory)
    """

    def create_calliope(self) -> Car:
        """Creates a Calliope car

        Returns:
            Car instance with the Capulet Engine and Splidner Battery
        """
        engine: Engine = CapuletEngine(last_service_milage=0, current_milage=0)
        battery: Battery = SplinderBattery(last_service_date=datetime.now().date())

        return Car(engine=engine, battery=battery)

    def create_glissade(self) -> Car:
        """Creates a Glissade Car

        Returns:
            Car instance wth the Willoughby Engine and Splinder Battery
        """
        engine: Engine = WilloughbyEngine(last_service_milage=0, current_milage=0)
        battery: Battery = SplinderBattery(last_service_date=datetime.now().date())

        return Car(engine=engine, battery=battery)

    def create_palindrome(self) -> Car:
        """Creates the Palindrome Car

        Returns:
            Car instance with the Sternman Engine and Splinder Battery
        """
        engine: Engine = SternmanEngine(warning_light_is_on=False)
        battery: Battery = SplinderBattery(last_service_date=datetime.now().date())

        return Car(engine=engine, battery=battery)

    def create_rorschach(self) -> Car:
        """Creates the Rorschach car

        Returns:
            Car instance with the Willoughby Engine and Nubbing Battery
        """
        engine: Engine = WilloughbyEngine(last_service_milage=0, current_milage=0)
        battery: Battery = NubbinBattery(last_service_date=datetime.now().date())

        return Car(engine=engine, battery=battery)

    def create_thovex(self) -> Car:
        """Creates the Thovex car

        Returns:
            Car instance with the Capulet Engine and Nubbin Battery
        """
        engine: Engine = CapuletEngine(last_service_milage=0, current_milage=0)
        battery: Battery = NubbinBattery(last_service_date=datetime.now().date())

        return Car(engine=engine, battery=battery)
