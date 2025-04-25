# 4.1. Listeners

## Goal

* Create a listener named `TimeListener` that logs the start time of the test execution to the console.

## Solution

!!! info "Hints"
    Listeners can be used to monitor the test execution.

    [Click here to learn more about the listener interface](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#listener-interface).

??? success "Solution: `tests/listeners/TimeListener.py`"
    ``` python
    from robot import result, running
    from robot.api import logger
    from robot.api.interfaces import ListenerV3


    class TimeListener(ListenerV3):
        """Logs the start time of the test execution to the console."""

        def start_test(self, data: running.TestCase, result: result.TestCase):
            logger.console(
                '\nTest execution started at: {}!'.format(result.starttime)
            )
    ```

## Results
To be able to use `TimeListener` without specifying the full path to the file, you need to specify its location with the `--pythonpath` parameter.

In the `tests` folder, execute the following command.


``` bash
robot --pythonpath libraries --pythonpath listeners --listener TimeListener .
```

The start time of the execution should be mentioned at every test case:

    ==============================================================================
    Tests.01-Greetings.01-Greetings                                               
    ==============================================================================
    Original Greetings :: This test case checks that the Print Your Na... 
    Test execution started at: 20200608 16:58:16.692!
    Original Greetings :: This test case checks that the Print Your Na... | PASS |

You can check the generated `log.html` file to see how your test cases worked.
