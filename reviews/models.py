from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
class ReviewsModel(models.Model):
    TIPE = (
        ("SENSITIVE", "SENSITIVE"),
        ("OILY", "OILY"),
        ("NORMAL", "NORMAL"),
        ("ACNE-PRONE", "ACNE-PRONE"),
        ("DRY", "DRY"),
        ("ALL-SKIN", "ALL-SKIN")
    )

    username = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    nama_produk = models.CharField(max_length=200, null=True)
    isi_review = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    tipe = models.CharField(max_length=200, null=True, choices=TIPE)
    likes = models.ManyToManyField(User, related_name='reviews')
    image = models.ImageField(upload_to='images', default=None)  
    #slug = models.SlugField(default=slugify(nama_produk), unique=True)
    
    def __str__(self):
        return self.nama_produk
    
    def number_of_likes(self):
        return self.likes.count()