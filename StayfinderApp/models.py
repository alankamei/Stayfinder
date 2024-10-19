
from django.db import models
from django.contrib.auth.models import User

class AdsSlide(models.Model):
    title = models.CharField(max_length=255)
    ads_image = models.FileField(upload_to="ads_image" ,blank=True, null=True,  default='no_image/noimage.png')
    def __str__(self):
        return self.title



class Role(models.Model):
    role_name = models.CharField(max_length=255)

    def __str__(self):
        return self.role_name

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_roles')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='user_roles')
    user_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    is_activate = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    longitude = models.CharField(max_length=50,blank=True, null=True )
    latitude = models.CharField(max_length=50 ,blank=True, null=True)

    hotel_banner = models.FileField(upload_to="hotel_image" , blank=True, null=True, default='no_image/noimage.png')
    interior_image = models.FileField(upload_to="hotel_image" ,blank=True, null=True,  default='no_image/noimage.png')

    user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE, related_name='hotels')
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    picked_of_day=models.BooleanField(default=False)

    def __str__(self):
        return self.hotel_name

class Room(models.Model):
    room_number = models.BigIntegerField()
    capacity = models.BigIntegerField()
    price = models.FloatField()
    is_empty = models.BooleanField(default=True)
    room_image = models.FileField(upload_to="room_images/", blank=True, null=True, default='no_image/noimage.png')
    description = models.CharField(max_length=255)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    top_ten=models.BooleanField(default=False)

    def __str__(self):
        return f"Room {self.room_number} at {self.hotel.hotel_name}"

class Payment(models.Model):
    transaction_id = models.CharField(max_length=255)
    payment_date = models.DateTimeField( auto_now_add=True)
    paid_amount = models.BigIntegerField()
    user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE, related_name='payments')

    def __str__(self):
        return f"Payment {self.transaction_id}"

class Booked(models.Model):
    number_of_days = models.BigIntegerField()

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    booked_date = models.DateTimeField(auto_now_add=True)

    user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE, related_name='bookings')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')

    def __str__(self):
        return f"Booking by {self.user_role.user_name}"

class Rating(models.Model):
    rating = models.CharField(max_length=255)
    review = models.BigIntegerField()
    user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE, related_name='ratings')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return f"Rating for {self.hotel.hotel_name}"



class SiteAsset(models.Model):
    logo = models.ImageField(upload_to='logos/', blank=True, null=True, default='no_image/noimage.png')
    instagram_icon = models.ImageField(upload_to='social_media/', blank=True, null=True, default='no_image/noimage.png')
    twitter_icon = models.ImageField(upload_to='social_media/', blank=True, null=True, default='no_image/noimage.png')

    def __str__(self):
        return "Site Assets"
