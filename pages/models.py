from django.db import models


class Client(models.Model):
    company_name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)

    def __str__(self):
        return self.company_name


class Bills(models.Model):
    description = models.CharField(max_length=50)
    issue_date = models.DateField()
    due_date = models.DateField()
    value = models.DecimalField(max_digits=12, decimal_places=2)
    referred_company = models.ForeignKey('Client', on_delete=models.CASCADE)

    def __str__(self):
        return self.description

