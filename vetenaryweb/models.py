from django.db import models
class Disease(models.Model):
    diseaseid=models.IntegerField()
    animal=models.CharField(max_length=50)
    name=models.CharField(max_length=300)
    treatment=models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "disease"

class FeedBack(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=300)
    message=models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "feedback"