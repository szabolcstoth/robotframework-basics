*** Settings ***
Suite Setup         Global Suite Setup
Suite Teardown      Global Suite Teardown


*** Variables ***
${NAME_FROM_INIT}       Global Name


*** Keywords ***
Global Suite Setup
    Log    Our Robot awesomeness begins!
    VAR    ${NAME_FROM_INIT}    ${NAME_FROM_INIT}    scope=GLOBAL

Global Suite Teardown
    Log    The end of the awesomeness!
