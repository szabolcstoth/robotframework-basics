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
