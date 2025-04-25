# 3.3. Do not hardcode passwords

## Goal

* Instead of hardcoding the `username` and `password` in the `Variables` test data section, the user should provide these variables.

## Solution

!!! info "Hints"
    You can set variables that are available globally from the command line using the `--variable` option.

    [Click here to learn more about setting variables from the command line.](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#setting-variables-in-command-line).

??? success "Solution: `tests/03-remote/01-connection.robot`"
    ``` robotframework hl_lines="19 20 28"
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
    ```

## Results

In the `tests` folder, execute the following command to execute the `03-Remote` suite.

``` bash
robot \
  --variable SSH_USERNAME:robotdev \
  --variable SSH_PASSWORD:Hn7c5%lyBpIn8*8Z \
  --suite 03-remote .
```

You can check the generated `log.html` file to see how your test cases worked.
