from django.db import models

# Create your models here.

class Cluster(models.Model):
    name = models.CharField(max_length=100)
    length = models.FloatField(null=False)
    width = models.FloatField(null=False)
    height = models.FloatField(null=False)

    def __str__(self):
        return self.name + ' | ' + str(self.length) + 'm x ' + str(self.width) + 'm x ' + str(self.height)

class Location(models.Model):
    cluster = models.ForeignKey('Cluster', on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    is_serviceable = models.BooleanField(default=True)

    def __str__(self):
        return self.city + ' @ ' + self.cluster.name

class Package(models.Model):
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    length = models.FloatField(null=False)
    width = models.FloatField(null=False)
    height = models.FloatField(null=False)
    weight = models.FloatField(null=False)
    x1 = models.FloatField(null=False)
    x2 = models.FloatField(null=False)
    y1 = models.FloatField(null=False)
    y2 = models.FloatField(null=False)
    z1 = models.FloatField(null=False)
    z2 = models.FloatField(null=False)
    arrival_date = models.DateTimeField(auto_now_add=True)
    is_fragile = models.BooleanField(default=False)

    def __str__(self):
        return 'L:' + str(self.length) + ' | Wi:'+ str(self.width) + ' | H:'+ str(self.height) + ' | We:' + str(self.weight)



