from django.db import models
from django.contrib.auth.models import User  # optional, username/password साठी default User model वापरू शकता

class Principal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class LoginAttempt(models.Model):
    username = models.CharField(max_length=100)
    role = models.CharField(max_length=50, default="principal")
    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.role} at {self.login_time}"