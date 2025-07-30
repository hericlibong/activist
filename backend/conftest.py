
import pytest
from rest_framework.test import APIClient

from authentication.factories import UserFactory


@pytest.fixture
def authenticated_client(db):
    """
        Returns an APIClient already authenticated with a test user.
        The user is generated via UserFactory.
        """
    user_password = "password123"  # Or any other password for the test
    user = UserFactory(plaintext_password=user_password)
    client = APIClient()
    # Use force_authenticate to simulate an authenticated client (DRF)
    client.force_authenticate(user=user)
    return client, user
