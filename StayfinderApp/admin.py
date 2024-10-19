

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Role, UserRole, Hotel, Room, Payment, Booked, Rating, AdsSlide, SiteAsset

# If you're using a custom user model, import it as well:
# from .models import CustomUser

# Optional: Customize how UserRole appears in the admin
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'user_name', 'phone', 'address', 'is_activate']
    search_fields = ['user__username', 'user_name', 'phone']

# Optional: Customize how Hotel appears in the admin
class HotelAdmin(admin.ModelAdmin):
    list_display = ['hotel_name', 'location', 'phone_number', 'email']
    search_fields = ['hotel_name', 'location']

# Optional: Customize how Room appears in the admin
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'capacity', 'price', 'is_empty', 'hotel']
    search_fields = ['room_number', 'hotel__hotel_name']

# Register Role
admin.site.register(Role)

# Register UserRole
admin.site.register(UserRole, UserRoleAdmin)

# Register Hotel
admin.site.register(Hotel, HotelAdmin)

# Register Room
admin.site.register(Room, RoomAdmin)

# Register Payment
admin.site.register(Payment)

# Register Booked
admin.site.register(Booked)

# Register Rating
admin.site.register(Rating)

# If using the built-in User model:
# Unregister the original User admin and register a custom one if needed
admin.site.unregister(User)
admin.site.register(User, BaseUserAdmin)
admin.site.register(AdsSlide)
admin.site.register(SiteAsset)

# If using a custom user model (e.g., CustomUser):
# admin.site.register(CustomUser, BaseUserAdmin)

