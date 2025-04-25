# 2.5. Module based libraries

## Goal

* Create a new module based library named `HelperLibrary` with a keyword named `Generate Random Number`. This keyword should return a random number between `0` and `100`.
* Make sure that the `HelperLibrary` is available to each test case.
* Create a new suite variable named `@{STUDENTS}` in the `02-Exams` suite and store some names in it.
* Create a new test case named `Generate Exam Results` in the `02-Exams` suite that uses the `Generate Random Number` keyword for each student. Save the results to a file named `yet_another_results_file.txt` in the following format: `Jane Doe: 80%`.
* Make sure that the `yet_another_results_file.txt` is removed before the test case execution starts.

## Solution

!!! info "Hints"
    Test libraries can be implemented as Python modules or classes.

    [Click here to learn more about creating test libraries](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-keywords).

    You can define a test setup with the `[Setup]` setting in the Test Case table.
    [Click here to learn more about test setup and teardown functionality](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-setup-and-teardown).

??? success "Solution: `tests/libraries/HelperLibrary.py`"
    ``` python
    from robot.api.deco import keyword
    import random


    @keyword(tags=['random'])
    def generate_random_number(min: int, max: int):
        """Generates a random number between `min` and `max`.

        Example:
        | ${random_number}= | Generate Random Number | ${0} | ${100} |
        =>
        | ${random_number}= 87
        """
        return random.randint(min, max)
    ```

??? success "Solution: `tests/02-classroom/02-exams.robot`"
    ``` robotframework hl_lines="9 10 11 12 13 14 15 16 19 21 25 26"
    *** Test Cases ***
    Get Exam Results
        &{results}=    Parse JSON File    ${EXAM_RESULTS_JSON}
        Log To Console    ${\n}    no_newline=True
        FOR    ${student}    ${results}    IN    &{results}
            Log To Console    ${student}: ${results}
        END

    Generate Exam Results
        [Setup]    Remove File    ${FILE_TO_CREATE}
        VAR    ${file_content}
        FOR    ${student}    IN    @{STUDENTS}
            ${grade}=    Generate Random Number    ${0}    ${100}
            ${file_content}=    Catenate    ${file_content}    ${student}: ${grade}%${\n}
        END
        Create File    ${FILE_TO_CREATE}    ${file_content}

    *** Settings ***
    Library    HelperLibrary
    Library    JSONLibrary
    Library    OperatingSystem

    *** Variables ***
    ${EXAM_RESULTS_JSON}    ${CURDIR}${/}test_data${/}exam_results.json
    ${FILE_TO_CREATE}       ${CURDIR}${/}test_data${/}yet_another_results_file.txt
    @{STUDENTS}             Jane Doe    John Doe
    ```

## Results

To be able to import `HelperLibrary` without specifying the full path to the file, you need to specify its location with the `--pythonpath` parameter.

In the `tests` folder, execute the following command to execute the `02-Exams` suite.


``` bash
robot --pythonpath libraries --suite 02-Exams .
```

The content of the `02-classroom/test_data/yet_another_results_file.txt` should be something like this:

    Jane Doe: 78%
    John Doe: 61%

You can check the generated `log.html` file to see how your test cases worked.
