import json

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.db_file, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = []

    def save_data(self):
        with open(self.db_file, 'w') as file:
            json.dump(self.data, file, ensure_ascii = False)

    def create_watch(self,model, manufacturer, price, descr):
        watch = {
            'id': len(self.data) + 1,
            'model': model,
            'manufacturer': manufacturer,
            'price': price,
            'description': descr
        }
        self.data.append(watch)
        self.save_data()
        return watch

    def get_watch_by_id(self, watch_id):
        for watch in self.data:
            if watch['id'] == watch_id:
                return watch
        return None

    def update_watch(self, watch_id, update_data):
        for watch in self.data:
            if watch['id'] == watch_id:
                for key, value in update_data.items():
                    if key in watch:
                        watch[key] = value
                self.save_data()
                return watch
        return None            

    
        
    def delete_watch(self, watch_id):
        for watch in self.data:
            if watch['id'] == watch_id:
                self.data.remove(watch)
                self.save_data()
                return f'Товар с id-{watch_id} успешно удален. '
        return f'Товара с id-{watch_id} нет!'

    def get_all_watches(self):
        return self.data
    
    def close(self):
        # self.save_data()
        self.data = []
class View():
    @staticmethod
    def view():
        file_path = 'smartwatches.json'
        with open(file_path, 'r') as file:
            data = json.load(file)
        return json.dumps(data, ensure_ascii=False, indent=2)

        

class Model(Database):
    def create(self,model, manufacturer, price, descr):
        super().create_watch(model, manufacturer, price, descr)
        

            

class Controller(Model,View):
    a=Database('smartwatches.json')
    while True:
        print("Что бы вы хотели сделать с базой данных?")
        print("Если вы хотите создать запись в базе данных введите 'c'")
        print("Если вы хотите получить запись с базы данных введите 'r'")
        print("Если вы хотите обновить запись в базе данных введите 'u'")
        print("Если вы хотите удалить запись из базы данных введите 'd'")
        print('0 - Выйти')
        key=input(':')
        if key=='c':
            name=input('Модель часов: ')
            company=input('Производитель: ')
            price=input('Цена: ')
            desc=input('Описание: ')
            a.create_watch(name,company,price,desc)
        elif key=='r':
            print('1 - вывести весь список товаров\n2 - вывести по id\n')
            key2=input(':')
            if key2=='1':
                print(View.view())
            elif key=='2':
                id=input('Введите id товара\n:')
                print(a.get_watch_by_id(id))
            else:
                print('Не корректный вводй!')
        elif key=='u':
            pass
        elif key=='d':
            id2=input('Введите id товара\n:')
            a.delete_watch(id2)
        elif key=='0':
            break
        else:
            print('Не корректный ввод!')