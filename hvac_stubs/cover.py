from __future__ import annotations

from homeassistant.components.cover import (
    CoverDeviceClass,
    CoverEntity,
)
from homeassistant.const import (
    STATE_CLOSED,
    STATE_OPEN,
)
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
        Cover("Living Room Northeast Vent", STATE_CLOSED),
        Cover("Living Room Northeast Vent", STATE_OPEN),
        Cover("Kitchen South Vent", STATE_OPEN),
        Cover("Kitchen Northwest Vent", STATE_CLOSED),
        Cover("Basement West Vent", STATE_CLOSED),
        Cover("Basement Northeast Vent", STATE_CLOSED),
        Cover("Basement Southeast Vent", STATE_CLOSED),
        Cover("Office Vent", STATE_OPEN),
        Cover("Guest Bedroom Vent", STATE_CLOSED),
        Cover("Master Bedroom Vent", STATE_OPEN),
        Cover("Upstairs Bathroom Vent", STATE_OPEN),
    ])


class Cover(CoverEntity):
    def __init__(self, name: str, current_cover_position: str) -> None:
        self._attr_unique_id = name
        self._attr_name = name
        self._attr_device_class = CoverDeviceClass.DAMPER
        self._attr_current_cover_position = current_cover_position
        self._attr_is_closed = current_cover_position == STATE_CLOSED