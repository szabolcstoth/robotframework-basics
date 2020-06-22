# 2.1. Lists

## Goal

* Create a new test suite named `02-Classroom`, which has a suite named `01-Lists`.
* Store multiple names in a suite variable. Examples: `Jane Doe` and `John Doe`.
* Create a new keyword named `Print Multiple Names` which takes a list of names and logs them to console.

## Solution

!!! info "Hints"
    You can iterate through elements of a list by using `FOR` loop.

    [Click here to learn more about `FOR` loops](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#for-loops).

    The old syntax of `FOR` loop is deprecated since Robot Framework 3.2 and [it will be removed in 4.0](https://github.com/robotframework/robotframework/blob/master/doc/releasenotes/rf-3.2.rst#old-for-loop-syntax).

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
        [Documentation]    This test case verifies the functionality of 'Print Multiple Names' keyword.
        Print Multiple Names    ${MULTIPLE_NAMES}

    *** Settings ***
    Resource    ${CURDIR}${/}resources${/}lists.resource

    *** Variables ***
    @{MULTIPLE_NAMES}    Jane Doe    John Doe
    ```

## Results

Inside the `tests` folder, execute the following command to execute `02-Classroom` suite.

``` bash
robot --suite 02-classroom .
```

The output should be something like this:

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
