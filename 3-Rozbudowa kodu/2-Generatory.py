ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

gen = ((a, b) for a in ports for b in ports if a != b and ports.index(b) > ports.index(a))
i = 0
while True:
    try:
        i += 1
        print(f'{i:3} - {next(gen)}')
    except StopIteration:
        i -= 1
        print(f'Total records: {i:>4}')
        print(' all values has been generated '.center(200, '-'))
        break
