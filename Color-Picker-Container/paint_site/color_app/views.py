from django.shortcuts import render
from django.views import View

from color_app.forms import ColorPickerForm


# Create your views here.

class ColorPickerView(View):
    def get(self, request):
        color_form = ColorPickerForm()

        
        
        red_value = 255
        green_value = 255
        blue_value = 255
        
        return render(
            request=request,
            template_name='color_picker.html',
            context=html_data,    
        )

    html_data = {
        'form': color_form,
        'red': red_value,
        'green': green_value,
        'blue': blue_value,
    }