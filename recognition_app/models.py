from django.db import models
from django.utils import timezone
from django.db import models
from django.utils import timezone

class KnownIndividual(models.Model):
    id_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    additional_info = models.TextField(blank=True)
    face_image = models.ImageField(upload_to='known_faces/')
    face_encoding = models.BinaryField(null=True)  # To store face encoding

    def __str__(self):
        return f"{self.name} ({self.id_number})"

class Result(models.Model):
    uploaded_image = models.ImageField(upload_to='uploads/')
    processed_image = models.ImageField(upload_to='processed/', null=True, blank=True)
    match_found = models.BooleanField(default=False)
    matched_individual = models.ForeignKey(KnownIndividual, on_delete=models.SET_NULL, null=True, blank=True)
    upload_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Recognition Result {self.id} - Match: {self.match_found}"

    class Meta:
        ordering = ['-upload_date']

class RecognitionResult(models.Model):
    original_image = models.ImageField(upload_to='uploads/')
    processed_image = models.ImageField(upload_to='processed/', null=True, blank=True)
    faces_detected = models.IntegerField(default=0)
    upload_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Recognition Result {self.id} - {self.faces_detected} faces detected"

    class Meta:
        ordering = ['-upload_date']