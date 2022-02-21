# py-applyrecursive

Apply a function to specific data keys in an iterable when a condition is met

&nbsp;

---

&nbsp;

## Map

&nbsp;

A map should follow the structure of the data being processed - omitting fields will simply cause them to be left untouched.

Fields that should be modified should hold a value containing a predetermined trigger field (such as `modify` below), and any other values to be passed into the function processing the data.

&nbsp;

```json
{
  "field_to_be_processed": {
    "__modify": true,
    "__other_value": "..."
  }
}
```

_References to functions may also be passed in the map where it's not desirable to use the main function._

&nbsp;

---

&nbsp;

## Usage

&nbsp;

Create an instance of the `ApplyRecursive` class, passing in the main function you want to apply to the data, a tuple of positional arguments, a dictionary of keyword arguments, and the name of the field you want the data to be passed to your function in (`data_field_name` below).

Then, call the `apply` function, passing in the map (`data_map`), the field that should trigger a modification (`TRIGGER_MODIFICATION`), and the data to be operated on. The modified data will be written back to the data object you pass in.

&nbsp;

```python
_applyrecursive = ApplyRecursive(function_to_apply, None, {'my_key': 'x.3'}, 'data_field_name')

_applyrecursive.apply(data_map, TRIGGER_MODIFICATION, data)
```

&nbsp;

---

&nbsp;

## Credits

&nbsp;

```json
{
  "author": "analyticsdept",
  "github": "https://github.com/analyticsdept"
}
```
