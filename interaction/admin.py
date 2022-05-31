from django.contrib import admin
from .models import Teacher, Member, ClassRoom, Checkout
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from interaction.models import Member

class MemberInline(admin.TabularInline):
    model = Member
    can_delete = False
    verbose_name_plural = "member"

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'class_room', 'teacher']
    list_per_page = 10
  
@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ['class_room', "day_of_week", "start_time", "end_time"]
    inlines = [MemberInline]
    list_per_page = 10

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher_name']
    inlines = [MemberInline]
    list_per_page = 10

@admin.register(Checkout)
class CheckOutAdmin(admin.ModelAdmin):
    list_display = ['checkout_time', 'checkout_choice', 'student', 'class_room']
    list_per_page = 10

class UserAdmin(BaseUserAdmin):
    inlines = (MemberInline,)
    list_per_page = 10

admin.site.unregister(User)
admin.site.register(User, UserAdmin)  