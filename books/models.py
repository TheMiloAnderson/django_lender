from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.models import User


class Book(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='books'
    )
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
    date_added = models.DateTimeField(default=timezone.now)
    last_borrowed = models.DateTimeField(default=timezone.now, blank=True)

    def __repr__(self):
        return f'<Title: {self.title} | Status: {self.status}>'

    def __str__(self):
        return f'{self.title} | Status: {self.status}'


        # @receiver(models.signals.post_save, sender=Book)

#     @staticmethod
#     def post_save(sender, **kwargs):
#         instance = kwargs.get('instance')
#         print(instance.previous_state)
#         # if instance.status in update_fields and instance.status == 'checked-out':
#         #     instance.last_borrowed = timezone.now


# models.signals.post_save.connect(Book.post_save, sender=Book)
