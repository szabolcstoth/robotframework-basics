# 2.2. File handling

## Goal

* Create a new test data file named `students.txt` which contains two names in separate lines.
* Create a new keyword named `Read Names From File` which will log the names to console from the `students.txt`.
* Create a new test case named `Students` which will utilize the previously created keyword.

## Solution

!!! info "Hints"
    You can handle files and directories by using keywords from the `OperatingSystem` library.

    [Click here to learn more about the `OperatingSystem` library](https://robotframework.org/robotframework/latest/libraries/OperatingSystem.html).

    You will need to use `Split To Lines` keyword from the `String` library.

    [Click here to learn more about the `String` library](https://robotframework.org/robotframework/latest/libraries/String.html).

??? success "Solution: `tests/02-classroom/test_data/students.txt`"
    ```
    Jane Doe
    John Doe
    ```

??? success "Solution: `tests/02-classroom/resources/lists.resource`"
    ``` robotframework hl_lines="9 10 11 12 13 15 16 17"
    *** Keywords ***
    Print Multiple Names
        [Arguments]    ${multiple_names}
        Log To Console    ${\n}    no_newline=True
        FOR    ${name}    IN    @{multiple_names}
            Log To Console    ${name}
        END

    Read Names From File
        [Arguments]    ${file_with_names}
        ${file_content}=    Get File    ${file_with_names}
        @{names}=    Split To Lines    ${file_content}
        [Return]    ${names}

    *** Settings ***
    Library    OperatingSystem
    Library    String
    ```

??? success "Solution: `tests/02-classroom/01-lists.robot`"
    ``` robotframework hl_lines="7 8 9 10 17"
    *** Test Cases ***
    Greetings Everyone
        [Tags]    loop
        [Documentation]    This test case verifies the functionality of 'Print Multiple Names' keyword.
        Print Multiple Names    ${MULTIPLE_NAMES}

    Students
        [Documentation]    This test case logs the names from students.txt to console.
        @{students}=    Read Names From File    ${STUDENTS_TXT}
        Print Multiple Names    ${students}

    *** Settings ***
    Resource    ${CURDIR}${/}resources${/}lists.resource

    *** Variables ***
    @{MULTIPLE_NAMES}    Jane Doe    John Doe
    ${STUDENTS_TXT}      ${CURDIR}${/}test_data${/}students.txt
    ```

## Results

Inside the `tests` folder, execute the following command to execute `02-Classroom` suite.

``` bash
robot --suite 02-classroom .
```

You can check the generated `log.html` file to see how your test cases worked.
