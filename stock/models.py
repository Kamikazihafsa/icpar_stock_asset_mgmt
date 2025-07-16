from django.db import models

class StockItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()
    reorder_level = models.IntegerField(default=10)

    def __str__(self):
        return self.name

class StockMovement(models.Model):
    IN = 'IN'
    OUT = 'OUT'
    MOVEMENT_CHOICES = [(IN, 'Stock In'), (OUT, 'Stock Out')]

    item = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_CHOICES)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movement_type} - {self.item.name} - {self.quantity}"
