from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserModel(User):
	MANAGEMENT_LOCATIONS_CHOICES = [
		('option1', '구역 1'),
		('option2', '구역 2'),
		('option3', '구역 3'),
		('option4', '구역 4'),
		('option5', '구역 5'),
		('option6', '구역 6'),
		('option7', '구역 7'),
		('option8', '구역 8'),
		('option9', '구역 9'),
	]
	management_locations = models.CharField(max_length=100, choices=MANAGEMENT_LOCATIONS_CHOICES)
	phone = models.CharField(max_length=100)
	nickname = models.CharField(max_length=100)

	