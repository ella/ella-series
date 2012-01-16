from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from ella_series.models import Serie, SeriePart
from ella.core.admin import ListingInlineAdmin


#class SeriePartInlineAdmin(admin.TabularInline):
#    model = SeriePart
#    extra = 5
#    raw_id_fields = ('publishable',)


class SerieAdmin(admin.ModelAdmin):
    list_display = ('title', 'started', 'is_active', 'parts_count',)
    list_filter = ('started', 'finished',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description',)

    fieldsets = (
        (None, {'fields': ('title',)}),
        (_("Slug, metadata"), {'fields': ('slug', 'started', 'finished', 'hide_newer_parts',), 'classes': ['collapse'],}),
        (_("Contents"), {'fields': ('description', 'category', 'photo',)}),
    )

    raw_id_fields = ('photo',)
    rich_text_fields = {None: ('description',)}

    inlines = [ListingInlineAdmin]


class SeriePartAdmin(admin.ModelAdmin):
    # TODO: admin
    list_display = ('target_admin', 'serie', 'published',)
    raw_id_fields = ('publishable',)
    list_filter = ('serie',)

    def target_admin(self, obj):
        return obj.target
    target_admin.short_description = _('Target')

admin.site.register(Serie, SerieAdmin)
admin.site.register(SeriePart, SeriePartAdmin)
