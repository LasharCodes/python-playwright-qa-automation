

def test_get_users(api_request):
  response = api_request.get("/users")
  
  assert response.status == 200
  
  users = response.json()
  
  assert isinstance(users, list)
  assert len(users) == 10
  
  print(f"API returned {len(users)} users")


def test_get_single_user(api_request):
    response = api_request.get("/users/1")


    assert response.status == 200

    user = response.json()

    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"
    assert user["username"] == "Bret"
    assert user["email"] == "Sincere@april.biz"

    print(f"Validated user: {user['name']}")


def test_create_post(api_request):
    new_post = {
            "title": "Learning API Automation",
            "body": "Testing POST requests with Playwright",
            "userId": 1,
        }
    response = api_request.post(
        "/posts",
        data=new_post,
    )

    assert response.status == 201

    created_post = response.json()

    assert created_post["title"] == new_post["title"]
    assert created_post["body"] == new_post["body"]
    assert created_post["userId"] == new_post["userId"]
    assert "id" in created_post

    print(f"Created post ID: {created_post['id']}")


def test_update_post_put(api_request):
    updated_post = {
        "id": 1,
        "title": "Updated with PUT",
        "body": "Learning full resource updates",
        "userId": 1,
    }

    response = api_request.put(
        "/posts/1",
        data=updated_post,
    )

    assert response.status == 200

    result = response.json()

    assert result["id"] == 1
    assert result["title"] == updated_post["title"]
    assert result["body"] == updated_post["body"]
    assert result["userId"] == updated_post["userId"]

    print("PUT request validated successfully")


def test_update_post_patch(api_request):
    response = api_request.patch(
         "/posts/1",
        data={
            "title": "Updated with PATCH"
        },
    )

    assert response.status == 200
        
    result = response.json()

    assert result["id"] == 1
    assert result["title"] == "Updated with PATCH"

    print("PATCH request validated successfully")


def test_delete_post(api_request):
   response = api_request.delete(
       "/posts/1"
    )
   
   assert response.status == 200
   
   print("DELETE request validated successfully")


def test_get_nonexistent_post(api_request):
    response = api_request.get(
        "/posts/999999"
    )

    assert response.status == 404

    print("Nonexistent post correctly returned 404")


def test_invalid_api_endpoint(api_request):
    response = api_request.get(
        "/invalid-endpoint"
    )

    assert response.status == 404

    print("Invalid endpoint correctly returned 404")

