from django.db import models


class Post(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE,related_name='posts')
    title = models.CharField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    cover_image = models.ImageField(upload_to='cover/')


class User(models.Model):
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    online_status = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatar/')

    def __str__(self) -> str:
        return self.name


class State(models.Model):
    state_name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.state_name


class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE ,related_name='districts')
    district_name = models.CharField(max_length=150)

    def __str__(self):
        return '%d: %s' % (self.id, self.district_name)
