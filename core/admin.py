from django.contrib import admin
from core.models import Dataset, Visualisation

# Register your models here.
class DatasetAdmin(admin.ModelAdmin):
    #fields display on change list
    list_display = ['name','creator','created','sep']
    #enable the save buttons on top of change form
    save_on_top = True
    
class VisualisationAdmin(admin.ModelAdmin):
    #fields display on change list
    list_display = ['dataset','chart_type','creator','created']
    #enable the save buttons on top of change form
    save_on_top = True

    
admin.site.register(Dataset,DatasetAdmin)
admin.site.register(Visualisation,VisualisationAdmin)
