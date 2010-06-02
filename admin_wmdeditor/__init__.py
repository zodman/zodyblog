# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .widgets import WmdEditorWidget

class WmdEditorModelAdmin(admin.ModelAdmin):
    wmdeditor_fields = ()
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(WmdEditorModelAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        
        for i in self.wmdeditor_fields:
            if db_field.name == i:
                field.widget = WmdEditorWidget(attrs=field.widget.attrs)
        
        return field
