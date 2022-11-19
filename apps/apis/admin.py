from .models import User, District, State
from django.contrib import admin
from .models import Post, Image
admin.site.register(Post)
admin.site.register(Image)
admin.site.register(User)
# admin.site.register(District)
admin.site.register(State)


@admin.register(District)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("district_name", "state",)
    list_filter = ("state", )

    class Meta:
        ordering = ("state",)


class BookInline(admin.StackedInline):
    model = District


class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]
