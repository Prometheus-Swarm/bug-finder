from src.server import create_app
import os

from prometheus_swarm.utils.logging import set_error_post_hook, set_logs_post_hook
import requests


def post_logs_to_server(
    level: str,
    message: str,
    task_id: str = None,
    swarm_bounty_id: str = None,
    signature: str = None,
):
    print("CALLING LOGGING ENDPOINT", level, message, task_id, swarm_bounty_id, signature)
    # requests.post(
    #     "https://your-logging-endpoint.com/logs",
    #     json={"context": context, "error": str(error), "stack_trace": stack_trace},
    #     timeout=5,
    # )


def post_error_logs_to_server(
    error: Exception,
    context: str,
    stack_trace: str,
    task_id: str = None,
    swarm_bounty_id: str = None,
    signature: str = None,
):
    print(
        "CALLING ERROR LOGGING ENDPOINT",
        error,
        context,
        stack_trace,
        task_id,
        swarm_bounty_id,
    )
    response = requests.post(
        f"http://host.docker.internal:30017/task/{task_id}/add-failed-info",
        json={
            "signature": signature,
            "swarmBountyId": swarm_bounty_id,
            "errorMessage": context + str(error),
        },
    )
    return response.json()

app = create_app()
# Register it once at startup
set_error_post_hook(post_error_logs_to_server)
set_logs_post_hook(post_logs_to_server)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
