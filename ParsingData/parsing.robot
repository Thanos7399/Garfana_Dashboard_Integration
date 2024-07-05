*** Settings ***
Library   OperatingSystem
Library   robot_log_parser.py

*** Variables ***
${OUTPUT_XML_PATH}    /home/einfochips/Desktop/Project/Robot_Frame_Work/Data_Parsing/output.xml

*** Test Cases ***
Get Test Case Counts
    [Documentation]    Get pass, fail, and skip counts from Robot Framework output.xml
    ${pass_count}    ${fail_count}    ${skip_count}=    Get Test Case Counts    ${OUTPUT_XML_PATH}
    Log    Pass count: ${pass_count}
    Log    Fail count: ${fail_count}
    Log    Skip count: ${skip_count}

    
*** Keywords ***

