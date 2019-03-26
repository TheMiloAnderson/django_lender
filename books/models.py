from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    year = models.IntegerField()
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('checked-out', 'Checked Out')
    ]
    status = models.CharField(
        choices=STATUS_CHOICES,
        default='available',
        max_length=32
    )
    date_added = models.DateField(auto_now_add=True)
    last_borrowed = models.DateField(auto_now=True)

    def __repr__(self):
        return f'<Note: {self.title} | Status: {self.status}>'

    def __str__(self):
        return f'{self.title} | Status: {self.status}'
