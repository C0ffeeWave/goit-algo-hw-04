def get_cats_info(path):
    try:
        if 'dog' in path.lower():
            print("Помилка: Назва файлу містить слово 'dog'.")
            return []  # Повертаємо порожній список, оскільки назва файлу містить слово 'dog'
        
        cats_info = []  
        with open(path, 'r', encoding='utf-8') as fh:
            for line in fh:
                cat_data = line.strip().split(',')
                cats_info.append({"id": cat_data[0], "name": cat_data[1], "age": int(cat_data[2])})
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено")
        return []
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return []
    return cats_info

cats = get_cats_info('D:\Projects\my_repo\goit-algo-hw-04\second_task_folder/cats.txt')
#Виводимо кожен словник з нового рядка
for cat in cats:
    print(cat)
