from django.db import models

# Create your models here.
class ReviewModel(models.Model):
    TIPE = (
        ("SENSITIVE", "SENSITIVE"),
        ("OILY", "OILY"),
        ("NORMAL", "NORMAL"),
        ("ACNE-PRONE", "ACNE-PRONE"),
        ("DRY", "DRY"),
        ("ALL-SKIN", "ALL-SKIN")
    )

    username = models.CharField(max_length=100)
    nama_produk = models.CharField(max_length=200, null=True)
    isi_review = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    tipe = models.CharField(max_length=200, null=True, choices=TIPE)
    def __str__(self):
        return self.nama_produk
