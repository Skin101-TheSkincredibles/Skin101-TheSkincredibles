from rest_framework import serializers
from reviews import models

class reviewSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username',
            'nama_produk',
            'isi_review',
            'date_created'
        )

        model = models.ReviewsModel