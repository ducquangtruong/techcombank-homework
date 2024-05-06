"""
    Tests for the POST endpoint
"""

from main import app

def test_post_new():
    """
        Test for adding a new pool
    """

    with app.test_client() as test_client:
        response = test_client.post(
            "/api/pools", 
            json = {
                "poolId": 564652,
                "poolValues": [2, 3, 8]
            }
        )
        assert response.status_code == 201
        assert response.get_json().get("status") == "Pool inserted."

def test_post_existing():
    """
        Test for adding into an existing pool
    """

    with app.test_client() as test_client:
        test_client.post(
            "/api/pools", 
            json = {
                "poolId": 342132,
                "poolValues": [1, 2, 3, 5]
            }
        )
        response = test_client.post(
            "/api/pools", 
            json = {
                "poolId": 342132,
                "poolValues": [8, 13, 21]
            }
        )
        assert response.status_code == 201
        assert response.get_json().get("status") == "Pool appended."
