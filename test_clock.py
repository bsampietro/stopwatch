import unittest
from unittest.mock import Mock
from unittest.mock import patch
import time
from clock import Clock

class TestClock(unittest.TestCase):
    # Using mocks directly. Not recommended because
    # it does not resets them after the test
    def test_works1(self):
        c = Clock()

        time.time = Mock(return_value=0)
        c.start()
        time.time = Mock(return_value=2)
        c.stop()

        self.assertEqual(c.elapsed_time(), 2)

        time.time = Mock(return_value=4)
        c.start()
        time.time = Mock(return_value=7)
        c.stop()

        self.assertEqual(c.elapsed_time(), 5)
        self.assertEqual(c.display_time(True), '00:00:05')

    # Should use patch for module methods, because they
    # are mocked only inside the context otherwise
    # it might generate weird side effects
    def test_work2(self):
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

    # As a decorator and patching only the time method
    @patch.object(time, 'time')
    def test_running_and_move(self, time_mock):
        c = Clock()
        self.assertFalse(c.running)

        time.time.return_value = 100
        c.start()
        self.assertTrue(c.running)
        c.move(300)

        time.time.return_value = 400
        c.stop()
        self.assertFalse(c.running)

        self.assertEqual(c.display_time(True), '00:10:00')


if __name__ == '__main__':
    unittest.main()
