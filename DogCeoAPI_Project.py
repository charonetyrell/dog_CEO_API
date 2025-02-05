import requests

#Test case to check the random dog image
def test_get_random_dog_image():
    
    #Send request
    response = requests.get("https://dog.ceo/api/breeds/image/random")

    #Check status code = 200
    assert response.status_code == 200

    #Parse the response
    json_data = response.json()

    #Assert status
    assert json_data["status"] == "success"

    #Assert the message field exists
    assert "message" in json_data

    #Assert the message field contains url
    assert json_data["message"].startswith("https://")
    print("Test passed for test_get_random_dog_image")

test_get_random_dog_image()

#Test case to check the breed list
def test_get_breed_list():

    #Send request
    response = requests.get("https://dog.ceo/api/breeds/list/all")

    #Check status code = 200
    assert response.status_code == 200

    #Parse the response
    json_data = response.json()

    #Assert status
    assert json_data["status"] == "success"

    #Assert the message field exists
    assert "message" in json_data

    #Assert the message field contains a dictionary
    assert isinstance(json_data["message"], dict)
    print("Test passed for test_get_breed_list")

test_get_breed_list()

#Test case to check the images by breed
def test_get_images_by_breed():
    breed = "hound"

    #Send request
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images")

    #Check status code = 200
    assert response.status_code == 200

    #Parse the response
    json_data = response.json()

    #Assert status
    assert json_data["status"] == "success"

    #Assert the message field exists
    assert "message" in json_data

    #Assert the message field contains a list
    assert isinstance(json_data["message"], list)
    print("Test passed for test_get_images_by_breed")

test_get_images_by_breed()

#Test Case to check the sub-breed list
def test_get_sub_breed():
    breed = "bulldog"

    #Send request
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/list")

    #Check status code = 200
    assert response.status_code == 200

    #Parse the response
    json_data = response.json()

    #Assert status
    assert json_data["status"] == "success"

    #Assert the message field exists
    assert "message" in json_data

    #Assert the message field contains a list
    assert isinstance(json_data["message"], list)
    print("Test passed for test_get_sub_breed")

test_get_sub_breed()