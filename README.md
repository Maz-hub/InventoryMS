# 🛒 Inventory Management System  

This is a small project to practice **Django** by building an **Inventory Management System** where you can **add, edit, view, and delete products**.  

## 📌 What This Project Includes  
This project has two main parts:  

- **Backend (Django)** – Manages data, forms, and server-side logic.  
- **Frontend (Bootstrap 5 + Django templates)** – Provides a simple user interface to interact with the inventory.  

---

## 🎯 Features  

✅ **Add products** with details like name, category, SKU, price, quantity, weight, color, size, supplier, and image.  
✅ **See all products** in a list format.  
✅ **Edit products** (update details & change images).  
✅ **Delete products** (with a confirmation page).  

---

## 🔹 Forms & Styling  
- **Product Form:** Built using Django **ModelForms** with `django-crispy-forms` to make it look clean.  
- **Bootstrap 5** is used for styling, making the UI simple and responsive.  

---

## 🌐 How The URLs Work  

| URL Pattern                  | What It Does?                     |
|------------------------------|---------------------------------|
| `/`                          | Home page                        |
| `/create/`                   | Add a new product                |
| `/list/`                     | Show all products                |
| `/update/<int:product_id>/`  | Update an existing product       |
| `/delete/<int:product_id>/`  | Delete a product (confirmation)  |

---

## 🖼️ **Image Uploads - Fix & Setup**  

### **💡 Issue:**  
Before, when editing a product, if no new image was uploaded, the **existing image disappeared**.  

### **✅ Fix:**  
- Updated `views.py` to **keep the old image** if no new one is uploaded.  
- Updated `product_form.html` to **show the current image** when editing a product.  
- Enabled **image uploads** by adding the following settings in `settings.py`:  

  ```python
  MEDIA_URL = '/media/'
  MEDIA_ROOT = BASE_DIR / 'media'
