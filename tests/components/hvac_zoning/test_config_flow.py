from homeassistant.helpers.area_registry import AreaEntry
from homeassistant.helpers.entity_registry import RegistryEntry

from homeassistant.components.hvac_zoning.config_flow import map_area_entries_to_id_and_name, filter_to_device_class_and_map_registry_entries_to_id_and_name

def test_map_area_entries_to_id_and_name():
    area_entries = [
        AreaEntry(
            id='living_room',
            name='Living Room',
            normalized_name='livingroom',
            aliases=set(),
            floor_id=None,
            icon=None,
            picture=None
        ),
        AreaEntry(
            id='kitchen',
            name='Kitchen',
            normalized_name='kitchen',
            aliases=set(),
            floor_id=None,
            icon=None,
            picture=None
        ),
        AreaEntry(
            id='bedroom',
            name='Master Bedroom',
            normalized_name='masterbedroom',
            aliases=set(),
            floor_id=None,
            icon=None,
            picture=None
        ),
        AreaEntry(
            id='basement',
            name='Basement',
            normalized_name='basement',
            aliases=set(),
            floor_id=None,
            icon=None,
            picture=None
        ),
        AreaEntry(
            id='guest_bedroom',
            name='Guest Bedroom',
            normalized_name='guestbedroom',
            aliases=set(),
            floor_id=None,
            icon=None,
            picture=None
        ),
        AreaEntry(
            id='office',
            name='Office',
            normalized_name='office',
            aliases=set(),
            floor_id=None,
            icon=None,
            picture=None
        ),
        AreaEntry(
            id='upstairs_bathroom',
            name='Upstairs Bathroom',
            normalized_name='upstairsbathroom',
            aliases=set(),
            floor_id=None,
            icon=None,
            picture=None
        )
    ]

    expected_area_entry_dict = {
        'living_room': 'Living Room',
        'kitchen': 'Kitchen',
        'bedroom': 'Master Bedroom',
        'basement': 'Basement',
        'guest_bedroom': 'Guest Bedroom',
        'office': 'Office',
        'upstairs_bathroom': 'Upstairs Bathroom'
    }

    area_entry_dict = map_area_entries_to_id_and_name(area_entries)

    assert area_entry_dict == expected_area_entry_dict

def test_filter_to_device_class_and_map_registry_entries_to_id_and_name():
    device_class = 'damper'
    registry_entries = [
        RegistryEntry(
            entity_id='sensor.basement_temperature',
            unique_id='Basement Temperature',
            platform='hvac_stubs',
            id='fcdf8c625327e2bd610ac6b4335ca438',
            original_name='Basement Temperature',
            original_device_class='temperature'
        ),
        RegistryEntry(
            entity_id='cover.basement_west_vent',
            unique_id='Basement West Vent',
            platform='hvac_stubs',
            id='800d6dcc0aef4b6a42476de9ff1403ad',
            original_name='Basement West Vent',
            original_device_class='damper'
        ),
        RegistryEntry(
            entity_id='cover.basement_northeast_vent',
            unique_id='Basement Northeast Vent',
            platform='hvac_stubs',
            id='0ae78e2e8f74045281a8ed154cd2b06d',
            original_name='Basement Northeast Vent',
            original_device_class='damper'
        ),
        RegistryEntry(
            entity_id='cover.basement_southeast_vent',
            unique_id='Basement Southeast Vent',
            platform='hvac_stubs',
            id='16d81f78e8b7917950f984277ba4feff',
            original_name='Basement Southeast Vent',
            original_device_class='damper'
        )
    ]

    expected_dict = {
        '800d6dcc0aef4b6a42476de9ff1403ad': 'Basement West Vent',
        '0ae78e2e8f74045281a8ed154cd2b06d': 'Basement Northeast Vent',
        '16d81f78e8b7917950f984277ba4feff': 'Basement Southeast Vent'
    }

    registry_dict = filter_to_device_class_and_map_registry_entries_to_id_and_name(
        registry_entries, device_class
    )

    assert registry_dict == expected_dict
