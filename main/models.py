import uuid
from django.db import models

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)  # Nama item, misalnya "Jersey Home 2025"
    price = models.IntegerField()  # Harga item dalam rupiah
    description = models.TextField()  # Deskripsi lengkap item
    thumbnail = models.URLField()  # URL gambar item
    category = models.CharField(max_length=50)  # Kategori item, misalnya "Jersey", "Sepatu", "Bola"
    is_featured = models.BooleanField(default=False)  # Status item unggulan

    def __str__(self):
        return f"{self.name} - Rp{self.price}"


    
# class Employee(models.Model):
#     name = models.CharField(max_length=255) #tipe datanya char ==> bisa nampung beberapa kata teteapi memiliki limit
#     age = models.IntegerField()
#     persona = models.TextField() #tipe datanya text ==> bisa nampung banyak kata dan dia bentuknya tuh kayak text box gitu

