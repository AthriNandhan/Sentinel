from app.models.state import RemediationState
from app.services.llm import llm_service

def green_agent(state: RemediationState) -> RemediationState:
    """
    Green Agent: Verifies the code by analyzing the patch.
    """
    print("--- Green Agent: Verifying ---")
    
    prompt = f"""
    You are a Security Auditor.
    Review the following code for {state.vulnerability_type}.
    
    Code:
    ```python
    {state.patch_diff}
    ```
    
    Task:
    1. Verify if the code is secure against {state.vulnerability_type}.
    2. CRITICAL: Verify that NO existing functionality (helper functions, classes, imports) was removed or broken.
       If the patch removes unrelated code (e.g., helper functions used by other modules), it must FAIL.
    
    Output strictly in the following format:
    Reasoning: <Detailed analysis of security AND regression check>
    Status: <PASS or FAIL>
    """
    
    response = llm_service.generate_text(prompt).strip()
    
    # Parse the response
    reasoning = "No reasoning provided."
    status = "FAIL"
    
    for line in response.split('\n'):
        if line.startswith("Reasoning:"):
            reasoning = line.replace("Reasoning:", "").strip()
        elif line.startswith("Status:"):
            status = line.replace("Status:", "").strip().upper()
            
    # Fallback if parsing fails but keywords exist
    if "Status:" not in response:
        if "PASS" in response: status = "PASS"
        if "FAIL" in response: status = "FAIL"
        reasoning = response # Store full response as reasoning if format is broken

    state.verification_status = status
    state.verification_reasoning = reasoning
        
    print(f"Verification Result: {state.verification_status}")
    print(f"Reasoning: {reasoning}")
    
    return state
