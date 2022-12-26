projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for pos, (p, l, d) in enumerate(zip(projects, leaders, dates), 1):
    print(f'{pos} - The leader of {p} started on {d} is {l}')
