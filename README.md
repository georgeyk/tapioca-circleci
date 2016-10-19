# Tapioca CircleCI

CircleCI API Wrapper using tapioca https://circleci.com/docs/api/

*under development, very unstable and not published to pypi yet*


## Instalation

```
pip install tapioca-circleci
```

**NOTE**: Only tested with Python 3.5+


## Documentation

``` python
from tapioca_circleci import CircleCI

api = CircleCI(
    token='{your-token}'  # required,
    timeout=5,  # Optional, defaults to 5s
)
```

To generate API tokens, access your dashboard: [https://circleci.com/account/api](https://circleci.com/account/api)

### Serialization

- datetime
- Decimal

### Deseralization

- datetime
- Decimal

## More

- Learn how Tapioca works [here](http://tapioca-wrapper.readthedocs.org/en/stable/quickstart.html)
- Explore this package using iPython
- Have fun!
