import unittest
import robot
from io import StringIO
from unittest.mock import patch

class MyTestCase(unittest.TestCase):
    #@patch("sys.stdin", StringIO("forward 10\noff\n"))
    def test_update_c_history(self):
        robot.update_c_history("forward 10")
        self.assertEqual(robot.command_list[0],'forward 10')
        robot.update_c_history("back 22")
        self.assertEqual(robot.command_list[1],'back 22')
    

    def test_retrieve_commands(self):
        robot.update_c_history("forward 10")
        self.assertEqual(['forward 10'], robot.retrieve_commands())
        