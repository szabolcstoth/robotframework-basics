# 2.4. Class based libraries

## Goal

* Create a new class based library named `JSONLibrary` with a keyword named `Parse JSON File`. This keyword should open and parse the content of the given JSON file and return the parsed data.
* Make sure that the `JSONLibrary` available to every test case.
* Modify the test case named `Get Exam Results` to use `JSONLibrary` and `Parse JSON File` keyword.

## Solution

!!! info "Hints"
    Test libraries can be implemented as Python modules and Python or Java classes.

    [Click here to learn more about creating test libraries](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-keywords).

??? success "Solution: `tests/libraries/JSONLibrary.py`"
    ``` python
    from robot.api.deco import keyword
    from robot.api.deco import library
    import json


    @library(scope='GLOBAL', version='1.0')
    class JSONLibrary():
        """Library which contains keywords to work with JSON files."""

        @keyword(tags=['json'], types={'json_file': str})
        def parse_json_file(self, json_file):
            """Returns the parsed ``json_file`` as a dictionary.

            Example:
            | &{parsed_json}= | Parse JSON File | exam_results.json |
            =>
            | ${parsed_json}= {'Jane Doe': {'math': '90%', 'physics': '85%'}}
            """
            with open(json_file, 'r') as json_content:
                return json.load(json_content)
    ```

??? success "Solution: `tests/02-classroom/02-exams.robot`"
    ``` robotframework hl_lines="3 10"
    *** Test Cases ***
    Get Exam Results
        &{results}=    Parse JSON File    ${EXAM_RESULTS_JSON}
        Log To Console    ${\n}    no_newline=True
        FOR    ${student}    ${results}    IN    &{results}
            Log To Console    ${student}: ${results}
        END

    *** Settings ***
    Library    JSONLibrary

    *** Variables ***
    ${EXAM_RESULTS_JSON}    ${CURDIR}${/}test_data${/}exam_results.json
    ```

## Results

To be able to import `JSONLibrary` without defining the whole path to the file, you need to set its location with `--pythonpath` parameter.

Inside the `tests` folder, execute the following command to execute `02-Exams` suite.

``` bash
robot --pythonpath libraries --suite 02-Exams .
```

You can check the generated `log.html` file to see how your test cases worked.
