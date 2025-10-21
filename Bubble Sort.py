import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bubble_sort.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def bubble_sort_with_logging(nums):
    """
    Сортировка пузырьком с подробным логированием всех операций

    Args:
        nums: список чисел для сортировки

    Returns:
        отсортированный список
    """
    logger.info("НАЧАЛО СОРТИРОВКИ ПУЗЫРЬКОМ")
    logger.info(f"Исходный массив: {nums}")
    logger.info(f"Длина массива: {len(nums)}")

    iterations = 0
    comparisons = 0
    swaps = 0
    passes = 0

    swapped = True

    while swapped:
        passes += 1
        iterations += 1
        logger.info(f"\n--- ПРОХОД {passes} ---")
        logger.info(f"Текущее состояние массива: {nums}")

        swapped = False
        logger.debug(f"Установлен swapped = False в начале прохода {passes}")

        for i in range(len(nums) - 1):
            iterations += 1
            comparisons += 1

            logger.debug(f"Сравнение элементов [{i}]={nums[i]} и [{i + 1}]={nums[i + 1]}")

            if nums[i] > nums[i + 1]:
                logger.info(f"ОБМЕН: nums[{i}]={nums[i]} ↔ nums[{i + 1}]={nums[i + 1]}")

                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swaps += 1

                swapped = True
                logger.debug(f"Установлен swapped = True (произошел обмен)")

                logger.debug(f"После обмена: {nums}")
            else:
                logger.debug("Элементы в правильном порядке, обмен не требуется")

        logger.info(f"Проход {passes} завершен. swapped = {swapped}")

    logger.info("СОРТИРОВКА ЗАВЕРШЕНА")
    logger.info(f"Итоговый массив: {nums}")
    logger.info("СТАТИСТИКА:")
    logger.info(f"Всего проходов: {passes}")
    logger.info(f"Всего итераций: {iterations}")
    logger.info(f"Всего сравнений: {comparisons}")
    logger.info(f"Всего обменов: {swaps}")

    return nums


def test_bubble_sort_with_different_data():
    """Тестирование сортировки пузырьком на различных наборах данных"""
    test_cases = {
        "Случайный массив": [5, 2, 1, 8, 4],
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

        sorted_data = bubble_sort_with_logging(data_to_sort)

        is_sorted = all(sorted_data[i] <= sorted_data[i + 1] for i in range(len(sorted_data) - 1))
        logger.info(f"Массив корректно отсортирован: {is_sorted}")


if __name__ == "__main__":

    test_data = [5, 2, 1, 8, 4]
    print(f"Исходные данные: {test_data}")

    result = bubble_sort_with_logging(test_data)
    print(f"Результат: {result}")

