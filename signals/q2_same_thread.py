import django
import threading
from django.conf import settings
from django.dispatch import Signal, receiver

settings.configure()
django.setup()

test_signal = Signal()

@receiver(test_signal)
def thread_checker(sender, **kwargs):
    print("Inside handler thread:", threading.current_thread().name)

print("Caller thread:", threading.current_thread().name)
test_signal.send(sender=None)
