## Assignment for SDE - Intern (Applications)

# Entry Notifier

The main motive of this venture was to create a software that can help a visitor check into an office without any kind of human intervention. The assignment aims
at automating check in's and check out's at a workplace. The user just has to specify some of his personal details like name, email and phone number and other details like who does he want to meet, his check in and check out time.

## Technology Stack

- **Programming Languages**
    - Python 3

- **Frameworks**
    - Flask 1.1.1

- **Database**
    - SQLAlchemy

- **Frontend**
    - HTML 5
    - CSS 3
    - JavaScript
    - jQuery 3.4.1
    - Bootstrap 4

- **APIs**
    - Twilio for sending sms.
    - Flask_mail (0.9.1) for sending emails.


## Implementation

The application can be primarily used for the following three tasks:

- Registration of a new host
- Host enters the expected visitors
- Visitor Check In
- Visitor Check Out

### Visitor Check In

As soon as the visitor opens the application a check in form appears. The visitor can only check in if he is already registered with a host by filling all the fields in the form.
 All the fields are mandatory to fill. The form is validated in the flask backend for any mistakes or null values and the check in is terminated. If the visitor was not expected
 a flash message will be shown which asks the visitor to contact host.

- **Check In Page**

![check-in home](https://drive.google.com/file/d/18qCo9mXdGBjlDFl0RsX4YzDBYm3vYR_c/view?usp=sharing "CHECK IN PAGE")

### Visitor Check Out

A separate check out page has been created where the user is required to mention the same mobile number they entered during check in.
 The checkout time is not required to be entered manually. If all details are correct and valid, the user will be checked out and will be sent all details through sms and email otherwise he will be asked to fill the details again.

- **Check Out Page Demo**

![check-out home](https://drive.google.com/file/d/1RZB3wEmETdssBJFo_7-WzRM3xwRBJBpa/view?usp=sharing "CHECK OUT PAGE")

> The visitor will be redirected to the home page, that is, the check in page as soon as the check out is successful.

### Host Registration
LOREM IPSUM

- **Host Login Demo**
![host-login](https://drive.google.com/file/d/1QDF-x49IH5KYDxcfUFzWxx_Kxx9wjopa/view?usp=sharing "HOST LOGIN")

- **The Database**

![firebase](images/database.jpg "FIREBASE")

> Lorem Ipsum is simply dummy text of the printing and typesetting industry.
 Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
  It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.

## Deployment & Testing



## Future Enhancements



## Credits

Created and Developed By: Geet Choudhary
Contact Email: geetchoudhary@gmail.com
