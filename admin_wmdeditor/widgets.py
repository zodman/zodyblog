# -*- coding: utf-8 -*-

from django import forms
from django.utils.safestring import mark_safe
from django.conf import settings

class WmdEditorWidget(forms.Textarea):
    def render(self, name, value, attrs=None):
        output = [super(WmdEditorWidget, self).render(name, value, attrs)]
        output.append(u'<br /><label>&nbsp;</label><div id="id_%s_preview" class="%s"></div>' % (name.lower(), getattr(settings, 'WMDEDITOR_PREVIEW_CLASS', 'wmd-preview')))
        output.append(u'<script type="text/javascript">create_wmdeditor("%s");</script>' % name.lower())
        return mark_safe(u''.join(output))

    class Media:
        js = (
            getattr(settings, 'WMDEDITOR_MEDIA_PREFIX', settings.MEDIA_URL + 'admin-wmdeditor') + '/starter.js',
            getattr(settings, 'WMDEDITOR_MEDIA_PREFIX', settings.MEDIA_URL + 'admin-wmdeditor') + '/wmd/wmd.js',
        )
        css = {
            'screen': (getattr(settings, 'WMDEDITOR_PREVIEW_CSS', settings.MEDIA_URL + 'admin-wmdeditor/preview.css'),),
        }
