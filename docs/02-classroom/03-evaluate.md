# 2.3. Evaluate

## Goal

* Create a new test data file named `exam_results.json` which contains two names as keys, the values should be dictionaries which contain exam results like: `{'math': '90%', 'physics': '85%'}`.
* Create a new suite named `02-Exams` in `02-Classroom` suite.
* Create a new test case named `Get Exam Results` in `02-Exams` suite which will read the `exam_results.json` and log the results to the console in the following format: `Jane Doe: {'math': '90%', 'physics': '85%'}`.

## Solution

!!! info "Hints"
    `JSON (JavaScript Object Notation)` is a lightweight data-interchange format.

    [Click here to learn more about the `JSON` format](https://www.json.org/json-en.html). [Click here to see examples for `JSON`](https://json.org/example.html).

    You can decode `JSON` strings by using Python module named `json`.

    [Click here to learn more about `json` module](https://docs.python.org/3/library/json.html#module-json).

    You can use `Evaluate` keyword to evaluate expressions in Python.

    [Click here to learn more about `Evaluate` keyword](https://robotframework.org/robotframework/latest/libraries/BuiltIn.html#Evaluate).

    Robot Framework supports native `&{dict}` iteration with `FOR` loops from [version 3.2.0`](https://github.com/robotframework/robotframework/blob/master/doc/releasenotes/rf-3.2.rst#native-dict-iteration-with-for-loops). Make sure you have at least that version of Robot Framework installed!

??? success "Solution: `tests/02-classroom/test_data/exam_results.json`"
    ``` json
    {
        "Jane Doe": {
            "math": "90%",
            "physics": "85%"
        },
        "John Doe": {
            "math": "85%",
            "physics": "90%"
        }
    }
    ```

??? success "Solution: `tests/02-classroom/02-exams.robot`"
    ``` robotframework
    *** Test Cases ***
    Get Exam Results
        ${json_content}=    Get File    ${EXAM_RESULTS_JSON}
        &{results}=    Evaluate    json.loads('''${json_content}''')    json
        Log To Console    ${\n}    no_newline=True
        FOR    ${student}    ${results}    IN    &{results}
            Log To Console    ${student}: ${results}
        END

    *** Settings ***
    Library    OperatingSystem

    *** Variables ***
    ${EXAM_RESULTS_JSON}    ${CURDIR}${/}test_data${/}exam_results.json
    ```

## Results

Inside the `tests` folder, execute the following command to execute `02-Exams` suite.

``` bash
robot --suite 02-Exams .
```

You can check the generated `log.html` file to see how your test cases worked.
