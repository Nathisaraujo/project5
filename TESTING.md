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

* [KNOWN BUGS](<#known-bugs>)

* [SUMMARY](<#summary>)

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
|*ABOUT APP*                    |      |      |      |      |      |
|about/                         | PASS | PASS | PASS | PASS | PASS |
|about/edit                     | PASS | PASS | PASS | PASS | PASS |
|*BAG APP*                      |      |      |      |      |      |
|bag/                           | PASS | PASS | PASS | PASS | PASS |
|*BLOG APP*                     |      |      |      |      |      |
|blog/                          | PASS | PASS | PASS | PASS | PASS |
|blog/post_detail               | PASS | PASS | PASS | PASS | PASS |
|blog/add_post                  | PASS | PASS | PASS | PASS | PASS |
|*CHECKOUT APP*                 |      |      |      |      |      |
|checkout/                      | PASS | PASS | PASS | PASS | PASS |
|checkout/checkout_success      | PASS | PASS | PASS | PASS | PASS |
|*COMMUNITY APP*                |      |      |      |      |      |
|community/                     | PASS | PASS | PASS | PASS | PASS |
|*EVENTS APP*                   |      |      |      |      |      |
|events/                        | PASS | PASS | PASS | PASS | PASS |
|events/add/                    | PASS | PASS | PASS | PASS | PASS |
|events/edit/                   | PASS | PASS | PASS | PASS | PASS |
|*HOME APP*                     |      |      |      |      |      |
|home/                          | PASS | PASS | PASS | PASS | PASS |
|home/privacy_policy            | PASS | PASS | PASS | PASS | PASS |
|*PRODUCTS APP*                 |      |      |      |      |      |
|products/                      | PASS | PASS | PASS | PASS | PASS |
|products/product_detail        | PASS | PASS | PASS | PASS | PASS |
|products/edit                  | PASS | PASS | PASS | PASS | PASS |
|products/add_product           | PASS | PASS | PASS | PASS | PASS |
|products/add_product_tags      | PASS | PASS | PASS | PASS | PASS |
|*PROFILES APP*                 |      |      |      |      |      |
|profile/                       | PASS | PASS | PASS | PASS | PASS |
|profile/management             | PASS | PASS | PASS | PASS | PASS |
|profile/wishilist              | PASS | PASS | PASS | PASS | PASS |
|profile/update_profile         | PASS | PASS | PASS | PASS | PASS |
|profile/saved_events           | PASS | PASS | PASS | PASS | PASS |
|profile/recomemmendation_form  | PASS | PASS | PASS | PASS | PASS |
|profile/orders                 | PASS | PASS | PASS | PASS | PASS |
|*ALLAUTH TEMPLATES*            |      |      |      |      |      |
|signup/                        | PASS | PASS | PASS | PASS | PASS |
|login/                         | PASS | PASS | PASS | PASS | PASS |
|logout/                        | PASS | PASS | PASS | PASS | PASS |
|accounts/confirm-email/        | PASS | PASS | PASS | PASS | PASS |

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

These values were tested on pages where login is not required. You can review the detailed results below.

*Please note that each value follows the format: mobile/desktop.*

LIGHTHOUSE

| File path                     | Performance | Accessibility | Best Practices | SEO      |
|-------------------------------|-------------|---------------|----------------|----------|
| *ABOUT APP*                   |             |               |                |          |
| about/                        | 34/74       | 94/94         | 96/96          | 100/100  |
| *BAG APP*                     |             |               |                |          |
| bag/                          | 60/96       | 94/96         | 96/96          | 100/100  |
| *BLOG APP*                    |             |               |                |          |
| blog/                         | 60/87       | 90/90         | 96/96          | 100/100  |
| blog/post_detail              | 56/87       | 94/91         | 93/93          | 91/91    |
| *COMMUNITY APP*               |             |               |                |          |
| community/                    | 59/79       | 95/95         | 100/100        | 100/100  |
| *EVENTS APP*                  |             |               |                |          |
| events/                       | 63/95       | 94/87         | 96/96          | 100/100  |
| *HOME APP*                    |             |               |                |          |
| home/                         | 57/87       | 90/90         | 96/96          | 100/100  |
| home/privacy_policy           | 62/95       | 94/95         | 96/96          | 100/100  |
| *PRODUCTS APP*                |             |               |                |          |
| products/                     | 55/79       | 82/83         | 96/96          | 91/91    |
| products/6/                   | 54/77       | 85/81         | 96/96          | 100/100  |
| *ALLAUTH*                     |             |               |                |          |
| signup/                       | 62/96       | 94/95         | 96/96          | 100/100  |
| login/                        | 59/96       | 94/95         | 96/96          | 100/100  |



WAVE

Note that he main nav is displaying missing label errors, empty button and orphaned form label although mitigated by screen reader-only classes.

| File path                     | Comment                                                                                               |
|-------------------------------|-------------------------------------------------------------------------------------------------------|
| *ABOUT APP*                   |                                                                                                       |
| about/                        | Raised alerts regarding shipping headings' level.                                                     |
| *BAG APP*                     |                                                                                                       |
| bag/                          | Raised alerts regarding shipping headings' level.                                                                                                         |
| *BLOG APP*                    |                                                                                                       |
| blog/                         | Raised alerts regarding shipping headings' level. Fixed pagination contrast error.                                                                                                      |
| blog/post_detail              |  Raised alerts regarding shipping headings' level. Fixed suspicious link text.                                                                                                     |
| *COMMUNITY APP*               |                                                                                                       |
| community/                    |  Raised alerts regarding shipping headings' level. Low contrast errors from mailchimp box.                                                                                                      |
| *EVENTS APP*                  |                                                                                                       |
| events/                       | Raised alerts regarding shipping headings' level. "login to save event" raised redundant link alerts.                                                                                                       |
| *HOME APP*                    |                                                                                                       |
| home/                         | Raised alerts regarding shipping headings' level and a deliberately redundant link designed to prompt user action. Fixed contrast errors by changing the color of the text from white to black. |
| home/privacy_policy           |   Skipped heading level                                                                                                    |
| *PRODUCTS APP*                |                                                                                                       |
| products/                     |    Raised alerts regarding shipping headings' level. Fixed seem more button contrast, added label to select, missinh h1 heading, see more button as redundant link                                                                                                   |
| products/product_detail       |     Fixed empty buttons, missing first level heading                                                                                                  |

# MANUAL TESTING

Performed comprehensive manual testing across all website features and functionalities, meticulously examining navigation, forms, buttons, links, and interactive elements. Ensured seamless functionality and user-friendliness across all aspects of the site. Scrutinized the website against predefined user stories and acceptance criteria, confirming successful implementation and seamless task completion for users.


| User Stories    | Links Active | Features Working | Pass/Fail |
|-----------------|--------------|------------------|-----------|
|*ABOUT*          |              |                  |           |
|**[About Me Page](https://github.com/Nathisaraujo/project5/issues/10)** | Yes           | Yes              | PASS      |
|*BAG*            |              |                  |           |
| **[Purchases Total](https://github.com/Nathisaraujo/project5/issues/18)**         | Yes           | Yes              | PASS      |
| **[Select Order Details - Standard Products](https://github.com/Nathisaraujo/project5/issues/39)**         |    Yes        |      Yes         |    PASS   |
| **[Delete Product from Bag](https://github.com/Nathisaraujo/project5/issues/20)**         |    Yes        |      Yes         |    PASS   |
| **[Add Product to Bag](https://github.com/Nathisaraujo/project5/issues/19)**         |    Yes        |      Yes         |    PASS   |
|*BLOG*           |              |                  |           |
| **[Like Blog Posts](https://github.com/Nathisaraujo/project5/issues/30)**         |     Yes       |       Yes        |   PASS    |
| **[Blog (Why Art) Post Detail Page](https://github.com/Nathisaraujo/project5/issues/8)**         |      Yes      |        Yes       |   PASS    |
| **[Why Art Blog Posts Page](https://github.com/Nathisaraujo/project5/issues/8)**         |     Yes       |       Yes        |   PASS    |
|*CHECKOUT*       |              |                  |           |
| **[Purchase Checkout](https://github.com/Nathisaraujo/project5/issues/34)**         |      Yes    |       Yes        |   PASS    |
| **[Payment Security](https://github.com/Nathisaraujo/project5/issues/42)**         |     Yes       |       Yes        |    PASS   |
| **[Cancel Order](https://github.com/Nathisaraujo/project5/issues/41)**         |            |               |       |
| **[Successful Purchase](https://github.com/Nathisaraujo/project5/issues/36)**         |      Yes      |       Yes        |    PASS   |
| **[Unsuccessful Purchase](https://github.com/Nathisaraujo/project5/issues/35)**         |      Yes      |        Yes       |   PASS    |
| **[Order Confirmation](https://github.com/Nathisaraujo/project5/issues/24)**         |     Yes       |      Yes         |    PASS   |
| **[Payment Details](https://github.com/Nathisaraujo/project5/issues/23)**         |     Yes       |       Yes        |   PASS    |
|*COMMUNITY*      |              |                  |           |
| **[Community Page](https://github.com/Nathisaraujo/project5/issues/46)**         |      Yes      |       Yes        |   PASS    |
| **[Newsletter Form](https://github.com/Nathisaraujo/project5/issues/32)**         |     Yes       |      Yes         |    PASS   |
|*EVENTS*         |              |                  |           |
| **[Events Page](https://github.com/Nathisaraujo/project5/issues/44)**         |      Yes      |       Yes        |    PASS   |
|*HOME*           |              |                  |           |
| **[Home Page](https://github.com/Nathisaraujo/project5/issues/1)**         |     Yes        |        Yes       |   PASS    |
|*PRODUCTS*       |              |                  |           |
| **[Product Details](https://github.com/Nathisaraujo/project5/issues/37)**         |       Yes     |       Yes        |   PASS    |
| **[Product Detail Page](https://github.com/Nathisaraujo/project5/issues/9)**         |      Yes      |      Yes         |    PASS   |
| **[Search Product](https://github.com/Nathisaraujo/project5/issues/22)**         |      Yes      |       Yes        |   PASS    |
| **[Sort Products](https://github.com/Nathisaraujo/project5/issues/21)**         |       Yes     |       Yes        |    PASS   |
| **[Special Offers Page](https://github.com/Nathisaraujo/project5/issues/4)**         |     Yes       |       Yes        |    PASS   |
|*PROFILES*       |              |                  |           |
| **[User Profile Page](https://github.com/Nathisaraujo/project5/issues/47)**          |      Yes     |         Yes      |    PASS   |
| **[Order History](https://github.com/Nathisaraujo/project5/issues/25)**          |     Yes      |       Yes        |   PASS    |
| **[Edit User Profile](https://github.com/Nathisaraujo/project5/issues/17)**          |     Yes      |       Yes        |   PASS    |
| **[Account Page](https://github.com/Nathisaraujo/project5/issues/2)**          |      Yes     |       Yes        |    PASS   |
|*WISHLIST*       |              |                  |           |
| **[Manage Wishlist](https://github.com/Nathisaraujo/project5/issues/40)**          |    Yes       |        Yes       |   PASS    |
|*AUTHENTICATION* |              |                  |           |
| **[Recover Password](https://github.com/Nathisaraujo/project5/issues/16)**          |      Yes     |        Yes       |   PASS    |
| **[Logout](https://github.com/Nathisaraujo/project5/issues/15)**          |    Yes       |      Yes         |   PASS    |
| **[Login](https://github.com/Nathisaraujo/project5/issues/14)**          |    Yes       |      Yes         |   PASS    |
| **[Confirm Registration](https://github.com/Nathisaraujo/project5/issues/13)**          |     Yes      |        Yes       |    PASS   |
| **[Register](https://github.com/Nathisaraujo/project5/issues/12)**          |      Yes     |        Yes       |   PASS    |
|*MANAGEMENT*     |              |                  |           |
| **[Admin - Management](https://github.com/Nathisaraujo/project5/issues/45)**          |    Yes       |       Yes        |   PASS    |
| **[Admin - Post Blog](https://github.com/Nathisaraujo/project5/issues/29)**          |     Yes      |      Yes         |   PASS    |
| **[Manage Products](https://github.com/Nathisaraujo/project5/issues/28)**          |     Yes      |       Yes        |    PASS   |
|*OTHERS*     |              |                  |           |
| **[Footer](https://github.com/Nathisaraujo/project5/issues/43)**          |      Yes     |       Yes        |   PASS    |
| **[Contact Details](https://github.com/Nathisaraujo/project5/issues/31)**          |     Yes      |       Yes        |    PASS   |
| **[Navigation Bar](https://github.com/Nathisaraujo/project5/issues/11)**          |     Yes      |        Yes       |   PASS    |
| **[Privacy Policy](https://github.com/Nathisaraujo/project5/issues/48)**          |     Yes      |        Yes       |   PASS    |
| **[404 error page](https://github.com/Nathisaraujo/project5/issues/49)**          |      Yes     |       Yes        |  PASS     |

# DEFENSIVE PROGRAMMING

Implemented defensive programming techniques to handle unexpected inputs, edge cases, and error conditions gracefully. Utilized exception handling, input validation, and error messages to enhance the robustness and reliability of the code. Users will experience a smooth and intuitive interface with features such as popups for confirming product deletions, informative messages if the payment process fails, and toast notifications when editing items. These additions, among others, ensure a seamless and user-friendly shopping experience, minimizing disruptions and enhancing overall satisfaction.

![defensive programming](/readme-images/defensive.jpg)

# KNOWN BUGS

- The "remove from bag" button was working perfectly, but during final testing, it suddenly stopped functioning. I managed to fix the bug, but I am unsure why it initially stopped working. I am documenting this in case the issue reoccurs.

- I received an email about the AWS free tier limit. I hope this doesn't impact the functionality of the project or cause it to stop working.

![AWS email](/readme-images/aws.png)

- Adding product tags: When editing a product, you can add tags if none are already assigned. If tags exist, you can update them using the update button. If a user tries to add product tags to a product that already has tags, an error message will be displayed, and the user will be instructed to use the update feature. This limitation is noted on the management page. While this is an area for potential improvement, I only discovered it while writing this document and do not have the time to make changes at this moment.

- The reset password template has an alignment issue. The text is not displayed correctly on large screens because I forgot to add some margin.

![reset password](/readme-images/reset-password.png)

# SUMMARY

I thoroughly tested the entire project using various validators to ensure the highest quality and compliance with web standards. Specifically, I validated the HTML, CSS, JavaScript, and Python code to identify and rectify any issues that could affect the functionality or performance of the application. For accessibility testing, I utilized tools like Lighthouse and WAVE to ensure that the application is accessible to all users, including those with disabilities. This comprehensive testing process helped to identify and address numerous potential issues, ensuring that the application meets the necessary accessibility standards.

In addition to using validators and accessibility tools, I read the documentation for each specific language and framework used in the project. This allowed me to adhere to best practices and meet the required guidelines. I focused on improving code readability and included comments throughout the codebase to guide future developers and maintainers. Wherever possible, I performed refactoring to enhance the structure and efficiency of the code. This not only improved the maintainability of the project but also ensured that the code is clean, well-organized, and easy to understand. My goal was to create a robust, user-friendly, and accessible application that adheres to industry standards and best practices.