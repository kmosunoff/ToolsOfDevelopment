import sorting
import unittest

class TestSorting(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(sorting.Sorter().bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_insertion_sort(self):
        self.assertEqual(sorting.Sorter().insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_selection_sort(self):
        self.assertEqual(sorting.Sorter().selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
if __name__ == '__main__':
    unittest.main()