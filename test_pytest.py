'''
Title: Tests in Pytest
Author: Your Name
Date: September 20, 2023
Description: This module contains unit tests for the 'app' using Pytest.
'''

from app import app

def test_client():
    '''
    Test Case: test_client
    Description: Makes a request and checks the message received is the same.
    '''
    response = app.test_client().get('/test')
    assert response.status_code == 200
    assert response.json['message'] == "Hello, World!"

def test_experience():
    '''
    Test Case: test_experience
    Description: Add a new experience and then get all experiences.
                 Check that it returns the new experience in that list.
    '''
    example_experience = {
        "title": "Software Developer",
        "company": "A Cooler Company",
        "start_date": "October 2022",
        "end_date": "Present",
        "description": "Writing JavaScript Code",
        "logo": "example-logo.png",
        "order": 1
    }

    item_id = app.test_client().post('/resume/experience',
                                     json=example_experience).json['id']
    response = app.test_client().get('/resume/experience')
    assert response.json[item_id] == example_experience

def test_education():
    '''
    Test Case: test_education
    Description: Add a new education and then get all educations.
                 Check that it returns the new education in that list.
    '''
    example_education = {
        "course": "Engineering",
        "school": "NYU",
        "start_date": "October 2022",
        "end_date": "August 2024",
        "grade": "86%",
        "logo": "example-logo.png",
        "order": 2
    }
    item_id = app.test_client().post('/resume/education',
                                     json=example_education).json['id']

    response = app.test_client().get('/resume/education')
    assert response.json[item_id] == example_education

def test_skill():
    '''
    Test Case: test_skill
    Description: Add a new skill and then get all skills.
                 Check that it returns the new skill in that list.
    '''
    example_skill = {
        "name": "JavaScript",
        "proficiency": "2-4 years",
        "logo": "example-logo.png",
        "order": 3
    }

    item_id = app.test_client().post('/resume/skill',
                                     json=example_skill).json['id']

    response = app.test_client().get('/resume/skill')
    assert response.json[item_id] == example_skill

def test_delete_experience():
    """
    Test Case: test_delete_experience
    Description: Delete an experience and then check that it's no longer in the list
    """

    example_experience = {
        "title": "Software Engineer",
        "company": "Tech Corp",
        "start_date": "January 2020",
        "end_date": "December 2021",
        "description": "Developing software solutions",
        "logo": "example-logo.png",
    }

    # Add a new experience
    item_id = (
        app.test_client().post("/resume/experience", json=example_experience).json["id"]
    )

    # Delete the added experience
    response = app.test_client().delete(f'/resume/experience?index={item_id}')
    assert response.status_code == 200  # Check for a successful delete
    assert "message" in response.json
    assert response.json["message"] == "Experience deleted successfully"

    # Check that the deleted experience is no longer in the list
    response_after_deletion = app.test_client().get("/resume/experience")
    assert item_id not in response_after_deletion.json
