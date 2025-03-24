import sys
import importlib.util
import unittest

# Function to dynamically load a module from the given file path
def load_module(file_path):
    print(f"Loading module from: {file_path}")  # Add this line for debugging
    module_name = file_path.replace('.py', '')
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# Unit test for factors function
class TestPrimeFactors(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Ensure module is properly loaded
        if hasattr(module, 'factors'):
            cls.factors = module.factors
        else:
            raise AttributeError(f"The module does not contain a 'factors' function.")

    def test_1(self):
        self.assertEqual(module.factors(1), [])
    
    def test_2(self):
        self.assertEqual(module.factors(2), [])
    
    def test_3(self):
        self.assertEqual(module.factors(3), [])
    
    def test_4(self):
        self.assertEqual(module.factors(4), [2, 2])
    
    def test_6(self):
        self.assertEqual(module.factors(6), [2, 3])
    
    def test_12(self):
        self.assertEqual(module.factors(12), [2, 2, 3])

    def test_15(self):
        self.assertEqual(module.factors(15), [3, 5])
    
    def test_29(self):
        self.assertEqual(module.factors(29), [])
    
    def test_30(self):
        self.assertEqual(module.factors(30), [2, 3, 5])
    
    def test_100(self):
        self.assertEqual(module.factors(100), [2, 2, 5, 5])
    
    def test_101(self):
        self.assertEqual(module.factors(101), [])
    
    def test_13195(self):
        self.assertEqual(module.factors(13195), [5, 7, 13, 29])
    
    def test_600851475143(self):
        self.assertEqual(module.factors(600851475143), [71, 839, 1471, 6857])

    def test_60(self):
        self.assertEqual(module.factors(60), [2, 2, 3, 5])
    
    def test_997(self):
        self.assertEqual(module.factors(997), [])
    
    def test_1024(self):
        self.assertEqual(module.factors(1024), [2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
    
    def test_large_prime_product(self):
        self.assertEqual(module.factors(999331 * 999979), [999331, 999979])
    
    def test_small_and_large_prime_product(self):
        self.assertEqual(module.factors(3 * 999331), [3, 999331])
    
    def test_360(self):
        self.assertEqual(module.factors(360), [2, 2, 2, 3, 3, 5])
    
    def test_81(self):
        self.assertEqual(module.factors(81), [3, 3, 3, 3])

# Main entry point
if __name__ == '__main__':
    # Ensure a module path is provided as argument
    if len(sys.argv) < 2:
        print("Please provide a Python module file as an argument.")
        sys.exit(1)
    
    file_path = sys.argv[1]

    # Dynamically load the module
    try:
        module = load_module(file_path)
        print(f"Module loaded: {module.__name__}")
    except Exception as e:
        print(f"Failed to load module: {e}")
        sys.exit(1)

    # Run the unit tests
    unittest.main(argv=[sys.argv[0]], exit=False)  # Pass only script name to unittest
