import requests

def log_to_server(task_id, signature, swarmBountyId, errorMessage):
    # Make a POST request with the result
    response = requests.post(
        f"http://host.docker.internal:30017/task/{task_id}/add-failed-info",
        json={
            "signature": signature,
            "swarmBountyId": swarmBountyId,
            "errorMessage": errorMessage,
        },
    )
    return response.json()