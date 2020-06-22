*** Test Cases ***
Get Date From Remote Host
    Switch Connection    ${HOST}[alias]
    ${date}=    Execute Command    date

    Log To Console    ${date}

Test Package Management
    APK Search    ${HOST}[alias]    ipython

*** Keywords ***
Open Connection And Log In With Password
    Open Connection
    ...    ${HOST}[name]
    ...    port=${HOST}[port]
    ...    alias=${HOST}[alias]

    Login
    ...    ${SSH_USERNAME}
    ...    ${SSH_PASSWORD}

*** Settings ***
Library        SSHLibrary
Resource       ${CURDIR}${/}resources${/}apk-management.resource
Suite Setup    Open Connection And Log In With Password

*** Variables ***
&{HOST}    name=localhost    port=2222    alias=openssh-server-for-robot
