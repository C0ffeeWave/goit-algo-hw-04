def total_salary(path):
    try:
        total = 0
        count = 0
        
        with open(path, 'r', encoding='utf-8') as fh:
            for line in fh:
                name, salary = line.strip().split(',')
                if salary.isdigit():  # Перевірка, чи зарплата є числом
                    total += int(salary)
                    count += 1
                else:
                    print(f"Помилка у даних файлу '{path}'. Зарплата '{salary}' не є числом.")
        
        if count == 0:
            return 0, 0  # Повертаємо (0, 0), якщо файл порожній
        else:
            average = total / count
            return total, average
    
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return None, None  # Повертаємо None, якщо файл не знайдено

# Визначення шляху до файлу
path = "D:\\Projects\\my_repo\\goit-algo-hw-04\\First_task_folder\\salary.txt"

# Виклик функції total_salary і отримання результатів
total, average = total_salary(path)

# Виведення результатів
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

