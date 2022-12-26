import pickle
import glob
import types


def export_1_cake_to_html(obj, path='htmls/1cake.html'):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
        f.write(content)


def export_all_cakes_to_html(cls, path='htmls/classCake.html'):
    template_header = '<table border=1>'
    template = """
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
"""
    template_footer = '</table>'

    with open(path, "a") as f:
        f.write(template_header)
        for obj in cls.bakery_offer:
            content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
            f.write(content)
        f.write(template_footer)

def export_this_cake_to_html(self, path='htmls/'):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""
    path = path + f'{self.name.replace(" ", "_")}.html'
    with open(path, "w") as f:
        content = template.format(self.name, self.kind, self.taste, self.additives, self.filling)
        f.write(content)

class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []


    def __init__(self, name:str, kind:str, taste:str, additives:list, filling:str=None, gluten_free:bool=False, text:str=''):
        Cake.bakery_offer.append(self)
        self.name = name
        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.__gluten_free = gluten_free
        if self.kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print(f'Cannot add text "{text}" to {self.name}')


    def show_info(self):
        print(f'''| {self.name.upper():29}|
| Kind:        {self.kind:16}|
| Taste:       {self.taste:16}|''')
        if self.additives:
            print(f'| Additives:{"":19}|')
            for a in self.additives:
                print(f'|{"":14}{a:16}|')
        if self.filling:
            print(f'| Filling:     {self.filling:16}|')
        print(f'| Gluten-free: {self.__gluten_free:<16}|')
        print(f'| Text:{"":24}|\n|{self.text:^30}|')
        print(f'|{"-"*30}|')


    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives:list):
        self.additives.extend(additives)

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print(f'Cannot add text "{new_text}" to {self.name}')


    def save_to_file(self, path):
        with open(path, "bw") as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, "br") as f:
            obj = pickle.load(f)
        cls.bakery_offer.append(obj)
        return obj

    @staticmethod
    def get_bakery_files(directory='.'):
        return glob.glob(fr'{directory}/*.bakery')


cake1 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream', text='Happy Anniversary!')
muffin1 = Cake('Chocolate Muffin', 'muffin', 'chocolate', ['chocolate'])
meringue1 = Cake('Super Sweet Meringue', 'meringue', 'very sweet', [], gluten_free=True)
waffle1 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa')

Cake.export_1_cake_to_html = export_1_cake_to_html
Cake.export_1_cake_to_html(cake1)

Cake.export_all_cakes_to_html = types.MethodType(export_all_cakes_to_html, Cake)
Cake.export_all_cakes_to_html()

for item in Cake.bakery_offer:
    item.export_this_cake_to_html = types.MethodType(export_this_cake_to_html, item)
    item.export_this_cake_to_html()

