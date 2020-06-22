# 1.5. Create a common resource file

## Goal

* Move the keyword named `Print Your Name` to a common resource file named `greetings.resource`.
* Import this resource file in `01-Greetings` suite to make `Greetings` test case pass.
* Rename `Greetings` test case to `Original Greetings`.
* Store another name in the `greetings.resource` and log it in a new test case named `Greetings Again` using `Print Your Name` keyword.

## Solution

!!! info "Hints"
    You can import resource files using the `Resource` setting in the `*** Settings ***` table.

    [Click here to learn more about importing resource files](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#resource-and-variable-files).

    You can use built-in variables related to operating system like `${CURDIR}`, `${EXECDIR}` and `${/}` when you define the path for a resource file.

    [Click here to learn more about operating system related variables](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#built-in-variables).

??? success "Solution: `tests/01-greetings/resources/greetings.resource`"
    ``` robotframework
    *** Keywords ***
    Print Your Name
        [Arguments]    ${your_name}=Jane Doe
        Log    ${your_name}

    *** Variables ***
    ${ANOTHER_NAME_IN_RESOURCE}    Common Name
    ```

??? success "Solution: `tests/01-greetings/01-greetings.robot`"
    ``` robotframework hl_lines="6 7 9 10"
    *** Test Cases ***
    Original Greetings
        Print Your Name
        Print Your Name    ${YOUR_NAME}

    Greetings Again
        Print Your Name    ${ANOTHER_NAME_IN_RESOURCE}

    *** Settings ***
    Resource    ${CURDIR}${/}resources${/}greetings.resource

    *** Variables ***
    ${YOUR_NAME}    Your Name
    ```

## Results

Inside the `tests` folder, execute the following command to execute both test cases.

``` bash
robot .
```

You can check the generated `log.html` file to see how your test cases worked.
