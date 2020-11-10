from django.contrib import admin

from board.models import Board, Employee


class BoardAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['id', 'title', 'userid', 'regdate']
    list_filter = ['title', 'userid', 'regdate']

class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['fname','lname','jobid']
    list_display = ['fname', 'lname', 'email', 'phone', 'hdate', 'sal']
    list_filter = ['hdate', 'jobid', 'deptid', 'mgrid']

admin.site.register(Board, BoardAdmin)
admin.site.register(Employee, EmployeeAdmin)
