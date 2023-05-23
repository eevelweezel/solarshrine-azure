from django.db import models



class Post(models.Model):
    slug = models.SlugField(
               max_length=50)
    content = models.TextField(
                         blank=True,
                         null=True,
                         default=' ')
    link_text = models.CharField(
                max_length=256)
    title = models.CharField(
                max_length=256)
    create_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return f'/pages/{self.slug}/'


class Slide(models.Model):
    image = models.FileField(upload_to='slides')
    text = models.CharField(max_length=256)

class Home(models.Model):
    content = models.TextField()

class Image(models.Model):
    post = models.ForeignKey(
                      Post,
                      blank=True, 
                      null=True,
                      on_delete=models.CASCADE)
    image = models.FileField(upload_to='images')
    text = models.TextField(blank=True, 
                            null=True,
                            default=None)
    video = models.BooleanField()

