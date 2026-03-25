from flask import Flask, render_template, request
from utils.health_score import calculate_score
from utils.ai_advisor import get_ai_advice
from utils.predictor import predict_future_score
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    steps = int(request.form['steps'])
    sleep = float(request.form['sleep'])
    heart = int(request.form['heart'])
    stress = int(request.form['stress'])

    score = calculate_score(steps, sleep, heart, stress)
    predicted = predict_future_score(steps, sleep, heart, stress)
    advice = get_ai_advice(steps, sleep, heart, stress)
    chart = generate_chart(score, predicted)

    return render_template(
    "result.html",
    score=score,
    predicted=predicted,
    advice=advice,
    chart=chart
) 
def generate_chart(score, predicted):
    values = [score, predicted]
    labels = ["Current", "Predicted"]

    plt.figure()
    plt.bar(labels, values)
    plt.title("Health Score Comparison")

    chart_path = "static/chart.png"
    plt.savefig(chart_path)
    plt.close()

    return chart_path
if __name__ == '__main__':
    app.run(debug=True)