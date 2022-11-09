from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField('Technology', upload_to='technology/', max_length=255, null=False, blank=False)

    def __str__(self):
        self.name

class Project(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    technologies = models.ManyToManyField(Technology, through='TechnologiesProject', through_fields=('project', 'technology'))
    repo = models.CharField(max_length=124, null=False, blank=False)
    deploy = models.CharField(max_length=124)
    description = models.TextField(null=True)
    image = models.ImageField('Project', upload_to='project/', max_length=255, null=False)
    
    def __str__(self):
        self.name

class TechnologiesProject(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)