from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Question banks
easy_questions = [
    "What is a REST API?",
    "What is a database?",
    "Explain OOP in simple terms."
]

medium_questions = [
    "Explain load balancing.",
    "Difference between SQL and NoSQL?",
    "What is caching?"
]

hard_questions = [
    "Design a scalable API handling 1M requests/day.",
    "How would you design a distributed system?",
    "Explain microservices architecture."
]

brain_teasers = [
    "A bat and ball cost 110. Bat costs 100 more than ball. What is ball price?",
    "You have two ropes that burn in 60 minutes. Measure 45 minutes.",
    "Three switches control three bulbs in another room. How identify them?"
]


@app.route("/")
def home():
    return "AI Interview System Running"


@app.route("/question")
def question():
    level = request.args.get("level", "easy")

    if level == "easy":
        q = random.choice(easy_questions)
    elif level == "medium":
        q = random.choice(medium_questions)
    else:
        q = random.choice(hard_questions)

    return jsonify({"question": q})


@app.route("/brain_teaser")
def teaser():
    q = random.choice(brain_teasers)
    return jsonify({"brain_teaser": q})


@app.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.json
    answer = data.get("answer")

    score = 0

    if len(answer) > 15:
        score += 5

    if "design" in answer.lower():
        score += 3

    return jsonify({
        "score": score,
        "message": "AI evaluated the response"
    })


if __name__ == "__main__":
    app.run(debug=True)
