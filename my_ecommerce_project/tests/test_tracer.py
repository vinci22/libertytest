import pytest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from my_ecommerce.tracer import tracer

def test_start_trace_and_log(capsys):
    trace_id, span_id = tracer.start_trace('unittest-op')
    tracer.log('info', 'testing trace log')
    captured = capsys.readouterr()
    # We expect the trace start event to have been printed and then the log JSON
    assert trace_id is not None
    assert span_id is not None
    assert 'TRACE START' in captured.out or 'trace_id' in captured.out

def test_span_context_manager(capsys):
    trace_id, root_span = tracer.start_trace('span-test')
    with tracer.span('inner') as s:
        tracer.log('info', 'inside inner span')
    captured = capsys.readouterr()
    assert 'SPAN START' in captured.out
    assert 'SPAN END' in captured.out
