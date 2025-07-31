from django.db import models

CATEGORY_CHOICES = [
    ('grocery', 'Grocery'),
    ('clothing', 'Clothing')
]

class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.category})"
