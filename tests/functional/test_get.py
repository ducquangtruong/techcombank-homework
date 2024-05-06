"""
    Tests for the GET endpoint
"""

from main import app

def test_get_simple():
    """
        Test for getting the percentile of an existing pool
    """

    with app.test_client() as test_client:
        test_client.post(
            "/api/pools", 
            json = {
                "poolId": 123546,
                "poolValues": [1, 7, 2, 6]
            }
        )
        response = test_client.get(
            "/api/pools", 
            json = {
                "poolId": 123546,
                "percentile": 99.5
            }
        )
        assert response.status_code == 200
        assert response.get_json().get("quantile") == 6.985
        assert response.get_json().get("element_count") == 4
