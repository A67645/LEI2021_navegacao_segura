*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}   firefox
${word}
${URL}   https://www.google.com/
@{ Word_list }  covid-19   jobs   health

*** Keywords ***
Set Environment Variable  webdriver.gecko.driver  ./geckodriver.exe
acessogoogle
	${word}=   Evaluate  random.choice($Word_list) 
	sleep   3
	Wait Until Element Is Visible   xpath=//*[@id="zV9nZe"]
	Click Button   xpath=//*[@id="zV9nZe"]
	Input Text   xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input   ${word}
	sleep   3
	Log To Console   ${word}
	sleep   3
	press keys   None   ENTER
	sleep   3
	${Page1}=   Get Element Attribute   xpath=/html/body/div[7]/div/div[9]/div[1]/div//a   href
	Log To Console   ${Page1}

*** Test cases ***
LoginTest
	Open Browser  ${URL} 
	Maximize Browser Window
	acessogoogle
	Close Browser



