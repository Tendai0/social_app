from django.contrib import admin
from django.contrib.auth.models import Group, User 
from .models import Profile, Tweet

#unregister Groups
admin.site.unregister(Group)
class ProfileInLine(admin.StackedInline):
    model = Profile

# Extend user Model
class UserAdmin(admin.ModelAdmin):
    model = User
    #Just dispaly UserName
    fields=["username"]
    inlines = [ProfileInLine]
#unregister initial user
admin.site.unregister(User)
#register initial user
admin.site.register(User,UserAdmin)

#Register Tweets
admin.site.register(Tweet)



