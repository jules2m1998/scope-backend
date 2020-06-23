from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Individual
from .serializers import IndividualSerializer
from person.models import Person, Image
from person.serializers import PersonSerializer, ImageSerializer


# API Individual
@api_view(['GET', ])
def api_detail_individual(request, id_individual):
    try:
        individual = Individual.objects.get(id=id_individual)
    except Individual.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = IndividualSerializer(individual)
        indiv = serializer.data
        indiv['person'] = get_person(individual.person_id_id)
        return Response(indiv)


# get all individual in databases
@api_view(['GET', ])
def api_all_individual(request):
    individual = Individual.objects.all()
    if request.method == "GET":
        serializer = IndividualSerializer(individual, many=True)
        print(serializer.data[0]['id'])
        for indiv in serializer.data:
            each = indiv['person_id']
            if each:
                indiv['person'] = get_person(each)
        return Response(serializer.data)


# update one individual
@api_view(['PUT', ])
def api_update_individual(request, id_individual):
    try:
        individual = Individual.objects.get(id=id_individual)
    except Individual.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        serializer = IndividualSerializer(individual, request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update successful !"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def api_delete_individual(request, id_individual):
    try:
        individual = Individual.objects.get(id=id_individual)
    except Individual.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        operation = individual.delete()
        data = {}
        if operation:
            data["success"] = "Delete successful !"
        else:
            data["failure"] = "Delete failed !"
        return Response(data=data)


@api_view(['POST', ])
def api_create_individual(request):
    individual = Individual.objects.create()
    if request.method == "POST":
        print(request.data)
        serializer = IndividualSerializer(individual, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_person(id_person):
    try:
        person = Person.objects.get(id=id_person)
    except Person.DoesNotExist:
        return None
    personser = PersonSerializer(person)
    persondata = personser.data
    try:
        imgs = Image.objects.filter(id_person=id_person)
    except Image.DoesNotExist:
        return persondata
    imgsser = ImageSerializer(imgs, many=True)
    persondata['imgs'] = imgsser.data
    print(persondata)
    return persondata
