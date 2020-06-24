from person.models import Person, Image
from person.serializers import PersonSerializer, ImageSerializer


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