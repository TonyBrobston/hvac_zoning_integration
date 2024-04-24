from homeassistant.helpers.area_registry import AreaEntry
from homeassistant.helpers.entity_registry import RegistryEntry

from homeassistant.components.hvac_zoning.config_flow import map_to_id_and_name

def test_map_to_dict_of_name_and_id():
    area_entries = [AreaEntry(name='Living Room', normalized_name='livingroom', aliases=set(), floor_id=None, icon=None,
                           id='living_room', labels=set(), picture=None),
                 AreaEntry(name='Kitchen', normalized_name='kitchen', aliases=set(), floor_id=None, icon=None,
                           id='kitchen', labels=set(), picture=None),
                 AreaEntry(name='Master Bedroom', normalized_name='masterbedroom', aliases=set(), floor_id=None,
                           icon=None, id='bedroom', labels=set(), picture=None),
                 AreaEntry(name='Basement', normalized_name='basement', aliases=set(), floor_id=None, icon=None,
                           id='basement', labels=set(), picture=None),
                 AreaEntry(name='Guest Bedroom', normalized_name='guestbedroom', aliases=set(), floor_id=None,
                           icon=None, id='guest_bedroom', labels=set(), picture=None),
                 AreaEntry(name='Office', normalized_name='office', aliases=set(), floor_id=None, icon=None,
                           id='office', labels=set(), picture=None),
                 AreaEntry(name='Upstairs Bathroom', normalized_name='upstairsbathroom', aliases=set(), floor_id=None,
                           icon=None, id='upstairs_bathroom', labels=set(), picture=None)]

    expected_area_entry_dict = {
        'living_room': 'Living Room',
        'kitchen': 'Kitchen',
        'bedroom': 'Master Bedroom',
        'basement': 'Basement',
        'guest_bedroom': 'Guest Bedroom',
        'office': 'Office',
        'upstairs_bathroom': 'Upstairs Bathroom'
    }

    area_entry_dict = map_to_id_and_name(area_entries)

    assert area_entry_dict == expected_area_entry_dict

def test_map_foo():
    original_device_class = 'damper'
    registry_entries = [RegistryEntry(entity_id='sensor.basement_temperature', unique_id='Basement Temperature', platform='hvac_stubs', previous_unique_id=None, aliases=set(), area_id='basement', categories={}, capabilities={'state_class': 'measurement'}, config_entry_id=None, device_class=None, device_id=None, disabled_by=None, entity_category=None, hidden_by=None, icon=None, id='fcdf8c625327e2bd610ac6b4335ca438', has_entity_name=False, labels=set(), name=None, options={'conversation': {'should_expose': True}, 'sensor': {'display_precision': None}}, original_device_class='temperature', original_icon=None, original_name='Basement Temperature', supported_features=0, translation_key=None, unit_of_measurement='°F'), RegistryEntry(entity_id='cover.basement_west_vent', unique_id='Basement West Vent', platform='hvac_stubs', previous_unique_id=None, aliases=set(), area_id='basement', categories={}, capabilities=None, config_entry_id=None, device_class=None, device_id=None, disabled_by=None, entity_category=None, hidden_by=None, icon=None, id='800d6dcc0aef4b6a42476de9ff1403ad', has_entity_name=False, labels=set(), name=None, options={'conversation': {'should_expose': True}}, original_device_class='damper', original_icon=None, original_name='Basement West Vent', supported_features=15, translation_key=None, unit_of_measurement=None), RegistryEntry(entity_id='cover.basement_northeast_vent', unique_id='Basement Northeast Vent', platform='hvac_stubs', previous_unique_id=None, aliases=set(), area_id='basement', categories={}, capabilities=None, config_entry_id=None, device_class=None, device_id=None, disabled_by=None, entity_category=None, hidden_by=None, icon=None, id='0ae78e2e8f74045281a8ed154cd2b06d', has_entity_name=False, labels=set(), name=None, options={'conversation': {'should_expose': True}}, original_device_class='damper', original_icon=None, original_name='Basement Northeast Vent', supported_features=15, translation_key=None, unit_of_measurement=None), RegistryEntry(entity_id='cover.basement_southeast_vent', unique_id='Basement Southeast Vent', platform='hvac_stubs', previous_unique_id=None, aliases=set(), area_id='basement', categories={}, capabilities=None, config_entry_id=None, device_class=None, device_id=None, disabled_by=None, entity_category=None, hidden_by=None, icon=None, id='16d81f78e8b7917950f984277ba4feff', has_entity_name=False, labels=set(), name=None, options={'conversation': {'should_expose': True}}, original_device_class='damper', original_icon=None, original_name='Basement Southeast Vent', supported_features=15, translation_key=None, unit_of_measurement=None)]

    expected_dict = {
        '800d6dcc0aef4b6a42476de9ff1403ad': 'Basement West Vent',
        '0ae78e2e8f74045281a8ed154cd2b06d': 'Basement Northeast Vent',
        '16d81f78e8b7917950f984277ba4feff': 'Basement Southeast Vent'
    }

    registry_dict = {entry.id: entry.original_name for entry in registry_entries if entry.original_device_class == original_device_class}

    assert registry_dict == expected_dict
