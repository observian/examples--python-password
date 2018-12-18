# python-password

## Installation

1. Set up a virtual environment
2. `pip install pip-tools`
3. `pip-sync`

## Examples

### Get Help
```bash
python app.py --help
```

### Create a new user
```bash
python app.py --user myuser --password coolpass --new
```

### Create a new admin user
```bash
python app.py --user myadminguy --password securepass --new --admin
```

### Test password
```bash
python app.py --user myuser --password coolpass

//Output
Login Successful!

```
