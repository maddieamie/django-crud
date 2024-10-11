# LAB 28 - Django CRUD and Forms

**Project:** Snacks CRUD Application  
**Author:** Your Name

## Links and Resources

- Back-end server URL: N/A
- Front-end application: N/A

## Setup

### .env requirements

No specific .env requirements for this project.

### How to initialize/run your application

To run your Django application, follow these steps:

1. Navigate to the project directory:
   ```bash
   cd snacks_crud_project
Run the development server:

```
python manage.py runserver
```

Access the application in your web browser at the local host given by your app.

### How to use the app

This project allows you to create, read, update, and delete snacks through a web interface. You can navigate to the following URLs:

- Snack List: `/`
- Add Snack: `/create/`
- Snack Details: `/1/` (replace 1 with the snack ID)
- Update Snack: `/1/update/` (replace 1 with the snack ID)
- Delete Snack: `/1/delete/` (replace 1 with the snack ID)

#### Tests

**How do you run tests?**

To run the tests for this project, use the following command in your terminal:


```
python manage.py test snacks
```

**Any tests of note?**

The following tests are included:

- Snack List View
- Snack Detail View
- Snack Create View
- Snack Update View
- Snack Delete View

**Describe any tests that you did not complete, skipped, etc.**

All planned tests were successfully completed, and the application behaves as expected.