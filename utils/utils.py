from person.models import Person, Image
from individual.models import Individual
from individual.serializers import IndividualSerializer
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
        return None
    imgsser = ImageSerializer(imgs, many=True)
    persondata['imgs'] = imgsser.data
    return persondata


def get_individu_wid_person(id_person):
    try:
        individu = Individual.objects.get(person_id=id_person)
        data = IndividualSerializer(individu).data
        data['person'] = get_person(id_person)
        return data
    except Individual.DoesNotExist:
        return None
