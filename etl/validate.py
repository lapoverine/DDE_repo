def validate_raw_data(data):
    if data.empty:
        raise ValueError("Датасет пустой")

    if data.isnull().sum().sum() > 0:
        print("В датасете есть пропущенные значения")

    print("Валидация выполнена")
    return True
