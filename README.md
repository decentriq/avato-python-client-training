# Confidential ML Training :weight_lifting:

Python client library for Training instance of the decentriq platform.

# What is Confidential ML Training?

By using Confidential Computing, Confidential ML Training enables you to train machine learning models based on data that nobody ever can access; not you, not us, not the infrastructure provider, nobody. This removes the risk for data breaches or data misuse.

## Installation

### Prerequisites

You need to have Python >= 3.6.1 installed (check using `python --version`) and internet access.

### Release

The library is published on PyPi so it can be easily installed by running:
```
pip install avato-training
```

### Development

After cloning the repository you can use different installation methods:

#### Poetry

To install with poetry just run:
```
poetry install
```

##### Notes:

1. If you get an error during the installation try to delete the `poetry.lock` file

2. Poetry installs the library in its own virtualenv, if you want to use it in your
global python installation disable virtualenvs in poetry

```
poetry config settings.virtualenvs.create false
```

#### Pip

To install with pip just run:

```
pip install .
```

## Usage:

To use the library just import the `avato` and `avato_training` modules and start interacting with the platform!

**Example-1**: *instance creation*

``` python
from avato import Client
from avato_training import TRAINING_Instance

client = Client(
    api_token="SECRET_TOKEN",
    instance_types=[TRAINING_Instance]
)
instance = client.create_instance(
    "genesis", TRAINING_Instance.type, ["friend@decentriq.ch"]
)
client.get_instances()
instance.shutdown()
instance.delete()
```

### Examples

Some examples showing how the library can be used are provided in the `examples` folder.
For more examples check out the `tests` directory
