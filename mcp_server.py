from mcp.server.fastmcp import FastMCP
import joblib
import numpy as np
import logging
from datetime import datetime, timezone
import hashlib

tool_name = "predict_hr_per_ab"

logging.basicConfig(
    filename="mcp_server.log",
    level=logging.INFO,
    format="%(message)s"
)

model = joblib.load("random_forest.pkl")

mcp = FastMCP("HRpAB Predictor")

@mcp.tool()
def predict_hr_per_ab(
    HR_per_AB_lag1: float,
    HR_per_AB_lag2: float,
    HR_per_AB_lag3: float,
    requester_tag: str = "unknown"
) -> float:
    """Predict HR per AB using lag features. Logs each invocation for compliance."""
    
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    input_str = f"{HR_per_AB_lag1:.4f}{HR_per_AB_lag2:.4f}{HR_per_AB_lag3:.4f}"
    input_hash = hashlib.sha256(input_str.encode()).hexdigest()

    log_entry = (
        f"timestamp={timestamp} "
        f"tool={tool_name} "
        f"input_hash={input_hash} "
        f"requester_tag={requester_tag}"
    )
    logging.info(log_entry)

    data = np.array([[HR_per_AB_lag1, HR_per_AB_lag2, HR_per_AB_lag3]])
    pred = model.predict(data)
    
    return float(pred[0])

if __name__ == "__main__":
    mcp.run()
