from django.db import models
from django.contrib.auth.models import User
import uuid

class ClothingEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_item = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    deskripsi = models.TextField()
