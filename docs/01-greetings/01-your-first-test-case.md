# 1.1. Your first test case

## Goal

* Create a new test case named `Greetings` in the `01-Greetings` suite, which logs your name.

## Solution

!!! info "Hints"
    You need to define your test cases in the `*** Test Cases ***` test data section.

    [Click here to learn more about test data sections](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-data-sections).

    Robot Framework has a standard library named `BuiltIn`, which provides the most generic keywords. This library is imported automatically, its keywords are accessible anytime.

    [Click here to learn more about `Log` keyword](https://robotframework.org/robotframework/latest/libraries/BuiltIn.html#Log).

??? success "Solution: `tests/01-greetings/01-greetings.robot`"
    ``` robotframework
    *** Test Cases ***
    Greetings
        Log    Your Name
    ```

## Results

!!! question "How to execute a test case?"
    Use the `robot` command. You need to define a folder or a file which contains at least one test case. [Click here to learn more about command line options](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#starting-test-execution).

Inside the `tests` folder, execute the following command.

``` bash
robot .
```

The output should be something like this:

    ==============================================================================
    Tests
    ==============================================================================
    Tests.01-Greetings
    ==============================================================================
    Tests.01-Greetings.01-Greetings
    ==============================================================================
    Greetings                                                             | PASS |
    ------------------------------------------------------------------------------
    Tests.01-Greetings.01-Greetings                                       | PASS |
    1 critical test, 1 passed, 0 failed
    1 test total, 1 passed, 0 failed
    ==============================================================================
    Tests.01-Greetings                                                    | PASS |
    1 critical test, 1 passed, 0 failed
    1 test total, 1 passed, 0 failed
    ==============================================================================
    Tests                                                                 | PASS |
    1 critical test, 1 passed, 0 failed
    1 test total, 1 passed, 0 failed
    ==============================================================================
    Output:  /tmp/robot_course/tests/output.xml
    Log:     /tmp/robot_course/tests/log.html
    Report:  /tmp/robot_course/tests/report.html

You can check the generated `log.html` file to see how your test case worked.
