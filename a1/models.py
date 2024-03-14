from django.db import models
# from django.contrib.auth.models import User

class data(models.Model):
   RI=models.FloatField()
   Na=models.FloatField()
   Mg=models.FloatField()
   AI=models.FloatField()
   Si=models.FloatField()
   K=models.FloatField()
   Ca=models.FloatField()
   Ba=models.FloatField()
   Fe=models.FloatField()