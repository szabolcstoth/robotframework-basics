# 1.8. Global variables

## Goal

* Store a differrent name in the `__init__.robot` file and log it in a new test case named `Greetings From Global` with the `Print Your Name` keyword.

## Solution

??? success "Solution: `tests/__init__.robot`"
    ``` robotframework hl_lines="8 13 14"
    *** Settings ***
    Suite Setup       Global Suite Setup
    Suite Teardown    Global Suite Teardown

    *** Keywords ***
    Global Suite Setup
        Log    Our Robot awesomeness begins!
        Set Global Variable    ${NAME_FROM_INIT}

    Global Suite Teardown
        Log    The end of the awesomeness!

    *** Variables ***
    ${NAME_FROM_INIT}    Global Name
    ```

??? success "Solution: `tests/01-greetings/01-greetings.robot`"
    ``` robotframework hl_lines="13 14 15 16"
    *** Test Cases ***
    Original Greetings
        [Tags]    ubuntu
        [Documentation]    This test case verifies that the Print Your Name keyword works as expected.
        Print Your Name
        Print Your Name    ${YOUR_NAME}

    Greetings Again
        [Tags]    centos
        [Documentation]    This test case proves that we can import variables from resource files.
        Print Your Name    ${ANOTHER_NAME_IN_RESOURCE}

    Greetings From Init
        [Tags]    centos    ubuntu
        [Documentation]    This test case proves that we can create global variables using initialization files.
        Print Your Name    ${NAME_FROM_INIT}

    *** Settings ***
    Resource    ${CURDIR}${/}resources${/}greetings.resource

    *** Variables ***
    ${YOUR_NAME}    Your Name
    ```

## Results

In the `tests` folder, execute the following command.

``` bash
robot .
```

You can check the generated `log.html` file to see how your test cases worked.
