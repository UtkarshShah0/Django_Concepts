import django
from django.conf import settings
from django.db import models, transaction, connection
from django.db.models.signals import post_save
from django.dispatch import receiver

settings.configure(
    DEBUG=True,
    SECRET_KEY="abc",
    INSTALLED_APPS=["django.contrib.contenttypes", "django.contrib.auth", "__main__"],
    DATABASES={
        "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
    },
)
django.setup()

class Item(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = "__main__"


@receiver(post_save, sender=Item)
def crash_on_save(sender, instance, **kwargs):
    print("Signal triggered, raising error...")
    raise Exception("Signal exception")


with connection.schema_editor() as schema_editor:
    schema_editor.create_model(Item)

try:
    with transaction.atomic():
        Item.objects.create(name="foo")  
except Exception as e:
    print("Transaction rolled back due to:", e)

print("Final count in DB:", Item.objects.count())
