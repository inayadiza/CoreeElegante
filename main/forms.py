from django.forms import ModelForm
from main.models import ClothingEntry
from django.utils.html import strip_tags

class ClothingEntryForm(ModelForm):
    class Meta:
        model = ClothingEntry
        fields = ["nama_item", "harga", "deskripsi"]  # Make sure the field names match the model

    def clean_clothing(self):
        nama_item = self.cleaned_data["nama_item"]
        return strip_tags(nama_item)

    def clean_price(self):
        harga = self.cleaned_data["harga"]
        return strip_tags(harga)
    
    def clean_desc(self):
        deskripsi = self.cleaned_data["deskripsi"]
        return strip_tags(deskripsi)