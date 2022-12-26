def make_list(colors, _n):
    return colors[:_n]


Colors = ['red', 'orange', 'green', 'violet', 'blue', 'yellow']

Text = r'''Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, 
która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem 
realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do 
wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli. '''
n = int(input('Insert number of categories: '))
ShortColors = make_list(Colors, n)
print(ShortColors)
print(Text[Text.index('(')+1:Text.index(')')])
