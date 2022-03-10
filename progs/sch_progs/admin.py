from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.
from .models import School, Program


class ProgramResource(resources.ModelResource):
    class Meta:
        model = Program

class SchoolResource(resources.ModelResource):
    class Meta:
        model = School
        exclude = ('id',)
        import_id_fields = ('code',)

class SchoolAdmin(ImportExportModelAdmin):
    resource_class = SchoolResource
    list_display = ('name', 'type', 'code')
    search_fields = ['name']

admin.site.register(School, SchoolAdmin)

class ProgramAdmin(ImportExportModelAdmin):
    resource_class = ProgramResource
    list_display = ('school1', 'title', 'category', 'timestamp')
    search_fields = ['title', 'school1__name']

admin.site.register(Program, ProgramAdmin)