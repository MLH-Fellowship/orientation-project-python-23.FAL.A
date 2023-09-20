"""
Flask Application
"""
from flask import Flask, jsonify, request
from models import Experience, Education, Skill

app = Flask(__name__)

data = {
    "experience": [
        Experience(
            "Software Developer",
            "A Cool Company",
            "October 2022",
            "Present",
            "Writing Python Code",
            "example-logo.png",
        )
    ],
    "education": [
        Education(
            "Computer Science",
            "University of Tech",
            "September 2019",
            "July 2022",
            "80%",
            "example-logo.png",
        )
    ],
    "skill": [Skill("Python", "1-2 Years", "example-logo.png")],
}


@app.route("/test")
def hello_world():
    """
    Returns a JSON test message
    """
    return jsonify({"message": "Hello, World!"})


@app.route("/resume/experience", methods=["GET", "POST"])
def experience():
    """
    Handle experience requests
    """
    if request.method == "GET":
        return jsonify()

    if request.method == "POST":
        return jsonify({})

    return jsonify({})


@app.route("/resume/education", methods=["GET", "POST"])
def education():
    """
    Handles education requests
    """
    if request.method == "GET":
        return jsonify({})

    if request.method == "POST":
        return jsonify({})

    return jsonify({})


@app.route("/resume/skill", methods=["GET", "POST"])
def skill(): # pylint: disable=W0621
    """
    Handles Skill requests
    """
    if request.method == "GET":
        return jsonify("skill", data["skill"])

    if request.method == "POST":
        api_data = request.get_json()

        # Check if data is valid
        if api_data is None or api_data == {}:
            return jsonify({"message": "No data provided"}), 400

        name = api_data.get("name")
        proficiency = api_data.get("proficiency")
        logo = api_data.get("logo")

        skill = Skill(name, proficiency, logo) # pylint: disable=W0621
        data["skill"].append(skill)

        skills = data["skill"]
        index_position = skills.index(skill)

        return jsonify({"message": "New Skill added", "index position": index_position})

    return jsonify({})
