import unittest
from django.test import TestCase
from transaction.models import Transaction, Keyword
from catalog.models import Category, Commerce
from uuid import uuid4
from datetime import date

class TransactionModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            id=uuid4(),
            name="Restaurantes",
            type="expense"
        )
        self.commerce = Commerce.objects.create(
            id=uuid4(),
            merchant_name="Uber Eats",
            merchant_logo="https://example.com/logo.png",
            category=self.category
        )
        self.transaction = Transaction.objects.create(
            id=uuid4(),
            description="Payment to Uber Eats",
            amount=-300.00,
            date=date(2025, 1, 12),
            category=self.category,
            commerce=self.commerce
        )

    def test_transaction_creation(self):
        self.assertEqual(self.transaction.description, "Payment to Uber Eats")
        self.assertEqual(self.transaction.amount, -300.00)
        self.assertEqual(self.transaction.date, date(2025, 1, 12))
        self.assertEqual(self.transaction.category, self.category)
        self.assertEqual(self.transaction.merchant, self.commerce)

    def test_transaction_invalid_amount(self):
        with self.assertRaises(Exception):
            Transaction.objects.create(
                id=uuid4(),
                description="Invalid Amount",
                amount=0.00,  # Invalid amount (zero)
                date=date(2025, 1, 12),
                category=self.category,
                commerce=self.commerce
            )

class KeywordModelTestCase(TestCase):
    def setUp(self):
        self.commerce = Commerce.objects.create(
            id=uuid4(),
            merchant_name="Uber",
            merchant_logo="https://example.com/logo.png",
            category=None
        )
        self.keyword = Keyword.objects.create(
            id=uuid4(),
            keyword="uber",
            merchant=self.commerce
        )

    def test_keyword_creation(self):
        self.assertEqual(self.keyword.keyword, "uber")
        self.assertEqual(self.keyword.merchant, self.commerce)

    def test_keyword_unique_constraint(self):
        with self.assertRaises(Exception):
            Keyword.objects.create(
                id=uuid4(),
                keyword="uber",
                merchant=self.commerce  # Duplicate keyword for the same merchant
            )
