from django.db import models

class Brand(models.Model):#Marca
    idBrand = models.AutoField(primary_key=True)#Chave primária
    name = models.CharField(max_length=200)#Nome

    def __str__(self):#Retorna o nome
        return self.name


class Car(models.Model):
    idCar = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)#Modelo
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')#Chave estrangeira de marca
    factory_year = models.IntegerField(blank=True, null=True)#Ano de fabricação
    model_year = models.IntegerField(blank=True, null=True)#Ano do veículo
    plate = models.CharField(max_length=10, blank=True, null=True)#Placa
    value = models.FloatField(blank=True, null=True)#Valor do veículo
    photo = models.ImageField(upload_to='cars/', default='cars/default.jpg')#Foto
    bio = models.TextField(blank=True, null=True)#Descrição

    def __str__(self):
        return self.model
    
class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'