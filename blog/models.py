from django.db import models
from django.contrib.auth import get_user_model

# User/Author
User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE),
    profile_img = models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True),
    image_url = models.CharField(max_length=500, default=None, blank=True),
    categories = models.ManyToManyField(Category),
    author = models.ForeignKey(Author, on_delete=models.CASCADE),
    pub_date = models.DateTimeField(),
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    # display body text only 100 chars
    def summary(self):
        return self.content[:100]

    # format date
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
