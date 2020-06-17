#!/usr/bin/env python
# coding: utf-8

# # Training Demo
# 
# This notebook demonstrates the use of the Confidential Training tool. It requires the [avato Training API](https://github.com/decentriq/avato-python-client-training) and its dependencies to be installed.  
# 
# Note that in a realistic, non-demo use of the Confidential Training tool, one analyst user and multiple dataowner users would upload data from different computers. In this workbook, for simplicity, the workflows of the analyst user and the two dataowner users are all shown together.   

# ### Import dependencies

# In[1]:
def test_complete():
    import os
    import pandas as pd
    import json
    from avato import Client
    from avato import Secret
    from avato_training import Training_Instance, Configuration
    import numpy as np

    analyst_username = "***REMOVED***"
    analyst_***REMOVED*** = "***REMOVED***"

    dataowner1_username = "***REMOVED***"
    dataowner1_***REMOVED*** = "***REMOVED***"

    dataowner2_username = "***REMOVED***"
    dataowner2_***REMOVED*** = "***REMOVED***"

    # This is the hash of the code
    expected_measurement = "4ff505f350698c78e8b3b49b8e479146ce3896a06cd9e5109dfec8f393f14025"

    # How the analyst expects the data to be formatted
    feature_columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']
    label_column = "quality"

    # The datafiles uploaded by the 
    dataowner1_file = "./examples/test-data/wine-dataowner1.csv"
    dataowner2_file = "./examples/test-data/wine-dataowner2.csv"


    # ### ANALYST USER
    # #### Create new instance

    # In[2]:


    # Create client.
    analyst_client = Client(
        username=analyst_username,
        ***REMOVED***=analyst_***REMOVED***,
        instance_types=[Training_Instance]
    )

    # Spin up an instance. Set who can participate in the instance.
    analyst_instance = analyst_client.create_instance(
        "Training", 
        Training_Instance.type, 
        [dataowner1_username, dataowner2_username]
    )
    print("Instance ID: {}".format(analyst_instance.id))


    # #### Check security guarantees
    # Validating the so-called fatquote. This step is crucial for all security guarantees.
    # This step gets and validates the cryptographic proof from the enclave:
    # 
    # * i)   It proves it is a valid SGX enclave (by checking a certificate).
    # * ii)  It compares the hash of the enclave code provided by the user to
    #      an expected value (to verify what code is running in the enclave).
    # * iii) As part of the proof also a public key is transmitted that allows
    #      establishing a secure connection into the enclave (as the private
    #      key is only known to the enclave).
    #      
    # As we are using a non-production environment, we whitelist the debug and out_of_data flags.

    # In[3]:


    analyst_instance.validate_fatquote(
        expected_measurement=expected_measurement,
        accept_debug=True,
        accept_group_out_of_date=True
    )


    # The quote is part of the fatquote and provides a detailed fingerprint of the program and state of the remote machine. For example:
    # * using `flags` we can detect if the CPU is running in un-trusted debug mode
    # * using `*_snv` we can verify if all security patches have been deployed to the infrastructure
    # * using `mrenclave` we can attest to the exact program being executed on the remote machine

    # In[4]:


    # Uncomment to inspect 
    # print(analyst_instance.quote)


    # #### Configure instance

    # In[5]:


    # Set the configuration
    configuration = Configuration(
        feature_columns=feature_columns,
        label_column=label_column,
        ***REMOVED***=analyst_***REMOVED*** # the ***REMOVED*** to execute
    )

    # Create and set public-private keypair for secure communication.
    analyst_secret = Secret()
    analyst_instance.set_secret(analyst_secret)

    # Upload
    analyst_instance.upload_configuration(configuration)


    # ### DATAOWNERS

    # In[6]:


    # This function submits for a given dataowner a data file to the instance.
    def dataowner_submit_data(dataowner_username, dataowner_***REMOVED***, instance_id, data_file):

        # Create client
        dataowner_client = Client(
            username=dataowner_username,
            ***REMOVED***=dataowner_***REMOVED***,
            instance_types=[Training_Instance]
        )

        # Connect to instance (using ID from the analyst user)
        dataowner_instance = dataowner_client.get_instance(instance_id)

        # Check security guarantees.
        dataowner_instance.validate_fatquote(
            expected_measurement=expected_measurement,
            accept_debug=True,
            accept_group_out_of_date=True
        )

        # Create and set public-private keypair for secure communication.
        dataowner_secret = Secret()
        dataowner_instance.set_secret(dataowner_secret)

        # Get data format from the enclave
        data_format = dataowner_instance.get_data_format()
        print("Data format:\n{}".format(data_format))

        # Load data
        df = pd.read_csv(data_file)
        
        print("Loaded data:\n")
        print(df)

        # Submit data
        (ingested_rows, failed_rows) = dataowner_instance.submit_data(df)
        print("Number of successfully ingested rows: {}, number of failed rows: {}".format(ingested_rows, failed_rows))
        
        return dataowner_instance


    # #### dataowner 1 - Submit data

    # In[7]:


    dataowner1_instance = dataowner_submit_data(
        dataowner1_username, 
        dataowner1_***REMOVED***, 
        analyst_instance.id, 
        data_file=dataowner1_file
    )


    # #### dataowner 2 - Submit Data

    # In[8]:


    dataowner2_instance = dataowner_submit_data(
        dataowner2_username, 
        dataowner2_***REMOVED***, 
        analyst_instance.id, 
        dataowner2_file
    )


    # ### ANALYST
    # #### Train with first set of hyperparameters

    # In[9]:


    hyperparameters = {
        "learning_rate": 0.1,
        "num_splits": 10,
        "num_epochs": 2,
        "l2_penalty": 0.0,
        "l1_penalty": 0.0,
    }

    analyst_instance.start_execution(analyst_***REMOVED***, hyperparameters)

    classifier, metadata = analyst_instance.get_results(analyst_***REMOVED***)
    print("metadata: {}".format(json.dumps(metadata, indent=2)))


    # #### Train with second set of hyperparameters

    # In[10]:


    hyperparameters = {
        "learning_rate": 1.0,
        "num_splits": 10,
        "num_epochs": 2,
        "l2_penalty": 0.0,
        "l1_penalty": 0.0,
    }

    analyst_instance.start_execution(analyst_***REMOVED***, hyperparameters)

    classifier, metadata = analyst_instance.get_results(analyst_***REMOVED***)
    print("metadata: {}".format(json.dumps(metadata, indent=2)))


    # #### Use classifier, compute accuracy on full dataset, compare with metadata results

    # In[11]:


    def load_data():
        Xy = np.array(
            pd.concat([
                pd.read_csv(dataowner1_file),
                pd.read_csv(dataowner2_file)
            ])
        );
        X = Xy[:,0:-1]
        y = Xy[:,-1]
        return X, y

    def compute_accuracy(classifier, X, y):

        y_hat = classifier.predict(X)
        assert len(y) == len(y_hat)
        n = len(y)
        n_eq = 0
        for yi, yi_hat in zip(y, y_hat):
            if float(yi) == float(yi_hat):
                n_eq = n_eq + 1
        accuracy = float(n_eq)/n
        return accuracy


    X, y = load_data()
    accuracy = compute_accuracy(classifier, X, y)

    print("Some predictions of the classifier: {}".format(classifier.predict(X[0:2, :])))
    print("Accuracy of the enclave classifier on the full dataset (as returned through the metadata object): {}".format(metadata["Fullset Accuracy"]))
    print("Accuracy of the local classifier on the full dataset: {}".format(accuracy))



    # ### ANALYST USER - Clean Up

    # In[12]:


    analyst_instance.shutdown()
    analyst_instance.delete()
    assert analyst_instance.id not in analyst_client.get_instances()

