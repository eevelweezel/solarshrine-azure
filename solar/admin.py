from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget

from solar.models import (
    Home,
    Image,
    Post,
    Slide
)

class HomeAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Home
        fields = '__all__'

class ImageAdminForm(forms.ModelForm):
    text = forms.CharField(
                     required=False,
                     widget=CKEditorWidget())
    class Meta:
        model = Image
        fields = '__all__'


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(
                        required=False,
                        widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdminForm

class HomeAdmin(admin.ModelAdmin):
    form = HomeAdminForm

class ImageAdmin(admin.ModelAdmin):
    form = ImageAdminForm

admin.site.register(Post, PostAdmin)
admin.site.register(Slide)
admin.site.register(Image, ImageAdmin)
admin.site.register(Home, HomeAdmin)
