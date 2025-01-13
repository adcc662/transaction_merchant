import unittest
from django.test import TestCase
from catalog.models import Category, Commerce
from uuid import uuid4

class CategoryModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            id=uuid4(),
            name="Restaurantes",
            type="expense"
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Restaurantes")
        self.assertEqual(self.category.type, "expense")

    def test_category_unique_constraint(self):
        with self.assertRaises(Exception):
            Category.objects.create(
                id=uuid4(),
                name="Restaurantes",
                type="expense"
            )

class CommerceModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            id=uuid4(),
            name="Transporte",
            type="expense"
        )
        self.commerce = Commerce.objects.create(
            id=uuid4(),
            merchant_name="Uber",
            merchant_logo="https://example.com/logo.png",
            category=self.category
        )

    def test_commerce_creation(self):
        self.assertEqual(self.commerce.merchant_name, "Uber")
        self.assertEqual(self.commerce.merchant_logo, "https://example.com/logo.png")
        self.assertEqual(self.commerce.category, self.category)

    def test_commerce_with_invalid_category(self):
        with self.assertRaises(Exception):
            Commerce.objects.create(
                id=uuid4(),
                merchant_name="UberEats",
                merchant_logo="https://example.com/logo_uber_eats.png",
                category=None  # No category provided
            )

