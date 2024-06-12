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
        * [Keyword Research](<#keyword-research>)
        * [Html Implementation](<#html-implementation>)
    * [Affiliate and Content Marketing](<#affiliate-and-content-marketing>)
    * [Email Marketing](<#email-marketing>)
    * [Facebook Business Page](<#facebook-business-page>)
    * [Privacy Policy](<#privacy-policy>)

* [FEATURES](<#features>)
    * [Existing Features](<#existing-features>)
        * [Navbar and Footer](<#navbar-and-footer>)
        * [Home page](<#home-page>)
        * [Products](<#products>)
        * [Community](<#community>)
        * [About](<#about>)
        * [Blog](<#blog>)
        * [Events](<#events>)
        * [Profile](<#profile>)
    * [Future Features](<#future-features>)

* [LOGIC](<#logic>)
    * [Initial Plans and Sketches](<#initial-plans-and-sketches>)
    * [Database](<#database>)
    * [Workflow](<#workflow>)
        * [About App](<#about-app>)
        * [Blog App](<#blog-app>)
        * [Bag App](<#bag-app>)
        * [Checkout App](<#checkout-app>)
        * [Community App](<#community-app>)
        * [Events App](<#events-app>)
        * [Home App](<#home-app>)
        * [Products App](<#products-app>)
        * [Profiles App](<#profiles-app>)
        * [Wishlist App](<#wishlist-app>)
    * [Agile](<#agile>)

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

- *Community*

:star: Users also have access to the **community page** to learn about the site's features. They can subscribe to the **newsletter** to receive emails about the latest news and updates. Community members can also send **drawing suggestions** to the artist.

- *Events*

:star: Additionally, there is an **events section** where users can view the events the artist has participated in and save the ones they are interested in to their profile.

- *Blog*

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

# WEB MARKETING STRATEGY

As mentioned earlier, I didn't want the website to have a constant "buy now" vibe with numerous explicit calls to action. Instead, my goal was to guide users towards making a purchase by helping them understand the importance of art. This approach naturally encourages purchases as users feel a closer connection to the artist and view the website more as a gallery than a typical e-commerce site. I aimed to build this trust by employing a "storyteller" approach.

Users can be directed to make a purchase as a first thing from the home page, but there's also an option to click on a picture of the artist to learn more about her. Additionally, there's a highlighted offers button on the home page, maintaining the narrative I established. If users aren't immediately inclined to click on the buy buttons, they're invited to explore the community page and the blog.

On the products page, each picture includes a brief description, encouraging users to contemplate each detail of the drawing. This also assists visually impaired users in imagining the art if they wish to buy it for themselves or as a gift. The detailed descriptions help everybody to understand the artwork and choose the right piece to convey the desired impression. Each product can also have a specification table, detailing the materials used, so users know what to expect upon receiving the art. Additionally, users can add items to their wishlist, allowing them to save pieces for future purchases without losing track.

The community page offers multiple links encouraging users to register on the website. It directs them to a newsletter signup form to stay updated with the latest news. Users are also informed that they can submit drawing suggestions, with the artist committing to select one suggestion per month to draw and display on the website. It encourages the the users to register as these selected suggestions will be available for a fixed price of 10 euros, and the person who submitted the suggestion will receive a free copy. This page also informs users about an events page where they can see all the art events the artist will be participating in. To further persuade users, we inform them that they can save interesting events to their profile if logged in. We also show how many people have saved each event, indicating the event's relevance to both the artist and the public.

The blog serves as a tool for users to learn more about the artist's work and its significance. Each post, authored by the artist, can include external links related to the post's subject.

On the about page, after some text about the artist, users can see cards with recommended features of the artist. They can be immediately redirected to the content that interests them.

Finally, the footer provides users with access to contact information, the artist's social media links, payment methods, and quick links to relevant website content.

## SEO

To optimize the website for search engines and improve its visibility, I employed a comprehensive SEO (Search Engine Optimization) strategy that includes keyword research, effective use of meta tags, meaningful image names, proper heading hierarchy, and both internal and external linking. By implementing these SEO strategies, the website aims to rank higher in search engine results, attract more visitors, and convert them into loyal customers.

### KEYWORD RESEARCH

The keywords I focused on include:
- Heartfelt
- Unique
- Affordable
- Handmade
- Art
- Gifts

These keywords were selected based on their relevance to the website's content and the search intent of potential users.

I conducted thorough keyword research using Google to identify the most commonly searched terms. Additionally, I leveraged [ChatGPT](https://chatgpt.com/) during brainstorming sessions to explore keywords relevant to the website's subject matter. Moreover, I installed a [ICT Keyword Generator](https://chromewebstore.google.com/detail/ict-keyword-generator/gaonneapfjigdaklggdabodjpmnfhlch?gad_source=1&gclid=CjwKCAjwvIWzBhAlEiwAHHWgvUEkWAkOXx6XtPmnniR3Kda5j-RGCjL8TeeU0r4JTOOmcJabG3BsrRoC1KgQAvD_BwE) and utilized [Wordtracker](https://www.wordtracker.com/) to assess factors such as competition and ranking. These comprehensive strategies allowed me to gather valuable insights into optimizing keyword selection for the website.

> [!NOTE]
> All keywords are strategically combined to create both short and long-tail keywords.

See below my keyword brainstorming:

![keywords list](/readme-images/keywords-list.png)

### HTML IMPLEMENTATION

Keywords are embedded within the text to enhance SEO while maintaining readability:

- **Meta Tags**: Each page has meta tags that include relevant keywords. 

- **Headings**: Proper use of heading tags (h1, h2, h3, h4, h5) ensures a clear hierarchy and includes keywords. 

- **Bold and Italic Text**: Keywords are highlighted using "strong" and "em" tags where appropriate to emphasize important points.

- **Images Optimization**: they are named meaningfully and include keywords to improve image search results.

## AFFILIATE AND CONTENT MARKETING

The blog, events and community pages are optimized with relevant keywords and include both internal and external links

- **Internal Links**: The community and blog pages contain internal links to other relevant parts of the website, improving navigation and keeping users engaged. For instance, blog posts can also link to related products.

- **External Links**: Blog posts include useful, well-informed, and trustworthy external links to enhance credibility. For example, an article about the importance of art might link to reputable sources on art history or techniques. External links use rel="noopener" to improve security.

## EMAIL MARKETING

To ensure users stay informed about new products, blog posts, events, and features on the website, I implemented an email marketing strategy using [Mailchimp](https://mailchimp.com/). By leveraging Mailchimp's user-friendly interface and robust features, I created engaging email campaigns tailored to the interests of our subscribers.

I chose to place the newsletter signup on the community page rather than in the footer because I believe users are more likely to subscribe when they understand its value. By positioning it on the community page, users can see the benefits of becoming part of our community. This page explains all the features and advantages, making it easier for users to decide to subscribe and stay informed. This approach fosters a sense of belonging and encourages users to engage more deeply with our content and updates.

![email marketing screenshot](/readme-images/email-marketing.png)

## FACEBOOK BUSINESS PAGE

The Facebook Business Page is a crucial component of web marketing strategy and to enhance it, I created a Facebook Business Page. This page serves as a dynamic platform to engage with my audience, promote new products, and share updates about the website, blog posts, and upcoming events. By leveraging Facebook's vast user base, I can reach a broader audience and drive more traffic to my website.

- [Drawing Gratitude on Facebook](https://www.facebook.com/profile.php?id=61560493948234)

![Facebook screenshot](/readme-images/facebook.png)

## SITEMAP AND ROBOTS

- **sitemap.xml**: A sitemap is created and submitted to search engines to ensure all pages are indexed. I used the following website to create it - [sitemap generator](https://www.xml-sitemaps.com/)

- **robots.txt**: This file is configured to guide search engines on which pages to crawl and index.

## PRIVACY POLICY

To ensure the protection of my users' data and comply with legal requirements, I used a privacy policy generator ([Terms Feed](https://www.termsfeed.com/)) to create a comprehensive privacy policy for my website. This policy is crucial in building trust with my audience, as it transparently outlines how their personal information is collected, used, and safeguarded.

# FEATURES

## EXISTING FEATURES

The website is designed with a variety of features to enhance user experience, engagement, and functionality. Each feature has been thoughtfully implemented to ensure ease of use, seamless navigation, and to provide value to our users. Below is a detailed overview of the existing features, showcasing the our website's capabilities. 

### NAVBAR AND FOOTER

Overall, the navbar and footer are designed to enhance user experience by offering easy navigation, essential contact information, and quick access to important sections of the site.

**Navbar**

The navbar on my Django project is designed for ready navigation and is attached to the top of every page. It features a sleek and intuitive layout:

- **Logo**: Positioned on the left side, providing a consistent brand identity.
- **Search Bar**: Centrally located, allowing users to easily search products within the site.
- **Account and Bag Buttons**: Located on the right side for quick access to user account details and shopping bag.
- **Navigation Buttons**: At the bottom of the navbar, there are buttons for quick access to various sections of the site, including:
  - Products
  - Categories
  - Main Materials
  - Community Page
  - Offers
  - About (featuring information about the artist, blog, and events)

![navbar](/readme-images/navbar.png)

**Footer**

The footer of the website is structured to provide essential information and links in a clear, organized manner:

- **Contact Me Section**: Includes the artist's email, phone number, and address, making it easy for visitors to get in touch.
- **Social Media Links**: A dedicated section for the artist's social media profiles, enabling visitors to connect and follow on various platforms.
- **Payment Methods**: Displays the accepted payment methods, ensuring users are informed about their payment options.
- **Quick Links**: Provides links to important pages on the website, including the privacy policy, ensuring users can easily navigate to key information.

![footer](/readme-images/footer.png)

### HOME PAGE

The home page is designed using a carefully curated color scheme that reflects the artistic essence of the site. This page introduces visitors to the unique, handmade art available for purchase. After presenting a warm and inviting introduction to the artist, a "Start Shopping" button invites users to explore and buy these unique creations.

Additionally, the home page features a picture of the artist, which, when clicked, redirects users to the About page. This allows visitors to get to know the artist better, fostering a personal connection and enhancing the authenticity of the shopping experience.

The navigation also guides users to the Offers page, highlighting special deals and promotions. If users need more convincing, the home page provides insights into the community and blog sections.

![home page screenshot](/readme-images/home-page.png)

### PRODUCTS

- **ALL PRODUCTS**

The Products page showcases the entire collection available on the website, presenting each item with its title, price, and a button to view more details. These features collectively enhance the user experience by providing clear, intuitive navigation, making it easy to find, sort, and identify products. The visual indicators for sales, community suggestions, and digital art ensure that users can quickly grasp the nature and status of each product, while the back-to-top button and product count improve usability and browsing efficiency. 

![products page screenshot](/readme-images/products.png)

- For **superusers**, additional buttons for editing and deleting products are also displayed, facilitating easy management of the inventory.

- Products **on sale** are marked with a prominent yellow banner, showing both the old and new prices, making it easy for users to spot discounts. 

- **Community suggestions** are highlighted with a purple banner, adding a sense of community involvement and exclusivity. 

- **Digital art** products are identified with a yellow exclamation icon, distinguishing them from physical items.

- At the bottom of the page, a round button allows users to quickly return to the top, enhancing navigation. 

- The top left corner displays the total number of products on the page, giving users an overview of the available items. 

- In the top right corner, a filter is provided to sort products by price or name, allowing users to find items based on their preferences.

![sorting](/readme-images/sorting.png)

- **PRODUCT DETAIL**

The Product Detail page provides an in-depth view of each product, enhancing the shopping experience by presenting all necessary information in a clear and organized manner. The page layout features the product image on the left side and all relevant details on the right side.

The right section includes the product title and price, along with color-coded banners to indicate the product category. This visual cue helps users quickly identify the type of product they are viewing. Below the title and price, the page provides a detailed description of the product, including size specifications and the materials used. This comprehensive information ensures that users have a thorough understanding of the product before making a purchase.

For digital products, a yellow exclamation icon is displayed, along with information about how digital art is delivered after purchase. This transparency helps set clear expectations for customers.

The page also includes an input field for users to specify the quantity they wish to add to their bag. Additionally, there are three key buttons to enhance the user experience:

1. **Buy Now**: This button takes users directly to the checkout page, streamlining the purchase process.
2. **Wishlist**: Allows users to save the product for future consideration.
3. **Keep Shopping**: Enables users to continue browsing the website without losing their place.

![product detail](/readme-images/product-detail.png)

### COMMUNITY

The Community page begins with a warm welcome message, inviting users to become a part of our vibrant community. It then provides a brief overview of the benefits of joining the website community, presented in a concise list. This list highlights all the features available to community members, creating an immediate sense of value.

After this introduction, the page encourages users to start exploring these features in more detail. Each feature is described with a dedicated section that includes both a text description and an accompanying image to enhance understanding and engagement. 

The features include:

1. **Newsletter**: Stay updated with the latest news, products, and events by subscribing to our newsletter.
2. **Drawing Suggestions**: Submit your own drawing suggestions and have the chance to see them created by the artist.
3. **Events**: Access a calendar of upcoming and past events that the artist will participate in, and save the ones you're interested in.
4. **Wishlist**: Add your favorite products to a wishlist for future reference and easy access.
5. **Save Delivery Information**: Save your delivery details to streamline future purchases.
6. **Order History**: Keep track of all your past orders in one convenient location.

Each section not only explains the feature but also showcases a relevant image to provide a visual representation, making it easier for users to understand the benefits and how to use them. This comprehensive and visually appealing presentation ensures users are well-informed and encouraged to fully engage with the community.

![community page](/readme-images/community-page.png)

### ABOUT

The About page offers a detailed and engaging introduction to the artist behind the website. You’ll find an image of the artist, giving a personal touch and creating a connection with visitors. Alongside this image, there is a thoughtfully curated list highlighting her interests and passions, providing insight into what inspires her work.

Also, there's a comprehensive text section delves into the artist’s background, explaining who she is. This narrative helps visitors understand the unique perspective and heartfelt dedication that goes into each piece of her handmade art.

If it's a superuser, it will display a green button to edit the page information.

![about page](/readme-images/about-page.png)

This well-structured layout not only introduces the artist in a personal and relatable way but also guides visitors to explore more of her work and interests, enhancing their overall experience on the website.

At the bottom of the page, there are six cards featuring the artist's top recommendations on the website. Each card offers a glimpse into the artist’s curated selections. When you hover over these cards, an image related to the recommendation is displayed, adding an interactive and visually appealing element to the page.

![about page recommendations](/readme-images/about-recommendations.gif)

### BLOG

- **BLOG FEED**

The Blog page serves as a hub for all the captivating stories and insights shared by the artist. It presents a curated list of blog posts, each accompanied by the post image and title, drawing visitors into the rich content that awaits them. 
With its engaging layout and user-friendly design, the Blog page invites visitors to immerse themselves in the artist's world, offering a treasure trove of inspiration and insight waiting to be discovered.

For each post, you'll find details about the author under the "Written By" section, providing a personal touch and adding credibility to the content. Additionally, the date and time of publication are prominently displayed, keeping visitors informed about the recency of the posts.

To ensure smooth navigation through the abundance of content, the page features a convenient pagination button at the bottom.

![blog page](/readme-images/blog-page.png)

- **POST DETAIL**

The Post Detail page offers an immersive experience for diving deep into each blog post, providing rich content and engaging features to captivate visitors.

On the left side of the page, visitors are greeted with the post's captivating image, accompanied by the "Written By" section. A thoughtful touch is the inclusion of the artist's picture. For those curious to learn more about the artist behind the words, a convenient link is provided to redirect visitors to the About page. Below these elements, a "Back to All Posts" button ensures seamless navigation back to the main blog feed.

Meanwhile, the right side of the page is dedicated to the post's content. Here, visitors encounter the post title, along with the content. The date and time of publication serve as a helpful reference point.

Below the post content lies the "Learn More" section, offering additional resources and related links to deepen the reader's understanding of the topic. This feature encourages further exploration and engagement, enriching the visitor's experience.

Finally, nestled at the bottom of the page is a heart-shaped button, inviting visitors to express their appreciation for the post by liking it. This delightful touch fosters a sense of community and encourages interaction.

![blog page](/readme-images/post-detail.png)

### EVENTS

The events page features a dynamic and user-friendly interface, showcasing all upcoming and past events through individual cards. Each card displays essential information about the event, including the title, description, organizer, date and time, and location. Overall, the events page is designed to be intuitive and interactive, providing users with all the necessary information and functionalities to engage with the events effectively.

Key features of the events page include:

- **Event Details**: Each event card provides a clear and concise overview of the event, making it easy for users to quickly understand the essential details.
- **Past Events Indication**: If an event has already occurred, the card will display a red text indicator, ensuring users can easily distinguish between upcoming and past events.
- **Save to Profile**: For upcoming events, logged-in users have the option to save the event to their profile with a simple click. This feature allows users to keep track of events they are interested in attending.
- **Interest Counter**: Each event card includes a counter that shows the number of people interested in the event. This counter increases by one each time a user saves the event to their profile.
- **Admin Controls**: If a superuser is viewing the page, they will see additional buttons to edit or delete events, allowing for easy management and updates to the event listings.

![events page](/readme-images/events-page.png)

### PROFILE

**Profile Page**

When you click on the profile button, you are directed to the main profile page, which is thoughtfully organized to enhance user experience. This profile section is designed to provide users with easy access to their information and activities, enhancing overall usability and engagement with the site.

The layout includes:

- **Menu on the Left Side**: This menu provides quick access to various sections, including:
  - Order History
  - Wishlist
  - Community Suggestions
  - Saved Events
  - (For superusers) Management Button
- **User Information on the Right Side**: Displays essential user details such as username, email, and phone number.
- **Default Delivery Information**: Presented in a table format below the user information, making it easy to view and update.
- **Update Delivery Information Button**: Positioned at the bottom of the page for convenient access.

![profile page](/readme-images/profile.png)

> [!NOTE]
> Every sub-page within the profile section includes a "Back to Profile" button, allowing for easy navigation back to the main profile page.

**Order History Page**

This page displays a comprehensive list of all orders made by the user in a clean, striped format for better readability. Each order line includes:
- Order number
- Date and time
- Items ordered
- Total price
- Product picture

![order history page](/readme-images/orders.png)

**Wishlist Page**

The wishlist page features a table listing all products the user has added. The table columns include:
- **Type**: Indicates whether the product is a community suggestion, on sale, or a standard product.
- **Product Picture**
- **Title**: With a link that redirects to the product page.
- **Price**
- **Option to Remove from Wishlist**

![wishlist page](/readme-images/wishlist-page.png)

**Community Suggestions Page**

This page contains a simple form where users can submit their drawing recommendations, facilitating direct input from the community.

![community suggestion page](/readme-images/community-suggestion.png)

**Saved Events Page**

The saved events page showcases cards for each event the user has saved to their profile. Users can easily manage their saved events, with an option to unsave an event by clicking the saved button on each card.

![saved events page](/readme-images/saved-events.png)


### MANAGEMENT

The management page is tailored to provide superusers with a clear and efficient interface for maintaining and updating website content, ensuring smooth and effective administration. It offers comprehensive control over the website's content. Access to this page is conveniently provided via the profile menu or the profile button on the navbar. Upon selecting the management option, superusers are redirected to the main management page.

The main management page features several cards, each with buttons to different management sections. These cards are color-coded for easy identification:
- **Products Management**: Yellow
- **Events Management**: Light Blue
- **About Management**: Green
- **Blog Management**: Red

Each card provides a brief explanation of how to manage the respective subject area. Depending on the section, clicking on a card may redirect superusers either directly to an update/edit/add page or to an intermediate page with edit and delete options. For example, the products management card redirects to the "All Products" page, where admins can locate the product they want to manage and access the edit or delete functions.

![management page](/readme-images/management.png)

**Add or Edit Pages**

Each add or edit page is designed with simplicity and efficiency in mind. They feature straightforward forms that capture all necessary information for the respective content type. At the bottom of these forms, there are buttons to either update existing entries or add new ones, facilitating quick and easy content management.

![edit or add example page](/readme-images/edit-or-add.png)

## FUTURE FEATURES

**Future Features**

These future features are aimed at making the website more interactive, user-friendly, and personalized, ensuring a richer and more engaging experience for all users. As the website continues to evolve, several exciting features are planned to enhance user experience and functionality:

1. **Personalized Orders**
   - A highly anticipated feature is the ability for users to order personalized drawings. This would allow users to specify details such as size, material, and other custom preferences. The price would be dynamically calculated based on these factors, providing a seamless and personalized shopping experience.

2. **Enhanced Events Section**
   - The events section has great potential for improvement. Planned upgrades include:
     - **Countdown Timer**: A timer for each event, allowing users to see how much time is left until the event starts.
     - **Reminder Emails**: Users will receive email reminders about upcoming events they are interested in, ensuring they don't miss out.

3. **Comment Sections**
   - To foster greater interaction and engagement, adding comment sections to both the product pages and the blog is planned. This will allow users to share their thoughts, ask questions, and engage with the community.

4. **Improved Newsletter Section**
   - The newsletter section will be revamped to be more compelling and user-friendly, encouraging more users to subscribe. This will include better design, clear benefits of subscribing, and possibly incentives for joining the mailing list.

5. **More Efficient Profile Page**
   - Enhancements to the profile page will allow users to update not just their delivery information but also their personal information such as username, email, and phone number. This will make it easier for users to keep their profiles up-to-date and manage their accounts efficiently.

6. **More Admin functionalities**
   - Enhancements to the profile page will allow users to update not just their delivery information but also their personal information such as username, email, and phone number. This will make it easier for users to keep their profiles up-to-date and manage their accounts efficiently.

# LOGIC

## Initial Plans and Sketches

In the initial planning phase, I outlined the core features and functionality for the page, creating detailed sketches to visualize the layout and user interactions. This helped in identifying the necessary components and their interactions within the project. Throughout the development process, I made numerous changes and adjustments to improve the design and functionality, ensuring a well-organized and efficient final product.

![Initial Plans](/readme-images/first-plan.png)

You can see below my initial sketch, which outlines the intended design, UI/UX, and overall look of the page.

![Sketches](/readme-images/rascunho.jpg)

## Database
A database diagram (ERD) was generated using Django Extensions.

You can see the documentation I've followed [here.](https://www.linkedin.com/pulse/generate-database-diagramerd-django-extensions-automatically-srujan-s/)

![database schema](/readme-images/database.png)

## Workflow

I used [Lucidcharts](https://www.lucidchart.com/) to create a detailed workflow diagram for each app in my project, illustrating how components like models, views, and forms interact with one another and integrate with various website features. This visualization helps in understanding the overall structure and flow of data within the project.

### About App

This app manages the content for the "About Me" page, providing a streamlined way to present and update information about the artist.

![about me app workflow](/readme-images/aboutme-app.png)

### Bag App

This app manages the shopping bag functionality for the website. The bag_contents context processor generates the context for the bag contents, calculating the total price, discounts, and delivery charges. The bag_tools.py file contains custom template filters to calculate subtotal and discount prices. The views handle adding, adjusting, and removing items from the bag, updating the session accordingly.

![bag app workflow](/readme-images/bag-app.png)

### Blog App

This blog app manages the creation, display, and interaction with blog posts on the website. It enables the management and interaction with blog posts, providing a platform for content creation and engagement.

![blog app workflow](/readme-images/blog-app.png)

### Checkout App

The checkout app facilitates the process of placing orders on the website. So the checkout app manages the entire order process, from collecting user information to processing payments and updating order status.

![checkout app workflow](/readme-images/checkout-app.png)

### Community App

The community app displays content related to community engagement and interaction.

![community app workflow](/readme-images/community-app.png)

### Events App

The events app is designed to manage events within a web application. The purpose of the events app is to facilitate the management and presentation of events within the web application, allowing users to discover, save, and interact with event information easily. It provides a user-friendly interface for both regular users and administrators to engage with events effectively.

![events app workflow](/readme-images/events-app.png)

### Home App

The home app serves as the landing page and main interface for users accessing the web application. Overall, it aims to engage users from the moment they enter the platform, providing them with valuable information about the artist, current offers, community engagement opportunities, and access to insightful blog content, ultimately encouraging them to explore further and interact with the platform's features.

![home app workflow](/readme-images/home-app.png)

### Products App

The products app serves as a page for managing and showcasing various products. Its primary purpose is to facilitate the administration of product listings and provide a user-friendly interface for customers to explore and purchase these items. 

> [!NOTE]
> I opted to incorporate multiple models related to the ProductTags model to allow for diverse and customizable product attributes such as materials, surfaces, paints, frames, and papers. One product can have different and varying numbers of materials, surfaces, paints, papers and frames based on its characteristics. By utilizing these models, each product can be enriched with detailed information about its composition, enhancing the user experience and enabling more precise categorization and search capabilities within the application.

![products app workflow](/readme-images/products-app.png)

### Profiles App

The profiles app is designed to manage user profiles and their related functionalities (such as order history, wishlist, community recommendation and saved events. It also displays a management section for superusers), providing a personalized experience for each user.

![profiles app workflow](/readme-images/profiles-app.png)

### Wishlist App

The Wishlist app allows users to manage a list of products they are interested in. This feature enhances the user experience by enabling them to save products they might want to purchase in the future. I inspired myself on a colleague project - [Gamerhood](https://github.com/fpatrick/p5gh/tree/master/wishlist)

![wishlist app workflow](/readme-images/wishlist-app.png)

## Agile

During the development of my website, I implemented Agile methodologies to enhance project management and ensure a streamlined development process. I utilized GitHub, where I created issues to outline specific tasks and enhancements. Each issue was associated with a project board, providing a visual representation of the project's status and priorities.  I adopted user stories to define the functionality from the user's perspective. Each user story was accompanied by acceptance criteria, detailing the conditions that must be met for the feature to be considered complete. Additionally, I categorized user stories using labels, allowing for easy classification based on the feature type or functionality.

By integrating Agile methodologies, GitHub for issue tracking, and user stories with acceptance criteria, I maintained an organized and efficient development process, ultimately leading to the successful creation of my website.

You can see check it [here](https://github.com/Nathisaraujo/project5/issues)

# TECHNOLOGIES USED

## Languages
- **HTML:** structure the content of web pages.

- **CSS:** style HTML elements.

- **JavaScript:** create interactive and dynamic features.

- **Python:** is used with the Django framework to handle server-side logic and data manipulation.

## Libraries and Programs:

- **Frameworks and Packages:**

    - **Django:** a high-level Python web framework that simplifies the process of building web applications.

    - **Crispy Forms:** Crispy Forms is a Python package used to style Django forms, making them more visually appealing and user-friendly.

    - **Bootstrap5:** front-end framework for building responsive and mobile-first websites.

    - **Allauth:** is a Django package that provides authentication, registration, and account management functionality for Django applications

    - **Gunicorn:** a WSGI HTTP server for running Python web applications, providing a fast and scalable solution for serving web requests in production environments.

    - **Whitenoise:** a Python library for serving static files efficiently.

    - **PyGraphviz:** a Python library used for working with Graphviz, to generate the ERD.

    - **Pillow:** Python Imaging Library (PIL) fork that adds support for opening, manipulating, and saving many different image file formats.

    - **Django-countries:** a Django application that provides country choices for use with forms, flag icon widgets, and a country field for models.

    - **boto3:** AWS SDK for Python. It allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2.

    - **AWS (Amazon Web Services):** a cloud computing platform that offers a wide range of services including computing power, storage options, and networking capabilities. It provides scalable and cost-effective solutions for hosting web applications and managing infrastructure.

    - **Django-storages:** a collection of custom storage backends for Django applications to work with different storage services like Amazon S3, Google Cloud Storage, and others.

    - **select2:** a jQuery-based replacement for select boxes. It provides a user-friendly interface for selecting elements from a dropdown list with features like search functionality and customizable styling.

- **Database:**
    
    - **CI PostgreSQL:** Code Institute Postgres Database server.

    - **SQLite:** database management system used as a local database during development.

- **Tools and Platforms:**

    - **Gitpod:** cloud-based integrated development environment (IDE) used for coding.

    - **Git and GitHub:** track changes in project files.

    - **Heroku:** cloud-based platform as a service (PaaS) that enables deployment and management.

    - **Google Developer Tools:** web development and debugging tools built into the Google Chrome browser.

    - **Mailchimp:** an email marketing service provider that allows users to create, send, and track email campaigns. It provides tools for managing subscriber lists, designing email templates, and analyzing campaign performance.

    - **Facebook Pages:** a feature of Facebook that allows businesses, organizations, and public figures to create a presence on Facebook and connect with their audience. It provides tools for sharing updates, engaging with followers, and promoting products or services.

    - **ChatGPT:** an AI-powered chatbot developed by OpenAI. It uses natural language processing techniques to understand and respond to user input in conversational contexts. 

    - **TermsFeed:** an online platform that generates legal documents such as privacy policies, terms and conditions, and cookie policies for websites and mobile apps. 

- **Design and Styling:**

    - **Summernote:** rich text editor that provides an easy-to-use interface for formatting and styling text in web applications.

    - **Fontawesome:** a library of scalable vector icons.

    - **Google Fonts:** a collection of open-source fonts hosted by Google. 

    - **Coolors:** Coolors is a color scheme generator.

    - **LucidChart:** diagramming tool used for creating flowcharts.

    - **Canva:** a graphic design platform used for creating visual content.

    - **Wave:** an accessibility testing tool that helps developers and designers ensure their web content is accessible to all users, including those with disabilities.

- **Validators:**

    - **Code Institute Python Linter:** Python.

    - **W3C Validator:** HTML and CSS.

    - **JS Hint:** JavaScript.

    - **flake8:** Python.

# TESTING

Refer to the [TESTING.MD](https://github.com/Nathisaraujo/project5/blob/main/TESTING.md)


# DEPLOYMENT

I followed the Code Institute walkthrough to deploy my project. Below are the steps I took:

### Heroku Setup:
1. **Create a New App:** log in to Heroku and create a new app with a unique name.
2. **Configure Settings:** in the settings tab of your Heroku app dashboard, set config vars for production:
    - Add a key of DISABLE_COLLECTSTATIC and a value of 1 and click Add.
3. **Add Buildpack:** Include a Python buildpack in the settings tab to install necessary dependencies.

### Create an External Database

Since ElephantSQL will no longer be available, I used the Code Institute Postgres Database server instead. I received my database URL via email.

1. Go to the config vars section on deploy section.
2. Add the config var DATABASE_URL and paste the database URL.

### Connect your database to your local development web server

1. In the terminal, install dj_database_url and psycopg2:
```
 pip3 install dj_database_url==0.5.0 psycopg2
```
2. Update your requirements.txt file with the newly installed packages:
```
 pip freeze > requirements.txt
```
3. In your settings.py file, import dj_database_url underneath the import for os:
```
 import os
 import dj_database_url
```
4. Scroll to the DATABASES section and update it to the following code, so that the original connection to sqlite3 is commented out and we connect to the new database instead. 
```
 # DATABASES = {
 #     'default': {
 #         'ENGINE': 'django.db.backends.sqlite3',
 #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 #     }
 # }
     
 DATABASES = {
     'default': dj_database_url.parse('your-database-url-here')
 }
```
5. In the terminal, run the showmigrations command to confirm you are connected to the external database:
```
 python3 manage.py showmigrations
```
6. Migrate your database models to your new database
```
 python3 manage.py migrate
```
7. Use an if statement in settings.py so that when our app is running on Heroku here the database URL environment variable will be defined, we connect to our database and, otherwise, we connect to SQLite.
```
 if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
    }
```

### Update the project for deployment

1. Install a production-ready webserver for Heroku.
```
pip3 install gunicorn~=20.1
```
2. Add gunicorn==20.1.0 to the requirements.txt file:
```
pip3 freeze --local > requirements.txt
```
3. Create Procfile: Specify the web dyno command in a Procfile. In the Procfile, declare this is a web process followed by the command to execute your Django project:
```
web: gunicorn drawing_gratitude.wsgi
```
4. Set DEBUG to False on drawing_gratitude/settings.py
5. In settings.py, append the Heroku hostname to the ALLOWED_HOSTS list:
```
,'.herokuapp.com'
```
6. Commit changes to GitHub and push them to Heroku for deployment. Heroku automatically detects changes in the repository and triggers the deployment process.

### Create an AWS Account

1. Create an AWS account.
2. Go to the services tab on the AWS Management Console and select S3.
3. Click on "Create new bucket", give it a name of your project and choose your region.
4. The Object Ownership setting needs to be set as shown with
the ACLs enabled and Bucket Owner Preferred option checked.
5. Click on "create bucket"
6. Go to the "Properties" tab, on static website hosting, click on edit and chande it to "enable".
7. On the permissions tab, go to CORS configuration, paste that into the Cross-origin resource sharing (CORS) section:
```
    [
        {
            "AllowedHeaders": [
            "Authorization"
            ],
            "AllowedMethods": [
            "GET"
            ],
            "AllowedOrigins": [
            "*"
            ],
            "ExposeHeaders": []
        }
    ]

```
8. Go to "Bucket Policy", click on Policy Generator and choose the "S3 Bucket Policy".
9. On "Step 2: Add Statements", add the settings:
```
Effect: Allow
Principal: *
Actions: GetObject
ARN: Bucket ARN   # copy and paste from the S3 Bucket
```
10. Click on add statement and then generate policy. Copy the policy, and paste it into the permissions tab, on the Bucket Policy Section.
11. Add '/*' at the end of the 'Resource' key, and save.
11. Go to the "Access Control List "section, click edit and enable List for Everyone (public access) and accept the warning box.

### Identify and Access Management (IAM)

1.  Go to the services tab on the AWS Management Console and select "IAM".
2. On the IAM page, click on User Groups, then on create group, and choose a name and click create.
3. Go to Policies tab, click "Create New Policy". 
4. Go to the JSON tab and click "Import Managed Policy".
5. Search for S3 and choose "AmazonS3FullAccess". Then, click "Import".
6. Retrieve the bucket ARN from 'S3 Permissions' as mentioned earlier. Replace the '*' in the 'Resource' key with the following code:

```
"Resource": [
    "YOUR-ARN-NO-HERE",
    "YOUR-ARN-NO-HERE/*"
]
```
7. Click on "Next Tags", then "Review Policy". Provide a name and description, then click "Create Policy".
8. Go to User Groups tab, open the created group, and navigate to the permissions tab. Click on "Add Permissions "and then "Attach Policies". Select the policy and click on "Add permissions" at the bottom.
9. To create a user for the group, select "Users" from the sidebar and click "Add User". Enter a username and check "Programmatic Access".
10. Click on "Next" and select the group you created. Continue clicking it until you reach the "Create User" button and click it.
12. Go to IAM and select 'Users'
11. Select the user for whom you wish to create a CSV file.
12. Select the 'Security Credentials' tab
13. Scroll to 'Access Keys' and click 'Create access key'
14. Select 'Application running outside AWS', and click next
15. On the next screen, you can leave the 'Description tag value' blank. Click 'Create Access Key'
16. Download the CSV file containing the AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID. You will need these for the Heroku variables as mentioned earlier and also in your env.py file.

### Set up hosting for static and media- AWS (Amazon Web Services) - S3 (“Simple Storage Service”)

1. Install two additional requirements:
```
pip3 install boto3
pip3 install django-storages
```
2. Update your `requirements.txt` file:
```
pip3 freeze --local > requirements.txt
```
3. Add "storages" to your installed apps:
4. In settings.py, create an if statement:
```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'insert-your-bucket-name-here'
    AWS_S3_REGION_NAME = 'insert-your-region-here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```
5. Create a file called custom_storages.py and import the settings from django.conf and the S3Boto3Storage class from django-storages. Add the following code:
```python
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
6. In settings.py, add the following inside the if statement:
```
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
7. And then add this at the top of the if statement:
```
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
```
8. Go to S3, navigate to your bucket, and click 'Create folder'. Name the folder 'media' and click 'Save'. 
9. Inside the folder, click 'Upload', 'Add files', and select all the images you are using for your site. Under 'Permissions', select the option 'Grant public-read access' and click 'Upload'.

### Back to Heroku Setup:

1. Go to the deploy tab, in the Deployment method section, and enable GitHub integration by clicking on Connect to GitHub.
2. Scroll to the bottom of the page and click Deploy Branch to start a manual deployment of the main branch.
3. Open the Resources tab and choose an eco dyno. 
4. Click on Open app to view your deployed project.

## Forking
Forking allows you to freely experiment with changes without affecting the original repository.

1. **Create a Fork:** Visit the GitHub repository and click on 'Fork' to create a copy of the repository under your account. 
2. **Customize Fork:** Customize the fork as needed before creating it. You can modify the fork's settings, description, and other details to suit your requirements.

## Cloning Repository
Cloning creates a local copy of the repository on your machine, allowing you to work on the codebase locally.

1. **Copy Repository Link:** Copy the repository link from GitHub.
2. **Clone Repository:** Use Git commands to clone the repository to your local environment.
3. **Set Up Environment:** Enter your workspace, set up a virtual environment, install dependencies from requirements.txt, and create an env.py file. 
4. **Configuration:** Modify settings.py and other necessary files to match your environment and configurations. Update settings.py with database connection details, secret keys, and other environment-specific configurations.


# CREDITS

- The "Boutique Ado" project by Code Institute played a crucial role in my learning journey. It provided invaluable insights and knowledge, significantly contributing to my project development.

- **Debugging and Error Resolution:** When encountering issues with the like button implementation, I utilized various resources for assistance, including tutoring sessions, browser developer tools, and ChatGPT.

- I used [ChatGPT](https://chat.openai.com/) to help me throughout the project, leveraging its capabilities in various ways:
    - **Error Understanding and Debugging:** ChatGPT assisted me in comprehending complex errors and provided insights to debug the code effectively.
    - **Typo Detection:** I employed ChatGPT to identify any typos present in my code or documentation files.
    - **Vocabulary and Grammar Enhancement:** ChatGPT helped refine the vocabulary and grammar in my project documentation, ensuring clarity as English is not my first language.

    - **Specific Use Cases:**
        - **To create a filter to calculate the offers** When faced with the task of creating a filter for the products on offer, I tried the following:

            ![chatgpt offers filter - my version ](/readme-images/offers-filter-1.png)

            But of course, it wasn't working, so ChatGPT suggested another approach:

            ![chatgpt offers filter - Chatgpt version ](/readme-images/offers-filter-2.png)

            Then I tried to add more context, making things more complex:

            ![chatgpt offers filter - my version ](/readme-images/offers-filter-3.png)

            It still wasn't working, so ChatGPT suggested this:

            ![chatgpt offers filter - Chatgpt version ](/readme-images/offers-filter-4.png)

            Realizing I wasn't understanding it well, I asked ChatGPT to explain the logic to me, which really helped:

            ![chatgpt offers filter - Chatgpt version ](/readme-images/offers-filter-5.png)
            ![chatgpt offers filter - Chatgpt version ](/readme-images/offers-filter-6.png)

            For this specific case, I also watched this video: [Adding Ecommerce Discount Prices](https://www.youtube.com/watch?v=H8uvpvpas_U)

            And referred to this documentation: [Decimal Field](https://docs.djangoproject.com/en/4.0/ref/models/fields/#decimalfield)
            
        - **Ideas to create new models:** I struggled to think of more models to create, knowing I needed to create three of my own. ChatGPT gave me a list of ideas:

            ![chatgpt models ideas](/readme-images/model-ideas.png)

            This led me to the idea of creating an events page.

        - **Clean Function on Events model**  I had an issue with my events model and received this error:

            ![events model error](/readme-images/events-error.png)

            ChatGPT suggested creating a clean function for the model:

            ![events model error - chatgpt suggestion](/readme-images/events-error-gpt.png)

- **Navbars and tables:** To create different navbars and tables, I frequently used:

    - [W3 Schools](https://www.w3schools.com/)
    - [Bootstrap5 Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

- **Boolean Field:** When I couldn't remember how to implement a Boolean field, I referred to [Geeks for Geeks](https://www.geeksforgeeks.org/boolean-data-type-in-python/)

- **Post Model:** I referred to my last project to create the post model.

- **Pagination:**  I referred to my last project and the Bootstrap documentation to implement pagination.

- **Wishilist App** I referred to a colleague's project to create the wishlist app:  [Gamerhood](https://github.com/fpatrick/p5gh)

- **Friend Collaboration:** A friend shared his code with me, providing insights into some requirements and features: [Easy Vape](https://github.com/gioZAK/easy_vape).

To craft this README, I referred to the the [Coffee Collective Project](https://github.com/LauraMayock/the-coffee-collective?tab=readme-ov-file)