from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import uuid

# ===== TASKS =====

@api_view(['GET', 'POST'])
def tasks_list_create(request):
    if request.method == 'GET':
        tasks_ref = settings.FIRESTORE_DB.collection('tasks')
        docs = tasks_ref.stream()
        tasks = []
        for doc in docs:
            task = doc.to_dict()
            task['id'] = doc.id
            tasks.append(task)
        return Response(tasks)

    elif request.method == 'POST':
        data = request.data
        task_id = str(uuid.uuid4())
        new_task = {
            'title': data.get('title'),
            'description': data.get('description', ''),
            'status': data.get('status', 'pending'),
            'category': data.get('category', None)
        }
        settings.FIRESTORE_DB.collection('tasks').document(task_id).set(new_task)
        new_task['id'] = task_id
        return Response(new_task, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def task_detail(request, task_id):
    task_ref = settings.FIRESTORE_DB.collection('tasks').document(task_id)

    if request.method == 'PUT':
        task_ref.update(request.data)
        updated = task_ref.get().to_dict()
        updated['id'] = task_id
        return Response(updated)

    elif request.method == 'DELETE':
        task_ref.delete()
        return Response({'message': 'Tarea eliminada'}, status=status.HTTP_204_NO_CONTENT)


# ===== CATEGORIES =====

@api_view(['GET', 'POST'])
def categories_list_create(request):
    if request.method == 'GET':
        cat_ref = settings.FIRESTORE_DB.collection('categories')
        docs = cat_ref.stream()
        categories = []
        for doc in docs:
            category = doc.to_dict()
            category['id'] = doc.id
            categories.append(category)
        return Response(categories)

    elif request.method == 'POST':
        data = request.data
        cat_id = str(uuid.uuid4())
        new_cat = {'name': data.get('name')}
        settings.FIRESTORE_DB.collection('categories').document(cat_id).set(new_cat)
        new_cat['id'] = cat_id
        return Response(new_cat, status=status.HTTP_201_CREATED)
@api_view(['PUT', 'DELETE'])
def category_detail(request, category_id):
    cat_ref = settings.FIRESTORE_DB.collection('categories').document(category_id)

    if request.method == 'PUT':
        cat_ref.update(request.data)
        updated = cat_ref.get().to_dict()
        updated['id'] = category_id
        return Response(updated)

    elif request.method == 'DELETE':
        cat_ref.delete()
        return Response({'message': 'Categoría eliminada'}, status=status.HTTP_204_NO_CONTENT)
