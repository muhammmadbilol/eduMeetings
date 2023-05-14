from modeltranslation.translator import TranslationOptions, translator
from .models import Meet

class meetingTR(TranslationOptions):
    fields = ('description',)
translator.register(Meet, meetingTR)

