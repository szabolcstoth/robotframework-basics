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