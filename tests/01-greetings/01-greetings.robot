*** Settings ***
Resource    ${CURDIR}${/}resources${/}greetings.resource


*** Variables ***
${YOUR_NAME}    Your Name


*** Test Cases ***
Original Greetings
    [Documentation]    This test case verifies that the Print Your Name keyword works as expected.
    [Tags]    ubuntu
    Print Your Name
    Print Your Name    ${YOUR_NAME}

Greetings Again
    [Documentation]    This test case proves that we can import variables from resource files.
    [Tags]    centos
    Print Your Name    ${ANOTHER_NAME_IN_RESOURCE}

Greetings From Init
    [Documentation]    This test case proves that we can create global variables using initialization files.
    [Tags]    centos    ubuntu
    Print Your Name    ${NAME_FROM_INIT}
