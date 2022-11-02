from django.urls import reverse
from students.models import Course, Student
import pytest
from rest_framework.test import APIClient
from model_bakery import baker


# создание api-client'а --> можно указывать в качестве входного аргумента в функции
@pytest.fixture
def client():
    return APIClient()

# создание фабрики студентов --> можно указывать в качестве входного аргумента в функции
@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

# создание фабрики курсов --> можно указывать в качестве входного аргумента в функции    
@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_create_course(client):
    
    count_course = Course.objects.count()
    student = Student.objects.create(
        name = 'Nikolay',
        birth_date = '1985-05-31'
    )

    data = {'name': 'Python', 'students': [student.id]}
    response = client.post('/api/v1/courses/', data, format = 'json')
    
    assert response.status_code == 201
    assert Course.objects.count() == count_course + 1


@pytest.mark.django_db
def test_update_course(client, course_factory):
    
    courses = course_factory(_quantity=10)
    course = courses[3]    
    new_course = {'name': 'Python'}

    url = reverse('courses-detail', args=[course.pk])
    response = client.put(url, new_course)
        
    assert response.status_code == 200
    data = response.json()
    assert new_course['name'] == data['name']



@pytest.mark.django_db
def test_get_courses_list(client, course_factory):
    courses = course_factory(_quantity=10)
    
    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()    
    assert len(data) == len(courses)
    for i, course in enumerate(data):
        assert course['name'] == courses[i].name


@pytest.mark.django_db
def test_get_course(client, course_factory):
    
    courses = course_factory(_quantity=10)
    course = courses[3]    
    
    url = reverse('courses-detail', args=[course.pk])
    response = client.get(url)

    assert response.status_code == 200
    data = response.json()    
    assert course.name == data['name']



@pytest.mark.django_db
def test_filter_course_by_name(client, course_factory):
  
    courses = course_factory(_quantity=10) 
    course = courses[5] 

    data = {'name': course.name}
    response = client.get('/api/v1/courses/', data) 
   
    assert response.status_code == 200
    data = response.json()     
    assert course.name == data[0]['name']


@pytest.mark.django_db
def test_filter_course_by_id(client, course_factory):
  
    courses = course_factory(_quantity=10)
    course = courses[5] 

    data = {'id': course.id}    
    response = client.get('/api/v1/courses/', data)    

    assert response.status_code == 200
    data = response.json()    
    assert course.id == data[0]['id']  
   
    
   
    
    
    




    




