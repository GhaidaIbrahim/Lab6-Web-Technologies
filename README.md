# Web Technologies - Lab 6: Django Web Search & Dynamic Templates

**Name:** Ghaida Al-harbi  
**Lab Number:** 6  

## Summary of Work
This lab focused on implementing a **Search Functionality** within a Django application, mastering the flow of data from user input (Forms) to backend processing (Views) and displaying results (Templates).

## Key Technical Tasks

### 1. Form Handling & Search Logic
* **Backend Processing**: Developed a search view in `views.py` that captures GET/POST requests and filters the book database based on user-defined keywords.
* **Querysets**: Applied Django ORM's `.filter()` method to retrieve specific data matching the search criteria.
* **Logic Flow**: Managed conditional rendering to handle cases where no results are found, ensuring a smooth user experience.

### 2. Frontend Development & UI
* **Search Interface**: Created `search.html` using HTML forms to capture user queries.
* **Dynamic Display**: Developed `bookList.html` using Django Template Language (DTL) to loop through search results dynamically.
* **Security**: Implemented the `{% csrf_token %}` tag to protect the application against Cross-Site Request Forgery during form submissions.

## Personal Notes & Key Takeaways
* **User Interaction**: Learned how to bridge the gap between user input on the frontend and data retrieval on the backend.
* **Error Handling**: Realized the importance of template directory structures (e.g., `templates/blog/`) in preventing `TemplateDoesNotExist` errors.
* **Professional Standards**: Continued utilizing Terminal-based Git operations to maintain a specialist-level workflow.

## Lab Deliverables
* **Source Code**: Implementation of search views, updated URLs, and search-specific templates.
* **Repository**: [GhaidaIbrahim/Lab6-Web-Technologies](https://github.com/GhaidaIbrahim/Lab6-Web-Technologies)

### 5. Quick Start Guide (Terminal)
To run this project on my local machine:
* **Navigate to the Project Root:** `cd ~/Desktop/CS471/bookproject`
* **Activate the Virtual Environment:** `source bin/activate`
* **Enter the Web Application Directory:** `cd bookwebsite`
* **Start the Development Server:** `python3 manage.py runserver`
* **Access the Search Function:** Open your browser and visit: `http://127.0.0.1:8000/books/search/`
