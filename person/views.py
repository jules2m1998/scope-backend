from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Person, Image
from .serializers import PersonSerializer, ImageSerializer
import face_recognition


# API PERSON
@api_view(['GET', ])
def api_detail_person(request, id_person):
    try:
        person = Person.objects.get(id=id_person)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = PersonSerializer(person)
        return Response(serializer.data)


# get all person in databases
@api_view(['GET', ])
def api_all_person(request):
    person = Person.objects.all()
    if request.method == "GET":
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)


# update one person
@api_view(['PUT', ])
def api_update_person(request, id_person):
    try:
        person = Person.objects.get(id=id_person)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        serializer = PersonSerializer(person, request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update successful !"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def api_delete_person(request, id_person):
    try:
        person = Person.objects.get(id=id_person)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        operation = person.delete()
        data = {}
        if operation:
            data["success"] = "Delete successful !"
        else:
            data["failure"] = "Delete failed !"
        return Response(data=data)


@api_view(['POST', ])
def api_create_person(request):
    if request.method == "POST":
        print(request.data)
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API IMAGE
@api_view(['GET', ])
def api_detail_image(request, id_image):
    try:
        image = Image.objects.get(id=id_image)
    except Image.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ImageSerializer(image)
        return Response(serializer.data)


@api_view(['GET', ])
def api_all_person_image(request, id_person):
    try:
        image = Image.objects.filter(id_person=id_person)
    except Image.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ImageSerializer(image, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
def api_all_image(request):
    image = Image.objects.all()
    if request.method == "GET":
        serializer = ImageSerializer(image, many=True)
        return Response(serializer.data)


@api_view(['PUT', ])
def api_update_image(request, id_image):
    try:
        image = Image.objects.get(id=id_image)
    except Image.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        serializer = ImageSerializer(image, request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update successful !"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def api_delete_image(request, id_image):
    try:
        image = Image.objects.get(id=id_image)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        operation = image.delete()
        data = {}
        if operation:
            data["success"] = "Delete successful !"
        else:
            data["failure"] = "Delete failed !"
        return Response(data=data)


@api_view(['POST', ])
def api_create_image(request):
    try:
        person = Person.objects.get(id=request.data['id_person'])
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
def find_person(request):
    if request.method == "POST":
        correspondances = []
        unknown = request.data['img'].file
        unknown_img = face_recognition.load_image_file(unknown)
        unknown_encoded = face_recognition.face_encodings(unknown_img)[0]

        known_imgs = Image.objects.all()
        for known_img in known_imgs:
            image = face_recognition.load_image_file(known_img.fullPictureLocation)
            encoded = face_recognition.face_encodings(image)[0]
            result = face_recognition.compare_faces([encoded], unknown_encoded)
            if result[0]:
                correspondances.append(known_img.id_person_id)
        set_list = set(correspondances)
        unique = list(set_list)
        return Response(data={'correspondances': unique}, status=status.HTTP_302_FOUND)
