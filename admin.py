from django.contrib import admin
from pyweb.models import Publisher,Author,Book
class BookAdmin(admin.ModelAdmin):
	search_fields = ('title',)#bu neng xie wai jian
	filter_vertical = ('authors',)
	list_display=('title','publisher','publication_date')
	list_filter = ('publication_date','publisher')
	ordering = ('-publication_date',)
	fields = ('title','authors','publication_date','publisher')
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book,BookAdmin)
