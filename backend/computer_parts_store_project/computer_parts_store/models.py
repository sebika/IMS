from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, first_name='admin', last_name='admin', **extra_fields):
        if not email:
            raise ValueError('Users must have an email')
        if not first_name:
            raise ValueError('Users must have an first name')
        if not last_name:
            raise ValueError('Users must have an last name')

        email = self.normalize_email(email)
        user = self.model(email=email,
                          first_name=first_name,
                          last_name=last_name,
                          **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    # REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'[{self.first_name} {self.last_name} - {self.email}]'


class Component(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    brand = models.CharField(max_length=255, blank=False, null=False)
    series = models.CharField(max_length=255, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    category = models.CharField(max_length=255, blank=False, null=False)
    # class Meta:
    #     abstract = True


class Cpu(models.Model):
    component_fk = models.ForeignKey(Component, on_delete=models.CASCADE)
    architecture = models.CharField(max_length=255, blank=False, null=False)
    cores = models.IntegerField(blank=False, null=False)
    clock_speed = models.FloatField(blank=False, null=False)


class Gpu(models.Model):
    component_fk = models.ForeignKey(Component, on_delete=models.CASCADE)
    memory_capacity = models.IntegerField(blank=False, null=False)
    memory_type = models.CharField(max_length=255, blank=False, null=False)
    clock_speed = models.FloatField(blank=False, null=False)

class CartProduct(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=False)


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=255, blank=False, null=False)
    phone = models.CharField(max_length=255, blank=False, null=False)
    date_ordered = models.DateTimeField(default=timezone.now)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=False)
