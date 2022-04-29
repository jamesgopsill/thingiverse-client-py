# A python client for the Thingiverse API

**Contents**
- [Getting Started](#getting-started)
- [Contributing](#contributing)

## Getting started

I haven't put the package on pypi just yet so installing the package requires installing it from the [repo](https://stackoverflow.com/questions/15268953/how-to-install-python-package-from-github).

```
pip install git+https://github.com/jamesgopsill/thingiverse-client-py.git#egg=gtr
```

You can then use it in your python code like so:

```python
from thingiverse import ThingiverseClient

client = ThingiverseClient()


```

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
pdoc ./docs ./src/gtr
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