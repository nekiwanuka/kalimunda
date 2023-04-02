from django.db import models

# Create your models here.
# models, means description of the space on the database where we store data
# MODELS are python classes


class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):  # here were are giving our..............
        return self.name

 # creating rows and columns  (fields)


class Product(models.Model):
    # Here we are connecting product model to category model.
    # This is a foregin ket column in one table that is being used by another table.
    # In this case the foreign is given to us by django and it is here to reference to the category table.
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    item_name = models.CharField(max_length=50, null=True, blank=True)
    total_quantity = models.IntegerField(default=0, null=True, blank=True)
    issued_quantity = models.IntegerField(default=0, null=True, blank=True)
    recieved_quantity = models.IntegerField(default=0, null=True, blank=True)
    unit_price = models.IntegerField(default=0, null=True, blank=True)
    manufacturer = models.CharField(max_length=50, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):  # here were are giving our..............
        return self.item_name


class Sale(models.Model):
    # purchaser's name, item name, qauntity, the price, VAT, date and time

    item = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0, null = False, blank = True)
    amount_recieved = models.IntegerField(default = 0, null = False, blank = True)
    issued_to = models.CharField(max_length = 50, null = True, blank = True)
    unit_price = models.IntegerField(default = 0, null = True, blank = True)
    date = models.DateTimeField(auto_now_add = True)

    # the method below calculates the tota sale
    def get_total(self):
        total = self.quantity * self.item.unit_price
        return int(total)

    # we calculate the change using the method below
    def get_change(self):
        change = int(self.get_total()) - self.amount_recieved
        return abs(int(change))
    # ad Vat function

    def vat():
        pass

    def __str__(self):
        return self.item.item_name
    # note whenever you add a class here, you have to make migrations.
