from django.contrib import admin
from configuration.models import APM, PM, TM, UI

class APMAdmin(admin.ModelAdmin):
	# display order for admin site
	fieldsets = [
		(None, {'fields': ['item_name']}),
		(None, {'fields': ['feature']}),
		(None, {'fields': ['settings']}),
		(None, {'fields': ['comments']}),
		(None, {'fields': ['additional_comments']})
	]
	# display all fields
	list_display = ('item_name', 'feature', 'settings', 'comments', 'additional_comments')
	# add search capability
	search_fields = ['item_name']

admin.site.register(APM, APMAdmin)

class PMAdmin(admin.ModelAdmin):
	# display order for admin site
	fieldsets = [
		(None, {'fields': ['item_name']}),
		(None, {'fields': ['feature']}),
		(None, {'fields': ['settings']}),
		(None, {'fields': ['comments']}),
		(None, {'fields': ['additional_comments']}),
	]
	# display all fields
	list_display = ('item_name', 'feature', 'settings', 'comments', 'additional_comments')
	# add search capability
	search_fields = ['item_name']

admin.site.register(PM, PMAdmin)

class TMAdmin(admin.ModelAdmin):
	# display order for admin site
	fieldsets = [
		(None, {'fields': ['item_name']}),
		(None, {'fields': ['feature']}),
		(None, {'fields': ['settings']}),
		(None, {'fields': ['comments']}),
		(None, {'fields': ['additional_comments']}),
	]
	# display all fields
	list_display = ('item_name', 'feature', 'settings', 'comments', 'additional_comments')
	# add search capability
	search_fields = ['item_name']

admin.site.register(TM, TMAdmin)

class UIAdmin(admin.ModelAdmin):
	# display order for admin site
	fieldsets = [
		(None, {'fields': ['item_name']}),
		(None, {'fields': ['feature']}),
		(None, {'fields': ['settings']}),
		(None, {'fields': ['comments']}),
		(None, {'fields': ['additional_comments']}),
	]
	# display all fields
	list_display = ('item_name', 'feature', 'settings', 'comments', 'additional_comments')
	# add search capability
	search_fields = ['item_name']

admin.site.register(UI, UIAdmin)
