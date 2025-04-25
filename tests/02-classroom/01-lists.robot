*** Test Cases ***
Greetings Everyone
    [Tags]    loop
    [Documentation]    This test case verifies the functionality of the 'Print Multiple Names' keyword.
    Print Multiple Names    ${MULTIPLE_NAMES}

Students
    [Documentation]    This test case logs the names from students.txt to the console.
    @{students}=    Read Names From File    ${STUDENTS_TXT}
    Print Multiple Names    ${students}

*** Settings ***
Resource    ${CURDIR}${/}resources${/}lists.resource

*** Variables ***
@{MULTIPLE_NAMES}    Jane Doe    John Doe
${STUDENTS_TXT}      ${CURDIR}${/}test_data${/}students.txt
