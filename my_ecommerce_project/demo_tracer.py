from my_ecommerce.tracer import tracer

def main():
    trace_id, span_id = tracer.start_trace('demo-operation')
    tracer.log('info', 'Started main operation', user='demo_user')

    with tracer.span('sub-task') as sub_span:
        tracer.log('info', 'inside sub-task', detail='doing work')
        try:
            1 / 0  # intentionally cause an error to demonstrate logging
        except ZeroDivisionError as e:
            tracer.log('error', 'caught an error inside span', error=str(e), code=123)

    tracer.log('info', 'Finished all operations')

if __name__ == '__main__':
    main()
