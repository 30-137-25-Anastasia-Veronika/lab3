import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('heap_sort_detailed.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

heapify_calls = 0
comparisons = 0
swaps = 0


def heapify_with_logging(nums, heap_size, root_index, depth=0):
    """
    Построение кучи с подробным логированием

    Args:
        nums: массив для сортировки
        heap_size: размер кучи
        root_index: корневой индекс
        depth: глубина рекурсии (для отступов в логах)
    """
    global heapify_calls, comparisons, swaps

    heapify_calls += 1
    current_call = heapify_calls
    indent = "  " * depth

    if root_index >= len(nums) or root_index < 0:
        logger.error(f"{indent} ОШИБКА: Неверный индекс root_index={root_index}, размер массива={len(nums)}")
        return

    logger.info(f"{indent} ВХОД В HEAPIFY (вызов #{current_call}, глубина {depth})")
    logger.info(f"{indent}Корень: индекс {root_index}, значение {nums[root_index]}")
    logger.info(f"{indent}Размер кучи: {heap_size}")
    logger.info(f"{indent}Текущее состояние массива: {nums}")

    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    left_val = nums[left_child] if left_child < heap_size and left_child < len(nums) else "N/A"
    right_val = nums[right_child] if right_child < heap_size and right_child < len(nums) else "N/A"

    logger.debug(f"{indent}Левый потомок: индекс {left_child}, значение {left_val}")
    logger.debug(f"{indent}Правый потомок: индекс {right_child}, значение {right_val}")

    if left_child < heap_size and left_child < len(nums):
        comparisons += 1
        logger.debug(
            f"{indent}Сравнение левого потомка: nums[{left_child}]={nums[left_child]} > nums[{largest}]={nums[largest]}")
        if nums[left_child] > nums[largest]:
            largest = left_child
            logger.info(
                f"{indent}Левый потомок больше корня. Новый наибольший: индекс {largest}, значение {nums[largest]}")
        else:
            logger.debug(f"{indent}Левый потомок не больше корня")

    if right_child < heap_size and right_child < len(nums):
        comparisons += 1
        logger.debug(
            f"{indent}Сравнение правого потомка: nums[{right_child}]={nums[right_child]} > nums[{largest}]={nums[largest]}")
        if nums[right_child] > nums[largest]:
            largest = right_child
            logger.info(
                f"{indent} Правый потомок больше. Новый наибольший: индекс {largest}, значение {nums[largest]}")
        else:
            logger.debug(f"{indent}Правый потомок не больше")

    if largest != root_index and largest < len(nums):
        swaps += 1
        logger.info(f"{indent} ОБМЕН: nums[{root_index}]={nums[root_index]} ↔ nums[{largest}]={nums[largest]}")

        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        logger.info(f"{indent}Состояние после обмена: {nums}")

        logger.info(f"{indent} Рекурсивный вызов heapify для нового корня (индекс {largest})")
        heapify_with_logging(nums, heap_size, largest, depth + 1)
    else:
        logger.info(f"{indent} Корень остался наибольшим элементом")

    logger.info(f"{indent} ВЫХОД ИЗ HEAPIFY (вызов #{current_call})")


def heap_sort_with_logging(nums):
    """
    Пирамидальная сортировка с подробным логированием

    Args:
        nums: массив для сортировки

    Returns:
        отсортированный массив
    """
    global heapify_calls, comparisons, swaps

    heapify_calls = 0
    comparisons = 0
    swaps = 0

    logger.info(" НАЧАЛО ПИРАМИДАЛЬНОЙ СОРТИРОВКИ")
    logger.info(f"Исходный массив: {nums}")
    logger.info(f"Длина массива: {len(nums)}")

    n = len(nums)

    if n == 0:
        logger.info("Массив пустой, сортировка не требуется")
        return nums

    logger.info("\n--- ЭТАП 1: ПОСТРОЕНИЕ MAX HEAP ---")
    logger.info("Создаём Max Heap из списка")
    logger.info("Второй аргумент означает остановку алгоритма перед элементом -1, т.е. перед первым элементом списка")
    logger.info("Третий аргумент означает повторный проход по списку в обратном направлении, уменьшая счётчик i на 1")

    for i in range(n - 1, -1, -1):
        logger.info(f"\n Построение кучи из корня с индексом {i}")
        heapify_with_logging(nums, n, i)
        logger.info(f"Состояние после heapify({i}): {nums}")

    logger.info(f"\n MAX HEAP ПОСТРОЕН: {nums}")

    logger.info("\n--- ЭТАП 2: ИЗВЛЕЧЕНИЕ ЭЛЕМЕНТОВ ИЗ КУЧИ ---")
    logger.info("Перемещаем корень Max Heap в конец списка")

    for i in range(n - 1, 0, -1):
        logger.info(f"\n Извлечение элемента {i + 1}/{n}:")
        logger.info(f"Обмен корня nums[0]={nums[0]} с последним элементом nums[{i}]={nums[i]}")

        swaps += 1
        nums[i], nums[0] = nums[0], nums[i]
        logger.info(f"После обмена: {nums}")

        logger.info(f"Восстановление свойства кучи для корня (новый размер кучи: {i})")
        heapify_with_logging(nums, i, 0)
        logger.info(f"Состояние после восстановления кучи: {nums}")

    logger.info(" ПИРАМИДАЛЬНАЯ СОРТИРОВКА ЗАВЕРШЕНА")
    logger.info(f"Итоговый массив: {nums}")

    return nums


def test_heap_sort_with_different_data():
    """Тестирование пирамидальной сортировки на различных наборах данных"""
    test_cases = {
        "Случайный массив": [35, 12, 43, 8, 51],
        "Уже отсортированный": [1, 2, 3, 4, 5],
        "Обратный порядок": [5, 4, 3, 2, 1],
        "С дубликатами": [3, 1, 4, 1, 5, 9, 2, 6],
        "Один элемент": [42],
        "Пустой массив": [],
        "Большой массив": [10, 3, 7, 1, 9, 2, 8, 6, 4, 5],
        "Все одинаковые": [5, 5, 5, 5, 5]
    }

    for test_name, test_data in test_cases.items():
        logger.info(f"\n{'#' * 80}")
        logger.info(f"ТЕСТ: {test_name}")
        logger.info(f"Данные: {test_data}")
        logger.info(f"{'#' * 80}")

        data_to_sort = test_data.copy()

        sorted_data = heap_sort_with_logging(data_to_sort)

        if len(sorted_data) > 0:
            is_sorted = all(sorted_data[i] <= sorted_data[i + 1] for i in range(len(sorted_data) - 1))
            logger.info(f"Массив корректно отсортирован: {is_sorted}")
        else:
            logger.info(" Пустой массив считается отсортированным")


if __name__ == "__main__":

    test_data = [35, 12, 43, 8, 51]
    print(f"Исходные данные: {test_data}")

    try:
        result = heap_sort_with_logging(test_data)
        print(f"Результат: {result}")

    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        print(f"Произошла ошибка: {e}")