from app.models.state import RemediationState
from app.services.llm import llm_service
import os

def blue_agent(state: RemediationState) -> RemediationState:
    """
    Blue Agent: Generates a fix for the vulnerability.
    """
    print("--- Blue Agent: Patching ---")
    
    with open(state.code_path, "r") as f:
        code_content = f.read()

    prompt = f"""
    You are an expert Secure Code Developer.
    Fixed the following code which has a {state.vulnerability_type}.
    An attacker found this exploit: {state.exploit_payloads[-1] if state.exploit_payloads else 'None'}
    
    Code:
    ```python
    {code_content}
    ```
    
    Provide the fixed code. Return ONLY the python code for the fixed file, without markdown formatting.
    """

    # Note: A better approach is to ask for a diff, but for simplicity asking for full code first
    # functionality to compute diff can be added here or just overwrite for now.
    
    fixed_code = llm_service.generate_text(prompt)
    
    # Strip markdown code blocks if present
    fixed_code = fixed_code.replace("```python", "").replace("```", "").strip()

    # Generate a simple diff (mocking a real diff for now to fit the state model)
    state.patch_diff = fixed_code # Storing full code in patch_diff for this iteration
    state.patch_explanation = "Applied secure coding practices."
    state.iteration_count += 1
    
    return state
