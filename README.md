# A python client for the Thingiverse API

A python client that provides access to the Thingiverse API using an apps `app_token`. Great for querying information on Thingiverse.

## Contents

- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [Documentation](#documentation)
- [Formatting](#formatting)
- [Testing](#testing)

## Getting started

I haven't put the package on pypi just yet so installing the package requires installing it from the [repo](https://stackoverflow.com/questions/15268953/how-to-install-python-package-from-github).

```
pip install git+https://github.com/jamesgopsill/thingiverse-client-py.git#egg=gtr
```

You can then use it in your python code like so:

```python
from thingiverse import ThingiverseClient

client = ThingiverseClient(app_token="")
```

The are more examples in the `examples` folder if you want to learn more about what the tool can do. The docs also provide an overview of all the functions one can call.

## Contributing

I would recommend creating a virtual environment for development work.

```
python -m venv .venv
```

Then activate it using.

**Mac / Linux**

```
source .venv/bin/activate
```

**Windows**

```
.venv/Scripts/activate
```

Then install the development requirements.

```
pip install -r requirements_dev.txt
```

And then install the package within your local virtual dev environment.

```
pip install -e .
```

## Documentation

Documentation is generated using:

```
pdoc ./src/thingiverse
```

```
pdoc ./src/thingiverse -o ./docs
```

- https://pdoc.dev/

## Formatting

And we format the code using black.

```
black src/
```

- https://github.com/psf/black

## Testing

Testing uses unittest.

```
python -m unittest -v
```