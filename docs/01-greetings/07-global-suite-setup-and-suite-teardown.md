# 1.7. "Global" Suite Setup and Suite Teardown

## Goal

* Define a suite setup, which executes before the first test case. The suite setup should log the following: `Our Robot awesomeness begins!`.
* Define a suite teardown, which will execute after the last test case. The suite teardown should log the following: `The end of the awesomeness!`.

## Solution

!!! info "Hints"
    You can set `Suite Setup` and `Suite Teardown` in `*** Settings ***` table. If you have a test suite which was created from a directory (a folder containing suite file(s) and folder(s)), you can define setup and teardown for that suite with using an initialization file.

    [Click here to learn more about initialization files](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-suite-directories).

??? success "Solution: `tests/__init__.robot`"
    ``` robotframework
    *** Settings ***
    Suite Setup       Global Suite Setup
    Suite Teardown    Global Suite Teardown

    *** Keywords ***
    Global Suite Setup
        Log    Our Robot awesomeness begins!

    Global Suite Teardown
        Log    The end of the awesomeness!
    ```

## Results

Inside the `tests` folder, execute the following command.

``` bash
robot .
```

You can check the generated `log.html` file to see how your test cases worked.
