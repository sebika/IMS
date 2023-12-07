from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connection

def index(request):
    if request.method != 'GET':
        return HttpResponse(status=405)

    with connection.cursor() as cursor:
        # cursor.execute("""
        #         SELECT name, price FROM
        #             cpus, gpus, memories, components
        #         WHERE cpus.id = components.id OR gpus.id = components.id OR memories.id = components.id;
        # """)
        cursor.execute("""
                SELECT id, name, price FROM components;
        """)
        entries = cursor.fetchall()

    response = [{
        'id': e[0],
        'name': e[1]
    } for e in entries]

    print(response)

    return JsonResponse({
        'response': response
    })

# Create your views here.
