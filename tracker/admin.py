from django.contrib import admin
from . import models

# Register your models here.
class LevelAdmin(admin.ModelAdmin):
    search_fields = ('label',)
    ordering = ('-name',)
    list_display = ('label','name','created_on','updated_on')

admin.site.register(models.Status, LevelAdmin)
    
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ('label',)
    ordering = ('-name',)
    list_display = ('label','name','status','start_date','due_date')

admin.site.register(models.Project, ProjectAdmin)

class AssetAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('-name',)
    list_display = ('name','status',)

admin.site.register(models.Asset, AssetAdmin)

class EpisodeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('-name',)
    list_display = ('name',)

admin.site.register(models.Episode, EpisodeAdmin)

class SequenceAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('-name',)
    list_display = ('name',)

admin.site.register(models.Sequence, SequenceAdmin)

class ShotAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('-name',)
    list_display = ('name',)

admin.site.register(models.Shot, ShotAdmin)

class TaskAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('-name',)
    list_display = ('name',)

admin.site.register(models.Task, TaskAdmin)