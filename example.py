from applyrecursive import ApplyRecursive
from random import randint
from re import match
import json

OVERWRITE_FUNCTION = "__function"
SKIP_FIELD = "__skip"
SKIP_PATTERN = "^skip.*"
TRIGGER_MODIFICATION = "__modify"

def function_to_apply(*args, **kwargs):
    """
    Pass this function to the ApplyRecursive class to run it on data when triggered
    """

    data = kwargs.get('data')
    key = kwargs.get('key')
    skip_pattern = kwargs.get(SKIP_FIELD)
    overwrite_fn = kwargs.get(OVERWRITE_FUNCTION)

    if overwrite_fn:
        return overwrite_fn(*args, **kwargs)

    if skip_pattern and match(skip_pattern, data):
        return f'SKIPPED >> {data}'
    else:
        return f'MOD >> {randint(111,999)} >> {data} ({key})'

def overwrite_function(*args, **kwargs):
    """
    Sample function used when the `OVERWRITE_FUNCTION` field is present in `map`
    """

    data = kwargs.get('data')
    skip_pattern = kwargs.get(SKIP_FIELD)

    if skip_pattern and match(skip_pattern, data):
        return f'SKIPPED >> {data}'
    else:
        return 'OVERWRITE!!!!'

if __name__ == "__main__":
    
    # Sample data

    data = {
        'id': 'x1234',
        'deep_list': [{
            'list_to_modify': ['1', '2', '3'],
            'another_list': [{
                'modify_this_field': 'test',
                'other_field': 200,
                'skippable_field': 'hello!',
                'function_overwrite_field': 'skip.no overwrite'
            }, {
                'modify_this_field': 'test part 2',
                'other_field': 699,
                'skippable_field': 'skip.hello!',
                'function_overwrite_field': '2000'
            }]
        }]
    }

    # Sample map
    # Matches the structure of data
    
    data_map = {
        'user': {TRIGGER_MODIFICATION: True},
        'deep_list': [{
            'list_to_modify': {TRIGGER_MODIFICATION: True},
            'another_list': [{
                'modify_this_field': {TRIGGER_MODIFICATION: True, SKIP_FIELD: SKIP_PATTERN},
                'skippable_field': {TRIGGER_MODIFICATION: True, SKIP_FIELD: SKIP_PATTERN},
                'function_overwrite_field': {TRIGGER_MODIFICATION: True, OVERWRITE_FUNCTION: overwrite_function}
            }]
        }]
    }

    # Create an instance of the ApplyRecursive class and call it

    _applyrecursive = ApplyRecursive(function_to_apply, None, {'key': 'x.3'}, 'data')
    _applyrecursive.apply(data_map, TRIGGER_MODIFICATION, data)

    print(json.dumps(data, indent=4))