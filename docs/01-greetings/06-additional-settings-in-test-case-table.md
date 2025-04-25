# 1.6. Additional settings in Test Case table

## Goal

* Tag one of your test cases with `ubuntu` and tag the other one with `centos`.
* Write brief documentation for both test cases.

## Solution

!!! info "Hints"
    You can tag test cases using the `[Tags]` setting in Test Case table.

    You can write documentation using the `[Documentation]` setting in Test Case table.

    [Click here to learn more about the available settings in Test Case table](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-case-section).

??? success "Solution: `tests/01-greetings/01-greetings.robot`"
    ``` robotframework hl_lines="3 4 9 10"
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

You can use the `--include` parameter to select test cases by a tag.
``` bash
robot --include centos .
robot --include ubuntu .
```

You can check the generated `log.html` file to see how your test cases worked.
