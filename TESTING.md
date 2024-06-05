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

# RESPONSIVENESS

I tested the responsiveness of the entire site to ensure it works well on mobile phones, tablets, and computers.

I would like to highlight that I developed the entire project on a 1920x1080 screen, which is why there are media queries designed for screens larger than 1600 pixels. I made every effort to correct any errors across various devices. I also utilized Bootstrap classes (such as m, t, lg, md, etc.) to enhance the responsiveness of the media queries.

I extensively tested the responsiveness of the website using the developer tools available in web browsers.

I inspired myself to do the table below on the following project: [The Coffee Collective](https://github.com/LauraMayock/the-coffee-collective/blob/main/TESTING.md?plain=1)

You can use this table for reference:

| Title | Screen Size | Description                | Reference on devtools              |
|-------|-------------|----------------------------|------------------------------------|
| xs    | <576px      | SmartPhone                 | Galaxy S8+                         |
| md    | >768px      | Tablets                    | iPad Mini                          |
| lg    | >992px      | Large Desktops             | Kindle Fire HDX                    |
| xl    | >1200px     | Extra Large Desktops       | Nest Hub Max                       |
| xxl   | >1400px     | Extra Extra Large Desktops | Tested on my own monitor           |



------------------------------------------------


|File path                      | XS   | MD   | LG   | XL   | XXL  |
|------------------------------ |----- | ---- | ---- | ---- | ---- |
|*ABOUT APP*                    | ---- | ---- | ---- | ---- | ---- |
|about/                         | PASS | PASS | PASS | PASS | PASS |
|about/edit                     | PASS | PASS | PASS | PASS | PASS |
|*BAG APP*                      | ---- | ---- | ---- | ---- | ---- |
|bag/                           | PASS | PASS | PASS | PASS | PASS |
|*BLOG APP*                     | ---- | ---- | ---- | ---- | ---- |
|blog/                          | PASS | PASS | PASS | PASS | PASS |
|blog/post_detail               | PASS | PASS | PASS | PASS | PASS |
|blog/add_post                  | PASS | PASS | PASS | PASS | PASS |
|*CHECKOUT APP*                 | ---- | ---- | ---- | ---- | ---- |
|checkout/                      | PASS | PASS | PASS | PASS | PASS |
|checkout/checkout_success      | PASS | PASS | PASS | PASS | PASS |
|*COMMUNITY APP*                | ---- | ---- | ---- | ---- | ---- |
|community/                     | PASS | PASS | PASS | PASS | PASS |
|*EVENTS APP*                   | ---- | ---- | ---- | ---- | ---- |
|events/                        | PASS | PASS | PASS | PASS | PASS |
|events/add/                    | PASS | PASS | PASS | PASS | PASS |
|events/edit/                   | PASS | PASS | PASS | PASS | PASS |
|*HOME APP*                     | ---- | ---- | ---- | ---- | ---- |
|home/                          | PASS | PASS | PASS | PASS | PASS |
|home/privacy_policy            | PASS | PASS | PASS | PASS | PASS |
|*PRODUCTS APP*                 | ---- | ---- | ---- | ---- | ---- |
|products/                      | PASS | PASS | PASS | PASS | PASS |
|products/product_detail        | PASS | PASS | PASS | PASS | PASS |
|products/edit                  | PASS | PASS | PASS | PASS | PASS |
|products/add_product           | PASS | PASS | PASS | PASS | PASS |
|products/add_product_tags      | PASS | PASS | PASS | PASS | PASS |
|*PROFILES APP*                 | ---- | ---- | ---- | ---- | ---- |
|profile/                       | PASS | PASS | PASS | PASS | PASS |
|profile/management             | PASS | PASS | PASS | PASS | PASS |
|profile/wishilist              | PASS | PASS | PASS | PASS | PASS |
|profile/update_profile         | PASS | PASS | PASS | PASS | PASS |
|profile/saved_events           | PASS | PASS | PASS | PASS | PASS |
|profile/recomemmendation_form  | PASS | PASS | PASS | PASS | PASS |
|profile/orders                 | PASS | PASS | PASS | PASS | PASS |


