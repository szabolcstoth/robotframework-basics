# 2.1. Lists

## Goal

* Create a new test suite named `02-Classroom`, which has a suite named `01-Lists`.
* Store multiple names in one suite variable. Examples: `Jane Doe` and `John Doe`.
* Create a new keyword named `Print Multiple Names` that takes a list of names and logs them to the console.

## Solution

!!! info "Hints"
    You can iterate through the elements of a list using the `FOR` loop.

    [Click here to learn more about the `FOR` loops](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#for-loops).

    The old syntax of the `FOR` loop is deprecated since Robot Framework 3.2 and [is no longer supported since 4.0](https://github.com/robotframework/robotframework/blob/master/doc/releasenotes/rf-4.0.rst#old-for-loop-syntax-is-not-supported-anymore).

??? success "Solution: `tests/02-classroom/resources/lists.resource`"
    ``` robotframework
    *** Keywords ***
    Print Multiple Names
        [Arguments]    ${multiple_names}
        Log To Console    ${\n}    no_newline=True
        FOR    ${name}    IN    @{multiple_names}
            Log To Console    ${name}
        END
    ```

??? success "Solution: `tests/02-classroom/01-lists.robot`"
    ``` robotframework
    *** Test Cases ***
    Greetings Everyone
        [Tags]    loop
        [Documentation]    This test case verifies the functionality of the 'Print Multiple Names' keyword.
        Print Multiple Names    ${MULTIPLE_NAMES}

    *** Settings ***
    Resource    ${CURDIR}${/}resources${/}lists.resource

    *** Variables ***
    @{MULTIPLE_NAMES}    Jane Doe    John Doe
    ```

## Results

In the `tests` folder, execute the following command to execute the `02-Classroom` suite.

``` bash
robot --suite 02-classroom .
```

The output should look similar to the following:

    ==============================================================================
    02-Classroom                                                                  
    ==============================================================================
    02-Classroom.01-Lists                                                         
    ==============================================================================
    Greetings Everyone :: This test case verifies the functionality of... 
    Jane Doe
    John Doe
    Greetings Everyone :: This test case verifies the functionality of... | PASS |

You can check the generated `log.html` file to see how your test cases worked.
