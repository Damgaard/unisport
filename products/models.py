from decimal import Decimal as D

from django.db import models


class Product(models.Model):
    """A Product sold at unisport.dk.

    By default a product is available for adult males and only adult males.
    Boolean flags are used to show those products that are available for
    different demographics.

    Note that due to the age of the codebase, some booleans are stored as
    0/1 rather than the boolean type.

    """

    DEMOGRAPHIC_DEFAULT = 0
    DEMOGRAPHIC_KIDS = 1
    DEMOGRAPHIC_KIDS_AND_ADULTS = 1
    DEMOGRAPHIC_WOMEN = 1

    KIDS_CHOICES = (
        (DEMOGRAPHIC_DEFAULT, "Default Demographic"),
        (DEMOGRAPHIC_KIDS, "Only for kids"),
    )

    KIDS_AND_ADULT_CHOICES = (
        (DEMOGRAPHIC_DEFAULT, "Default Demographic"),
        (DEMOGRAPHIC_KIDS_AND_ADULTS, "For Kids and Adults"),
    )

    WOMEN_CHOICES = (
        (DEMOGRAPHIC_DEFAULT, "Default Demographic"),
        (DEMOGRAPHIC_WOMEN, "For women only"),
    )

    SOLD_SEPERATELY = 0
    SOLD_AS_PACKAGE = 1

    PACKAGE_CHOICES = (
        (SOLD_SEPERATELY, "Sold as a seperate product"),
        (SOLD_AS_PACKAGE, "Sold as part of a package"),
    )

    delivery = models.CharField(max_length=125,
                                help_text="Estimated remaining delivery time.")
    free_porto = models.BooleanField(default=False,
                                     help_text="Is product sold porto free?")
    img_url = models.CharField(max_length=255,
                               help_text="The relative url on the static url "
                                         "for a product image.""")
    name = models.CharField(max_length=255,
                            help_text="The user displayed name/description of "
                                      "the product. Not used internally.")
    sizes = models.TextField(help_text="List of available sizes. Elements "
                                       "seperated by '/'.")
    url = models.CharField(max_length=255,
                           help_text="The relative url for indepth information"
                                     "on the product.")
    kids = models.IntegerField(default=0,
                               help_text="Is this product only available for "
                                         "kids?",
                               choices=KIDS_CHOICES)
    kids_adult = models.IntegerField(default=0,
                                     help_text="Is this product available for "
                                               "both kids and adults?",
                                     choices=KIDS_AND_ADULT_CHOICES)
    package = models.IntegerField(default=0,
                                help_text="Is this product sold in package?",
                                choices=PACKAGE_CHOICES)
    price = models.DecimalField(decimal_places=2, max_digits=9, default=0,
                                help_text="What this product cost. Denominated"
                                          " in DKK.")
    price_old = models.DecimalField(decimal_places=2, max_digits=9, default=0,
                                    help_text="The previous price of this "
                                              "product. Used to evaluated "
                                              "benefits of price changes.")
    women = models.IntegerField(default=0,
                                help_text="Is this product only available"
                                          "for women?",
                                choices=WOMEN_CHOICES)

    def __unicode__(self):
        return "[Product: {}]".format(self.name)

