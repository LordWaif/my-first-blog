from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Especialidade(models.Model):
    Tipo = models.CharField(max_length=50)
    Salario = models.FloatField()
    def __str__(self):
        return self.Tipo
    

class Medico(models.Model):
    Especialidade = models.ForeignKey('Especialidade',on_delete=models.CASCADE)
    Nome = models.CharField(max_length=50)
    CRM = models.IntegerField(primary_key=True)
    CPF = models.CharField(max_length=11)
    Data_de_Nascimento = models.DateField()
    Email = models.EmailField()

    def __str__(self):
        return self.Nome

    
