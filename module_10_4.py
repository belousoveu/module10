from threading import Thread, Lock
from queue import Queue
from time import sleep


class Table:
    def __init__(self, id):
        self.id = id
        self.is_busy = False


class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.queue = Queue()

    def customer_arrival(self):
        for i in range(20):
            sleep(1)
            customer = Customer(i + 1, self)
            print(f"{customer} пришел")
            self.serve_customer(customer)

    def serve_customer(self, customer):
        available_table = next((table for table in self.tables if not table.is_busy), None)
        if available_table:
            available_table.is_busy = True
            print(f"{customer} сел за стол {available_table.id}. (начало обслуживания)")
            customer.table = available_table
            customer.start()
        else:
            print(f"П{customer} ожидает свободный стол. (помещение в очередь)")
            self.queue.put(customer)

    def customer_finish(self, customer):
        sleep(5)
        print(f"{customer} покушал и ушёл. (конец обслуживания)")
        customer.table.is_busy = False
        if not self.queue.empty():
            next_customer = self.queue.get()
            self.serve_customer(next_customer)


class Customer(Thread):
    def __init__(self, id, cafe):
        Thread.__init__(self)
        self.id = id
        self.cafe = cafe
        self.table = None

    def run(self):
        self.cafe.customer_finish(self)

    def __str__(self):
        return f"Посетитель номер {self.id}"


if __name__ == '__main__':
    # Создаем столики в кафе
    tables = [Table(i) for i in range(1, 4)]

    # Инициализируем кафе
    cafe = Cafe(tables)

    # Запускаем поток для прибытия посетителей
    customer_arrival_thread = Thread(target=cafe.customer_arrival)
    customer_arrival_thread.start()

    # Ожидаем завершения работы прибытия посетителей
    customer_arrival_thread.join()
