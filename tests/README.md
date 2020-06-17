## Auto-generated tests

The tests here should always reflect the current state of the example notebooks.  
To convert a notebook to a Python script just execute the following command:  
`jupyter nbconvert --to script 'training-demo.ipynb'`

Some small modification might be necessary:
* Make sure tests are prefixed with `test_*.py`
* Don't hard-code backend host address and port
* Reduce run-time to <10sec -> often amount of data or precision of the model needs to be reduced
* Change paths to fixtures and define them as absolute paths
* Don't assert MRENCLAVE. We don't want to pin the MRENCLAVE in tests
