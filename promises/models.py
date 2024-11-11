from django.db import models

class Promise(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    STATUS_CHOICES = [
        ('fulfilled', 'Fulfilled'),
        ('in_progress', 'In Progress'),
        ('stalled', 'Stalled'),
        ('broken', 'Broken'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    date_promised = models.DateField()
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
