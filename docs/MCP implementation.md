### Key Points
- **Framework**: Python, using modelcontextprotocol/python-sdk
- **Model**: sklearn RandomForestRegressor
- **Features**: Synchronous prediction, no authentication/logging
- **Goal**: Expose the model via MCP so that an LLM or other client can query it for predictions
- **Input Features**: The model expects the following features as input (all numeric, from the previous season):
    - wOBA_lag1
    - HR_lag1
    - BB_lag1
    - HBP_lag1
    - 1B_lag1
    - 2B_lag1
    - 3B_lag1
    - AB_lag1
    - SF_lag1
    - IBB_lag1

---

## Step-by-Step Implementation

### 1. Save Your Trained Model

Train and save your RandomForestRegressor using joblib or pickle:
```python
from sklearn.ensemble import RandomForestRegressor
import joblib

# Train your model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "random_forest.pkl")
```

### 2. Implement MCP Server

Create a Python file (e.g., `mcp_server.py`) in your project root:

```python
from modelcontextprotocol.server import MCPServer, MCPModel
import joblib
import numpy as np

# List of features in the order expected by the model
FEATURE_ORDER = [
    "wOBA_lag1", "HR_lag1", "BB_lag1", "HBP_lag1", "1B_lag1",
    "2B_lag1", "3B_lag1", "AB_lag1", "SF_lag1", "IBB_lag1"
]

# Load the trained model
model = joblib.load("random_forest.pkl")

class SklearnRFModel(MCPModel):
    def predict(self, inputs):
        # Ensure input order matches training
        data = np.array([[row[feat] for feat in FEATURE_ORDER] for row in inputs])
        preds = model.predict(data)
        return preds.tolist()

if __name__ == "__main__":
    server = MCPServer()
    server.register_model("random_forest", SklearnRFModel())
    server.run()
```

#### Example Input Payload

```json
{
  "instances": [
    {
      "wOBA_lag1": 0.350,
      "HR_lag1": 25,
      "BB_lag1": 60,
      "HBP_lag1": 5,
      "1B_lag1": 80,
      "2B_lag1": 30,
      "3B_lag1": 2,
      "AB_lag1": 500,
      "SF_lag1": 5,
      "IBB_lag1": 3
    }
  ]
}
```

#### Notes:
- All input features are required and must be numeric.
- The order of features in the input dictionary must match FEATURE_ORDER.
- The MCP server will return a list of predicted next season's wOBA values.

### 3. Run Your Server

```bash
python mcp_server.py
```

### 4. Test the Endpoint

The MCP protocol uses HTTP/JSON. You can test prediction with curl or Postman:
```bash
curl -X POST http://localhost:8080/v1/models/random_forest:predict \
  -H "Content-Type: application/json" \
  -d '{"instances": [{"wOBA_lag1": 0.350, "HR_lag1": 25, "BB_lag1": 60, "HBP_lag1": 5, "1B_lag1": 80, "2B_lag1": 30, "3B_lag1": 2, "AB_lag1": 500, "SF_lag1": 5, "IBB_lag1": 3}]}'
```

---

## Summary

- Minimal, synchronous, no-auth server
- Uses the official MCP Python SDK
- Exposes your RandomForestRegressor via a standard protocol for LLM or other clients
- **Input features must match the lagged feature columns used in Batting.ipynb**