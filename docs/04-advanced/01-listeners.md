# 4.1. Listeners

## Goal

* Create a listener named `TimeListener` which logs the start time of the test execution to the console.

## Solution

!!! info "Hints"
    Listeners can be used to monitor the test execution.

    [Click here to learn more about the listener interface](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#listener-interface).

??? success "Solution: `tests/listeners/TimeListener.py`"
    ``` python
    from robot.api import logger


    class TimeListener():
        """Logs the start time of the test execution to console."""

        ROBOT_LISTENER_API_VERSION = 3

        def start_test(self, test, result):
            logger.console(
                '\nTest execution started at: {}!'.format(result.starttime)
            )
    ```

## Results

To be able to use `TimeListener` without defining the whole path to the file, you need to set its location with `--pythonpath` parameter.

Inside the `tests` folder, execute the following command.


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
