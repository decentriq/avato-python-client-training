import os
import nox


@nox.session(python=["python3.6", "python3.7"])
def py37(session):
    env = {
        "TEST_API_TOKEN_1": os.environ["TEST_API_TOKEN_1"],
        "TEST_API_TOKEN_2": os.environ["TEST_API_TOKEN_2"],
        "TEST_API_TOKEN_3": os.environ["TEST_API_TOKEN_3"],
        "TEST_USER_ID_2": os.environ["TEST_USER_ID_2"],
        "TEST_USER_ID_3": os.environ["TEST_USER_ID_3"]
    }
    session.install("pytest")
    session.run("pip", "install", ".")
    session.run("pytest", "tests/", env=env)

