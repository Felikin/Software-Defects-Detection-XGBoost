import pickle
import pandas as pd
from flask import Flask
from flask import jsonify

model_file = 'xgb_model.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

app = Flask('midterm-project')

@app.route('/predict', methods=['POST'])
def predict():
    software = request.get_json()
    X = pd.read_json(software)
    y_pred = model.predict_proba(X)[0, 1]
    defects = y_pred >= 0.5

    result = {
        'defects_probability': float(y_pred),
        'defects': bool(defects)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
