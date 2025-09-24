from django.forms import ModelForm
from main.models import Item
# from main.models import Car

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price", "category", "thumbnail", "is_featured", "description"]

# class CarForm(ModelForm):
#     class Meta:
#         model = Car
#         fields = ["name", "brand", "stock"]