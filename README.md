# avato-training
Python client library for Training instance of the Avato platform.

## Prerequisites
You need to have Python >=3.7 installed (check using `python --version`) and internet access.

## Installation

Execute the following steps in the `avato-python-client-training` folder.

1. Create a new Python environment to install into using
`python -m venv .env`
2. Activate the environment using
`source .env/bin/activate`
3. Install dependencies using `.env/bin/pip install .`

## Run Demo
Make sure you have the correct Python environment activated. If you just installed the module, it's already set. Otherwise you may have to run `source .env/bin/activate` again.

Set the trial user credentials via

```bash
export ANALYST_ID="user_1@gmail.com"
export ANALYST_PASSWORD="password"
export DATAOWNER1_ID="user_2@gmail.com"
export DATAOWNER1_PASSWORD="password"
export DATAOWNER2_ID="user_3@gmail.com"
export DATAOWNER2_PASSWORD="password"
```

To run the demo start a notebook server with `.env/bin/jupyter notebook` which should open a browser window. 

In the browser window, open the `examples/training-demo-all-in-one.ipynb` notebook to perform a **full demonstration** in one go.

Alternatively, for a **simple yet fully realistic** simulation execute:

* `examples/training-demo-data-owner-1-simple.ipynb`
* `examples/training-demo-data-owner-2-simple.ipynb`
* `examples/training-demo-analyst-simple.ipynb`

Or, if you prefer a **more detailed perspective**, you can try:

* `examples/training-demo-data-owner-1.ipynb`
* `examples/training-demo-data-owner-2.ipynb`
* `examples/training-demo-analyst.ipynb`

