from django.db import models

class Estate(models.Model):

    address=models.TextField()

    price=models.PositiveIntegerField()

    property_options=(
        ("apartment","apartment"),
        ("house","house"),
        ("land","land"),
    )

    property_type=models.CharField(max_length=100,choices=property_options,default="land")

    number_of_bedrooms=models.PositiveIntegerField()

    square_footage=models.PositiveIntegerField()

    location=models.CharField(max_length=100)

    property_image=models.ImageField(upload_to="estate_img",null=True,blank=True)

    contact_details=models.CharField(max_length=100)

    def __str__(self):

        return self.address



