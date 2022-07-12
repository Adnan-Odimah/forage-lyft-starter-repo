import unittest
from datetime import datetime

from battery import NubbinBattery, SplinderBattery
from car_factory import CarFactory
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from tire import CarriganTires, OctoprimeTires


class TestCarFactory(unittest.TestCase):
    """Tests the creation of cars using the Car Factory"""

    factory = CarFactory()

    def test_create_calliope(self):
        """Tests the creation of a Calliope"""
        car = self.factory.create_calliope()
        self.assertTrue(
            (
                isinstance(car.engine, CapuletEngine)
                and isinstance(car.battery, SplinderBattery)
            )
        )

    def test_create_glissade(self):
        """Tests the creation of a Glissade"""
        car = self.factory.create_glissade()
        self.assertTrue(
            (
                isinstance(car.engine, WilloughbyEngine)
                and isinstance(car.battery, SplinderBattery)
            )
        )

    def test_create_palindrome(self):
        """Tests the creation of a Palindrome"""
        car = self.factory.create_palindrome()
        self.assertTrue(
            (
                isinstance(car.engine, SternmanEngine)
                and isinstance(car.battery, SplinderBattery)
            )
        )

    def test_create_rorschach(self):
        """Tests the creation of a Rorschach"""
        car = self.factory.create_rorschach()
        self.assertTrue(
            (
                isinstance(car.engine, WilloughbyEngine)
                and isinstance(car.battery, NubbinBattery)
            )
        )

    def test_create_thovex(self):
        """Tests the creation of a Thovex"""
        car = self.factory.create_thovex()
        self.assertTrue(
            (
                isinstance(car.engine, CapuletEngine)
                and isinstance(car.battery, NubbinBattery)
            )
        )


class TestCalliope(unittest.TestCase):
    """Tests different cases for the Calliope car"""

    def test_battery_should_be_serviced(self):
        """Checks to see that it returns true when more than 3 years have passed (for car battery)"""
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 4)
        car = CarFactory().create_calliope(last_service_date=last_service_date)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        """Checks to see that it false when less than 3 years have passed (for car battery)"""
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 2)
        car = CarFactory().create_calliope(last_service_date=last_service_date)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        """Checks to see that it returns true when more than 30,000 miles have passed (for car engine)"""
        last_service_mileage = 0
        current_mileage = 30001
        car = CarFactory().create_calliope(last_service_mileage=last_service_mileage)
        car.engine.set_mileage(current_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        """Checks to see that it returns false when less than 30,000 miles have passed (for car engine)"""
        last_service_mileage = 0
        current_mileage = 29999
        car = CarFactory().create_calliope(last_service_mileage=last_service_mileage)
        car.engine.set_mileage(current_mileage)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    """Tests different cases for the Glissade car"""

    def test_battery_should_be_serviced(self):
        """Checks to see that it returns true when more than 3 years have passed (for car battery)"""
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 4)
        car = CarFactory().create_glissade(last_service_date=last_service_date)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        """Checks to see that it false true when less than 3 years have passed (for car battery)"""
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 2)
        car = CarFactory().create_glissade(last_service_date=last_service_date)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        """Checks to see that it returns true when more than 60,000 miles have passed (for car engine)"""
        last_service_mileage = 0
        current_mileage = 60001
        car = CarFactory().create_glissade(last_service_mileage=last_service_mileage)
        car.engine.set_mileage(current_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        """Checks to see that it returns false when less than 60,000 miles have passed (for car engine)"""
        last_service_mileage = 0
        current_mileage = 59999
        car = CarFactory().create_glissade(last_service_mileage=last_service_mileage)
        car.engine.set_mileage(current_mileage)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    """Tests different cases for the Palindrome car"""

    def test_battery_should_be_serviced(self):
        """Checks to see that it returns true when more than 3 years have passed (for car battery)"""
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 4)
        car = CarFactory().create_palindrome(last_service_date=last_service_date)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        """Checks to see that it false true when less than 3 years have passed (for car battery)"""
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 2)
        car = CarFactory().create_palindrome(last_service_date=last_service_date)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        """Checks to see that it returns true when the warning light is on (for car engine)"""
        car = CarFactory().create_palindrome()
        car.engine.set_light(True)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        """Checks to see that it returns false when the warning light is off (for car engine)"""
        car = CarFactory().create_palindrome()
        car.engine.set_light(False)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    """Tests different cases for the Rorschach car"""

    def test_battery_should_be_serviced(self):
        """Checks to see that it returns true when more than 4 years have passed (for car battery)"""
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 5)
        car = CarFactory().create_rorschach(last_service_date=last_service_date)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        """Checks to see that it false true when less than 4 years have passed (for car battery)"""
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 3)
        car = CarFactory().create_rorschach(last_service_date=last_service_date)
        self.assertFalse(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        """Checks to see that it returns true when more than 60,000 miles have passed (for car engine)"""
        last_service_mileage = 0
        current_mileage = 60001
        car = CarFactory().create_rorschach(last_service_mileage=last_service_mileage)
        car.engine.set_mileage(current_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        """Checks to see that it returns false when less than 60,000 miles have passed (for car engine)"""
        last_service_mileage = 0
        current_mileage = 59999
        car = CarFactory().create_rorschach(last_service_mileage=last_service_mileage)
        car.engine.set_mileage(current_mileage)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    """Tests different cases for the Thovex car"""

    def test_battery_should_be_serviced(self):
        """Checks to see that it returns true when more than 4 years have passed (for car battery)"""
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 5)
        car = CarFactory().create_thovex(last_service_date=last_service_date)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        """Checks to see that it false true when less than 4 years have passed (for car battery)"""
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 3)
        car = CarFactory().create_thovex(last_service_date=last_service_date)
        self.assertFalse(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        """Checks to see that it returns true when more than 30,000 miles have passed (for car engine)"""
        last_service_mileage = 0
        current_mileage = 30001
        car = CarFactory().create_thovex(last_service_mileage=last_service_mileage)
        car.engine.set_mileage(current_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        """Checks to see that it returns false when less than 30,000 miles have passed (for car engine)"""
        last_service_mileage = 0
        current_mileage = 29999
        car = CarFactory().create_thovex(last_service_mileage=last_service_mileage)
        car.engine.set_mileage(current_mileage)
        self.assertFalse(car.needs_service())


class TestTires(unittest.TestCase):
    """Checks that tire service checks work properly"""

    def test_carrigan_tires_should_be_serviced(self):
        """Checks to see that it returns true when the tires need to be serviced (for Carrigan Tires)"""
        tires = CarriganTires([0.9, 0.4, 0.5, 0.2])
        car = CarFactory().create_calliope(tires=tires)
        self.assertTrue(car.needs_service())

    def test_carrigan_tires_should_not_be_serviced(self):
        """Checks to see that it returns false when the tires do not need to be serviced (for Carrigan Tires)"""
        tires = CarriganTires([0.7, 0.8, 0.8, 0.2])
        car = CarFactory().create_calliope(tires=tires)
        self.assertFalse(car.needs_service())

    def test_octoprime_tires_should_be_serviced(self):
        """Checks to see that it returns true when the tires need to be serviced (for Octoprime Tires)"""
        tires = OctoprimeTires([0.9, 0.8, 0.8, 0.9])
        car = CarFactory().create_calliope(tires=tires)
        self.assertTrue(car.needs_service())

    def test_octoprime_tires_should_not_be_serviced(self):
        """Checks to see that it returns false when the tires do not need to be serviced (for Octoprime Tires)"""
        tires = OctoprimeTires([0.8, 0.8, 0.8, 0.5])
        car = CarFactory().create_calliope(tires=tires)
        self.assertFalse(car.needs_service())


class TestCarEdit(unittest.TestCase):
    """Tests that modifying the car works fine"""

    def test_change_engine(self):
        """Checks if the engine change works"""
        car = CarFactory().create_calliope()
        car.set_engine(SternmanEngine(False))
        self.assertIsInstance(car.engine, SternmanEngine)

    def test_change_battery(self):
        """Checks if the battery change works"""
        car = CarFactory().create_calliope()
        car.set_battery(NubbinBattery(datetime.now().date()))
        self.assertIsInstance(car.battery, NubbinBattery)

    def test_change_tires(self):
        """Checks if the tire change works"""
        car = (
            CarFactory().create_calliope()
        )  # Default tires are octoprime with [0, 0, 0, 0]
        newTires = CarriganTires([0.5, 0.2, 0.1, 0.5])
        car.set_tires(newTires)
        self.assertIsInstance(car.tires, CarriganTires)


if __name__ == "__main__":
    unittest.main()
