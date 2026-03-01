# 1.8. Global variables

## Goal

* Store a differrent name in the `__init__.robot` file and log it in a new test case named `Greetings From Global` with the `Print Your Name` keyword.

## Solution

??? success "Solution: `tests/__init__.robot`"
    ``` robotframework hl_lines="6 7 13"
    *** Settings ***
    Suite Setup         Global Suite Setup
    Suite Teardown      Global Suite Teardown


    *** Variables ***
    ${NAME_FROM_INIT}       Global Name


    *** Keywords ***
    Global Suite Setup
        Log    Our Robot awesomeness begins!
        VAR    ${NAME_FROM_INIT}    ${NAME_FROM_INIT}    scope=GLOBAL

    Global Suite Teardown
        Log    The end of the awesomeness!
    ```

??? success "Solution: `tests/01-greetings/01-greetings.robot`"
    ``` robotframework hl_lines="21 22 23 24"
    *** Settings ***
    Resource    ${CURDIR}${/}resources${/}greetings.resource


    *** Variables ***
    ${YOUR_NAME}    Your Name


    *** Test Cases ***
    Original Greetings
        [Documentation]    This test case verifies that the Print Your Name keyword works as expected.
        [Tags]    ubuntu
        Print Your Name
        Print Your Name    ${YOUR_NAME}

    Greetings Again
        [Documentation]    This test case proves that we can import variables from resource files.
        [Tags]    centos
        Print Your Name    ${ANOTHER_NAME_IN_RESOURCE}

    Greetings From Init
        [Documentation]    This test case proves that we can create global variables using initialization files.
        [Tags]    centos    ubuntu
        Print Your Name    ${NAME_FROM_INIT}
    ```

## Results

In the `tests` folder, execute the following command.

``` bash
robot .
```

You can check the generated `log.html` file to see how your test cases worked.
