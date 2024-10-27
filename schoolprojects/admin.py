from django.contrib import admin
from .models import Project
'''
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'room_number')  # Specify the fields to display in the list
    search_fields = ('name',)  # Optional: Enable search by project name
    list_filter = ('room_number',)
    #readonly_fields = ('name', 'room_number')
# Register the Project model with the custom ProjectAdmin
admin.site.register(Project, ProjectAdmin) 
'''