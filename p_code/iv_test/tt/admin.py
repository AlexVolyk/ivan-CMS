from django.contrib import admin

from .ulib import remove_by_number

from .models import Type, Brand, Country, Size, Sm, Date, Footwear, Marked, State, Status

# Register your models here.
# maximum = 1400
maximum = 100



class TypeAdmin(admin.ModelAdmin):
    list_per_page = maximum
    search_fields = ('name',)

    
admin.site.register(
    Type,
    TypeAdmin
)


class BrandAdmin(admin.ModelAdmin):
    list_per_page = maximum
    search_fields = ('name',)


admin.site.register(
    Brand,
    BrandAdmin
)

class MarkedAdmin(admin.ModelAdmin):
    list_per_page = maximum
    search_fields = ('name',)


admin.site.register(
    Marked,
    MarkedAdmin
)


class CountryAdmin(admin.ModelAdmin):
    list_per_page = maximum
    search_fields = ('name',)


admin.site.register(
    Country,
    CountryAdmin
)


class SizeAdmin(admin.ModelAdmin):
    list_per_page = maximum
    search_fields = ('size',)


admin.site.register(
    Size,
    SizeAdmin
)


class SmAdmin(admin.ModelAdmin):
    list_per_page = maximum
    search_fields = ('sm',)


admin.site.register(
    Sm,
    SmAdmin
)

class StatusAdmin(admin.ModelAdmin):
    list_per_page = maximum
    search_fields = ('name',)


admin.site.register(
    Status,
    StatusAdmin
)

class StateAdmin(admin.ModelAdmin):
    list_per_page = maximum
    search_fields = ('name',)


admin.site.register(
    State,
    StateAdmin
)


class DateAdmin(admin.ModelAdmin):
    list_per_page = maximum
    search_fields = ('date',)   

    def delete_queryset(self, request, queryset):
        if queryset.__len__() > 1:
            raise Exception('You will not delete this dates')
        else:
            raise Exception('You will not delete this date')


    def delete_model(self, request, obj):
        raise Exception('You will not delete this date')



admin.site.register(
    Date,
    DateAdmin
)


class FootwearAdmin(admin.ModelAdmin):
    list_per_page = maximum
    list_display = ('number', 'type_p', 'brand', 'marked', 'color', 'notice', 'size', 'sm', 'price', 'old_price', 'status', 'state', 'extra_notice', 'date')
    search_fields = ('number', 'color', 'notice', 'extra_notice')
    list_filter = ('type_p', 'brand', 'marked', 'size', 'sm',  'status', 'state', 'date')

    def delete_queryset(self, request, queryset):
        # print('==========================delete_queryset==========================')
        # print(queryset)
        for i in queryset:
            # print(i)
            footwear = Footwear.objects.get(number=i)
            date = footwear.date
            number = footwear.number
            remove_by_number(date=date, number=number)
        queryset.delete()
        # print('==========================delete_queryset==========================')


    def delete_model(self, request, obj):
        # print('==========================delete_model==========================')
        # print(obj)
        footwear = Footwear.objects.get(number=obj)
        date = footwear.date
        number = footwear.number
        remove_by_number(date=date, number=number)
        obj.delete()
        # print('==========================delete_model==========================')


admin.site.register(
    Footwear,
    FootwearAdmin
)

