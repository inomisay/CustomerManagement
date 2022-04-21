# CustomerManagement

Creating an app that gives some of users to have full access to the customer data and some of them to have only access of reading the data of the customers. 


The user should be able to view all customer registrations that have been recorded so far on the listing screen, with the most recent one at the top of the list.
There will be displayed 25 customers on each page. This value must be changeable by fronted. (Pagination property)
The user should be able to search among the registrations according to the following information. ▪ ID number
▪ Turkish Identity Number ▪ Name
▪ Surname
▪ Phone number
▪ City
▪ District
The user can update the customer registrations. (Except the ID number column) The user can delete the customer registrations.
There should be a form which the user can create a new customer registration.
In this form, the following information of the customer should be obtained and registered in the system. ▪ Turkish Identity Number
▪ Name
▪ Surname
▪ Phonenumber
▪ City and District
Validation of all this information must be provided. For instance, a 6-digit Turkish ID number should not be allowed to be registered in the system. These faults should also be displayed on the frontend.
• • •
• •
•
There cannot be two customers with the same Turkish ID number on the system.
The user must be authorized to make these operations. The unauthorized users should not be able to do any operations in the system.
You should use the Django template for frontend design. (http://docs.djangoproject.com/en/3.2/topics/templates). It is up to you to use the CSS library.
You can use PostgreSQL or SQLite as a database.
Let's try to follow the PEP8 guidelines whenever possible.


