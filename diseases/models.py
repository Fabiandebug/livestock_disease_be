from django.db import models

# Create your models here.


# Diseases Model
class disease(models.Model):
    LANGUAGE_CHOICES = (
        ("en", "English"),
        ("sw", "Kiswahili"),
    )
    identifier = models.CharField(max_length=100, unique=False)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    name = models.CharField(max_length=100)
    local_names = models.TextField()
    other_livestock_affected = models.TextField()
    transmission = models.TextField()
    number_affected_in_herd = models.TextField()
    death_rate = models.TextField()
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
    disease = models.ForeignKey(
        disease, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="media/", null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.description
