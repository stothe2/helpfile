from django.contrib import admin
from configuration.models import APMControls

class APMControlsAdmin(admin.ModelAdmin):
	# display order for admin site
	fieldsets = [
		(None, {'fields': ['item_name']}),
		(None, {'fields': ['feature']}),
		(None, {'fields': ['settings']}),
		(None, {'fields': ['comments']}),
		#(None, {'fields': ['extra']}),
	]
	# display all fields
	list_display = ('item_name', 'feature', 'settings', 'comments')
	# add search capability
	search_fields = ['item_name']

admin.site.register(APMControls, APMControlsAdmin)
