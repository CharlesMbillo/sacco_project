from django.db import models

from django.db import models

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('deposit', 'Deposit'),
        ('savings', 'Savings'),
        ('withdrawal', 'Withdrawal'),
    )
    member_id = models.CharField(max_length=10)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    face_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member_id} - {self.transaction_type} - {self.face_amount}"

