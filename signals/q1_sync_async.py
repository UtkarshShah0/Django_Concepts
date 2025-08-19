import django
from django.conf import settings
from django.dispatch import Signal, receiver
import time

settings.configure()
django.setup()

test_signal = Signal()

@receiver(test_signal)
def slow_handler(sender, **kwargs):
    print("Handler started")
    time.sleep(5)
    print("Handler finished")

print("Sending signal...")
test_signal.send(sender=None)
print("Signal send complete")
