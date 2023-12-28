from django.contrib import admin
from security.models import Accuracy_SQL, Accuracy_Phishing
# Register your models here.
admin.site.register(Accuracy_Phishing)
admin.site.register(Accuracy_SQL)

