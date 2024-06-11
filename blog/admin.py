from django.contrib import admin

# Register your models here.
from .models import BlogAuthor, Blog, BlogComment
admin.site.register(BlogAuthor)
admin.site.register(BlogComment)


class BlogCommentsInline(admin.TabularInline): #admin.TabularInline: 1 loại inline form mà Django sử dụng để hiển thị các đối tượng dưới dạng bảng
    model = BlogComment
    max_num=0

@admin.register(Blog)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'post_date')
    inlines = [BlogCommentsInline]