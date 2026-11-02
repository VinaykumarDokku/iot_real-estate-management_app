"""Validate property IoT sensor readings and generate alerts."""

from dataclasses import dataclass


@dataclass
class SensorReading:
    property_id: str
    temperature: float
    humidity: float
    battery_level: float


def check_sensor(reading: SensorReading) -> list[str]:
    """Return alerts for abnormal sensor readings."""
    alerts = []

    if not reading.property_id.strip():
        raise ValueError("Property ID is required")

    if not 0 <= reading.humidity <= 100:
        raise ValueError("Humidity must be between 0 and 100")

    if not 0 <= reading.battery_level <= 100:
        raise ValueError("Battery level must be between 0 and 100")

    if reading.temperature > 35:
        alerts.append("High temperature detected")

    if reading.temperature < 5:
        alerts.append("Low temperature detected")

    if reading.humidity > 70:
        alerts.append("High humidity detected")

    if reading.battery_level < 20:
        alerts.append("Low sensor battery")

    return alerts


if __name__ == "__main__":
    reading = SensorReading(
        property_id="PROPERTY-101",
        temperature=38.5,
        humidity=75.0,
        battery_level=15.0,
    )

    alerts = check_sensor(reading)

    print(f"Property: {reading.property_id}")

    if alerts:
        for alert in alerts:
            print(f"ALERT: {alert}")
    else:
        print("All sensor readings are normal")
