from fastapi.testclient import TestClient
from main import app, db

client = TestClient(app)

def test_get_next_proxy():
    # Reset DB state for testing
    global proxy_index
    import main
    main.proxy_index = 0
    main.db["proxies"] = [
        {"ip": "192.168.1.100", "active": True},
        {"ip": "10.0.0.5", "active": False},
        {"ip": "172.16.0.2", "active": True}
    ]
    
    response = client.get("/api/proxy/next")
    assert response.status_code == 200
    assert response.json() == {"proxy": "192.168.1.100"}
    
    response2 = client.get("/api/proxy/next")
    assert response2.status_code == 200
    assert response2.json() == {"proxy": "172.16.0.2"}

def test_get_next_proxy_no_active():
    import main
    main.db["proxies"] = [{"ip": "10.0.0.5", "active": False}]
    
    response = client.get("/api/proxy/next")
    assert response.status_code == 404
    assert response.json() == {"detail": "No active proxies available"}

def test_submit_job():
    import main
    main.db["jobs"] = []
    
    job_payload = {
        "job_id": "job_123",
        "target_url": "https://example.com",
        "status": "success",
        "data": "<html>...</html>"
    }
    
    response = client.post("/api/jobs", json=job_payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Job submitted successfully", "job_id": "job_123"}
    assert len(main.db["jobs"]) == 1
    assert main.db["jobs"][0]["job_id"] == "job_123"
