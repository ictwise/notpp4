## **Contents**


- [**Manual Testing**](#manual-testing)
  - [**Browsers**](#browsers)
  - [**Devices Used**](#devices-used)
  - [**Navigation**](#navigation)
  - [**Home Page**](#home-page)
  - [**Register Page**](#register-page)
  - [**Log In Page**](#log-in-page)
  - [**Profile Page**](#profile-page)
  - [**Products Pages**](#products-pages)
    - [**Products**](#products)
    - [**Product Details**](#product-details)
    - [**Add Product**](#add-product)
    - [**Edit Product**](#edit-product)
  - [**Bag**](#bag)
  - [**Checkout**](#checkout)
  - [**Blog Page**](#blog-page)
- [**User Stories Testing**](#user-stories-testing)
- [**Wave**](#wave)
- [**Lighthouse**](#lighthouse)
- [**Validators**](#validators)
  - [**HTML Validator**](#html-validator)
  - [**CSS Jigsaw**](#css-jigsaw)
  - [**JSHint**](#jshint)
  - [**PEP8**](#pep8])


### **Manual Testing**
#### **Browsers**
The site was tested on:
- Edge
- Google Chrome
- Firefox

#### **Devices Used**
The site was tested on these devices:
- Huawei P30 Lite
- Samsung 20
- Windows Laptop - windows 11



### User Stories Testing

| User Story ID  | As a/an  | I want to be able to...  | So that I can... | Testing | Pass/Fail |
|-------------------|-------------------|-----------------|-------------------|-------------------|---------------|
| Viewing Products & Navigation |
| 1  | User/Shopper | view individual product details | so that I can identity the price, descriptionmand view the product image (where one is available) | View Products [Page](static/docs/images/user-story-testing/us1-view-all.png), view product [1](static/docs/images/user-story-testing/us1-view-individual.png), [2](static/docs/images/user-story-testing/us1-view-individual2.png), [3](static/docs/images/user-story-testing/us1-view-individual3.png) | Pass |
| 2  |   | be able to add, edit quantity and remove items from my bag | buy them after browsing. | [Add](static/docs/images/user-story-testing/us2-add-to-bag.png) product to bag, view [toast](static/docs/images/user-story-testing/us2-add-to-bag-toast.png), [update](static/docs/images/user-story-testing/us2-update-bag.png) item quantity, [remove](static/docs/images/user-story-testing/us2-remove-from-bag.png) from bag | Pass |
| 3  |   | see any special offers | take advantage of saving money on products I'd like to buy. | Navigation bar displays free shipping if shopper spends £50 or [more](static/docs/images/user-story-testing/us3-special.png) | Pass |
| 4  |   | gain inspiration from the blog | decide what to buy and make next. | Blog Page displays knitted [goods](static/docs/images/user-story-testing/us4-inspiration.png) with comments linking [products](static/docs/images/user-story-testing/us4-knit-happens.png) to the store | Pass |
| 5  |   | add posts to the blog | show other users what I have made and gain their opinions through comments. | Blog add to post function allows users to add posts to the [blog](static/docs/images/user-story-testing/us5-add-blog-post.png), [2](static/docs/images/user-story-testing/us5-add-blog-post2.png) | Pass |
| Registration and Accounts |
| 6  | User/Shopper | register for an account | keep track of my orders and check my personal details. | Users can [register](static/docs/images/user-story-testing/us6-registration.png), [2](static/docs/images/user-story-testing/us6-registration-successful.png), [3](static/docs/images/user-story-testing/us6-verify-email.png) for an account and view their orders in the profile [page](static/docs/images/user-story-testing/us9-view-profile.png) | Pass |
| 7  |   | receive email confirmation upon signing up | verify my set up was successful. | User receives [email](static/docs/images/user-story-testing/us7-email-confirmation.png) when they register for an account | Pass |
| 8  |   | be able to reset my password in case I forget it | gain access to my account. | User can request [email](static/docs/images/user-story-testing/us8-reset-email.png) [2](static/docs/images/user-story-testing/us8-reset-email.png) to reset their [password](static/docs/images/user-story-testing/us8-password.png) | Pass |
| 9  |   | have the ability to log in to the site with my details | view my orders and personal details | Users can [log in](static/docs/images/user-story-testing/us9-log-in.png) using their registered details and view their orders and personal [details](static/docs/images/user-story-testing/us9-view-profile.png) | Pass |
| 10  |   | update my personal details | keep them up to date. | Users can update their [personal](static/docs/images/user-story-testing/us10-update-profile.png) details in the profile section | Pass |
| 11 |   | purchase from the site without having to create an account | check out quickly and easily. | Users can use the checkout without registering for an account [1](static/docs/images/user-story-testing/us11-guest.png), [2](static/docs/images/user-story-testing/us11-guest2.png), [3](static/docs/images/user-story-testing/us11-guest-confirm.png) | Pass |
| 12  | User/Shopper | search for specific products | find products I am interested in buying. | Users can [search](static/docs/images/user-story-testing/us12-search.png), on the site for [products](static/docs/images/user-story-testing/us12-search2.png) and if no product available message to confirm [this](static/docs/images/user-story-testing/us12-no-products.png) | Pass |
| 13  |   | easily understand the search results | quickly decide which product I want to buy. | Users can search for products and quickly see how many match their [criteria](static/docs/images/user-story-testing/us13-search.png) | Pass |
| 14  |   | sort by price, name, category | view a wide range and choose which to buy. | Users can sort by [price](static/docs/images/user-story-testing/us14-price.png), [name](static/docs/images/user-story-testing/us14-name.png) and [category](static/docs/images/user-story-testing/us14-category.png) on the products page | Pass |
| Checkout  |
| 15  | Shopper | have a running total of my bag | stay within my budget. | Users can see the total in the bag icon on the navbar. Product [1](static/docs/images/user-story-testing/us15-add1.png), [2](static/docs/images/user-story-testing/us15-add2.png), [3](static/docs/images/user-story-testing/us15-add3.png) | Pass |
| 16  |   | view my bag contents | keep track of which products I have selected. | Users can view their bag to see which products and quantities have been [added](static/docs/images/user-story-testing/us16-view-bag.png) | Pass |
| 17  |   | easily select the correct size | ensure I have ordered the right size for my project. | Users use the [dropdown](static/docs/images/user-story-testing/us17-size.png) to select the required [size](static/docs/images/user-story-testing/us17-select.png)/weight and this is confirmed in the bag| Pass |
| 18  |   | adjust the quantity of products to buy | update the order without going back to the product page. | Users can update quantities in the shopping bag successfully. see [before](static/docs/images/user-story-testing/us18-before-update.png), [after](static/docs/images/user-story-testing/us18-update-quantity.png) | Pass |
| 19  |   | easily enter my payment details | checkout as quickly and easily as possible. | Users can navigate the [checkout](static/docs/images/user-story-testing/us19-checkout.png) form payment input easily | Pass |
| 20  |   | view the full order before entering card details | check it before confirmation. | The [Order](static/docs/images/user-story-testing/us20.png) can be viewed on the checkout page before entering card details | Pass |
| 21  |   | receive email notifications when I make an order | confirm my order has been placed and refer back to. | Users receive an [email](static/docs/images/user-story-testing/us21-email.png) when they make an [order](static/docs/images/user-story-testing/us21-conf.png) | Pass |
| Admin/Management  |
| 22  | Store owner/Admin | add a product | sell new items in my store  | Super users can add a product see [here](static/docs/images/user-story-testing/us22-add-product-button.png) and [here](static/docs/images/user-story-testing/us22-add-product-form.png) | Pass |
| 23  |   | update a product | change descriptions, sizes, images in my store. | Super users can [edit](static/docs/images/user-story-testing/us23-edit-product-form.png) a [product](static/docs/images/user-story-testing/us23-edit-product-form-post.png) | Pass |
| 24  |   | delete a product | remove items no longer on sale. | Super users can delete a product [1](static/docs/images/user-story-testing/us24-product-before.png), [2](static/docs/images/user-story-testing/us24-delete-modal.png), [3](static/docs/images/user-story-testing/us24-delete-toast.png) | Pass |


[Back to contents](#contents)

### **Wave**

The site was inspected for accessibility using the [Wave Browser Extension](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh) and changes made to HTML following this inspection. 
The result is no major errors.

### **Lighthouse**

Lighthouse testing was completed on all pages of the site
- [Home](static/docs/images/validation/lighthouse-home.png)
- [Products](static/docs/images/validation/lighthouse-products.png)
- [Product Detail](static/docs/images/validation/lighthouse-product_detail.png)
- [Bag](static/docs/images/validation/lighthouse-bag.png)
- [Checkout](static/docs/images/validation/lighthouse-checkout.png)
- [Checkout Success](static/docs/images/validation/lighthouse-checkout-success.png)
- [Profile](static/docs/images/validation/lighthouse-profile.png)
- [Blog](static/docs/images/validation/lighthouse-blog.png)
- [Post Detail](static/docs/images/validation/lighthouse-post-detail.png)
- [Add Blog Post](static/docs/images/validation/lighthouse-add-post.png)
- [Add Product](static/docs/images/validation/lighthouse-add-product.png)


The Lighthouse scores are quite good in my opinion and a lot of the warnings that appeared were due to things outside my control like external CSS, JS and JQuery libraries. One of the main warnings was regarding the explicit height and width of images however as all the images are different ratios and generated from the backend it was not possible for me to fix this. 


### **Validators**

#### **HTML Validator**
HTML validator was used for all pages and only one minor warning about the use of h1 element as this is used for the title but not the first child of the section. The section and h1 were used for accessibility reasons and this warning is very minor so the structure was kept in place.
- [Home](static/docs/images/validation/index.png)
- [Products](static/docs/images/validation/products-pag.png)
- [Product Detail](static/docs/images/validation/product_detail.png)
- [Bag](static/docs/images/validation/bag.png)
- [Checkout](static/docs/images/validation/checkout.png)
- [Checkout Success](static/docs/images/validation/checkout-success.png)
- [Profile](static/docs/images/validation/profile.png)
- [Blog](static/docs/images/validation/blog.png)
- [Post Detail](static/docs/images/validation/post-detail.png)
- [Add Blog Post](static/docs/images/validation/add-blog-post.png)
- [Edit Blog Post](static/docs/images/validation/edit-blog-post.png)
- [Add Product](static/docs/images/validation/add-product.png)
- [Edit Product](static/docs/images/validation/edit-product.png)

#### **CSS Jigsaw**
CSS Jigsaw validation passed for all pages
- [products.css](static/docs/images/validation/jigsaw-product-css.png)
- [blog.css](static/docs/images/validation/jigsaw-blog-css.png)
- [bag.css](static/docs/images/validation/jigsaw-bag-css.png)
- [checkout.css](static/docs/images/validation/jigsaw-checkout-css.png)
- [profile.css](static/docs/images/validation/jigsaw-profile-css.png)
- [style-uni-form.css](static/docs/images/validation/jigsaw-style-uni-form-css.png)
- [uni-form.css](static/docs/images/validation/jigsaw-uni-form-css.png)
- [base.css](static/docs/images/validation/jigsaw-base-css.png)

#### **JSHint**
JavaScript JSHint validator passed for all pages
- [base.js](static/docs/images/validation/jshint-base-js.png)
- [back-to-top.js](static/docs/images/validation/jshint-back-to-top-js.png)
- [modal.js](static/docs/images/validation/jshint-modal-js.png)
- [sort-selector.js](static/docs/images/validation/jshint-sort-selector-js.png)
- [uni-form-validation.jquery.js](static/docs/images/validation/jshint-uni-form-validation-jquery-js.png)

#### **PEP8**
- Checkout [signals](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1642780620039300) imported but not used in problems tab however this is required as it is being accessed elsewhere so the problem can be ignored.  
- [Line too long](static/docs/images/validation/test_models_problem.png) error in test_models.py however this is required to confirm the test passes.

[With all Python files open](static/docs/images/validation/pep8.png) those are the only two issues.
[Back to contents](#contents)