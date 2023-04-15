from django.contrib import admin
from .models import UserProfile, Media, Portfolio, Skill


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user")


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    readonly_fields = ("slug",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "score")
