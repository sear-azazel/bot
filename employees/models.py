from django.db import models


class Division(models.Model):
    division_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Employee(models.Model):
    employee_code = models.PositiveIntegerField()
    employee_name = models.CharField(max_length=100)
    employee_tel = models.CharField(max_length=10)
    employee_tel_mobile = models.CharField(max_length=11)
    employee_division = models.ForeignKey(Division, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
