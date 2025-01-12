from django.core.exceptions import ValidationError
from django.db import models
from catalog.models import UUIDModel, Category, Commerce

class Keyword(UUIDModel):
    keyword = models.CharField(max_length=150)
    merchant = models.ForeignKey(Commerce, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['keyword', 'merchant'], name='unique_keyword_merchant')
        ]

    def __str__(self):
        return self.keyword


class Transaction(UUIDModel):
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    merchant = models.ForeignKey(Commerce, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.description

    def clean(self):
        if self.amount == 0:
            raise ValidationError("Amount cannot be zero.")
        super().clean()
