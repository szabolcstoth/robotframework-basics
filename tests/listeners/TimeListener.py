from robot.api import logger


class TimeListener():
    """Logs the start time of the test execution to console."""

    ROBOT_LISTENER_API_VERSION = 3

    def start_test(self, test, result):
        logger.console(
            '\nTest execution started at: {}!'.format(result.starttime)
        )
