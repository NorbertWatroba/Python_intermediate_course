ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
connections = [(a, b) for a in ports for b in ports if a != b and ports.index(b) > ports.index(a)]
num_con = list(enumerate(connections, 1))
for pos, con in num_con:
    print(f'{pos:>3} - {con}')
