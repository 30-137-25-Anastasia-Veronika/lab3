import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('insertion_sort.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def insertion_sort_with_logging(nums):
    """
    Сортировка вставками с подробным логированием всех операций

    Args:
        nums: список чисел для сортировки

    Returns:
        отсортированный список
    """
    logger.info("НАЧАЛО СОРТИРОВКИ ВСТАВКАМИ")
    logger.info(f"Исходный массив: {nums}")
    logger.info(f"Длина массива: {len(nums)}")

    iterations = 0
    comparisons = 0
    shifts = 0

    for i in range(1, len(nums)):
        iterations += 1
        logger.info(f"\n--- ВНЕШНИЙ ЦИКЛ i={i} ---")
        logger.info(f"Текущее состояние массива: {nums}")
        logger.info(f"Обрабатываем элемент nums[{i}] = {nums[i]}")

        item_to_insert = nums[i]
        j = i - 1
        logger.debug(f"Начинаем внутренний цикл с j={j}")

        shift_count = 0
        comparison_count = 0

        while j >= 0 and nums[j] > item_to_insert:
            iterations += 1
            comparisons += 1
            comparison_count += 1

            logger.debug(f"Сравнение: nums[{j}]={nums[j]} > {item_to_insert} = True")
            logger.debug(f"Сдвиг элемента nums[{j}]={nums[j]} на позицию nums[{j + 1}]")

            nums[j + 1] = nums[j]
            shifts += 1
            shift_count += 1
            j -= 1

            logger.debug(f"Новая позиция j={j}")

        if comparison_count > 0:
            comparisons += 1  # Последнее сравнение, которое завершило цикл
            logger.info(f"Внутренний цикл завершен. Выполнено сравнений: {comparison_count}")
            logger.info(f"Выполнено сдвигов: {shift_count}")
            logger.info(f"Найдена позиция для вставки: j+1={j + 1}")
        else:
            if j >= 0:
                comparisons += 1
                logger.debug(f"Сравнение: nums[{j}]={nums[j]} > {item_to_insert} = False")
            logger.info(f"Элемент уже на правильной позиции, сдвиги не требуются")

        nums[j + 1] = item_to_insert
        logger.info(f"Вставлен элемент {item_to_insert} на позицию nums[{j + 1}]")
        logger.info(f"Массив после итерации i={i}: {nums}")

    logger.info("СОРТИРОВКА ВСТАВКАМИ ЗАВЕРШЕНА")
    logger.info(f"Итоговый массив: {nums}")
    logger.info("СТАТИСТИКА:")
    logger.info(f"Всего итераций: {iterations}")
    logger.info(f"Всего сравнений: {comparisons}")
    logger.info(f"Всего сдвигов: {shifts}")

    return nums


def test_insertion_sort_with_different_data():
    """Тестирование сортировки вставками на различных наборах данных"""
    test_cases = {
        "Случайный массив": [9, 1, 15, 28, 6],
        "Уже отсортированный": [1, 2, 3, 4, 5],
        "Обратный порядок": [5, 4, 3, 2, 1],
        "С дубликатами": [3, 1, 4, 1, 5, 9, 2, 6],
        "Один элемент": [42],
        "Пустой массив": [],
        "Большой массив": [10, 3, 7, 1, 9, 2, 8, 6, 4, 5]
    }

    for test_name, test_data in test_cases.items():
        logger.info(f"\n{'#' * 60}")
        logger.info(f"ТЕСТ: {test_name}")
        logger.info(f"{'#' * 60}")

        data_to_sort = test_data.copy()

        sorted_data = insertion_sort_with_logging(data_to_sort)

        if len(sorted_data) > 0:
            is_sorted = all(sorted_data[i] <= sorted_data[i + 1] for i in range(len(sorted_data) - 1))
            logger.info(f"Массив корректно отсортирован: {is_sorted}")
        else:
            logger.info("Пустой массив считается отсортированным")


if __name__ == "__main__":

    test_data = [9, 1, 15, 28, 6]
    print(f"Исходные данные: {test_data}")

    result = insertion_sort_with_logging(test_data)
    print(f"Результат: {result}")
