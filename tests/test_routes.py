import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_health():
    """Test health endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_apply_discount():
    """Test apply_discount endpoint - should fail due to logic bug"""
    response = client.post("/api/cart/discount", params={"price": 100, "discount": 10})
    # With the bug (using + instead of -), final will be 110
    # The check is: if final > price (110 > 100 = True), so it returns error
    # But the test expects it to work correctly and return a valid result
    assert response.status_code == 200
    result = response.json()
    assert result["final_price"] == 90  # Expected correct result, but will fail
