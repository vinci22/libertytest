import json
import threading
import uuid
from datetime import datetime
from contextlib import contextmanager


class AppTracer:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(AppTracer, cls).__new__(cls)
                cls._instance.trace_id = None
                cls._instance.span_stack = []
                cls._instance._lock = threading.Lock()
        return cls._instance

    def start_trace(self, operation_name: str):
        """Start a new trace and initial span."""
        with self._lock:
            self.trace_id = str(uuid.uuid4())
            root_span_id = self._new_span_id()
            self.span_stack = [root_span_id]
            self._emit_event('TRACE START', {
                'operation': operation_name,
                'trace_id': self.trace_id,
                'span_id': root_span_id
            })
        return self.trace_id, root_span_id

    def _new_span_id(self):
        return str(uuid.uuid4())

    def current_span(self):
        return self.span_stack[-1] if self.span_stack else None

    def log(self, level: str, message: str, **kwargs):
        timestamp = datetime.utcnow().isoformat() + 'Z'
        entry = {
            'timestamp': timestamp,
            'level': level,
            'message': message,
            'trace_id': self.trace_id,
            'span_id': self.current_span(),
        }
        if kwargs:
            entry['meta'] = kwargs
        # Print structured JSON-like string
        print(json.dumps(entry, ensure_ascii=False))

    def _emit_event(self, title: str, payload: dict):
        entry = {
            'event': title,
            'timestamp': datetime.utcnow().isoformat() + 'Z',
        }
        entry.update(payload)
        print(json.dumps(entry, ensure_ascii=False))

    @contextmanager
    def span(self, name: str):
        """Context manager to create nested spans."""
        with self._lock:
            parent = self.current_span()
            new_span = self._new_span_id()
            self.span_stack.append(new_span)
            self._emit_event('SPAN START', {
                'name': name,
                'trace_id': self.trace_id,
                'span_id': new_span,
                'parent_span_id': parent
            })
        try:
            yield new_span
        except Exception as e:
            # log exception within span
            self.log('error', f'Exception in span {name}: {e}', exception=str(e))
            raise
        finally:
            with self._lock:
                ended = self.span_stack.pop() if self.span_stack else None
                self._emit_event('SPAN END', {
                    'name': name,
                    'trace_id': self.trace_id,
                    'span_id': ended
                })


# module-level singleton for easy import
tracer = AppTracer()
