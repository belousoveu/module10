from time import sleep, time
from threading import Thread


def write_word(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(word_count):
            f.write(f"Какое-то слово № {i+1}" + '\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


if __name__ == '__main__':
    start_time = time()
    write_word(10, 'example1.txt')
    write_word(30, 'example2.txt')
    write_word(200, 'example3.txt')
    write_word(100, 'example4.txt')

    print(f'Время записи при последовательном вызове: {time() - start_time}')

    start_time = time()
    tr1 = Thread(target=write_word, args=(10, 'example5.txt'))
    tr1.start()
    tr2 = Thread(target=write_word, args=(30, 'example6.txt'))
    tr2.start()
    tr3 = Thread(target=write_word, args=(200, 'example7.txt'))
    tr3.start()
    tr4 = Thread(target=write_word, args=(100, 'example8.txt'))
    tr4.start()
    tr1.join()
    tr2.join()
    tr3.join()
    tr4.join()
    print(f'Время записи при использовании потоков: {time() - start_time}')
