from django.db import models

# Create your models here.
class LanguageLanguage(models.Model): # Our LanguageLanguage class is inheriting models.Model 
    # word ( in lang1 ) : meaning ( in lang2)
    # lang1 : is of type String
    # lang2 : is of type String
    # inside django, we use CharField(which is defined in models) to store String
    lang1 = models.CharField(max_length=220)
    lang2 = models.CharField(max_length=220)
    # class : attributes + functions