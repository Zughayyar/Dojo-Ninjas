from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(default="old dojo")

class Ninja(models.Model):
    dojo_id = models.ForeignKey(Dojo, related_name="ninjas" , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

def get_all_dojos():
    return Dojo.objects.all()

def get_all_ninjas():
    return Ninja.objects.all()

def add_dojo(data):
    Dojo.objects.create(
        name=data['dojo_name'], 
        city=data['dojo_city'], 
        state=data['dojo_state']
        )

def delete_dojo(dojo_id):
    c = Dojo.objects.get(id=dojo_id)
    c.delete()


def add_ninja(data):
    Ninja.objects.create(
        dojo_id=Dojo.objects.get(id=data['dojo_id']),
        first_name=data['ninja_first_name'],
        last_name=data['ninja_last_name']
        )

def delete_ninja(dojo_id):
    c = Ninja.objects.get(id=dojo_id)
    c.delete()