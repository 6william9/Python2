import time
import unittest
from functools import wraps

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} executed in {execution_time:.6f} seconds")
        return result, execution_time
    return wrapper

@time_it
def slow_function():
    time.sleep(1)
    return "Done"

class TestTimeItDecorator(unittest.TestCase):
    def test_decorator_execution_time(self):
        _, exec_time = slow_function()
        self.assertGreaterEqual(exec_time, 1)

    def test_decorator_preserves_return_value(self):
        result, _ = slow_function()
        self.assertEqual(result, "Done")

if __name__ == "__main__":
    unittest.main()
