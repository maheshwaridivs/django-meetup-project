from django.db import models

# Create your models here.


class Location(models.Model):

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class Participant(models.Model):

    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.email}'


class Meetup(models.Model):

    title = models.CharField(max_length=500)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(
        Participant,blank=True, null=True)  # it will create extra table

    # to change view name for created records in admin panel
    # def __str__(self):
    # 	return {
