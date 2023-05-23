from django.conf import settings
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic.edit import FormView
from solar.forms import CaptchaContactForm
from solar.models import (
    Home,
    Image,
    Post,
    Slide
)


def get_home_page(request, *args, **kwargs):
    posts = Post.objects.filter(published=True).order_by('id')
    slides = Slide.objects.all().order_by('id').values()
    home = Home.objects.all().values()
    return TemplateResponse(
               request,
               'home.html',
               context={'posts': posts,
                        'slides': slides,
                        'home': home},
               status=200)

def get_post(request, slug, *args, **kwargs):
    post = Post.objects.get(slug=slug)
    images = Image.objects.filter(post_id=post.id, 
                                  video=False).order_by('id')
    videos = Image.objects.filter(post_id=post.id,
                                  video=True).values()
    posts = Post.objects.filter(published=True).order_by('id')
    return TemplateResponse(
               request,
               'post.html',
               context={'post': post,
                        'videos': videos,
                        'posts': posts,
                        'images': images},
               status=200)

def thanks_view(request, *args, **kwargs):
    posts = Post.objects.filter(published=True).order_by('id')
    return TemplateResponse(
               request,
               'thanks.html',
               context={'posts': posts},
               status=200)


class ContactView(FormView):
    form_class = CaptchaContactForm
    template_name = 'contact.html'
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(published=True).order_by('id')
        return TemplateResponse(
                   request,
                   'contact.html',
                   context={'posts': posts,
                            'form': self.form_class()},
                   status=200)
        
