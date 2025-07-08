import requests

# === Config ===
FAB_ENDPOINTS = {
    "FAB-GPT-Pro": "https://xmy6yovg6aaq4db7brijnsww6q0phnvv.lambda-url.us-east-1.on.aws/agent/fab-gpt-pro/execute",
    "FAB-nova-lite": "https://xmy6yovg6aaq4db7brijnsww6q0phnvv.lambda-url.us-east-1.on.aws/agent/nova-lite/execute",
    "FAB-claude-sonnet": "https://xmy6yovg6aaq4db7brijnsww6q0phnvv.lambda-url.us-east-1.on.aws/agent/claude-sonnet/execute",
    "FAB-geminipro": "https://xmy6yovg6aaq4db7brijnsww6q0phnvv.lambda-url.us-east-1.on.aws/agent/geminipro/execute"
}

FAB_OPTIMIZE_ENDPOINT = "https://xmy6yovg6aaq4db7brijnsww6q0phnvv.lambda-url.us-east-1.on.aws/agent/violet-iapetus/execute"

# Replace these with your actual credentials
USER_ID = "<your_user_id>"
API_KEY = "<your_api_key>"

# Session for performance
session = requests.Session()


def generate_code(model: str, language: str, user_prompt: str) -> str:
    """
    Generate code using the selected FAB agent.

    Args:
        model (str): FAB model key (e.g., 'FAB-GPT-Pro')
        language (str): Language to use in the prompt (e.g., 'Python')
        user_prompt (str): The task for code generation

    Returns:
        str: Generated code or error message
    """
    endpoint = FAB_ENDPOINTS.get(model)
    if not endpoint:
        return f"# Error: Model '{model}' is not recognized."

    full_prompt = f"Write a {language} function that does the following:\n{user_prompt}"

    headers = {
        "Content-Type": "application/json",
        "x-user-id": USER_ID,
        "x-authentication": f"api-key {API_KEY}"
    }

    payload = {
        "input": {
            "query": full_prompt
        }
    }

    try:
        response = session.post(endpoint, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("output", "# No code returned.")
    except requests.exceptions.RequestException as e:
        return f"# Network error: {e}"
    except ValueError:
        return "# Error: Invalid JSON in response"
    except Exception as e:
        return f"# Unexpected error: {e}"


def optimize_code(code: str, language: str = "python") -> str:
    """
    Optimize existing code using the FAB optimizer agent.

    Args:
        code (str): Raw code to optimize
        language (str): Programming language (default: Python)

    Returns:
        str: Optimized code or error message
    """
    prompt = f"Optimize the following {language} code:\n\n{code}"

    headers = {
        "Content-Type": "application/json",
        "x-user-id": USER_ID,
        "x-authentication": f"api-key {API_KEY}"
    }

    payload = {
        "input": {
            "query": prompt
        }
    }

    try:
        response = session.post(FAB_OPTIMIZE_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("output", "# No optimized code returned.")
    except requests.exceptions.RequestException as e:
        return f"# Optimization network error: {e}"
    except ValueError:
        return "# Error: Invalid JSON in optimizer response"
    except Exception as e:
        return f"# Unexpected error during optimization: {e}"


