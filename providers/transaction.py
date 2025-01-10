from unicodedata import category

from transaction.models import Transaction

def create_transactions(transactions):
    created_transactions = []
    for transaction_data in transactions:
        try:
            category_id = transaction_data.get('category_id')
            merchant_id = transaction_data.get('merchant_id')

            transaction = Transaction.objects.create(
                id=transaction_data.get['id'],
                description=transaction_data.get['description'],
                amount=transaction_data.get['amount'],
                date=transaction_data.get['date'],
                category_id=category_id,
                merchant_id=merchant_id
            )
            created_transactions.append(transaction)
        except Exception as e:
            print(f"Error creating transaction: {e}")

    return created_transactions