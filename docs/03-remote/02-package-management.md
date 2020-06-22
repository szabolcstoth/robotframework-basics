# 3.2. Package management

## Goal

* Create a new resource file named `apk-management.resource`.
* Create a new keyword named `APK Search` in the previously created resource file.
    * This keyword should accept two arguments: `remote_host` and `package_name`.
    * Using these arguments the keyword should execute `apk search package_name` command the given `remote_host`.
    * You should check that the command was executed successfully and log the found package(s) to the console.

## Solution

!!! info "Hints"
    Using one particular argument of `Execute Command` keyword will make sure that it returns the return code of the executed command. You can use that return code to check if the command was executed successfully.

    [Click here to learn more about the parameters of `Execute Command` keyword.](http://robotframework.org/SSHLibrary/SSHLibrary.html#Execute%20Command).

??? success "Solution: `tests/03-remote/resources/apk-management.resource`"
    ``` robotframework
    *** Keywords ***
    APK Search
        [Documentation]    This keyword searches package(s) by the given `pattern`
        ...    on the given `remote_host`.
        [Arguments]    ${remote_host}    ${package_name}

        Switch Connection    ${remote_host}
        ${stdout}    ${rc}=    Execute Command
        ...    apk search ${package_name}
        ...    return_rc=${TRUE}

        Should Be Equal As Integers    ${rc}    0
        Log To Console    ${\n}The following packages were found: ${stdout}
    ```

??? success "Solution: `tests/03-remote/01-connection.robot`"
    ``` robotframework hl_lines="8 9 24"
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
        ...    ${AUTH}[username]
        ...    ${AUTH}[password]

    *** Settings ***
    Library        SSHLibrary
    Resource       ${CURDIR}${/}resources${/}apk-management.resource
    Suite Setup    Open Connection And Log In With Password

    *** Variables ***
    &{HOST}    name=localhost    port=2222    alias=openssh-server-for-robot
    &{AUTH}    username=robotdev    password=Hn7c5%lyBpIn8*8Z
    ```

## Results

Inside the `tests` folder, execute the following command to execute `03-Remote` suite.

``` bash
robot --suite 03-remote .
```

The output should be something like this:

    -----------------------------------------------------------------------------
    Test Package Management
    The following packages were found: ipython-7.14.0-r0
    ipython-doc-7.14.0-r0
    py3-ipython_genutils-0.2.0-r2
    Test Package Management                                               | PASS |

You can check the generated `log.html` file to see how your test cases worked.
