*** Settings ***
Suite Setup       Global Suite Setup
Suite Teardown    Global Suite Teardown

*** Keywords ***
Global Suite Setup
    Log    Our Robot awesomeness begins!
    Set Global Variable    ${NAME_FROM_INIT}

Global Suite Teardown
    Log    The end of the awesomeness!

*** Variables ***
${NAME_FROM_INIT}    Global Name
