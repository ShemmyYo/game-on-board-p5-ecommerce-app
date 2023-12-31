# Portfolio Project 5 - E-commerce Applications

![GamerOnBoard](README/readme-files/am-i-responsive-2.png)
## __Roll, Play, Win – GamerOnBoard is Your Board Game Destination.__

GamerOnBoard is a B2C (business-to-consumer) board game web store which aims to audiences, such as families, tabletop gamers, or collectors and specialising in strategic and role-playing board games. We have built a diverse and attractive inventory of board games, including popular titles such as Catan, Ticket to Ride, Chess, Monopoly and many many more... 

When designing GamerOnBoard store, I focused on creating a user-friendly, visually appealing e-commerce website with a responsive design and focused on implementing a secure and easy-to-navigate online shopping experience. One of my prorities was also to be able to optimise website for search engines (SEO) to improve organic visibility.

I ensured to include high-quality backlinks from reputable websites in the board game industry, gaming communities, and related niches.
The Customer is encourage to buy, like product and as a future function, reviews and rate, which can enhance GamerOnBoard visibility in local and product-specific search results.

# Project Goal

The goal of this project was to build a Full-Stack site based on business logic used to control a centrally-owned dataset. 
Page has an authentication mechanism and provides paid access to the site's data and allows the user to purchase a product. 
It was also my goal to implement SEO and create a dummy social media product page on FB.

## __Tech Stack__

<img height="50" src="README/readme-files/python-django.png">  <img height="50" src="README/readme-files/elephantsql.png">   <img height="50" src="README/readme-files/html.png">  <img height="50" src="README/readme-files/css.png">  <img height="50" src="README/readme-files/js.png"> <img height="50" src="README/readme-files/stripe.png"> 


<img height="50" src="README/readme-files/gitpod.png">  <img height="50" src="README/readme-files/github.png">  <img height="50" src="README/readme-files/bootstrap.png">  <img height="50" src="README/readme-files/aws_images.png"> 

## __Live Web-Page__
<a href ='https://gamer-on-board-6fa9b306b6d7.herokuapp.com/' target="_blank">GamerOnBoard</a>

## __GitHub Repository__
<a href ='https://github.com/ShemmyYo/game-on-board-p5-ecommerce-app' target="_blank">https://github.com/ShemmyYo/game-on-board-p5-ecommerce-app</a>

***

# Contents

- [Overview](#portfolio-project-4---full-stack-toolkit)
- [Project Goal](#project-goal)
- [UX User Experience](#ux-user-experiance)
    - [Design](#design)
        - [Colour Scheme](#colour-scheme)
        - [Typography](#typography)
        - [Imagery](#imaginary)
    - [Agile](#agile)
        - [The Ideal User/Persona](#the-ideal-userpersona)
        - [Epics & Admin/User Stories](#epics--adminuser-stories)
        - [MoSCoW Prioritization](#moscow-prioritization)
	- [Ecommerce Business Model](#ecommerce-business-model)
		- [Web Marketing](#web-marketing)
		- [Search Engine Optimization (SEO)](#search-engine-optimization-seo)
    - [Wireframes](#wireframes)
	- [Data Model](#data-model)
	- [Features](#features)
    	- [Existing Features](#existing-features)   
    	- [Future Features](#future-features)
		- [Errors](#error-pages)
- [Testing](TESTING.md)
- [Tools & Technologies Used](#tools--technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks & Tools](#frameworks--tools)
    - [Imported Libraries and Packages](#imported-libraries-and-packages)
- [Deployment](#deployment)
    - [ElephantSQL](#elephantsql-database)
    - [Amazon AWS](#amazon-aws)
		- [S3 Bucket](#s3-bucket)
		- [IAM](#iam)
		- [Final AWS Setup](#final-aws-setup)
	- [Stripe API](#stripe-api)
	- [Gmail API](#gmail-api)
    - [Heroku Deployment](#heroku-deployment)
    - [Local Deployment](#local-deployment)
		- [Cloning](#cloning)
		- [Forking](#forking)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

***

# UX User Experiance

**Creating a user-friendly e-commerce web store is essential to attract and retain customers hencethe below are some of the key UX (User Experience) characteristics I ensured to be used in my Project are as follow:** 

- **Intuitive Navigation:** Ensured that the website has a clear and logical navigation structure. Users should be able to easily find product categories, search for specific items, and navigate to their shopping cart or checkout page without confusion.

- **Responsive Design:** My e-commerce site is fully responsive, meaning it adapts seamlessly to various screen sizes and devices, including smartphones and tablets.

- **Fast Loading Speed:** I optimised store's performance to ensure fast load times by i.e.: compressing images.

- **Clear Product Presentation:** I used high-quality images and provided product descriptions. Include pricing, product specifications, and availability information as well as age group suitability and other.

- **User-Friendly Search:** I implemented a search feature which allow users to refine their search results by price, category, age, and other relevant criteria.

- **User Reviews and Ratings:** I includes user-generated reviews and ratings for products which builds trust and helps shoppers make informed decisions.

- **Shopping Cart and Checkout Optimization:** I made it easy for users to add items to their cart and proceed to checkout. I provided a clear and concise checkout process with Stripe payment option and guest checkout for convenience.

- **Security and Trust:** Displayed trust indicators such as secure payment logo.

- **Personalization:** Implement features like product recommendations based on user behavior and purchase history. Personalization enhances the shopping experience and can increase sales.

- **User Account Management:** Users are allowed to create accounts, save their address and view order history. AllAuth offers easy password recovery and account management options.

- **Error Handling:** Clear error messages and guidance when users encounter issues, such as out-of-stock products or incorrectly filled-out forms.

- **Accessibility:** I ensured that website is accessible to all users, including those with disabilities. 


## Design

### Colour Scheme

I opted for a very minimalistic aesthetic and only apllied 3 colours (2 with additional shades) to this project.

```css
root {
    --background-col: #fff;
    --background-accent: #7A92A5;
    --text-black: #0F1519;
    --text-gray: #6A92A5;
    --accent-col: #69101E;
    --accent-ligh: #A42435;
}
```

To provide a better user experience, I went for a light and neutral theme with an hints of red to add spice to the site. 
The colours have been implemented across the site and are included in the buttons/links and their hover effects.

I used <img height="14" src="README/readme-files/colormind-logo.png"> [Colormind](http://colormind.io/) colour scheme for this project:

![Colour Scheme](README/readme-files/colormind-colours.png)


[Back to top &uarr;](#contents)

### Typography

'Montserrat' has been used as a main font:

The old posters and signs in the traditional Montserrat neighborhood of Buenos Aires inspired Julieta Ulanovsky to design this typeface and rescue the beauty of urban typography that emerged in the first half of the twentieth century. As urban development changes that place, it will never return to its original form and loses forever the designs that are so special and unique. 

![Alt text](README/readme-files/montserrat-font.png)

```font
root {
    --main-font: 'Montserrat', sans-serif;
}
```


***

### Imaginary

I designed a GamerOnBoard logo with <img height="20" src="README/readme-files/figma-logo.png"> [Figma](https://www.figma.com/)

same logo has then been used to create [Favicon](https://favicon.io/) icons.

<img height="150" src="README/readme-files/game-on-board-logo.jpg">

***

## Agile 

### The Ideal User/Persona

**Garry GameGeek**

- **Age:** 28
- **Gender:** Male
- **Occupation:** Software Developer
- **Hobbies:** Board games, video games, and attending gaming conventions
- **Location:** Urban area, lives in a small apartment
- **Income:** Middle-class
- **Marital Status:** Single
- **Education:** Bachelor's degree in Computer Science

**Tech-savvy:** Gary is comfortable using technology, especially when it comes to shopping online.
Social Gamer: He enjoys board games because they provide a great way to socialize with friends, either in-person or online.
Value Shopper: Gary is price-conscious and looks for good deals or discounts.
Game Collector: He is an avid board game collector and is always on the lookout for the latest and greatest titles.
Research-Oriented: Gary does extensive research before buying a game, reading reviews, and watching video tutorials.
Minimalist Lifestyle: Due to limited space in his apartment, Gary prefers games that are compact and versatile.
Environmental Consciousness: He cares about the environment and appreciates eco-friendly or sustainable game options.

**Goals:**
Discover new and exciting board games.
Get the best value for his money.
Stay up-to-date with the latest board game releases.
Find games suitable for various group sizes and occasions.

**Pain Points:**
Limited storage space for board games.
Worries about the environmental impact of buying new games.
Struggles to find time to attend physical board game events or conventions.
How the Online Board Game Shop Can Appeal to GameGeek Gary:

***

### Epics & Admin/User Stories

7 Epics (milestones) were created which were then further developed into 41 User Stories. 

 __[EPIC 1](https://github.com/ShemmyYo/game-on-board-p5-ecommerce-app/milestone/1)  Django & Project Basic Setup__

 - As an ADMIN, I want to **setup Django app** so that I can start building my web store `MUST HAVE`  
 - As an ADMIN,  I want to **create 'home' app** so that I can start creating base templates `MUST HAVE`  
 - As an ADMIN, I want to be able to **configure and deploy to Heroku** so that my page is available for everyone to view `MUST HAVE`  
 - As a USER, I want to be able to **clearly see the site's purpose** is so that I can decide whether or not to continue browsing it `MUST HAVE`   


 __[EPIC 2](https://github.com/ShemmyYo/game-on-board-p5-ecommerce-app/milestone/3)  User Authentication & Page Admin__

 - As an ADMIN, I want **setup AllAuth** so that I can manage users from the Admin Panel  `MUST HAVE`  
 - As an ADMIN, I will **make copies of allauth templates** so that I can adjust them to my user needs `MUST HAVE`  
 - As a USER, I want to be able to **register my account** so that I can view my profile `SHOULD HAVE`   
 - As a USER, I want to be able to **create a personalised user profile** so that I can re-use my details easily and view order history `SHOULD HAVE`   
 - As a USER, I want to be able to **login and logout** so that I can access my account info `SHOULD HAVE`   
 - As a USER, I want to be able to **get a confirmation email after registration** so that I can verify my account has been successfully registered `SHOULD HAVE`  
 - As an Admin I want to be able **let users sign in with SSO** so that *they can log in easily and securely**  `WONT HAVE` 


 __[EPIC 3](https://github.com/ShemmyYo/game-on-board-p5-ecommerce-app/milestone/2)  Product App__

 - As an ADMIN/Product Owner, I want to be able to **add product** so that I add or increase stock  `MUST HAVE`  
 - As an ADMIN/Product Owner, I want to be able to **edit or update product** so that change product price, description etc.  `MUST HAVE`  
 - As an ADMIN/Product Owner, I want to be able to **delete product** so that I can remove it if it's not for sale `MUST HAVE`  
 - As a USER, I want to be able to **identify deals, clearance areas and special offers** so that ** I can take advantage of special offers** `MUST HAVE`  
 - As a USER, I want to be able to **view a list of products** so that I can browse and shop easily `MUST HAVE`  
 - As a USER, I want to be able to **see a detailed view of the product** so that I can read details of the product. `MUST HAVE`  
 - As a USER, I want to be able to **search the webpage** so that I can find specific products and check if it's in stock `SHOULD HAVE`  
 - As a USER, I want to be able to **view product by category** so that find product I'm looking for quickly and easily `MUST HAVE`  
 - As a USER, I want to be able to **sort available products** so that easily identify the best rated, best priced and by category products `MUST HAVE`  
 - As a USER, I want to be able to **view additional details** such as age group, play time and number of players so that I am fully aware of benefits of the product I want to buy `COULD HAVE`  
 - As a USER, I want to be able to **view a carousel of images** on the home page so that I feel engaged and enticed straight away `COULD HAVE`  
 - As a User, I want to be able to **like product** so that I can easily **view my liked products** `COULD HAVE`  
 - As a User, I want the have the ability **to like product count** so that I can **clearly see how many people like the same product** `COULD HAVE`  



 __[EPIC 4](https://github.com/ShemmyYo/game-on-board-p5-ecommerce-app/milestone/4)  Bag, Checkout and Payment__

 - As a USER, I want to be able to **add products to a bag** so that I can purchase products i want `MUST HAVE`   
 - As a USER, I want to be able to **view the total of my purchas**e so that I'm in full control of what I am buying `MUST HAVE`   
 - As a USER, I want to be able to **add/remove product quantity** so that I am in full control of how many items I am buying `MUST HAVE`   
 - As a USER, I want to be able to **view my bag** so that view product info, quantity and price of my purchase `MUST HAVE`   
 - As a USER, I want to be able to **enter payment info** so that I can check out easily `MUST HAVE`   
 - As a USER, I want to feel that my **payment is safe and secure** so that I feel confident to provide my card details `MUST HAVE`   
 - As a USER, I want to get **an email confirmation after my purchase** so that I keep a record of what I've purchased `MUST HAVE`   
 - As a USER, I want to be able to type in a **discount code** so that I can avail of a shop promo `WONT HAVE`  


 __[EPIC 5](https://github.com/ShemmyYo/game-on-board-p5-ecommerce-app/milestone/5)  Subscriptions__   

 - As a USER,  I want to be able to **subscribe to a newsletter** so that I'm being kept up to date with all things new at GamerOnBoard `SHOULD HAVE`  


 __[EPIC 6](https://github.com/ShemmyYo/game-on-board-p5-ecommerce-app/milestone/6)  Reviews and Blog__   

 - As a site user, I want to be able to view blog posts on the website so that I can read any posts/comments `COULD HAVE`   
 - As a User, I want to be able to create blog posts from the front end so that I can share information with site visitors `COULD HAVE`   
 - As a User, I want to be able to edit existing blog posts so that I can ensure that posts are up to date  `COULD HAVE`   
 - As a User, I want to be able to delete existing blog posts so that I can remove any unwanted posts from the site `COULD HAVE`   


 __[EPIC 7](https://github.com/ShemmyYo/game-on-board-p5-ecommerce-app/milestone/7)  Marketing and Search Engine Optimalisation__

 - As an ADMIN, I want to be able to - Marketing `MUST HAVE`   
 - As an ADMIN, I want to be able to - Social Media `MUST HAVE`   
 - As an ADMIN, I want to be able to - Social Media Extra `SHOULD HAVE` 


[Back to top &uarr;](#contents)

***

### MoSCoW Prioritization

This project was developed using agile methodologies by delivering small features (User Stories) across the project.

The Kanban board was created using Github projects and can be located [here](https://github.com/users/ShemmyYo/projects/6) and can be viewed to see more information on the project cards. 

Using this approach, I was able to apply the MoSCow prioritization and label user stories.
User Stories were assigned to Epics, prioritized under the labels:

- `MUST HAVE` - guaranteed to be delivered (*max 60% of stories*)
- `SHOULD HAVE` - adds significant value, but not vital (*the rest ~20% of stories*)
- `COULD HAVE` - has small impact if left out (*20% of stories*)
- `WON'T HAVE` - not a priority for this iteration

To ensure that all core requirements were completed I worked on the 'MUST HAVE' epics/user stories first.

A few `COULD HAVE` user stories have been implemented before project due date i.e. ...


[Back to top &uarr;](#contents)

***

## Ecommerce Business Model

GamerOnBoard is a B2C (business-to-consumer) as it sells goods to individual customers.

In B2C model, the success of board game online business will depend on ability to connect with individual consumers, offer a compelling product, and deliver exceptional customer service. Adapting and evolving business strategy based on consumer feedback and market trends will be crucial for long-term success.


#### Other Google services available to boost business awareness:

- Google My Business - registering business address 
- Google Ads - powerfull advertising tool
- Google Analytics - visual analytics on clicks, track etc

### Web Marketing

GamerOnBoard has links for social media marketing and a Newsletter model is linked to the form on the page.


#### Social Media Marketing

Social Media can potentially build a community of users around the business, and boost site visitor numbers,
especially when using larger platforms such a Facebook.

Social marketing in the context of online business refers to the use of social media platforms and strategies to promote products or services, build brand awareness, engage with customers, and ultimately drive sales and business growth. It's an essential component of digital marketing that leverages the vast reach and influence of social media to connect with potential customers. 

Common platforms include Facebook, Instagram, Twitter, LinkedIn, Pinterest, and TikTok.

Social marketing in online business is an ongoing effort that requires a deep understanding of your target audience and the ability to adapt to the ever-changing landscape of social media. It's essential to maintain a strategic and customer-focused approach to maximize your online business's success through social media channels.

I've started this journey by creating a Facebook account

![FB](README/readme-files/fb-marketing.png)


[Back to top &uarr;](#contents)

***

#### Newsletter Marketing

A newsletter list can be used by the business to send regular messages to site users.
For example, what items are on special offer, new items in stock, updates to business hours, notifications of events, and much more!

I have incorporate a newsletter sign-up form on my application, to allow users to supply their
email address if they are interested in learning more about what the business has to offer.

I created a custom newsletter app in my project with a custom NewsletterSignup model and added a form to the site's footer to collect user email addresses 

Newsletter model:

```python
class NewsletterSignup(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.email
```

I set the email address to be unique to avoid users signing up multiple times with the same email address. 
If a user tries to sign up twice with the same address they will be shown a message letting them know they've already signed up.

Once a user signs up, I used the `send_mail()` functionality in the `webhook_handler.py` file to trigger a welcome email for the user to acknowledge that they've successfully signed up for the newsletter.

<details>
<summary>Click to View Newsletter Form Page</summary>

![Newsletter](README/features/footer.png)
</details>

[Back to top &uarr;](#contents)

***

### Search Engine Optimization (SEO)

Keyword research is the process of finding and analyzing search terms that people enter into search engines, with the goal of using that data for SEO or general web marketing.

#### Keywords

Keywords have been identified to align with my site, that should help users
when searching online to find my page easily from a search engine.
This included a series of the following keyword types

- Short-tail (head terms) keywords
These short-tail keywords can serve as the foundation for your SEO strategy. However, keeping in mind that competition for these keywords can be high, it's also essential to consider long-tail keywords and specific game titles to reach a more targeted audience. Additionally, regularly updating your website with fresh and relevant content, optimizing your site's structure, and acquiring backlinks from reputable sources can help improve search engine rankings.


**Long-tail keywords:**
| ---------- | ---------- | ------------ |
| "Best board games" | "Board game collection" | "Top Game store" |
| "Tabletop games" | "Board game store" | "Board game retailer" |
| "Board game store near me" | "Buy board games" | "Tabletop game shop" |
| "Game board shop" | "Board games online" | "Best board games" |
| "Board games for sale" | "Game store online" | "Board games for adults" |
| "Board games for kids" | "Popular board games" | "Board games to buy" |


#### SEO Optimlisation

Website's content, including product descriptions, category pages, and blog posts, by incorporating chosen keywords naturally.
High-quality, informative, and engaging content that satisfies user intent and answers common questions related to board games.
Use header tags (H1, H2, H3, etc.) to structure your content and make it more readable:

**For the Homepage:**
 "Discover the Best Selection of Board Games Online. Shop Now for Family Fun, Strategy, and Classic Titles. Find Your Next Adventure!"

**For a Category Page (e.g., Strategy Board Games):**
 "Explore a World of Strategy Board Games – From Chess to Eurogames. Upgrade Your Game Night with Our Collection of Engaging Titles."

**For a Product Page (e.g., "Catan: Settlers of Catan Board Game"):**
 "Get Ready to Conquer Catan! Shop the Classic 'Settlers of Catan' Board Game. Build, Trade, and Win in this Award-Winning Title."

**For a Blog Post (future function, e.g., "Top 10 Board Games for Family Game Night"):**
 "Planning a Family Game Night? Discover Our Top 10 Board Games for Unforgettable Fun. Start the Countdown to Laughter and Memories!"


#### External Link

- [The Boardgame Players Association](https://www.boardgamers.org/)
`The Boardgame Players Association started in 1991. The gaming convention which would eventually evolve into the present WBC got its start in 1991 as Avaloncon when years of campaigning for it by Don Greenwood finally convinced Avalon Hill management that a “return to basics” gaming convention emphasizing competitive play of the games was the best way for The Avalon Hill Game Company to reverse its flagging fortunes. Having started the Origins gaming convention two decades earlier—with all of 13 tournaments—Avalon Hill had freely relinquished control of that annual gaming fest to the fledgling Game Manufacturer’s Association to concentrate on the production of its own games.`

- [The Irish Games Association](https://iga.ie/)
`The Irish Games Association CLG is dedicated to promoting gaming in Ireland, by running, supporting and publicising gaming events, while seeking to communicate and cooperate with others that do likewise. The IGA engages in a number of activities designed to further its stated aim of promoting gaming in Ireland and has evolved substantially over its lifespan. Originally, the IGA was a group composed of different gaming interests from around the country who came together to organise an event known as Convention: Gaelcon. Since that time, a number of changes have taken place, and the IGA has expanded into other fields. The goal of the IGA is to help the gaming community in whatever way possible, be it by organising events, providing information, or offering what assistance it can to others who are working on behalf of the gaming community in Ireland. If you are running an event and need some assistance or some friendly advice please don’t hesitate to reach out to us.`


#### GDPR:
 The European Union introduced the  General Data Protection Regulation, known as GDPR in May 2018. GDPR is the toughest privacy and security law in the world and even though it was passed by the European Union, it imposes obligations onto organizations anywhere in the world, as long as they target or collect data related to people in the EU.

 GamerOnBoard [Privacy Policy](https://www.privacypolicygenerator.info/live.php?token=IAqA6K5oi5wyOB0Wrs3XHhpYfMa3PMyi) has been generated and inluded in the footer of the page.

<details>
<summary>Click to View Privacy Policy Page</summary>

![privacy-policy](README/features/privacy-policy.png)
</details>


#### META:

**META keywords:**
| ---------- | ---------- | ------------ | ----------- | ----------- |   
| Board | Tabletop | Card | Strategy | Family board |  
| Board game store | Game night | Role-playing games (RPGs) | Classic board | Board game recommendations |   
| Board game shop  | Party games | Board game collection | Board game accessories | Board game reviews |  
 

#### Sitemap

I've used [XML-Sitemaps](https://www.xml-sitemaps.com) to generate a sitemap.xml file.
File generated using deployed site URL: https://gamer-on-board-6fa9b306b6d7.herokuapp.com/

After it finished crawling the entire site, it created a
[sitemap.xml](sitemap.xml) which I've downloaded and included in the repository's root dir.

#### Robots

I've created the [robots.txt](robots.txt) file at the root-level.
Inside, I've included the default settings:

```
User-agent: *
Disallow:
Sitemap: https://gamer-on-board-6fa9b306b6d7.herokuapp.com/sitemap.xml
```

[Back to top &uarr;](#contents)

***

## Wireframes

I've used [Balsamiq](https://balsamiq.com/wireframes) to create my page wireframes.

### Home Page Wireframes
<details>
<summary>Click to View Wireframes</summary>

![Alt text](README/wireframes/landing.png) 
</details>

### Sign Up Page Wireframes
<details>
<summary>Click to View Wireframes</summary>

![Alt text](README/wireframes/user-register.png)
</details>

### Login Page Wireframes
<details>
<summary>Click to View Wireframes</summary>

![Alt text](README/wireframes/user-login.png)
</details>

### Logout Page Wireframes
<details>
<summary>Click to View Wireframes</summary>

![Alt text](README/wireframes/user-logout.png)
</details>

### User Update Page Wireframes
<details>
<summary>Click to View Wireframes</summary>

![Alt text](README/wireframes/profile-update.png)
</details>

### Product Wireframes
<details>
<summary>Click to View Wireframes</summary>

![Alt text](README/wireframes/product.png)
</details>

### Product Details Wireframes
<details>
<summary>Click to View Wireframes</summary>

![Alt text](README/wireframes/product-detail.png) 
</details>

### Product Managment - Add Wireframes
<details>
<summary>Click to View Wireframes</summary>

![Alt text](README/wireframes/product-management.png)
</details>

### Product Management - Edit Wireframes
<details>
<summary>Click to View Wireframes</summary>

![Alt text](README/wireframes/product-edit.png)
</details>

### Bag Wireframes
<details>
<summary>Click to View Wireframes</summary>

![Alt text](README/wireframes/bag.png) 
</details>

### Checkout Wireframes
<details>
<summary>Click to View Wireframes</summary>

![Alt text](README/wireframes/checkout.png) 
</details>


[Back to top &uarr;](#contents)

***

## Data Models
The below is the Data Schema created for GamerOnBoard

![Schema](README/readme-files/schema.png)


The following are the models created for GamerOnBoard.

- **Category**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |  
    | | name | CharField | |  
	| | friendly_name | CharField | |  
	| | cat_desc | CharField | |  
	| | cat_image | ImageField | |  

- **Condition**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | | name | CharField | |
	| | condition_desc | CharField |  

- **AgeGroup**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | | name | CharField | |
	| | restriction_name | CharField | |  
	| | restriction_desc | CharField | |  
	| | restriction_image | ImageField | |  

- **SpecialCategory**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |  
    | | name | CharField | |  
	| | sp_cat_desc | CharField | |  

- **Product**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | **FK** | category | ForeignKey | FK to **Category** model |
	| **FK** | special_cat | ForeignKey | FK to **SpecialCategory** model |
	| | sku | CharField | |  
	| | name | CharField | |
	| | description | TextField | |  
	| **FK** | age | ForeignKey | FK to **AgeGroup** model |
	| | min_players | CharField | |  
	| | max_players | CharField | |  
	| | game_play_time | CharField | |  
	| **FK** | condition | ForeignKey | FK to **Condition** model |
	| | price | DecimalField | |  
	| | rating | DecimalField | |  
	| | image | ImageField | |  
	| | image2 | ImageField | |  
	| | image2 | ImageField | |  
	| | video | URLField | |  
	| | stock | IntegerField | |   
	| **M2M** | likes | ManyToManyField | M2M related to **product_likes** |

- **Order**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | | order_number | CharField | |
    | **FK** | user_profile | ForeignKey | FK to **UserProfile** model |
    | | full_name | CharField | |
    | | email | EmailField | |
    | | phone_number | CharField | |
    | | country | CountryField | |
    | | postcode | CharField | |
    | | town_or_city | CharField | |
    | | street_address1 | CharField | |
    | | street_address2 | CharField | |
    | | county | CharField | |
	| | date | DateTimeField | |  
    | | delivery_cost | DecimalField | |
    | | order_total | DecimalField | |
    | | grand_total | DecimalField | |
    | | original_basket | TextField | |
    | | stripe_pid | CharField | |

- **OrderLineItem**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | **FK** | order | ForeignKey | FK to **Order** model |
    | **FK** | product | ForeignKey | FK to **Product** model |
    | | quantity | IntegerField | |
    | | lineitem_total | DecimalField | |


- **NewsletterSignup**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | | email | EmailField | unique=True | 
	| | date | DateTimeField | auto_now_add=True |
	| | date_update | DateTimeField | auto_now=True |  
	| | gdpr | BooleanField | Default=False |

- **Allauth User Model**
    - The User model was built using [Django's Allauth library](https://django-allauth.readthedocs.io/en/latest/overview.html)
    - When a user is created, they're automatically assigned a profile through the Profile model.

- **UserProfile**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | **FK** | user | OneToOne | FK to **User** model |
    | | default_phone_number | CharField | |
    | | default_street_address1 | CharField | |
    | | default_street_address2 | CharField | |
    | | default_town_or_city | CharField | |
    | | default_county | CharField | |
    | | default_postcode | CharField | |
    | | default_country | CountryField | |


[Back to top &uarr;](#contents)

***

## Features

### Existing Features

**Landing Page** is where a user lands on arrivial to the page. 
 It welcomes them to the site and gives them an idea of what the site sells. 
 A 'SHOP NOW' button invites users to enter and show around the site's product page. My intention was to keep it simple but enhance it to grab the attention of the users and invite them to shop.

![landing page](README/features/game-on-board-roll-play-win%E2%80%93destination.png)

***

**Navigation Menu** features include a search bar, profile access, bag and its total (showing the value of products currently in the bag), and links to filter products by different categories. When logged in as a super user, one gets access to the additional menu 'Admin'. Nav bar also includes the Delivery threshold info which is set to 50 Euro.

<details>
<summary>>>> Click to View Navigation Menu Picture</summary>

![Nav Bar](README/features/nav-bar.png)
</details>

***

**Product Sorting and Filtering** - User can sort and filter products in a number of ways. Products can be sorted by: Price (low to high), Price (high to low), Age (low to high),Age (high to low), Rating (low to high), Rating (high to low),Name (A-Z), Name (Z-A), Category (A-Z), Categoty(Z-A). If the user chooses to filter product by category, relevant category is also shown on top of the page (as a link).

<details>
<summary>>>> Click to View Sorting and Filtering Pictures</summary>

![Filtering](README/features/filtering.png)
![Sorting](README/features/sorting-1.png)
![Sorting](README/features/sorting-2.png)
![Sorting](README/features/sorting-3.png)

![Sorting](README/features/sorting-show-results.png)

</details>

***

**Search Bar** - the 'Search GamerOnBoard' bar gives the user the possibility to search product data by keyword which is matched up with the products' name and description.
The user can also see how many results were returned for their search term and the exact fraze they were looking for.
If the user hits the search button without entering anything, an error message is shown.

<details>
<summary>>>> Click to View Search Bar Pictures</summary>

![Search](README/features/search-bar.png)
![Search](README/features/search-bar-results.png)
</details>

***

**My Account** - A user has the option to either purchase the product without creating an account or create one in the 'My Account' menu. If the user is logged in, and has admin permissions, they will see an admin icon in the main nav menu. Clicking this will give the admin options to add a new product or open Admin Panel. Both, Admin and regular user, have access to 'My Account' menu which provides links to 'My Profile' or log out from the App. 

<details>
<summary>>>> Click to View My Account Link Picture</summary>

![My Account](README/features/my-account.png)
</details>

***

**Sign Up Page** - A User has an option to create their account traditionally with their email/password combination or by useing Google SSO. User is asked to confirm their email via email.

<details>
<summary>>>> Click to View Sign Up Page</summary>

![Sign Up](README/features/sign-up.png)
![Confirmation](README/features/confirmation-email.png)
</details>

***

**Sign In Page** - A User has an option to login with their traditional email/password combination or by useing Google SSO. There's also a checkbox to let the user be remembered on their current device to avoid having to log in every time they visit the site.

<details>
<summary>>>> Click to View Sign In Picture</summary>

![Sign In](README/features/sign-in.png)
</details>

***

**Log Out Page**

<details>
<summary>>>> Click to View Sign Out Picture</summary>

![Sign Out](README/features/sign-out.png)
</details>

***

**Password Reset Page**

<details>
<summary>>>> Click to View Password Reset Pictures</summary>

![Pass Reset](README/features/password-reset.png)
![Pass Reset](README/features/password-reset-done.png)
![Pass Reset](README/features/password-reset-email.png)
</details>

***

**User Profile / Deliver Information / Order History Page** - Fully registered users get a profile which contains the user's default delivery information if set and a list of the user's previous orders. The form on the user's profile contains the default delivery information if the user has saved it. The user can update this information from their profile by altering the form and clicking the update information button. This information will be automatically used for the user's next purchase to make the site easier to use for customers. Logged in users can view their list of order history on their profiles. The order number contains a link which when the user clicks on it, are brought to the order confirmation page for that specific order which contains all the details for that order and a link to return to the user's profile. User can also reset their password from their Profile view.

<details>
<summary>>>> Click to View User Profile / Deliver Information / Order History Page</summary>

![User Profile](README/features/user-profile-update.png)
![history](README/features/order-history.png)
</details>

***

**Admin** - Superusers can access extra menu with links to 'Product Management' and 'Admin Panel' 

<details>
<summary>>>> Click to View Admin Picture</summary>

![Admin](README/features/admin-menu.png)
</details>

***

**Product Management** - Superusers can add new products to the webstore. The add product contains a form for the admin to fill out with the details of the new product.

<details>
<summary>>>> Click to View Product Management Picture</summary>

![Product Add](README/features/product-managment.png)
</details>

***

**Products Page** have their own pages for the user to view more information about the product including a description for every game, category, age restrictions etc. Similar to the all products page, the product's images (max 3 plus a video), name, condition and availability badges and price appear on the individual page along with buttons to add the product to the user's basket or to return to the all products page and keep shopping.

![Product All](README/features/product-page.png)

***

**Product Card Page / Product Card Admin View**

<details>
<summary>>>> Click to View Product Cards Pictures</summary>

![Product Card](README/features/product-card.png)
![Product Card Admin](README/features/product-card-super.png)
</details>

***

**Product Card Page - Add to Bag - Stock Availability Badges** Products have a stock availability badges which show stock left for each product so that the user is informed whether the product is in stock (>3 items), how many are left in stock (<3 items) or 'Out of Stock' (cannot be added to bag).

- Products with more than 3 items left in stock have a teal badge with the 'in stock' info displayed.
- If the product has less than 3 items left in stock then the badge displays the item count and is turned yellow.
- A Red 'Out of Stock' badge and locked 'Add to Bag' button is shown for products stock even 0.
- When a product is purchased, the stock will automatically decrease by the number of units of each product the customer purchases.

<details>
<summary>>>> Click to View Card Page - Add to Bag - Stock Availability Badges</summary>

![Sold Out](README/features/add-to-bag-sold-out.png)
![Limited Stock](README/features/add-to-bag-limited.png)
![In Stock](README/features/add-to-bag-in-stock.png)

</details>

***

**Product Card Page - Condition Badges** Products may have a condition badge attached to let the user know whether the product is new, like new, user or collectable.

***

**Product Details Page** Users can use a quantity selector to select how many items they want to purchase. The selector lets the user add a minimum of 1 and a maximum of whatever the product's current stock is to their bag. After setting the quantity, a user can click the add to bag button to add that number of the product to their bag. If the user already has an item in their bag and tries to add more than the stock, an error message will be shown. 

![Product Details](README/features/product-details.png)
![Product Details](README/features/product-details-additional-info.png)

***

**Editing Product** A Superusers can edit products by clicking the edit icon on either the product card on the all products page or the individual product page.The edit product page contains the same form as the add product page but the fields are already populated with the product's current data. 

<details>
<summary>>>> Click to View Edit Product Page</summary>

![Edit](README/features/product-edit.png)
</details>

***

**Deleting Product** A Superusers can delete products by clicking the delete icon on either the product card on the all products page or the individual product page.
After clicking the icon, the admin will be promped with a popup message and asked to confirmation deletione to avoid products being deleted accidentally.

<details>
<summary>>>> Click to View Delete Page Confirmation Picture</summary>

![Delete](README/features/product-delete-conf.png)
</details>

***

**Product Card Page - Add to Bag** Every product has a button that lets the user add to bag when viewing it both on the products page or the individual product page. By clicking the 'Add to Bag' button, one unit of the product is added to the user's bag. A user is shown a message confirming when an item has been added, removed or updated in their bag.

<details>
<summary>>>> Click to View Product Card Page - Add to Bag Pictures</summary>

![Add](README/features/add-to-basket.png)
![Add text](README/features/add-to-basket-update.png)

![Alert](README/features/bag-alert-updated.png)
![Alert](README/features/bag-alert-removed.png)
![Alert](README/features/err-add-to-bag-no-stock.png)
![Alert](README/features/bag-alert-stock-not-available.png)

</details>

***

**Bag Empty Page**

<details>
<summary>>>> Click to View Empty Bag Picture</summary>

![Empty Bag](README/features/empty-bag.png)
</details>

***

**Bag Page** - Users can use a quantity selector to select, update or delete items they wish to purchase. The selector lets the user add a minimum of 1 and a maximum of whatever the product's current stock is to their bag. After setting the quantity, a user can click the add to bag button to add that number of the product to their bag. If the user already has an item in their bag and tries to add more than the stock, an error message will be shown.  User is also presented with Bag Total, Delivery Costs, Grand Total and is encuraged to buy by pressing 'Pay Stripe' button which brings the User to Stripe payments page.

![Bag](README/features/bag.png)

***

**Checkout Page** - The user is asked to complete the customer details form if not logged in or if a previous profile with details has been saved form is pre-populated with delivery details. Order Summary is shown with all products sitting in the bag and the 'Complete Order' button lets the User complete the transaction using Stripe Payments. Upon successful transaction completion, an order confirmation email is sent to the user's email address and an order confirmation page is shown. Users have the option to 'Go back to Your Profile' if logged in or the 'View Our Deals' button is purchase made incognito.

<details>
<summary>>>> Click to View Checkout Page</summary>

![Checkout](README/features/checkout.png)

![payment](README/features/checkout-payment.png)

![Order Confirmation](README/features/checkout-confirmation.png)

![Confirmation Order Email](README/features/confirmation-order-email.png)
</details>

***

**Footer Page** is always shown through each page and contains links to the blog (future function), privacy policy and social media. Also, quick links to games by category are presented in the centre section. On the right side, users can use a form to submit to the Newsletter as well as view the links for the Association we are working with/are members of. 

![Footer](README/features/footer.png)

***

**Newsletter Page** - Users can sign up for the GamerOnBoard newsletter where on submission, they will be sent a welcome email. Users can only sign up to the newsletter once and if they try to sign up with an already registered email address, they will see a message letting them know.

<details>
<summary>>>> Click to View Newsletter Pictures</summary>

![Newsletter](README/features/newsletter-aler-created.png)
![Newsletter](README/features/newsletter-aler-duplicate.png)
![Newsletter](README/features/newsletter-email.png)
</details>

[Back to top &uarr;](#contents)


***

### Future Features

- Ranking - as a future development step, I'd like incorporate Ranking functionality. t the moment rakning onthe page doesn not work correctly and its missing functionality to calculate ranking. 
- Blog - as a future development step, I'd like incorporate a Blog which would build and gather the like-minded, board-games focused enhusiasts.
- Discount - as a future development step, I'd like incorporate discounts so that I can reward existing users as well as invite new mambers over the Social Media.

[Back to top &uarr;](#contents)

***

### Error Pages


**404 Page not found** - page has been implemented and will display if a user navigates to a broken link.

<details>
<summary>Click to View http404 Error Page</summary>

![Error 404](README/features/404.png)
</details>

***

**500 Internal Server Error** - error page has been displayed to alert users when an internal server error occurs. 

<details>
<summary>Click to View http500 Error Page</summary>

![Error 500](README/features/500.png)
</details>

***

**403 Action Forbidden** - error page has been implemented to provide feedback to the user when they try to access unauthorized content. 


[Back to top &uarr;](#contents)

***

## Testing

[TESTING.md](TESTING.md) file.

[Back to top &uarr;](#contents)

***

## Tools & technologies used

### Languages Used

- [HTML5](https://html.spec.whatwg.org/) used for page content and structure 
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html) used for page styling
- [Javascript](https://www.javascript.com/) used for dynamically updated content
- [Python](https://www.python.org/) - used for the functionality of the program

### Frameworks & Tools

- [Django](https://www.djangoproject.com/) used as main python framework
- [Stripe Payments](https://stripe.com/) Payments infrastructure for the Internet
- [Bootstrap](https://blog.getbootstrap.com/) used for page layout and spacing
- [PostgreSQL](https://www.postgresql.org) used for database management
- [ElephantSQL](https://www.elephantsql.com/) used for production database
- [Heroku](https://dashboard.heroku.com/apps) used to deploy application
- [AWS](https://aws.amazon.com/s3/) used for online static file storage
- [Gitpod](https://www.gitpod.io/) used to create and host the website
- [Github](https://github.com/) used to deploy the website 
- [Balsamiq](https://balsamiq.com/) used to create page wireframes
- [Stackoverflow](https://stackoverflow.com/) used to troubleshoot code issues
- [CI Python Linter](https://pep8ci.herokuapp.com/) used as Python code validator
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
- [Grammarly](https://www.grammarly.com/) used to check typography
- [Am I Responsive](https://amiresponsive.co.uk/) mockup image of the home page on various devices 
- [LucidChart](https://lucid.app/) - Data Schema
- [ChatGPT](chat.openai.com) - which is a very usefull tool and helped with many questions related to the code itself

### Imported Libraries and Packages

- [gunicorn]() - Python WSGI HTTP Server for UNIX
- [psycopg2]() - PostgreSQL database adapter for Python
- [dj-database-url]() - Django utility to utilise the DATABASE_URL environment variable to configure the Django application. Used with PostgreSQL
- [Django]() - Python package for the Django framework
- [django-allauth]() - Django user authentication, registration and account management
- [django-crispy-forms]() - Django package that provides tags and filters to control the rendering behaviour of Django forms
- [django-countries] - A Django application that provides country choices for use with forms
- [django-storages] - provides a variety of storage backends in a single library
- [sqlparse] - is a non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements
- [stripe] - Stripe Payments webhook
- [boto3] -  to create, configure, and manage AWS services
- [s3transfer] - a Python library for managing Amazon S3 transfers
- [botocore] - A low-level interface to a growing number of Amazon Web Services
- [jmespath] - allows you to declaratively specify how to extract elements from a JSON document.
- [oauthlib] - is a framework which implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework
- [asgiref] -  Provides an optional template to start ASGI channel layers from with the two exceptions you need provided and all APIs
- [Pillow] -  adds image processing capabilities to your Python interpreter
- [PyJWT] - A library which allows you to encode and decode JSON Web Tokens 
- [pytz] - This library allows accurate and cross platform timezone calculations using Python


[Back to top &uarr;](#contents)

***

## Deployment

The live deployed application can be found deployed on [Heroku](https://gamer-on-board-6fa9b306b6d7.herokuapp.com/).

***

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:
- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: tribe).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

[Back to top &uarr;](#contents)

***

### Amazon AWS

This project uses [AWS](https://aws.amazon.com) to store media and static files online, due to the fact that Heroku doesn't persist this type of data.

Once you've created an AWS account and logged-in, follow these series of steps to get your project connected.
Make sure you're on the **AWS Management Console** page.

#### S3 Bucket

- Search for **S3**.
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
- From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click **Save**.
- From the **Permissions** tab, paste in the following CORS configuration:

	```shell
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

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
	- Policy Type: **S3 Bucket Policy**
	- Effect: **Allow**
	- Principal: `*`
	- Actions: **GetObject**
	- Amazon Resource Name (ARN): **paste-your-ARN-here**
	- Click **Add Statement**
	- Click **Generate Policy**
	- Copy the entire Policy, and paste it into the **Bucket Policy Editor**

		```shell
		{
			"Id": "Policy1234567890",
			"Version": "2012-10-17",
			"Statement": [
				{
					"Sid": "Stmt1234567890",
					"Action": [
						"s3:GetObject"
					],
					"Effect": "Allow",
					"Resource": "arn:aws:s3:::your-bucket-name/*"
					"Principal": "*",
				}
			]
		}
		```

	- Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
	- Click **Save**.
- From the **Access Control List (ACL)** section, click "Edit" and enable **List** for **Everyone (public access)**, and accept the warning box.
	- If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled** (mentioned above).

#### IAM

Back on the AWS Services Menu, search for and open **IAM** (Identity and Access Management).
Once on the IAM page, follow these steps:

- From **User Groups**, click **Create New Group**.
	- Suggested Name: `gamer-on-board` (group + the project name)
- Tags are optional, but you must click it to get to the **review policy** page.
- From **User Groups**, select your newly created group, and go to the **Permissions** tab.
- Open the **Add Permissions** dropdown, and click **Attach Policies**.
- Select the policy, then click **Add Permissions** at the bottom when finished.
- From the **JSON** tab, select the **Import Managed Policy** link.
	- Search for **S3**, select the `AmazonS3FullAccess` policy, and then **Import**.
	- You'll need your ARN from the S3 Bucket copied again, which is pasted into "Resources" key on the Policy.

		```shell
		{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Effect": "Allow",
					"Action": "s3:*",
					"Resource": [
						"arn:aws:s3:::gamer-on-board",
						"arn:aws:s3:::gamer-on-board/*"
					]
				}
			]
		}
		```
	
	- Click **Review Policy**.
	- Suggested Name: `gamer-on-board` (policy + the project name)
	- Provide a description:
		- "Access to S3 Bucket for gamer-on-board static files."
	- Click **Create Policy**.
- From **User Groups**, click your "gamer-on-board".
- Click **Attach Policy**.
- Search for the policy you've just created ("gamer-on-board") and select it, then **Attach Policy**.
- From **User Groups**, click **Add User**.
	- Suggested Name: `gamer-on-board` (user + the project name)
- For "Select AWS Access Type", select **Programmatic Access**.
- Select the group to add your new user to: `gamer-on-board`
- Tags are optional, but you must click it to get to the **review user** page.
- Click **Create User** once done.
- You should see a button to **Download .csv**, so click it to save a copy on your system.
	- **IMPORTANT**: once you pass this page, you cannot come back to download it again, so do it immediately!
	- This contains the user's **Access key ID** and **Secret access key**.
	- `AWS_ACCESS_KEY_ID` = **Access key ID**
	- `AWS_SECRET_ACCESS_KEY` = **Secret access key**

#### Final AWS Setup

- If Heroku Config Vars has `DISABLE_COLLECTSTATIC` still, this can be removed now, so that AWS will handle the static files.
- Back within **S3**, create a new folder called: `media`.
- Select any existing media images for your project to prepare them for being uploaded into the new folder.
- Under **Manage Public Permissions**, select **Grant public read access to this object(s)**.
- No further settings are required, so click **Upload**.

[Back to top &uarr;](#contents)

***

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://gamer-on-board-6fa9b306b6d7.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

[Back to top &uarr;](#contents)

***

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for account verification and purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (verify your password and account)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords**.
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
	- Any custom name, such as "Django" or gamer-on-board
- You'll be provided with a 16-character password (API key).
	- Save this somewhere locally, as you cannot access this key again later!
	- `EMAIL_HOST_PASS` = user's 16-character API key
	- `EMAIL_HOST_USER` = user's own personal Gmail email address

[Back to top &uarr;](#contents)

***

### Heroku Deployment

[Setting up basic Django Project and Deploying to Heroku CI Doc](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit)

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

1. Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
1. Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select *Create App*.
1. Further down, to support dependencies, select *Add Buildpack*.
1. The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)
1. From the new app *Settings*, click *Reveal Config Vars*, and set your environment variables.

    
    -  Key Value
    -  `AWS_ACCESS_KEY_ID`
    -  `AWS_SECRET_ACCESS_KEY`
    -  `DATABASE_URL`
    -  `DISABLE_COLLECTSTATIC`
    -  `EMAIL_HOST_PASS`
    -  `EMAIL_HOST_USER`
    -  `SECRET_KEY`
    -  `STRIPE_PUBLIC_KEY`
    -  `STRIPE_SECRET_KEY`
    -  `STRIPE_WH_SECRET`
    -  `USE_AWS`

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's *requirements* (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The *Procfile* can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace *app_name* with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select *Automatic Deployment* from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <app_name>` (replace app_name with your app, without the angle-brackets)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

[Back to top &uarr;](#contents)

***

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("AWS_ACCESS_KEY_ID", `HEROKU CONFIG VARS`)
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", `HEROKU CONFIG VARS`)
os.environ.setdefault("DATABASE_URL", `HEROKU CONFIG VARS`)
os.environ.setdefault("EMAIL_HOST_PASS", `HEROKU CONFIG VARS`)
os.environ.setdefault("EMAIL_HOST_USER", `HEROKU CONFIG VARS`)
os.environ.setdefault("SECRET_KEY", `HEROKU CONFIG VARS`)
os.environ.setdefault("STRIPE_PUBLIC_KEY", `HEROKU CONFIG VARS`)
os.environ.setdefault("STRIPE_SECRET_KEY", `HEROKU CONFIG VARS`)
os.environ.setdefault("STRIPE_WH_SECRET", `HEROKU CONFIG VARS`)

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

[Back to top &uarr;](#contents)

***
#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/ShemmyYo/game-on-board-p5-ecommerce-app) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/ShemmyYo/game-on-board-p5-ecommerce-app.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ShemmyYo/)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

[Back to top &uarr;](#contents)

***
#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
To make a copy or ‘fork’ the repository - 

1. Log into GitHub and locate the repository  
2. On the right-hand side of the page select the ‘fork’ option to create and copy the original

Alternatively, if using Gitpod, you can click below to create your workspace using this repository

[Back to top &uarr;](#contents)

***

## Credits

Throughout the building process I found many helpful tutorials online.
I sometimes applied principles within them to the site, after fully understanding their code and modifying to fit the site's needs.

1. [Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template) - This repository was created using the template provided by Code Institute.
1. [Django Documentation](https://docs.djangoproject.com/en/4.0/) - Django step-by-step document to ensure everything is set up correctly.
1. [Setting up basic Django Project and Deploying to Heroku](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit) - Documentation on how to create django project provided by [Code Institute](https://codeinstitute.net/ie/) 
1. [Allauth Documentation](https://django-allauth.readthedocs.io/en/latest/faq.html) - referenced during development.
1. [Cloudinary Documentation](https://cloudinary.com) - referenced during development.
1. [Summernote Documentation](https://summernote.org/) and [Git](https://github.com/summernote/django-summernote) - referenced during development.
1. [Crispy Forms Documentation](https://django-crispy-forms.readthedocs.io/en/latest/) - referenced during development.
1. [Privacy Policy Generator](https://www.privacypolicygenerator.info/) - The fastest free Privacy Policy generator.

1. [Stackoverflow](https://stackoverflow.com/) - I found myself on Stackoverflow so many times researching issues. This a fantastic place to learn and troubleshoot code.
1. [Slack](https://slack.com/intl/en-ie/) - The slack community is great and I reached out to fellow students who had already completed their P5 for their advice and got some nice tips and feedback. I attending some webinars by CI staff which I found very beneficial.

1. [unsplash](https://unsplash.com/s/photos/Sauce) - Graphics used on the page
1. [Markdown Builder by Tim Nelson](https://traveltimn.github.io/markdown-builder/) - tool to help generating some parts of the Markdown files
1. [GitHub - Ian Lunn](https://github.com/IanLunn) - GitHub repo with awsome CSS codes 
1. [GitHub - Bootstrap](https://github.com/twbs/bootstrap) - bootstrap repo
1. [CSS effects](https://css-tricks.com/snippets/css/css-triangle/) - some awsome CSS-tricks.com 
1. [uiverse.io](https://uiverse.io/) - some awsome CSS

1. [BPA World Boardgaming](https://www.boardgamers.org/index.html) - which I lineked on my page.
1. [BPA World Boardgaming](https://www.boardgamers.org/index.html) - which I lineked on my page.
1. [Wikipedia](https://en.wikipedia.org/) - PEGI classification and description and other.
1. [bordgamer.ie](https://www.boardgamer.ie/) - for inspiration

***

## Acknowledgements

As always, big thank you to [Harry Dhillon](https://github.com/Harry-Leepz), my mentor who provided me with guide and excellent feedback throughout the project.
I'd like to thank my fellow coders from my group but not limiting, for advise, support and sharing their knowledge over the last one year.

GamerOnBoard was developed for educational purpouses and as part of my Diploma in Software Development with [Code Institute](https://codeinstitute.net/). 

[Back to top &uarr;](#contents)
