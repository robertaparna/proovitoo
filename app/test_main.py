from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_get_source_info():
    response = client.get("/source_info")

    assert response.status_code == 200
    assert len(response.json()["https://tehisintellekt.ee/"]) > 0
    assert len(response.json()["https://tehisintellekt.ee/tehisintellekt/"]) > 0
    assert len(response.json()["https://tehisintellekt.ee/liitu-meiega/"]) > 0

def test_ask():
    question = "Miks peaksin ettevõttega liituma?"
    response = client.post("/ask", json={
        "question": question,
    })

    assert response.status_code == 200
    assert response.json()["user_question"] == question
    assert len(response.json()["answer"]) > 0
    assert response.json()["usage"]["input_tokens"] > 0
    assert response.json()["usage"]["output_tokens"] > 0
    assert response.json()["sources"][0] == "https://tehisintellekt.ee/liitu-meiega/"
