# avato-tflite-training-demo

## Installation 

### Prerequisites

You need to have Python >=3.6 installed (check using `python --version`) and internet access.

### Installation

1. Create a new Python environment to install into using
   `python -m venv .env`
2. Activate the environment using
   `source .env/bin/activate`
3. Install all dependencies using `.env/bin/pip install -r requirements.txt`

### Run Demo

Make sure you have the correct Python environment activated. If you just installed the module, it's already set. Otherwise you may have to run `source .env/bin/activate` again.

Set the trial user credentials via

```
export ANALYST_API_TOKEN="#PLACEHOLDER#"
export ANALYST_ID="#PLACEHOLDER#"
export DATAOWNER1_API_TOKEN="#PLACEHOLDER#"
export DATAOWNER1_ID="#PLACEHOLDER#"
export DATAOWNER2_API_TOKEN="#PLACEHOLDER#"
export DATAOWNER2_ID="#PLACEHOLDER#"
```
To run the demo start a notebook server with `.env/bin/jupyter notebook` which should open a browser window. 

In the browser window, open the `examples/training-demo-all-in-one.ipynb` notebook to perform a **full demonstration** in one go.

Alternatively, for a **simple yet fully realistic** simulation execute:

* `examples/training-demo-data-owner-1-simple.ipynb`
* `examples/training-demo-data-owner-2-simple.ipynb`
* `examples/training-demo-analyst-simple.ipynb`
