from django.db import models
from django.db.models import Sum
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_type = models.CharField(max_length=50)
    UPC = models.CharField(max_length=20)
    bottle_size = models.IntegerField()

    def __str__(self):
        return str(self.product_name)

    @property
    def number_of_strays(self):
        return Stray.objects.filter(name=self).count()

    @property
    def number_of_cases(self):
        return InventoryItem.objects.filter(name=self).count()

    @property
    def total_liters(self):
        cases = InventoryItem.objects.filter(name=self)
        liters = []
        for case in cases:
            liters.append(case.liters)
        return sum(liters)

    @property
    def total_wine_gallons(self):
        return round((int(self.total_liters) * .264172),2)

    @property
    def total_proof_gallons(self):
        cases = InventoryItem.objects.filter(name=self)
        proof_gallons = []
        for case in cases:
            proof_gallons.append(case.proof_gallons)
        return round(sum(proof_gallons),2)


class InventoryItem(models.Model):
    case_number = models.IntegerField(unique=True)
    date_assigned = models.DateField()
    name = models.ForeignKey(Product, on_delete=models.PROTECT)
    proof = models.DecimalField(max_digits=5,decimal_places=2)
    date_removed = models.DateTimeField(null=True,blank=True)


    @property
    def bottles_per_case(self):
        if self.name.bottle_size == 750:
            return 6
        elif self.name.bottle_size == 375:
            return 12

    @property
    def product(self):
        return self.name.product_type

    @property
    def liters(self):
        return round(self.name.bottle_size/1000 * self.bottles_per_case,2)

    @property
    def wine_gallons(self):
        return round((int(self.liters) * .264172),2)

    @property
    def proof_gallons(self):
        return round((int(self.proof)/100 * self.wine_gallons), 2)

class Stray(models.Model):
    date_assigned = models.DateTimeField(auto_now_add=True)
    name = models.ForeignKey(Product, on_delete=models.PROTECT)
    proof = models.DecimalField(max_digits=5,decimal_places=2)

    @property
    def product(self):
        return self.name.product_type
