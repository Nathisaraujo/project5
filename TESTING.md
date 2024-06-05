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

* [ACCESSIBILITY](<#accessibility>) 

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

* I'd like to point out that the quantity input on the products page appears too small on devices with screen widths less than 390px. To address this, I added the following code to the CSS file. Although it seemed to work when tested in the browser's developer tools, it didn't have the desired effect in the final testing phase.

![quantity button css](/readme-images/qty-css.png)

# BROWSER COMPATIBILITY
Tested the website on different web browsers to ensure consistent functionality and appearance across all major browsers.

| Browser | Comments | Pass/Fail |
| --- | --- | --- | 
| Google Chrome | Displays and functions correctly  | PASS |
| Mozilla Firefox | Displays and functions correctly  | PASS |
| Microsoft Edge | Displays and functions correctly  | PASS |
| Opera | Displays and functions correctly  | PASS |
| Samsung Internet | Displays and functions correctly  | FAIL |

* The project encountered issues specifically on the Samsung Internet Browser, as it exhibited numerous responsiveness problems. Interestingly, the same website displayed no responsiveness issues in other browsers.

# ACCESSIBILITY

I utilized Lighthouse, an automated tool integrated into web browsers and available as a Chrome extension, to evaluate the website's performance, accessibility, best practices, and SEO. Additionally, I employed the WAVE accessibility tool to further assess the site's accessibility. I addressed most of the issues or recommendations provided by Lighthouse and Wave.

You can review the detailed results below.

LIGHTHOUSE

| File path                     | Performance | Accessibility | Best Practices | SEO | 
|-------------------------------|-------------|---------------|----------------|-----|
| *ABOUT APP*                   |             |               |                |     |
| about/                        | 45          | 94            | 74             | 92  |
| about/edit                    | 45          | 94            | 74             | 92  |
| *BAG APP*                     |             |               |                |     |
| bag/                          | 45          | 94            | 74             | 92  |
| *BLOG APP*                    |             |               |                |     |
| blog/                         | 45          | 94            | 74             | 92  |
| blog/post_detail              | 45          | 94            | 74             | 92  |
| blog/add_post                 | 45          | 94            | 74             | 92  |
| *CHECKOUT APP*                |             |               |                |     |
| checkout/                     | 45          | 94            | 74             | 92  |
| checkout/checkout_success     | 45          | 94            | 74             | 92  |
| *COMMUNITY APP*               |             |               |                |     |
| community/                    | 45          | 94            | 74             | 92  |
| *EVENTS APP*                  |             |               |                |     |
| events/                       | 45          | 94            | 74             | 92  |
| events/add/                   | 45          | 94            | 74             | 92  |
| events/edit/                  | 45          | 94            | 74             | 92  |
| *HOME APP*                    |             |               |                |     |
| home/                         | 45          | 94            | 74             | 92  |
| home/privacy_policy           | 45          | 94            | 74             | 92  |
| *PRODUCTS APP*                |             |               |                |     |
| products/                     | 45          | 94            | 74             | 92  |
| products/product_detail       | 45          | 94            | 74             | 92  |
| products/edit                 | 45          | 94            | 74             | 92  |
| products/add_product          | 45          | 94            | 74             | 92  |
| products/add_product_tags     | 45          | 94            | 74             | 92  |
| *PROFILES APP*                |             |               |                |     |
| profile/                      | 45          | 94            | 74             | 92  |
| profile/management            | 45          | 94            | 74             | 92  |
| profile/wishilist             | 45          | 94            | 74             | 92  |
| profile/update_profile        | 45          | 94            | 74             | 92  |
| profile/saved_events          | 45          | 94            | 74             | 92  |
| profile/recomemmendation_form | 45          | 94            | 74             | 92  |
| profile/orders                | 45          | 94            | 74             | 92  |
