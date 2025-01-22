from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    client = models.ForeignKey(CustomUser, related_name='projects', on_delete=models.CASCADE)
    workers = models.ManyToManyField(CustomUser, related_name='assigned_projects', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    client = models.ForeignKey(CustomUser, related_name='reviews_as_client', on_delete=models.CASCADE)
    worker = models.ForeignKey(CustomUser, related_name='reviews_as_worker', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review from {self.client.username} to {self.worker.username}"


class Image(models.Model):
    worker = models.ForeignKey(
        CustomUser,
        related_name='images',
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': True},
    )
    image = models.ImageField(upload_to='workers/')
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'Image of {self.worker.username}'
