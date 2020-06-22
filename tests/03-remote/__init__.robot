*** Keywords ***
Open Connection And Log In With Password
    Set Global Variable    ${HOST}
    Open Connection
    ...    ${HOST}[name]
    ...    port=${HOST}[port]
    ...    alias=${HOST}[alias]

    Login
    ...    ${SSH_USERNAME}
    ...    ${SSH_PASSWORD}

*** Settings ***
Library        SSHLibrary
Suite Setup    Open Connection And Log In With Password

*** Variables ***
&{HOST}    name=localhost    port=2222    alias=openssh-server-for-robot
