import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('selection_sort.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def selection_sort_with_logging(nums):
    """
    Сортировка выбором с подробным логированием всех операций

    Args:
        nums: список чисел для сортировки

    Returns:
        отсортированный список
    """
    logger.info("НАЧАЛО СОРТИРОВКИ ВЫБОРОМ")
    logger.info(f"Исходный массив: {nums}")
    logger.info(f"Длина массива: {len(nums)}")

    total_iterations = 0
    total_comparisons = 0
    total_swaps = 0

    for i in range(len(nums)):
        total_iterations += 1
        logger.info(f"\n--- ВНЕШНИЙ ЦИКЛ i={i} ---")
        logger.info(f"Текущее состояние массива: {nums}")
        logger.info(f"Поиск минимального элемента начиная с позиции {i}")

        lowest_value_index = i
        logger.debug(f"Начальный минимальный элемент: nums[{lowest_value_index}] = {nums[lowest_value_index]}")

        for j in range(i + 1, len(nums)):
            total_iterations += 1
            total_comparisons += 1

            logger.debug(f"  Сравнение: nums[{j}]={nums[j]} < nums[{lowest_value_index}]={nums[lowest_value_index]} ?")

            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
                logger.debug(f"  Новый минимальный элемент: nums[{lowest_value_index}] = {nums[lowest_value_index]}")
            else:
                logger.debug(f"  Текущий минимум остается: nums[{lowest_value_index}] = {nums[lowest_value_index]}")

        if lowest_value_index != i:
            logger.info(f"ОБМЕН: nums[{i}]={nums[i]} ↔ nums[{lowest_value_index}]={nums[lowest_value_index]}")

            nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
            total_swaps += 1

            logger.info(f"После обмена: {nums}")
        else:
            logger.info(f"Элемент на позиции {i} уже минимальный, обмен не требуется")

        logger.info(f"Завершен внешний цикл i={i}. Минимальный элемент '{nums[i]}' установлен на позицию {i}")

    logger.info("СОРТИРОВКА ВЫБОРОМ ЗАВЕРШЕНА")
    logger.info(f"Итоговый массив: {nums}")
    logger.info("СТАТИСТИКА ЭФФЕКТИВНОСТИ:")
    logger.info(f"Всего итераций: {total_iterations}")
    logger.info(f"Всего сравнений: {total_comparisons}")
    logger.info(f"Всего обменов: {total_swaps}")
    logger.info(f"Размер массива: {len(nums)}")

    return nums


def test_selection_sort_with_different_data():
    """Тестирование сортировки выбором на различных наборах данных"""
    test_cases = {
        "Случайный массив": [12, 8, 3, 20, 11],
        "Уже отсортированный": [1, 2, 3, 4, 5],
        "Обратный порядок": [5, 4, 3, 2, 1],
        "С дубликатами": [3, 1, 4, 1, 5, 9, 2, 6],
        "Один элемент": [42],
        "Пустой массив": [],
        "Отрицательные числа": [5, -2, 0, -8, 3],
        "Большой массив": [10, 3, 7, 1, 9, 2, 8, 6, 4, 5]
    }

    for test_name, test_data in test_cases.items():
        logger.info(f"\n{'#' * 70}")
        logger.info(f"ТЕСТ: {test_name}")
        logger.info(f"Данные: {test_data}")
        logger.info(f"{'#' * 70}")

        data_to_sort = test_data.copy()

        sorted_data = selection_sort_with_logging(data_to_sort)

        if len(sorted_data) > 0:
            is_sorted = all(sorted_data[i] <= sorted_data[i + 1] for i in range(len(sorted_data) - 1))
            logger.info(f"Массив корректно отсортирован: {is_sorted}")
        else:
            logger.info("Пустой массив считается отсортированным")


if __name__ == "__main__":
    test_data = [12, 8, 3, 20, 11]
    print(f"Исходные данные: {test_data}")

    result = selection_sort_with_logging(test_data)
    print(f"Результат: {result}")
