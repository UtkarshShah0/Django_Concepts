# Python & Django Signal

_Questions for Django Trainee at AccuKnox_

I have used `django.setup()` to run the files as scripts without entire django project.
---

## Files
- [signals/q1_sync_async.py](signals/q1_sync_async.py) — Are signals synchronous by default?
- [signals/q2_same_thread.py](signals/q2_same_thread.py) — Do signals run in the same thread as the caller?
- [signals/q3_same_transaction.py](signals/q3_same_transaction.py) — Do signals run in the same database transaction as the caller?
- [custom_class/rectangle.py](custom_class/rectangle.py) — Iterable `Rectangle` class example
- [requirements.txt](requirements.txt) — Dependencies

---

## Django Signals

### 1) Synchronous vs. Asynchronous
File: [signals/q1_sync_async.py](signals/q1_sync_async.py)

- **Concept:** Django signals are synchronous by default. The sender blocks until all connected handlers finish.
- **Output:**
```text
Sending signal...
Handler started
Handler finished
Signal send complete
```

### 2) Same Thread as Caller
File: [signals/q2_same_thread.py](signals/q2_same_thread.py)

- **Concept:** Signal handlers run in the same thread as the sender.
- **Output:**
```text
Caller thread: MainThread
Inside handler thread: MainThread
```

### 3) Same Database Transaction
File: [signals/q3_same_transaction.py](signals/q3_same_transaction.py)

- **Concept:** Signal handlers execute within the same database transaction as the caller (unless explicitly separated). If a handler raises an exception, the transaction is rolled back.
- **Output:**
```text
Signal triggered, raising error...
Transaction rolled back due to: Signal exception
Final count in DB: 0
```

---

## Custom Classes in Python

### Iterable Rectangle
File: [custom_class/rectangle.py](custom_class/rectangle.py)

- **Output:**
```text
{'length': 10}
{'width': 5}
```

---

## Running the Examples

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run each script individually from the repository root:
```bash
python signals/q1_sync_async.py
python signals/q2_same_thread.py
python signals/q3_same_transaction.py
python custom_class/rectangle.py
```

