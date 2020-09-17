import numpy as np
import pandas as pd
from avato import Client
from avato import Secret
from avato_training import Training_Instance, Configuration
import time

data_filenames = ("test-data/wine-dataowner1.csv", "test-data/wine-dataowner2.csv")

expected_measurement = "71b81c5d4a1879fd75905bd207b079274fdcd095f2ff145d0b560574f5733df3"

backend_host = "api.decentriq.ch"
backend_port = 15005


def load_data():
    Xy = np.array(
        pd.concat([
            pd.read_csv(data_filenames[0]),
            pd.read_csv(data_filenames[1])
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


def analyst_set_up_instance(analyst_api_token, analyst_password, data_owner_usernames, feature_columns, label_column):

    # Create client.
    analyst_client = Client(
        api_token=analyst_api_token,
        instance_types=[Training_Instance],
        backend_host=backend_host,
        backend_port=backend_port,
        use_ssl=True
    )

    # Spin up an instance. Set who can participate in the instance.
    analyst_instance = analyst_client.create_instance(
        "Training",
        Training_Instance.type,
        data_owner_usernames
    )
    print("Created Instance with ID: {}".format(analyst_instance.id))

    analyst_instance.validate_fatquote(
        expected_measurement=expected_measurement,
        accept_debug=True,
        accept_group_out_of_date=True
    )

    # Set the configuration
    configuration = Configuration(
        feature_columns=feature_columns,
        label_column=label_column,
        password=analyst_password
    )

    print("\nConfigured instance with feature columns \n{}\n and label column \n{}".format(
        "\n".join(["  '{}'".format(c) for c in configuration.feature_columns]),
        "  '{}'".format(configuration.label_column)
    ))

    # Create and set public-private keypair for secure communication.
    analyst_secret = Secret()
    analyst_instance.set_secret(analyst_secret)

    # Upload
    analyst_instance.upload_configuration(configuration)

    return analyst_instance


# This function submits for a given data owner a data file to the instance.
def data_owner_submit_data(dataowner_api_token, instance_id, data_file):

    # Create client
    data_owner_client = Client(
        api_token=dataowner_api_token,
        instance_types=[Training_Instance],
        backend_host=backend_host,
        backend_port=backend_port,
        use_ssl=True
    )

    # Connect to instance (using ID from the analyst user)
    data_owner_instance = data_owner_client.get_instance(instance_id)

    # Check security guarantees.
    data_owner_instance.validate_fatquote(
        expected_measurement=expected_measurement,
        accept_debug=True,
        accept_group_out_of_date=True
    )
    print("Verifying security...")
    time.sleep(0.3)
    print("... signature verified.")
    time.sleep(0.3)
    print("... code hash verified.")
    time.sleep(0.3)
    print("Security successfully verified.\n")

    # Create and set public-private keypair for secure communication.
    data_owner_instance.set_secret(Secret())
    print("Created random keypair for e2e encryption.\n")

    # Get data format from the enclave
    data_format = data_owner_instance.get_data_format()

    # print("Data format:\n{}".format(data_format))

    # Load data
    df = pd.read_csv(data_file)

    print("Loaded data:")
    print(df.head(2))

    # Submit data
    print("\nEncrypting data...")
    time.sleep(0.3)
    print("Submitting encrypted data...")
    time.sleep(0.3)
    (ingested_rows, failed_rows) = data_owner_instance.submit_data(df)
    print("\nNumber of successfully ingested rows: {}, number of failed rows: {}".format(ingested_rows, len(failed_rows)))
