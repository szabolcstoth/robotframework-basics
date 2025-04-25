from robot import result, running
from robot.api import logger
from robot.api.interfaces import ListenerV3


class TimeListener(ListenerV3):
    """Logs the start time of the test execution to the console."""

    def start_test(self, data: running.TestCase, result: result.TestCase):
        logger.console(
            '\nTest execution started at: {}!'.format(result.starttime)
        )
