import pytest

@pytest.fixture(scope="session")  # This ensures the constant is shared across the session
def creation_text():
    text = "take the sales from the sales table in mysql server and show them by customers regions that you can take from the SAP tables and put the result in Azure warehouse"
    return text
