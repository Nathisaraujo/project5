# Drawing Gratitude

Developer: [Nathalia de Araujo Silva](https://www.linkedin.com/in/nathaliaaraujosilva/)

![home page print](/readme-images/inicial.png)

Drawing Gratitude is an e-commerce platform where users can purchase handmade, heartfelt art gifts. In addition to buying unique pieces, users can read engaging articles about art and join a vibrant community to suggest new art ideas to the artist.

Deployed website: [Go to Drawing Gratitude](https://drawing-gratitude-07bcca57b95d.herokuapp.com/)

# CONTENT

* [Overview](<#overview>)

* [DESIGN](<#design>)
    * [Typography](<#typography>)
    * [Color Scheme](<#color-scheme>)

* [USER EXPERIENCE](<#user-experience>)
    * [Audience](<#audience>)
    * [User Stories](<#user-stories>)

* [WEB MARKETING STRATEGY](<#web-marketing-strategy>)
    * [SEO](<#SEO>)
    * [XML Sitemap](<#xml-sitemap>)
    * [Newsletter](<#newsletter>)
    * [Community](<#community>)

* [FEATURES](<#features>)
    * [Existing Features](<#existing-features>)
        * [Home page](<#home-page>)
        * [Products](<#products>)
        * [Community](<#community>)
        * [About](<#about>)
        * [Blog](<#blog>)
        * [Events](<#events>)
        * [Profile](<#profile>)
    * [Future Features](<#future-features>)

* [LOGIC](<#logic>)
    * [Database](<#database>)
    * [Workflow](<#workflow>)
         * [Agile](<#agile>)
    * [Django Apps](<#django-apps>)
        * [About App](<#about-app>)
        * [Bag App](<#bag-app>)
        * [Checkout App](<#checkout-app>)
        * [Community App](<#community-app>)
        * [Events App](<#events-app>)
        * [Home App](<#home-app>)
        * [Products App](<#products-app>)
        * [Profiles App](<#profiles-app>)
        * [Wishlist App](<#wishlist-app>)

* [Techonologies Used](<#technologies-used>)
    * [Languages](<#languages>)
    * [Libraries and Programs](<#libraries-and-programs>)

* [TESTING](<#testing>)

* [DEPLOYMENT](<#deployment>)
    
* [CREDITS](<#credits>)

# OVERVIEW

Drawing Gratitude is an e-commerce platform designed to sell art. This idea came to life because I am an amateur artist. Drawing and painting are my favorite hobbies, and I decided to incorporate them into my final project.

This platform specializes in selling **heartfelt art gifts**. There's nothing better than a handmade gift full of meaning. The artwork available uses various materials, ranging from traditional paper art to digital drawings. 

The goal is for users to have an overview of all the available art pieces and purchase them directly from my website. Users can search for art by name or term using the search bar in the navbar, or they can browse by category and materials used.

### *Community*

:star: Users also have access to the **community page** to learn about the site's features. They can subscribe to the **newsletter** to receive emails about the latest news and updates. Community members can also send **drawing suggestions** to the artist.

### *Events*

:star: Additionally, there is an **events section** where users can view the events the artist has participated in and save the ones they are interested in to their profile.

### *Blog*

:star: Finally, users can access the **blog** to stay updated on various art-related topics and understand why consuming art is essential for life.

# DESIGN

The chosen design focuses on enhancing the user experience by fostering a close connection between the user and the artist selling the art. Unlike typical e-commerce sites cluttered with information and constant "buy now" prompts, the goal was to create a clean, friendly, and welcoming website. I wanted users to genuinely understand the reasons behind my work and feel inspired to purchase it, appreciating the meaningful story behind each piece.

## Typography

Each font was carefully selected to cultivate a relaxed, warm, and engaging atmosphere on the website, enhancing the overall user experience.

1. **Quicksand SemiBold 600** - it was chosen to give the website a softer and more inviting feel. Unlike harsh, squared fonts, Quicksand's smooth, rounded edges and balanced letterforms create a sense of comfort and coziness. This choice of font aligns with the overall design goal of making users feel welcome and at ease as they explore the art pieces. 

![Quicksand Font](/readme-images/quicksand.png)

- Sourced from the [Google Fonts library](https://fonts.google.com/)

2. **Le Jour Serif** - it was exclusively chosen for the logo image to add a touch of sophistication. Its elegant design provides a subtle yet distinct contrast to the overall relaxed and warm atmosphere of the website, creating a memorable and refined brand identity.

![Drawing Gratitude Logo](media/home/logo.png)

- Sourced from [Canva](https://canva.com/)

## Color Scheme

See below what is said about the color *purple* in [Color Theory](https://www.nixsensor.com/blog/color-column-violet/#:~:text=The%20color%20purple%20is%20often,mystery%2C%20independence%2C%20and%20magic.):

> Purple combines the calm stability of blue and the fierce energy of red. The color purple is often associated with royalty, nobility, luxury, power, and ambition. Purple also represents meanings of wealth, extravagance, creativity, wisdom, dignity, grandeur, devotion, peace, pride, mystery, independence, and magic.

The vibrant hue of purple was deliberately incorporated into the website's color scheme for two primary reasons:

1. Firstly, it is my favorite color, it serves as a personal touch, infusing the platform with a sense of passion and individuality. 

2. Secondly, taking into consideration the color theory, using purple on the website not only captures attention but also conveys a sense of exclusivity, inviting users to explore and indulge in the artistic experience it offers.

Inspired by the richness of the color purple, I created the following color scheme:

![Color Scheme](/readme-images/color-scheme.png)

In addition, for alerts, edit, and remove buttons, I incorporated shades of red, green, and yellow that harmonize with the overall color scheme, leveraging the color tool to ensure consistency and visual coherence throughout the design.

![alerts colors](/readme-images/alerts-colors.png)

- Sourced from [Coolors](https://coolors.co/)

# USER EXPERIENCE

## Audience

This website is designed for art enthusiasts, collectors, and individuals seeking unique, handmade gifts. It caters to those who appreciate the personal touch and meaningfulness of heartfelt art, whether they're looking to purchase a special piece for their home, find a thoughtful present, or connect with an artist's creative journey. Additionally, it appeals to community-minded individuals who enjoy engaging with art-related content, participating in community suggestions, and staying updated on the latest artistic trends and events. 

## User Stories

Taking into consideration my audience, I crafted several user stories to guide the website's development, ensuring it meets their needs and enhances their overall experience.

| Reference    | User Stories | Acceptance Criteria | 
|--------------|--------------|---------------------|
|*ABOUT*       |              |                     |
| **[About Me Page](https://github.com/Nathisaraujo/project5/issues/10)** | As a **user** I can **click on the “get to know me” button** so that **I can learn more about the artist**| - As a user, I expect to find the artist's photo and relevant personal details. <br>- As a user, I anticipate reading an engaging narrative about the artist's background and inspirations. <br>- As a user, I appreciate clickable elements within the narrative, providing direct access to respective pages. |
|*BAG*         |              |                     |
| **[Purchases Total](https://github.com/Nathisaraujo/project5/issues/18)** | As a **shopper** I can **view the total amount in my bag** so that **I can track my spending** | - The total purchases made by the user are prominently displayed in their bag dashboard. <br>- The purchases total is dynamically updated to reflect the sum of all completed purchases made by the user. <br>- Users can view their purchases total at any time within their navbar, providing them with a quick overview of their order total. |
| **[Select Order Details - Standard Products](https://github.com/Nathisaraujo/project5/issues/39)** | As a **shopper** I can **select specific order details for standard products** so that **I can tailor my order to my preferences.** | - During the checkout process, users have the option to review and confirm their selected order details before finalizing the purchase. <br> - Users can modify quantities, add or remove items, apply promo codes, and select shipping methods as needed. <br> - Clear prompts and options are provided for users to adjust their order details before proceeding to checkout. |
| **[Delete Product from Bag](https://github.com/Nathisaraujo/project5/issues/20)** | As a **shopper** I can **remove products from my shopping bag** so that ** I can manage my selections and finalize my purchase.** | - Each item in the shopping bag has a visible option to remove it. <br>- Clicking on the delete option removes the selected product from the user's shopping bag. <br>- After deleting a product from the bag, the bag content updates automatically, reflecting the removal of the item.|
| **[Add Product to Bag](https://github.com/Nathisaraujo/project5/issues/19)** | As a **shopper** I can **easily add products to my shopping bag** so that **I can keep track of items I intend to purchase.**| :- Each product listing displays an "Add to Bag" button or icon next to it. <br>- Clicking on the "Add to Bag" button adds the selected product to the user's shopping bag. <br>- Upon adding a product to the bag, users receive a confirmation message or visual indication that the item has been successfully added.|
|*BLOG*        |              |                     |
| **[Like Blog Posts](https://github.com/Nathisaraujo/project5/issues/30)** | As an **user** I can ** like blog posts** so that **I can show appreciation for content I enjoy and help promote popular articles.*| - Each blog post includes a button or icon for users to like the post. <br>- Users can click the like button to indicate their approval or enjoyment of the blog post. <br>- The number of likes is displayed alongside each post, allowing users to see which articles are popular among the community.|
| **[Blog (Why Art) Post Detail Page](https://github.com/Nathisaraujo/project5/issues/8)** | As a **user** I can **click on the post** so that **I can read their content**| - As a user, I can view engaging visuals, titles, excerpts, and author details for each post. <br>- As a user, I can view links to related subjects on the "learn more" section. <br>- As a logged-in user, I aim to express my appreciation for posts by liking them. <br>- As a non-logged-in user, I expect clear guidance on how to proceed to like a post by being redirected to the login page. |
| **[Why Art Blog Posts Page](https://github.com/Nathisaraujo/project5/issues/8)** | As a **shopper** I can **navigate to the “why art” page** so that **I can explore insights about art**| - As a user, I anticipate finding a list of engaging blog posts. <br>- As a user,  I can utilize a search bar to discover specific blog posts efficiently. <br>- As a user, I expect to see engaging visuals, titles, and excerpts for each blog post. | 
|*CHECKOUT*    |              |                     |
| **[Purchase Checkout](https://github.com/Nathisaraujo/project5/issues/34)** | As a **shopper** I can **proceed through the checkout process to complete my purchase** so that **I can finalize my order and receive the products.** | - During the checkout process, users are guided through each step, including entering shipping and payment details. <br>- Users can review their order summary, enter shipping information, select a payment method, and confirm their purchase. <br>- The checkout process includes clear navigation buttons or indicators, allowing users to progress from one step to the next.|
| **[Payment Security](https://github.com/Nathisaraujo/project5/issues/42)** | As a **shopper** I expect **robust payment security measures to protect my financial information during online transactions** so that **I can shop with confidence.** | - The website employs industry-standard encryption protocols and secure payment gateways to safeguard sensitive payment data. <br> - Users can trust that their payment information is encrypted and securely transmitted during checkout, minimizing the risk of unauthorized access or fraud. <br> - Information about payment security measures is typically provided in the website's privacy policy, terms of service, or checkout pages for users' reference. |
| **[Successful Purchase](https://github.com/Nathisaraujo/project5/issues/36)** | As a **shopper** I can **receive confirmation of a successful purchase after completing an order** so that **I have assurance that my order has been processed.** | - Users receive an immediate on-screen confirmation message <br> - Users receive an order confirmation message or email immediately after successfully completing a purchase. <br>- Users are provided with a clear call-to-action to continue shopping, track their order, or access their order history. |
| **[Unsuccessful Purchase](https://github.com/Nathisaraujo/project5/issues/35)** | As a **shopper** I can ** be notified if a purchase attempt is unsuccessful** so that **I can address any issues and successfully complete my order.**| - If a purchase attempt fails due to payment issues or other reasons, users receive an error message or notification. <br>- The error message provides details about why the purchase was unsuccessful and suggests steps for resolving the issue. <br>- Users can follow the provided instructions to update payment information, resolve any errors, and retry the purchase.|
| **[Order Confirmation](https://github.com/Nathisaraujo/project5/issues/24)** | As a **shopper** I can **receive a confirmation of my order after completing a purchase** so that ** I have assurance that my order has been successfully placed.** | -  Users receive a confirmation message or email immediately after placing an order. <br>- The order confirmation includes details such as order number, items purchased, total cost, shipping details, and estimated delivery date. <br>- Users can view their order confirmation both on the website and in their email inbox for reference. |
| **[Payment Details](https://github.com/Nathisaraujo/project5/issues/23)** | As a **shopper** I can **securely provide my payment details during checkout** so that **I can complete my purchase.**| - A section is provided during the checkout process where users can input their payment information. <br>- Users can enter their payment card details, including card number, expiration date, CVV, and billing address. <br> - Upon submitting payment details, the system securely processes the transaction and confirms successful payment.|
|*COMMUNITY*   |              |                     |
| **[Community Page](https://github.com/Nathisaraujo/project5/issues/46)** | As a **user** I can **access the community page** so that **I can obtain information on how to interact with the site** | - As a user, I can learn about the benefits of registering, such as: <br> 1. Signing up for the newsletter. <br> 2. Submitting suggestions for drawings. <br> 3. Keeping track of ongoing events. <br> 4. Simplifying the shopping experience by saving items to the wishlist. <br> 5. Accessing shipping information and order history. |
| **[Newsletter Form](https://github.com/Nathisaraujo/project5/issues/32)** | As a **user** I can **subscribe to the website's newsletter,** so that **I can stay informed about new products, promotions, and blog updates.** | - A newsletter subscription form is displayed prominently on website's community page. <br>- Users can enter their email address to subscribe to the newsletter. <br>- Upon submitting the subscription form, users receive a confirmation message and are added to the newsletter mailing list.|
|*EVENTS*      |              |                     |
| **[Events Page](https://github.com/Nathisaraujo/project5/issues/44)** | As a **user** I can **access the events tab** so that **I can view both upcoming and past events that the artist will participate in.** | - As a user, I expect to see details such as the event's name, description, location, organization, and date. <br> - As a logged-in user, I can save future event information to my profile for future reference. <br> - As a user, I can see how many people are interested in the event by checking how many have saved it. |
|*HOME*        |              |                     |
| **[Home Page](https://github.com/Nathisaraujo/project5/issues/1)** | As a **shopper** I can ** land on the website's home page** so that **I can effortlessly access all pertinent information.**| :- As a shopper, I expect clear guidance on how the website operates. <br>- As a shopper, I anticipate visible navigation buttons leading to different sections of the website. <br>- As a shopper, I desire an easily identifiable button to commence my shopping experience. |
|*PRODUCTS*    |              |                     |
| **[Product Details](https://github.com/Nathisaraujo/project5/issues/37)** | As a **shopper** I can **view detailed information about each product** so that **I can make informed purchasing decisions.** | - Product detail pages display comprehensive information about individual products, including images, descriptions, specifications, pricing and categories. <br>- Users can click on a product to access its dedicated detail page, where they can explore various attributes and features. <br>- Navigation to product detail pages is intuitive, either through category browsing, search results, or promotional banners. |
| **[Product Detail Page](https://github.com/Nathisaraujo/project5/issues/9)** | As a **shopper** I can **click on a product card** so that **I can view product details and make purchases** | - As a shopper,  I expect to see clear product photos, descriptions, and prices. <br>- As a shopper,  I expect to see tags indicating if the product is digital, a community suggestion or if it's on sale. |
| **[Search Product](https://github.com/Nathisaraujo/project5/issues/22)** | As a **shopper** I can **search for specific products using a search feature** so that **I can quickly find items of interest.** | - A search bar is prominently displayed on the website's header. <br>- Users can enter keywords or phrases into the search bar to find products matching their search query.  <br>- Upon entering a search query and pressing enter or clicking the search button, users are directed to a search results page displaying relevant products. |
| **[Sort Products](https://github.com/Nathisaraujo/project5/issues/21)** | As a **shopper** I can **sort products based on various criteria** so that **I can find items that match my preferences more easily.**| - Sorting options are provided prominently, either as dropdown menus or buttons on the products page, allowing users to select their preferred sorting method. <br>- Users can choose to sort products by criteria such as price or name. <br>- Upon selecting a sorting option, the product list refreshes or reorders itself accordingly, providing users with a sorted view of products.|
| **[Special Offers Page](https://github.com/Nathisaraujo/project5/issues/4)** | As a **shopper** I can **click on the special offers button** so that **explore special offers of the month**| - As a shopper,   I look forward to viewing discounted products with relevant descriptions. <br>- As a shopper, I expect to see the extent of discounts offered on each product.<br> - As a shopper,  I appreciate the option to filter special offers based on price or name. |
|*PROFILES*    |              |                     |
| **[User Profile Page](https://github.com/Nathisaraujo/project5/issues/47)** | As a **user** I can **access the profile page** so that **I can manage my personal information** | - As a user, I can access the profile page to view my personal and shipping information. <br> - As a user, my profile page will redirect me to: <br> 1. Order history <br> 2. Wishlist <br> 3. Page for submitting drawing suggestions <br> 4. Saved events <br> - As an admin, my profile page will also redirect me to the management page. |
| **[Order History](https://github.com/Nathisaraujo/project5/issues/25)** | As a **shopper** I can **view my order history to track past purchases** so that **I can keep a record of my transactions.** | - A dedicated section in the user account dashboard displays the user's order history. <br>- Users can access details of previous orders, including order date, items purchased, order status, and total cost. <br> - Users can navigate through their order history to view details of specific past orders or track the status of recent purchases. |
| **[Edit User Profile](https://github.com/Nathisaraujo/project5/issues/17)** | As a **shopper** I can **easily find and update my profile information** so that **I can keep my details accurate and up to date.**| :- The "Edit Profile" option is prominently displayed within the user's account profile page. <br>- Clicking on the "Edit Profile" link opens a form where users can update their personal information, such as name, email, and profile picture. <br>- After saving the changes, users are redirected to their updated profile page, ensuring their modifications are successfully applied. |
| **[Account Page](https://github.com/Nathisaraujo/project5/issues/2)** | As a **shopper** I can **click on the account button** so that ** I can log in or register.**| - As a shopper, I seek a seamless login process to proceed with my order. <br>- As a shopper, I can register on the website (if I haven't already done so) to proceed with my order. |
|*WISHLIST*    |              |                     |
| **[Manage Wishlist](https://github.com/Nathisaraujo/project5/issues/40)** | As a **shopper** I can **manage my wishlist by adding, removing, or editing items** so that **I can keep track of products I'm interested in purchasing in the future.** | - Users have access to a wishlist feature where they can save products for future consideration. <br> - Users can add products to their wishlist from product detail pages or search results, and remove or edit wishlist items as needed. <br> - The wishlist interface allows users to easily browse, organize, and manage their saved items. |
|*AUTHENTICATION* |          |                     |
| **[Recover Password](https://github.com/Nathisaraujo/project5/issues/16)** | As a **shopper** I can **click on the "recover password" button** so that **I can regain access to my account efficiently** | - The password recovery option is easily accessible on the login page or via a "Forgot Password" link. <br>- Clicking on the password recovery link opens a form where users can input their registered email address to initiate the password reset process. <br>- After submitting the password recovery form, users receive an email with instructions on resetting their password, including a link to a password reset page. Upon resetting their password, users are redirected to the login page to access their account with the new credentials. |
| **[Logout](https://github.com/Nathisaraujo/project5/issues/15)** | As a **shopper** I can **click on the logout button** so that **I can exit my session when I'm done shopping**| - The logout option is prominently displayed in the user account dropdown menu or navigation bar. <br>- Clicking on the logout link securely logs the user out of their account, clearing any session data. <br>- After logging out, users are redirected to the homepage, confirming their successful logout.|
| **[Login](https://github.com/Nathisaraujo/project5/issues/14)** | As an **user** I can **capability** so that **received benefit**| -  The login option is prominently displayed on the website's navigation bar through the dropdown menu, ensuring registered users can easily access it. <br> - Clicking on the login link opens a login form where users can input their credentials, such as username/email and password. <br>- Upon successful login, users are redirected to their account dashboard, providing seamless access to their account features. |
| **[Confirm Registration](https://github.com/Nathisaraujo/project5/issues/13)** | As a **shopper**  I want **to receive a confirmation email** so that **I can verify my account and complete the registration process.** | - Users receive a confirmation email immediately after registering, prompting them to verify their account. <br>- The confirmation page confirms successful account verification and provides clear instructions on the next steps, such as logging in to access the account. |
| **[Register](https://github.com/Nathisaraujo/project5/issues/12)** | As a **shopper** I can **provide necessary information for registration** so that **I can easily sign up for an account**| -  The registration option is prominently displayed on the website's homepage, ensuring new users can easily find it. <br>- Clicking on the registration link opens a registration form where users can input their details, such as username, email, and password. <br>- After submitting the registration form, users are redirected to a confirmation page or receive an email with a confirmation link to complete the registration process. |
|*MANAGEMENT*  |              |                     |
| **[Admin - Management](https://github.com/Nathisaraujo/project5/issues/45)** | As a **superuser** I can **access the management page via the nav-bar or my profile** so that **I can manage many website functionalities** | - As a superuser, I can see cards on the management page for editing, deleting, and creating new products and events. <br> - As a superuser, I can edit the "About Me" page and add new posts to the blog. <br> - Each administrative page will have buttons that lead to the corresponding actions. |
| **[Admin - Post Blog](https://github.com/Nathisaraujo/project5/issues/29)** | As a **an admin** I can **I can manage post blog articles** so that **I can keep the website content up to date and relevant.** | - A backend interface provides options for creating blog posts.|
| **[Manage Products](https://github.com/Nathisaraujo/project5/issues/28)** | As a **an admin** I can **manage products** so that **I can keep the website content up to date and relevant.**| - Admins have access to backend interfaces for managing products <br>- Admins can add new products, edit existing product details, update inventory, and delete products if necessary. <br>- Admins can navigate through the admin dashboard to access product management |
|*OTHERS*      |              |                     |
| **[Footer](https://github.com/Nathisaraujo/project5/issues/43)** | As a **user** I can **access important links, contact information, and additional resources from the website footer** so that **I can find relevant information and navigate the site efficiently.** | - The footer section is displayed consistently across all pages of the website, typically at the bottom of the page. <br> - The footer includes essential links to social media, contact, and payment method information. <br> - The footer includes a quick link section that redirects users to the respective page or section of the website. |
| **[Contact Details](https://github.com/Nathisaraujo/project5/issues/31)** | As a **user** I can **easily find contact details on the website footer** so that **I can reach out for assistance or inquiries.** | -Contact information, including email address, phone number, and physical address, is prominently displayed on the website. <br>- Users can use the provided contact information to get in touch with customer support. <br>- Contact details are accessible from the website footer or a dedicated "Contact Us" page, ensuring easy access for users.|
| **[Navigation Bar](https://github.com/Nathisaraujo/project5/issues/11)** | As a **shopper** I can **easily access the navigation bar** so that **I can seamlessly navigate through the website.**| :- The navigation bar is prominently displayed, ensuring it's immediately visible upon accessing the site. <br>- Hovering over a section triggers a dropdown menu, providing clear options for further navigation. <br>- Each link within the dropdown menu redirects the shopper to the corresponding page, ensuring a smooth browsing experience. |
| **[Privacy Policy](https://github.com/Nathisaraujo/project5/issues/48)** | As a **user** I can **access the privacy policy page** so that **I can understand how my data is collected** | - As a user concerned about privacy, I want to easily locate and access the privacy policy page on the website so that I can understand how my personal information is collected, used, and protected. <br> - I can return to the shop page using the button on the bottom of the page. |
| **[404 error page](https://github.com/Nathisaraujo/project5/issues/49)** | As a **user** I can **see the 404 error page** so that **I can be informed of the error and be redirected to another page** | - As a user encountering a broken link or missing page, I expect to be directed to a helpful and informative 404 error page. |





# WEB MARKETING EXPERIENCE
