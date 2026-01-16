from django.contrib import admin
from employee_app.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','name','email','department','role']
admin.site.register(Employee,EmployeeAdmin)
