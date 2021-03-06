import ella_newman
from django.utils.translation import ugettext_lazy as _

from ella_series.models import Serie, SeriePart
from ella.core.newman_admin import ListingInlineAdmin, PublishableAdmin


class SerieAdmin(PublishableAdmin):
    list_filter = ('started', 'finished',)

    fieldsets = (
        (None, {'fields': ('title', 'slug', 'photo')}),
        (_("Metadata"), {'fields': ('category', 'authors', ('started', 'finished'), 'hide_newer_parts',),}),
        (_("Description"), {'fields': ('description', 'text', ), 'classes': ('small',)}),
    )

    raw_id_fields = ('photo',)
    rich_text_fields = {None: ('description', 'text',)}

    inlines = [ListingInlineAdmin]


class SeriePartAdmin(ella_newman.NewmanModelAdmin):
    # TODO: admin
    list_display = ('target_admin', 'serie', 'published',)
    raw_id_fields = ('publishable',)
    list_filter = ('serie',)

    def target_admin(self, obj):
        return obj.target
    target_admin.short_description = _('Target')


ella_newman.site.register(Serie, SerieAdmin)
ella_newman.site.register(SeriePart, SeriePartAdmin)


