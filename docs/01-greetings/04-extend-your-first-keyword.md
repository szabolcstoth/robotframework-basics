# 1.4. Extend your first keyword

## Goal

* Modify the `Print Your Name` keyword to take a name as an argument.
* The keyword should work even if you do not specify a name, in which case the keyword should log `Jane Doe`.

## Solution

!!! info "Hints"
    You must define the expected arguments in the `[Arguments]` setting within the keyword table.

    [Click here to learn more about specifying arguments](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#user-keyword-arguments).

??? success "Solution: `tests/01-greetings/01-greetings.robot`"
    ``` robotframework hl_lines="4 8 9"
    *** Test Cases ***
    Greetings
        Print Your Name
        Print Your Name    ${YOUR_NAME}

    *** Keywords ***
    Print Your Name
        [Arguments]    ${your_name}=Jane Doe
        Log    ${your_name}

    *** Variables ***
    ${YOUR_NAME}    Your Name
    ```

## Results

In the `tests` folder, execute the following command.

``` bash
robot .
```

You can check the generated `log.html` file to see how your test case worked.
