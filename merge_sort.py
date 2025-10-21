import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('merge_sort.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

merge_calls = 0
merge_sort_calls = 0
comparisons = 0
elements_processed = 0


def merge_with_logging(left_list, right_list, depth=0):
    """
    Слияние двух отсортированных списков с логированием

    Args:
        left_list: левый отсортированный список
        right_list: правый отсортированный список
        depth: глубина рекурсии (для отступов в логах)
    """
    global merge_calls, comparisons, elements_processed

    merge_calls += 1
    indent = "  " * depth

    logger.info(f"{indent}ВХОД В MERGE (вызов #{merge_calls})")
    logger.info(f"{indent}Левый список: {left_list}")
    logger.info(f"{indent}Правый список: {right_list}")

    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    step = 0
    merge_comparisons = 0

    logger.debug(f"{indent}Длины: left={left_list_length}, right={right_list_length}")
    logger.debug(f"{indent}Начальные индексы: left_index=0, right_index=0")

    for i in range(left_list_length + right_list_length):
        step += 1
        elements_processed += 1

        logger.debug(f"{indent}--- Шаг {step} ---")
        logger.debug(f"{indent}Текущий sorted_list: {sorted_list}")
        logger.debug(f"{indent}Индексы: left_index={left_list_index}, right_index={right_list_index}")

        if left_list_index < left_list_length and right_list_index < right_list_length:
            comparisons += 1
            merge_comparisons += 1

            left_val = left_list[left_list_index]
            right_val = right_list[right_list_index]

            logger.debug(
                f"{indent}Сравнение: left[{left_list_index}]={left_val} <= right[{right_list_index}]={right_val}")

            if left_val <= right_val:
                sorted_list.append(left_val)
                left_list_index += 1
                logger.debug(f"{indent}Добавлен left элемент: {left_val}, новый left_index={left_list_index}")
            else:
                sorted_list.append(right_val)
                right_list_index += 1
                logger.debug(f"{indent}Добавлен right элемент: {right_val}, новый right_index={right_list_index}")

        elif left_list_index == left_list_length:
            # Достигнут конец левого списка, добавляем из правого
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
            logger.debug(f"{indent}Левый список закончился, добавлен right: {right_list[right_list_index - 1]}")

        elif right_list_index == right_list_length:
            # Достигнут конец правого списка, добавляем из левого
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
            logger.debug(f"{indent}Правый список закончился, добавлен left: {left_list[left_list_index - 1]}")

    logger.info(f"{indent} ВЫХОД ИЗ MERGE (вызов #{merge_calls})")
    logger.info(f"{indent}Результат слияния: {sorted_list}")
    logger.info(f"{indent}Статистика вызова: сравнений={merge_comparisons}, элементов={len(sorted_list)}")

    return sorted_list


def merge_sort_with_logging(nums, depth=0):
    """
    Сортировка слиянием с подробным логированием

    Args:
        nums: массив для сортировки
        depth: глубина рекурсии (для отступов в логах)

    Returns:
        отсортированный массив
    """
    global merge_sort_calls

    merge_sort_calls += 1
    current_call = merge_sort_calls
    indent = "  " * depth

    logger.info(f"{indent} ВХОД В MERGE_SORT (вызов #{current_call}, глубина {depth})")
    logger.info(f"{indent}Входные данные: {nums}")
    logger.info(f"{indent}Длина массива: {len(nums)}")

    # Базовый случай рекурсии
    if len(nums) <= 1:
        logger.info(f"{indent} БАЗОВЫЙ СЛУЧАЙ: массив уже отсортирован (длина <= 1)")
        logger.info(f"{indent} ВЫХОД ИЗ MERGE_SORT (вызов #{current_call}) -> {nums}")
        return nums

    mid = len(nums) // 2
    logger.info(f"{indent}  Разделение массива: mid={mid}")
    logger.info(f"{indent}Левый подмассив: {nums[:mid]}")
    logger.info(f"{indent}Правый подмассив: {nums[mid:]}")

    logger.info(f"{indent} Рекурсивный вызов для левой части...")
    left_list = merge_sort_with_logging(nums[:mid], depth + 1)
    logger.info(f"{indent} Рекурсивный вызов для правой части...")
    right_list = merge_sort_with_logging(nums[mid:], depth + 1)

    logger.info(f"{indent} Левая часть отсортирована: {left_list}")
    logger.info(f"{indent} Правая часть отсортирована: {right_list}")

    # Слияние отсортированных частей
    logger.info(f"{indent} Вызов merge для слияния частей...")
    result = merge_with_logging(left_list, right_list, depth)

    logger.info(f"{indent} ВЫХОД ИЗ MERGE_SORT (вызов #{current_call})")
    logger.info(f"{indent}Финальный результат: {result}")

    return result


def test_merge_sort_with_different_data():
    """Тестирование сортировки слиянием на различных наборах данных"""
    global merge_calls, merge_sort_calls, comparisons, elements_processed

    test_cases = {
        "Случайный массив": [120, 45, 68, 250, 176],
        "Уже отсортированный": [1, 2, 3, 4, 5],
        "Обратный порядок": [5, 4, 3, 2, 1],
        "С дубликатами": [3, 1, 4, 1, 5, 9, 2, 6],
        "Один элемент": [42],
        "Пустой массив": [],
        "Большой массив": [10, 3, 7, 1, 9, 2, 8, 6, 4, 5],
        "Все одинаковые": [5, 5, 5, 5, 5]
    }

    for test_name, test_data in test_cases.items():
        merge_calls = 0
        merge_sort_calls = 0
        comparisons = 0
        elements_processed = 0

        logger.info(f"\n{'#' * 80}")
        logger.info(f"ТЕСТ: {test_name}")
        logger.info(f"Данные: {test_data}")
        logger.info(f"{'#' * 80}")

        data_to_sort = test_data.copy()

        sorted_data = merge_sort_with_logging(data_to_sort)

        if len(sorted_data) > 0:
            is_sorted = all(sorted_data[i] <= sorted_data[i + 1] for i in range(len(sorted_data) - 1))
            logger.info(f"Массив корректно отсортирован: {is_sorted}")
        else:
            logger.info("Пустой массив считается отсортированным")

        # Выводим итоговую статистику для этого теста
        logger.info(f"\n ИТОГОВАЯ СТАТИСТИКА ДЛЯ ТЕСТА '{test_name}':")
        logger.info(f"Вызовов merge_sort: {merge_sort_calls}")
        logger.info(f"Вызовов merge: {merge_calls}")
        logger.info(f"Всего сравнений: {comparisons}")
        logger.info(f"Обработано элементов: {elements_processed}")
        logger.info(f"Размер массива: {len(test_data)}")


if __name__ == "__main__":


    test_data = [120, 45, 68, 250, 176]
    print(f"Исходные данные: {test_data}")

    result = merge_sort_with_logging(test_data)
    print(f"Результат: {result}")