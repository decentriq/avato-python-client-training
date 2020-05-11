import os
import nox


@nox.session(python=["python3.6", "python3.7"])
def tests(session):
    env = {
        "ADMIN_USER_ID_1": os.environ["TEST_USER_ID_1"],
        "ADMIN_USER_PASSWORD_1": os.environ["TEST_USER_PASSWORD_1"],
        "TRAINING_USER_ID_1": os.environ["TEST_USER_ID_2"],
        "TRAINING_USER_PASSWORD_1": os.environ["TEST_USER_PASSWORD_2"],
        "TRAINING_USER_ID_2": os.environ["TEST_USER_ID_3"],
        "TRAINING_USER_PASSWORD_2": os.environ["TEST_USER_PASSWORD_3"],
    }
    session.install("pytest")
    session.run("pip", "install", ".")
    session.run("pytest", "tests/", env=env)
