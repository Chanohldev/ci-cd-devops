import sys
from pathlib import Path
import unittest

# Obtiene el directorio del archivo actual (test_main.py)
test_dir = Path(__file__).parent
# Obtiene el directorio padre (tests)
project_dir = test_dir.parent
# Agrega el directorio 'src' al sys.path
src_dir = project_dir / 'src'
sys.path.insert(0, str(src_dir))
import main  # noqa


class TestMathOperation(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.add(1, 2), 3)

        class TestMathOperation(unittest.TestCase):
            def test_add(self):
                self.assertEqual(main.add(1, 2), 3)
                self.assertEqual(main.add(-1, 1), 0)
                self.assertEqual(main.add(-1, -1), -2)
                self.assertEqual(main.add(0, 0), 0)
                self.assertEqual(main.add(100, 200), 300)

        if __name__ == '__main__':
            unittest.main()
