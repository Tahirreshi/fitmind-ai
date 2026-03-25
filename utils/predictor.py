def predict_future_score(steps, sleep, heart, stress):
    import pickle
    import numpy as np

    with open("model/model.pkl", "rb") as f:
        model = pickle.load(f)

    calories = steps * 0.04  

    input_data = np.array([[steps, sleep, calories, stress]])
    prediction = model.predict(input_data)[0]

    return round(prediction, 2)