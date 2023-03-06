from django.db import models
class Disease(models.Model):
    diseaseid=models.IntegerField()
    animal=models.CharField(max_length=50)
    name=models.CharField(max_length=300)
    treatment=models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "disease"

class Symptoms(models.Model):
    animal=models.CharField(max_length=50)
    question=models.TextField()
    step=models.CharField(max_length=50)
    class Meta:
        db_table = "symptoms"