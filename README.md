# hvac_zoning_integration

This project is in the experimentation phase. I'm slowly learning to write a Home Assistant Intergration (https://developers.home-assistant.io/docs/creating_component_index), but I have only a few hours of experience.

## The goal of this project
The idea is to take this POC I wrote and write it as a Home Assistant Integration. https://github.com/BrobstonCreations/mqtt-hvac-vent-control
- Click + ADD INTEGRATION and search for HVAC Zoning Integration.
- Display a config modal with all rooms that have a temperature sensor, smart vent, or thermostat with checkboxes next to each, defaulted to checked, one number field for default target temperature, and a submit button at the bottom.
- On submit, create one thermostat per room, begin monitoring temperatures, controlling vents, and control the central thermostat.


## TODO:
- Update `hvac_stubs` to create areas and add entities to areas (climate, cover, sensor).
- Figure out how to import a def from `hvac_stubs` into `tests/components/hvac_stubs`.
- Build config flow views for sensor selection, cover selection, and climate selection.
- Figure out how to store selections to be used later.