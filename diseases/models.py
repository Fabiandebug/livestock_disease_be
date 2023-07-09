from django.db import models

# Create your models here.


# Diseases Model
class disease(models.Model):
    LANGUAGE_CHOICES = (
        ("en", "English"),
        ("sw", "Kiswahili"),
    )
    identifier = models.CharField(max_length=100, unique=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    name = models.CharField(max_length=100)
    local_names = models.TextField()
    other_livestock_affected = models.CharField(max_length=100)
    transmission = models.TextField()
    number_affected_in_herd = models.CharField(max_length=100)
    death_rate = models.CharField(max_length=100)
    predisposing_factors = models.TextField()
    key_signs = models.TextField()
    other_signs = models.TextField()
    prevention = models.TextField()

    def __str__(self):
        return f"{self.identifier} ({self.get_language_display()})"

    class Meta:
        unique_together = ("identifier", "language")


# Images Model
class image(models.Model):
    identifier = models.ForeignKey(disease, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/", null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.description
