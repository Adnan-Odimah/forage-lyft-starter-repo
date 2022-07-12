from abstract_classes import Battery, Engine, Tires


class Car:
    """
    General Car class
    """

    def __init__(self, engine: Engine, battery: Battery, tires: Tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self) -> bool:
        """Checks if the car needs service"""
        return (
            self.engine.needs_service()
            or self.battery.needs_service()
            or self.tires.needs_service()
        )

    def set_engine(self, engine: Engine) -> None:
        """Sets the engine of the car

        Args:
            engine (Engine): The new engine that will be added to the car
        """
        self.engine = engine

    def set_battery(self, battery: Battery) -> None:
        """Sets the battery of the car

        Args:
            battery (Battery): The new battery that will be added to the car
        """
        self.battery = battery

    def set_tires(self, tires: Tires) -> None:
        """Sets the tires of the car

        Args:
            tires (Tires): the new tires that will be added to the car
        """
        self.tires = tires
