import pytest
from rest_framework.test import APIClient
from todo.models import Task
from django.urls import reverse
from django.contrib.auth.models import User



@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def common_user():
    user = User.objects.create(username='test_api',password='a/@123456')
    return user

@pytest.fixture
def create_task():
    user = User.objects.get(username='test_api')

    task = Task.objects.create(content='test_api',user=user)
    return task



@pytest.mark.django_db
class TestTodoApi:

    def test_get_tasks_list_response_200(self,api_client,common_user):
        url = reverse("todo:api-tasks-list")
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.get(url)
        assert response.status_code == 200

    def test_get_tasks_list_no_login_response_403(self,api_client,common_user):
        url = reverse("todo:api-tasks-list")
        user = common_user
        response = api_client.get(url)
        assert response.status_code == 403

    def test_create_task_response_201(self,api_client,common_user):
        url = reverse("todo:api-tasks-list")
        user = common_user
        data = {
            'content':'test content'
        }
        
        api_client.force_authenticate(user=user)
        response = api_client.post(url,data)
        assert response.status_code == 201

    def test_create_task_invalid_data_response_400(self,api_client,common_user):
        url = reverse("todo:api-tasks-list")
        user = common_user
        data = {
            'test':'test invalid data'
        }
        
        api_client.force_authenticate(user=user)
        response = api_client.post(url,data)
        assert response.status_code == 400


    def test_get_task_detail_response_200(self,api_client,common_user,create_task):
        url = reverse("todo:api-tasks-detail",kwargs={"pk":create_task.id})
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.get(url)
        assert response.status_code == 200


    def test_update_task_detail_response_200(self,api_client,common_user,create_task):
        url = reverse("todo:api-tasks-detail",kwargs={"pk":create_task.id})
        user = common_user
        api_client.force_authenticate(user=user)
        data = {
            'content':'test api task update'
        }
        response = api_client.put(url,data)
        print(response)
        assert response.status_code == 200


    def test_delete_task_detail_response_204(self,api_client,common_user,create_task):
        url = reverse("todo:api-tasks-detail",kwargs={"pk":create_task.id})
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.delete(url)
        print(response)
        assert response.status_code == 204
