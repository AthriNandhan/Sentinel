import os
import subprocess

def ping_host(hostname):
    """
    Level: MEDIUM
    Vulnerability: Command Injection
    Why: Uses a blacklist that is easy to bypass.
    """
    
    # Weak security attempt: Blacklisting common separators
    bad_chars = [";", "&", "|"]
    for char in bad_chars:
        if char in hostname:
            return "Invalid character detected!"
            
    # Vulnerability: Doesn't block newlines, backticks, or $()
    # Exploit: `ls` or $(ls) or using encoded characters
    command = f"ping -c 1 {hostname}"
    
    try:
        # shell=True is the root cause
        output = subprocess.check_output(command, shell=True)
        return output.decode()
    except Exception as e:
        return str(e)
