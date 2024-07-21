*** Settings ***
Library   SeleniumLibrary

*** Variables ***
${REPORT_PATH}    file:///home/einfochips/Desktop/Project/Robot_Frame_Work/Data_Parsing/report.html


*** Test Cases ***
Test 1
    Open Browser    https://www.google.com/    chrome
    Sleep    3s
    Close Browser
Test 2
    Open Browser    https://city.imd.gov.in/citywx/city_weather.php?id=42647    chrome
    Sleep    5s
    Close Browser

HTML Report Validation  
    Open Browser    ${REPORT_PATH}    chrome
    Maximize Browser Window
    Sleep    5 seconds    # Wait for 5 seconds to view the report
    Close Browser

    
*** Keywords ***

