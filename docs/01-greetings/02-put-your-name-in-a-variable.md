# 1.2. Put your name in a variable

## Goal

* Store your name in a variable using the `*** Variables ***` table.
* Modify the `Greetings` test case to use the newly created variable instead of the hardcoded name!

## Solution

!!! info "Hints"
    You can define suite variables in the `*** Variables ***` test data section.

    [Click here to learn more about variables](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#variables).

??? success "Solution: `tests/01-greetings/01-greetings.robot`"
    ``` robotframework hl_lines="3 5 6"
    *** Test Cases ***
    Greetings
        Log    ${YOUR_NAME}

    *** Variables ***
    ${YOUR_NAME}    Your Name
    ```

## Results

In the `tests` folder, execute the following command.

``` bash
robot .
```

You can check the generated `log.html` file to see how your test case worked.
