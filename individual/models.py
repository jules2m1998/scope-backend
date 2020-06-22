from django.db import models
from person.models import Person


class Individual(models.Model):
    isFound = models.BooleanField(default=False)
    lose_date = models.DateField(auto_now_add=True)
    found_date = models.DateField(null=True)
    created_at = models.DateField(auto_now_add=True)
    person_id = models.OneToOneField(Person, on_delete=models.CASCADE, null=True)
