from django.forms import ModelForm
from main.models import ClothingEntry

class ClothingEntryForm(ModelForm):
    class Meta:
        model = ClothingEntry
        fields = ["nama_item", "harga", "deskripsi"]  # Make sure the field names match the model
