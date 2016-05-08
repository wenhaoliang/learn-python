from __future__ import unicode_literals

from django.db import models
 
class CompressedTextField(models.TextField):
    """    model Fields for storing text in a compressed format (bz2 by default)    """
    __metaclass__ = models.SubfieldBase
 
    def to_python(self, value):
        if not value:
            return value
 
        try:
            return value.decode('base64').decode('bz2').decode('utf-8')
        except Exception:
            return value
 
    def get_prep_value(self, value):
        if not value:
            return value
 
        try:
            value.decode('base64')
            return value
        except Exception:
            try:
                tmp = value.encode('utf-8').encode('bz2').encode('base64')
            except Exception:
                return value
            else:
                if len(tmp) > len(value):
                    return value
 
                return tmp