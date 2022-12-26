days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
workdays = days.copy()
workdays = workdays[:-2]    # also possible workdays.pop() x2 / workdays.remove('sat') workdays.remove('sun')

print(days)
print(workdays)
