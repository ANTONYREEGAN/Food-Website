from django.db import models

class Item(models.Model):
    def __str__(self):
        return self.item_name
    item_name =models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500 ,default = "https://th.bing.com/th/id/OIP.kRfblRpg8bm4PcJqIF6SRgHaFj?rs=1&pid=ImgDetMain")
     