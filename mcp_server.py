from mcp.server import MCPServer, MCPModel
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
