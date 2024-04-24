"""Config flow for HVAC Zoning integration."""

from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
# from homeassistant.const import CONF_HOST, CONF_PASSWORD, CONF_USERNAME
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers.area_registry import AreaRegistry
from homeassistant.helpers.entity_registry import EntityRegistry, async_entries_for_area

import json

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

# TODO adjust the data schema to the data that you need
STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required("living_room_thermostat", default=True): bool,
        vol.Required("living_room_temperature", default=True): bool,
        vol.Required("living_room_northeast_vent", default=True): bool,
        vol.Required("living_room_northeast_vent", default=True): bool,
        vol.Required("kitchen_south_vent", default=True): bool,
        vol.Required("kitchen_northwest_vent", default=True): bool,
        # vol.Required("basement_west_vent", default=True): bool,
        # vol.Required("basement_northeast_vent", default=True): bool,
        # vol.Required("basement_southeast_vent", default=True): bool,
        # vol.Required("basement_temperature", default=True): bool,
        # vol.Required("office_vent", default=True): bool,
        # vol.Required("office_temperature", default=True): bool,
        # vol.Required("guest_bedroom_vent", default=True): bool,
        # vol.Required("guest_bedroom_temperature", default=True): bool,
        # vol.Required("master_bedroom_vent", default=True): bool,
        # vol.Required("master_bedroom_temperature", default=True): bool,
        # vol.Required("upstairs_bathroom_vent", default=True): bool,
        # vol.Required("upstairs_bathroom_temperature", default=True): bool,
    }
)


class PlaceholderHub:
    """Placeholder class to make tests pass.

    TODO Remove this placeholder class and replace with things from your PyPI package.
    """

    def __init__(self, host: str) -> None:
        """Initialize."""
        self.host = host

    async def authenticate(self, username: str, password: str) -> bool:
        """Test if we can authenticate with the host."""
        return True


async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
    """Validate the user input allows us to connect.

    Data has the keys from STEP_USER_DATA_SCHEMA with values provided by the user.
    """
    # TODO validate the data can be used to set up a connection.

    # If your PyPI package is not built with async, pass your methods
    # to the executor:
    # await hass.async_add_executor_job(
    #     your_validate_func, data[CONF_USERNAME], data[CONF_PASSWORD]
    # )

    # hub = PlaceholderHub(data[CONF_HOST])
    #
    # if not await hub.authenticate(data[CONF_USERNAME], data[CONF_PASSWORD]):
    #     raise InvalidAuth

    # If you cannot connect:
    # throw CannotConnect
    # If the authentication is wrong:
    # InvalidAuth

    # Return info that you want to store in the config entry.
    return {"title": "Name of the device"}


class ConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for HVAC Zoning."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        areaRegistry = AreaRegistry(self.hass)
        await areaRegistry.async_load()
        areas = list(areaRegistry.async_list_areas())
        _LOGGER.info(f"FOO1: {areas}");
        print(f"FOO1: {areas}");
        entityRegistry = EntityRegistry(self.hass)
        await entityRegistry.async_load()
        living_room_entities = async_entries_for_area(entityRegistry, "basement")
        _LOGGER.info(f"FOO2: {living_room_entities}");
        print(f"FOO2: {living_room_entities}");
        errors: dict[str, str] = {}
        if user_input is not None:
            try:
                info = await validate_input(self.hass, user_input)
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except InvalidAuth:
                errors["base"] = "invalid_auth"
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
            else:
                return self.async_create_entry(title=info["title"], data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=STEP_USER_DATA_SCHEMA, errors=errors
        )


class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""


class InvalidAuth(HomeAssistantError):
    """Error to indicate there is invalid auth."""

def map_area_entries_to_id_and_name(area_entries):
    return {entry.id: entry.name for entry in area_entries}

def filter_to_device_class_and_map_registry_entries_to_id_and_name(
        registry_entries, device_class
):
    return {
        entry.id: entry.original_name
        for entry in registry_entries
        if entry.original_device_class == device_class
    }
