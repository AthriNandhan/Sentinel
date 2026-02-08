from app.models.state import RemediationState
from app.services.llm import llm_service
import os

def red_agent(state: RemediationState) -> RemediationState:
    """
    Red Agent: Simulates an attack on the vulnerable code.
    """
    print("--- Red Agent: Attacking ---")
    
    # Read the vulnerable code
    if not os.path.exists(state.code_path):
        print(f"Error: File {state.code_path} not found.")
        state.exploit_success = False
        return state

    with open(state.code_path, "r") as f:
        code_content = f.read()

    prompt = f"""
    You are an expert Red Team security researcher. 
    Analyze the following code for a {state.vulnerability_type} vulnerability.
    
    Code:
    ```python
    {code_content}
    ```
    
    If the vulnerability exists, provide a specific input string or payload that exploits it.
    Return ONLY the payload string. If no vulnerability is found, return "SAFE".
    """

    response = llm_service.generate_text(prompt).strip()
    
    if "SAFE" in response:
        state.exploit_success = False
    else:
        state.exploit_success = True
        state.exploit_payloads.append(response)
        print(f"Generated Exploit: {response}")

    return state
