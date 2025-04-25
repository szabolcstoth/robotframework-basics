# 3.2. Package management

## Goal

* Create a new resource file named `apk-management.resource`.
* Create a new keyword named `APK Search` in the resource file you created earlier.
    * This keyword should take two arguments: `remote_host` and `package_name`.
    * With these arguments, the keyword should execute the `apk search --no-cache --exact package_name` command on the specified `remote_host`.
    * You should verify that the command ran successfully and log the package(s) found to the console.

## Solution

!!! info "Hints"
    Using a particular argument of the `Execute Command` keyword ensures that it returns the return code of the executed command. You can use this return code to check if the command was executed successfully.

    [Click here to learn more about the parameters of the `Execute Command` keyword.](https://marketsquare.github.io/SSHLibrary/SSHLibrary.html#Execute%20Command).

??? success "Solution: `tests/03-remote/resources/apk-management.resource`"
    ``` robotframework
    *** Settings ***
    Library    SSHLibrary

    *** Keywords ***
    APK Search
        [Documentation]    Searches for package(s) based on the specified
        ...    `pattern` on the specified `remote_host`.
        [Arguments]    ${remote_host}    ${package_name}

        Switch Connection    ${remote_host}
        ${stdout}    ${rc}=    Execute Command
        ...    apk search --no-cache --exact ${package_name}
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

In the `tests` folder, execute the following command to execute the `03-Remote` suite.

``` bash
robot --suite 03-remote .
```

The output should look similar to the following:

    -----------------------------------------------------------------------------
    Test Package Management
    The following packages were found: fetch http://dl-cdn.alpinelinux.org/alpine/v3.21/main/x86_64/APKINDEX.tar.gz
    fetch http://dl-cdn.alpinelinux.org/alpine/v3.21/community/x86_64/APKINDEX.tar.gz
    ipython-8.30.0-r0
    Test Package Management                                               | PASS |

You can check the generated `log.html` file to see how your test cases worked.
