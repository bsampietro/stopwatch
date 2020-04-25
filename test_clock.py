import unittest
from unittest.mock import Mock, patch
from clock import Clock

class TestClock(unittest.TestCase):
    def test_works(self):
        with patch('time.time') as time_mock:
            c = Clock()

            time_mock.return_value = 0
            c.start()
            time_mock.return_value = 5
            c.stop()

            self.assertEqual(c.elapsed_time(), 5)

            time_mock.return_value = 10
            c.start()
            time_mock.return_value = 65
            c.stop()

            self.assertEqual(c.elapsed_time(), 60)
            self.assertEqual(c.display_time(True), '00:01:00')

    @patch('time.time')
    def test_running_and_move(self, time_mock):
        c = Clock()
        self.assertFalse(c.running)

        time_mock.return_value = 100
        c.start()
        self.assertTrue(c.running)
        c.move(300)

        time_mock.return_value = 400
        c.stop()
        self.assertFalse(c.running)

        self.assertEqual(c.display_time(True), '00:10:00')


if __name__ == '__main__':
    unittest.main()
