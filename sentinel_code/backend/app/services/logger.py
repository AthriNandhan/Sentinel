import json
import logging
import os
from datetime import datetime
from typing import Any, Dict

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

class WorkflowLogger:
    def __init__(self, workflow_id: str):
        self.workflow_id = workflow_id
        self.log_file = os.path.join(LOG_DIR, f"{workflow_id}.json")
        self._initialize_log()

    def _initialize_log(self):
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w") as f:
                json.dump({"workflow_id": self.workflow_id, "events": []}, f)

    def log_event(self, agent: str, action: str, details: Dict[str, Any]):
        timestamp = datetime.utcnow().isoformat()
        event = {
            "timestamp": timestamp,
            "agent": agent,
            "action": action,
            "details": details
        }
        
        with open(self.log_file, "r+") as f:
            data = json.load(f)
            data["events"].append(event)
            f.seek(0)
            json.dump(data, f, indent=4)

    def get_logs(self):
        with open(self.log_file, "r") as f:
            return json.load(f)

def get_logger(workflow_id: str) -> WorkflowLogger:
    return WorkflowLogger(workflow_id)
