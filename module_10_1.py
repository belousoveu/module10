from time import sleep

def write_word(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(word_count):
            f.write(f"Какое-то слово № {i}" + '\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')
