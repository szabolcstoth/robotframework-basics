# 2.5. Module based libraries

## Goal

* Create a new module based library named `HelperLibrary` with a keyword named `Generate Random Number`. This keyword should return a random number between `0` and `100`.
* Make sure that the `HelperLibrary` available to every test case.
* Create a new suite variable named `@{STUDENTS}` in `02-Exams` suite and store some names in it.
* Create a new test case named `Generate Exam Results` in `02-Exams` suite which will use `Generate Random Number` keyword for every student. Save the results in a file named `yet_another_results_file.txt` in the following format: `Jane Doe: 80%`.
* Make sure that the `yet_another_results_file.txt` is removed before the test case execution starts.

## Solution

!!! info "Hints"
    Test libraries can be implemented as Python modules and Python or Java classes.

    [Click here to learn more about creating test libraries](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-keywords).

    You can define test setup with `[Setup]` setting in the Test Case table.
    [Click here to learn more about test setup and teardown functionality](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-setup-and-teardown).

??? success "Solution: `tests/libraries/HelperLibrary.py`"
    ``` python
    from robot.api.deco import keyword
    import random


    @keyword(tags=['random'], types={'min': int, 'max': int})
    def generate_random_number(min, max):
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
        ${file_content}=    Set Variable
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

To be able to import `HelperLibrary` without defining the whole path to the file, you need to set its location with `--pythonpath` parameter.

Inside the `tests` folder, execute the following command to execute `02-Exams` suite.


``` bash
robot --pythonpath libraries --suite 02-Exams .
```

The content of the `02-classroom/test_data/yet_another_results_file.txt` should be something like this:

    Jane Doe: 78%
    John Doe: 61%

You can check the generated `log.html` file to see how your test cases worked.
