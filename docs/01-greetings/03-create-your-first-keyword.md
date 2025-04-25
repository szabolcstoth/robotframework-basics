# 1.3. Create your first keyword

## Goal

* Create a new keyword named `Print Your Name` which will log the value of `${YOUR_NAME}` variable.
* Use this newly created keyword in the `Greetings` test case.

## Solution

!!! info "Hints"
    You must define your keywords in the `*** Keywords ***` test data section.

    [Click here to learn more about creating keywords](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-user-keywords).

??? success "Solution: `tests/01-greetings/01-greetings.robot`"
    ``` robotframework hl_lines="3 5 6 7"
    *** Test Cases ***
    Greetings
        Print Your Name

    *** Keywords ***
    Print Your Name
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
