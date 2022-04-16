from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Car(models.Model):
    """
    Contains all the cars.
    """
    GEARBOX_CHOICES = [("M", "Manuel Vites"), ("O", "Otomatik Vites")]
    GASOLINE_CHOICES = [("D", "Dizel"), ("B", "Benzin")]

    brand = models.CharField(max_length=200, verbose_name="Marka & Model")
    capacity = models.IntegerField(verbose_name="Kapasite", blank=True, null=True)
    car_model_year = models.IntegerField(verbose_name="Üretim yılı", blank=True, null=True)
    slug = models.SlugField(max_length=200)
    price = models.IntegerField(verbose_name="Fiyat")
    gearbox = models.CharField(default="M", verbose_name="Vites", choices=GEARBOX_CHOICES, max_length=25)
    is_active = models.BooleanField(default=True, verbose_name="Visibility", help_text="Anasayfada görünürlüğünü değiştir")
    created_at = models.DateTimeField(verbose_name="Oluşturulduğu tarih", auto_now_add=True, editable=False)
    updated_at = models.DateTimeField("Güncellenme tarihi", auto_now=True)
    gasoline = models.CharField(verbose_name="Benzin / Dizel", choices=GASOLINE_CHOICES, max_length=25, default="D")

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return self.brand


class CarImageTable(models.Model):
    """
    Car image Table.
    """
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="car_image")
    image = models.ImageField(
        verbose_name="Resim",
        help_text="Upload an image",
        upload_to="images/",
        default="images/default.png"
    )
    alt_text = models.CharField(
        verbose_name="Alt text",
        help_text="Please add an alternative text",
        max_length=255,
        null=True,
        blank=True
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(verbose_name="Oluşturulduğu tarih", auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name="Güncellenme tarihi", auto_now=True)

    class Meta:
        verbose_name = "Car image"
        verbose_name_plural = "Car images"


class Header(models.Model):
    title = models.CharField(verbose_name="Slogan", max_length=500)
    default = models.BooleanField(verbose_name="Default", default=False)
    created_at = models.DateTimeField(verbose_name="Oluşturulma tarihi", auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name="Güncellenme tarihi", auto_now=True)

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Header"
        verbose_name_plural = "Headers"

    def __str__(self):
        return self.title


class Offer(models.Model):
    title = models.CharField(verbose_name="Kampanya başlığı", max_length=250)
    subtitle = models.CharField(verbose_name="Kampanya alt başlığı", max_length=250)
    description = models.CharField(verbose_name="Açıklama", max_length=500)
    is_active = models.BooleanField(default=True, verbose_name="Aktif kampanya")
    created_at = models.DateTimeField(verbose_name="Oluşturulma tarihi", auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name="Güncellenme tarihi", auto_now=True)

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Offer"
        verbose_name_plural = "Offers"

    def __str__(self):
        return self.title



