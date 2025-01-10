import uuid
from django.db import models


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class Category(UUIDModel):
    EXPENSE = "expense"
    INCOME = "income"
    CATEGORY_TYPE = [
        (EXPENSE, "Expense"),
        (INCOME, "Income"),
    ]
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=50, choices=CATEGORY_TYPE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'type'], name='unique_category_name_type')
        ]

    def __str__(self):
        return self.name


class Commerce(UUIDModel):
    merchant_name = models.CharField(max_length=150)
    merchant_logo = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.merchant_name

