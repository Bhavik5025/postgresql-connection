from django.db import models
class employee(models.Model):
    ename=models.CharField(max_length=100)
    email=models.EmailField()
    class Meta:
        db_table="employee_employee"
# Create your models here.
