from app.models.state import RemediationState
from app.services.llm import llm_service

def green_agent(state: RemediationState) -> RemediationState:
    """
    Green Agent: Verifies the code by analyzing the patch.
    """
    print("--- Green Agent: Verifying ---")
    
    # In a real scenario, we would apply the patch and run tests.
    # Here we simulate verification by asking the LLM to review the code.
    
    prompt = f"""
    You are a Security Auditor.
    Review the following code for {state.vulnerability_type}.
    
    Code:
    ```python
    {state.patch_diff}
    ```
    
    Is this code secure against {state.vulnerability_type}?
    Return PASS or FAIL.
    """
    
    response = llm_service.generate_text(prompt).strip().upper()
    
    if "PASS" in response:
        state.verification_status = "PASS"
    else:
        state.verification_status = "FAIL"
        
    print(f"Verification Result: {state.verification_status}")
    
    return state
