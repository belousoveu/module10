import multiprocessing
from multiprocessing import Manager


class WarehouseManager:

    def __init__(self):
        self.data = {}

    def process_request(self, operation):
            if operation[1] == 'receipt':
                self.add(operation[0], operation[2])
            elif operation[1] == 'shipment':
                self.remove(operation[0], operation[2])

    def add(self, product, value):
        if product in self.data:
            self.data[product] += value
        else:
            self.data[product] = value

    def remove(self, product, value):
        if product in self.data:
            self.data[product] -= value
            if self.data[product] < 0:
                self.data[product] = 0

    def run(self, request):
        processes = []
        self.data = Manager().dict()
        for request in requests:
            process = multiprocessing.Process(target=self.process_request, args=(request,))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()


if __name__ == '__main__':
    manager = WarehouseManager()

    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    manager.run(requests)

    print(manager.data)
