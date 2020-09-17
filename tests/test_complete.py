import os
import pandas as pd
import json
from avato import Client
from avato import Secret
from avato_training import Training_Instance, Configuration
import numpy as np

tests_root = os.path.dirname(__file__)
fixtures_dir = os.path.join(tests_root, "fixtures")

analyst_api_token = os.getenv('TEST_API_TOKEN_1')
analyst_password = "SECRET_PASSWORD"

dataowner1_username = os.getenv('TEST_USER_ID_2')
dataowner1_api_token = os.getenv('TEST_API_TOKEN_2')

dataowner2_username = os.getenv('TEST_USER_ID_3')
dataowner2_api_token = os.getenv('TEST_API_TOKEN_3')

# How the analyst expects the data to be formatted
feature_columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']
label_column = "quality"

# The datafiles uploaded by the 
dataowner1_file = os.path.join(fixtures_dir, "wine-dataowner1.csv")
dataowner2_file = os.path.join(fixtures_dir, "wine-dataowner2.csv")

# Create client.
analyst_client = Client(
    api_token=os.environ["TEST_API_TOKEN_1"],
    instance_types=[Training_Instance],
)

def test_training_complete():
    # Spin up an instance. Set who can participate in the instance.
    analyst_instance = analyst_client.create_instance(
        "Training", 
        Training_Instance.type, 
        [dataowner1_username, dataowner2_username]
    )

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

    analyst_instance.validate_fatquote(
        accept_debug=True,
        accept_group_out_of_date=True
    )


    # The quote is part of the fatquote and provides a detailed fingerprint of the program and state of the remote machine. For example:
    # * using `flags` we can detect if the CPU is running in un-trusted debug mode
    # * using `*_snv` we can verify if all security patches have been deployed to the infrastructure
    # * using `mrenclave` we can attest to the exact program being executed on the remote machine


    # #### Configure instance
    # Set the configuration
    configuration = Configuration(
        feature_columns=feature_columns,
        label_column=label_column,
        password=analyst_password # the password to execute
    )

    # Create and set public-private keypair for secure communication.
    analyst_secret = Secret()
    analyst_instance.set_secret(analyst_secret)

    # Upload
    analyst_instance.upload_configuration(configuration)


    # ### DATAOWNERS
    # This function submits for a given dataowner a data file to the instance.
    def dataowner_submit_data(dataowner_api_token, instance_id, data_file):

        # Create client
        dataowner_client = Client(
            api_token=dataowner_api_token,
            instance_types=[Training_Instance]
        )

        # Connect to instance (using ID from the analyst user)
        dataowner_instance = dataowner_client.get_instance(instance_id)

        # Check security guarantees.
        dataowner_instance.validate_fatquote(
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

    dataowner1_instance = dataowner_submit_data(
        dataowner1_api_token, 
        analyst_instance.id, 
        data_file=dataowner1_file
    )


    # #### dataowner 2 - Submit Data

    dataowner2_instance = dataowner_submit_data(
        dataowner2_api_token, 
        analyst_instance.id, 
        dataowner2_file
    )


    # ### ANALYST
    # #### Train with first set of hyperparameters

    hyperparameters = {
        "learning_rate": 0.1,
        "num_splits": 10,
        "num_epochs": 2,
        "l2_penalty": 0.0,
        "l1_penalty": 0.0,
    }

    analyst_instance.start_execution(analyst_password, hyperparameters)

    classifier, metadata = analyst_instance.get_results(analyst_password)

    # #### Train with second set of hyperparameters

    hyperparameters = {
        "learning_rate": 1.0,
        "num_splits": 10,
        "num_epochs": 2,
        "l2_penalty": 0.0,
        "l1_penalty": 0.0,
    }

    analyst_instance.start_execution(analyst_password, hyperparameters)

    classifier, metadata = analyst_instance.get_results(analyst_password)

    # #### Use classifier, compute accuracy on full dataset, compare with metadata results

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

    # ### ANALYST USER - Clean Up

    analyst_instance.shutdown()
    analyst_instance.delete()
    assert analyst_instance.id not in list(map(lambda x: x["id"], analyst_client.get_instances()))
