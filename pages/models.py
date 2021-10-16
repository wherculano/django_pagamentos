from django.db import models


class Client(models.Model):
    company_name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)


class Bills(models.Model):
    issue_date = models.DateField()
    due_date = models.DateField()
    value = models.DecimalField(max_digits=12, decimal_places=2)
    referred_company = models.ForeignKey('Client', on_delete=models.CASCADE)

