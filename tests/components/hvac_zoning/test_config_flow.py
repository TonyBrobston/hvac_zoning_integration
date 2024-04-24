

def test_map_to_dict_of_name_and_id():
    areas_entries = dict_values([AreaEntry(name='Living Room', normalized_name='livingroom', aliases=set(), floor_id=None, icon=None,
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
                 AreaEntry(name='Upstaris Bathroom', normalized_name='upstarisbathroom', aliases=set(), floor_id=None,
                           icon=None, id='upstaris_bathroom', labels=set(), picture=None)])

    expected_dict = {
        'Living Room': 'living_room',
        'Kitchen': 'kitchen',
        # ... (add the rest of the expected key-value pairs)
    }

    area_dict = {}
    for entry in area_entries:
        area_dict[entry.name] = entry.id

    assert area_dict == expected_dict
