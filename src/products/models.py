from django.db import models
from django.urls import reverse
from django.contrib.admin import ModelAdmin


# Create your models here.

class Product(models.Model):
    title       = models.CharField(max_length=120) #max_length = required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    summary     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField(default=False) # null=True, default=True

    def get_absolute_url(self):
        # products: - is the app_name
        return reverse("products:product-detail", kwargs={"id":self.id})
        #
        #another method, hardcoded and not correct
        #return f"/{self.id}/"
        # Or like this:
        #return "/" + str(self.id) + "/"

# for admin
class ProductAdmin(ModelAdmin):

    # for list view
    list_display = ['title', 'price', 'featured']
    list_filter = ('title', 'price')

    # for deatailed view
    fields = [
                ('title','featured'),
                ('price', 'summary'),
                ('description')
    ]
    # fieldsets = (
    #                 ('Section 1', {'fields': ('title','featured')}),
    #                 ('Section 2', {'fields': ('price','summary')}),
    #                 ('Section 3', {'fields': ('description')})
    # )
