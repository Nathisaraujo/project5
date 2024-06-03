# TESTING

Back to [Drawing Gratitude README](https://github.com/Nathisaraujo/project5/blob/main/README.md)

# TABLE OF CONTENTS

* [CODE VALIDATION](<#code-validation>)
    * [HTML](<#html>) 
    * [CSS](<#css>) 
    * [Python](<#python>)
    * [JavaScript](<#javascript>)

* [RESPONSIVENESS](<#responsivess>) 

* [BROWSER COMPATIBILITY](<#browser-compatibility>) 

* [LIGHTHOUSE](<#lighthouse>) 

* [MANUAL TESTING](<#manual-testing>)

* [DEFENSIVE PROGRAMMING](<#defensive-programming>) 

* [USER STORY TESTING](<#user-story-testing>)

# CODE VALIDATION

## Html 
Ensured that all HTML code adheres to the standards set by the W3C Markup Validation Service.

![html validation](/readme-images/html.png)

## Css
Validated all CSS code using the W3C CSS Validation Service to ensure compliance with CSS standards.

An error persisted in the Font Awesome minified CSS file. 

![css validation](/readme-images/css.png)

Additionally, while there were several warnings, it's noteworthy that they were primarily associated with third-party resources. The only warning directly related to my own CSS file stemmed from the allauth and Code Institute walkthrough CSS. For more details, please refer to the image below:

![css validation](/readme-images/css_validation.png)

## Python
Validated all Python Files using CI Python Linter to ensure code quality and adherence to PEP 8 guidelines.

![python validation](/readme-images/python.png)

## JavaScript
I validated all JavaScript code using JSHint. Below are my settings, as I encountered syntax errors when the "new JavaScript features" option was unchecked.

Additionally, the AWS and ChimpMail JavaScript files generate numerous warnings. However, since these are third-party libraries, I chose not to address them to avoid potential disruptions in my project's functionality.

![js validation settings](/readme-images/js-settings.png)

