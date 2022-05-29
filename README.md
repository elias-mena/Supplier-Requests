# Supplier Request

App for make a request for buy an item in a company using Flask and PostgresSQL, there are 6 kind of users, the admin who can manage the users; the customer who can make requests; the chief approver, who can accept or decline in its first revision, and there are 3 kinds of financial approvers, who can accept or decline requests according to its amount.

## **How to start the app**

- Create virtual environment: `python3 -m venv venv`
- Activate virtual environment: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`
- Run the app: `python3 main.py`

## UML

![UML](apps/static/images/UML.png)

## E/R Diagram

![ER](apps/static/images/ER.png)

---

## Templates

---

### Register

![Register](apps/static/images/Register.png)

Login

![Login](apps/static/images/Login.png)

Admin Users

![Admin](apps/static/images/Admin.png)

New User

![NewUser](apps/static/images/NewUser.png)

Customer Main Page

![Customers](apps/static/images/NewRequest.png)

Customer requests page

![CustomerRequests](apps/static/images/CustomerRequests.png)

![CustomerRequests](apps/static/images/CustomerRequests2.png)

Approvers Main Page

![Approvers](apps/static/images/Approvers.png)

Reports Page

![Reports](apps/static/images/Reports.png)