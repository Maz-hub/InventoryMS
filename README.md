# Inventory Management System

This project is divided into two parts: Backend and Frontend.

- Backend: Focuses on server setup and database management. Django is used for handling the backend, with the help of [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html#installing-django-crispy-forms) to manage forms in a clean and elegant way.
- Frontend: Utilizes [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/), an extension of django-crispy-forms, to seamlessly integrate Bootstrap 5 styling into Django forms for a polished and responsive user interface.


### Forms
- **Product Form**: Added a `forms.py` file in the `InventoryApp` to manage product-related forms. 
  - Includes fields for product details such as name, category, SKU, price, quantity, weight, color, size, supplier, description, and image.
  - Utilizes `django-crispy-forms` for improved form rendering and Bootstrap 5 styling.


## Features

### Product Management (CRUD)
The application now supports full **CRUD (Create, Read, Update, Delete)** functionality for managing products in the inventory.

- **Create:** Users can add new products through a form.
- **Read:** A product list page displays all existing products.
- **Update:** Users can update existing product details.
- **Delete:** Products can be removed from the system with a confirmation step.

### Templates
The following HTML templates have been added to improve the UI:
- **home.html** – Landing page.
- **layout.html** – Base layout for consistent styling.
- **product_form.html** – Used for both creating and updating products.
- **product_list.html** – Displays the list of products.
- **product_confirm_delete.html** – Confirmation page before deleting a product.

The templates use **Django forms** for structured input and leverage `django-crispy-forms` for improved styling.

### URL Patterns for Product Management
The following routes have been added to handle **CRUD operations** for products:

| URL Pattern                  | View Function            | Description                     |
|------------------------------|-------------------------|---------------------------------|
| `/`                          | `home_view`             | Home page                       |
| `/create/`                   | `product_create_view`   | Create a new product            |
| `/list/`                     | `product_list_view`     | Display all products            |
| `/update/<int:product_id>/`  | `product_update_view`   | Update an existing product      |
| `/delete/<int:product_id>/`  | `product_delete_view`   | Delete a product (confirmation) |

This ensures all product management functionality is accessible via clean and structured URLs.



