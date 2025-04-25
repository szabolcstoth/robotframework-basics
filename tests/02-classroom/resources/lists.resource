*** Keywords ***
Print Multiple Names
    [Arguments]    ${multiple_names}
    Log To Console    ${\n}    no_newline=True
    FOR    ${name}    IN    @{multiple_names}
        Log To Console    ${name}
    END

Read Names From File
    [Arguments]    ${file_with_names}
    ${file_content}=    Get File    ${file_with_names}
    @{names}=    Split To Lines    ${file_content}
    RETURN    ${names}

*** Settings ***
Library    OperatingSystem
Library    String