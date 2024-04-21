from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType


def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    add_entities([
        TemperatureSensor("Main Floor Temperature", 71),
        TemperatureSensor("Basement Temperature", 69),
        TemperatureSensor("Office Temperature", 76),
        TemperatureSensor("Guest Bedroom Temperature", 72),
        TemperatureSensor("Master Bedroom Temperature", 75),
        TemperatureSensor("Upstairs Bathroom Temperature", 74),
    ])


class TemperatureSensor(SensorEntity):
    def __init__(self, name: str, temperature: int) -> None:
        self._attr_name = name
        self._attr_native_unit_of_measurement = UnitOfTemperature.FAHRENHEIT
        self._attr_device_class = SensorDeviceClass.TEMPERATURE
        self._attr_state_class = SensorStateClass.MEASUREMENT
        self._attr_native_value = temperature