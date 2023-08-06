from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, null=False)
    time = models.TimeField(auto_now=True)
    email = models.EmailField(max_length=254, null=True, primary_key=True),
    telegram = models.CharField(max_length=100, null=True)
    annotation = models.JSONField(null=True)


class Game(models.Model):
    time_of_performance = models.TimeField(null=True)
    time_created = models.TimeField(auto_now_add=True)
    time_changed = models.TimeField(auto_now=True)
    name = models.CharField(max_length=500, null=False)
    date_start = models.DateTimeField(null=False)

# class Loan(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
#     # Add more fields as required
#
# class Transaction(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateTimeField(auto_now_add=True)
#     # Add more fields as required
