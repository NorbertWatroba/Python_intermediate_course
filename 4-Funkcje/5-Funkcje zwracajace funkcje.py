from datetime import datetime


def create_function(span):
    if span == 'm':
        sec = 60
    elif span == 'h':
        sec = 3600
    elif span == 'd':
        sec = 86400
    else:
        sec = 1
        print('error! vailable values: m/h/d')
    source = f'''
def f(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {sec})[0]'''
    exec(source, globals())
    return f


'''
def time_span_m(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 60)[0]


def time_span_h(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 3600)[0]


def time_span_d(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 86400)[0]
    

print(time_span_m(start, end))
print(time_span_h(start, end))
print(time_span_d(start, end))'''
start = datetime(2022, 7, 4, 0, 0, 0)

f = create_function(input('Function type: '))

end = datetime.now()
print(f(start, end))
