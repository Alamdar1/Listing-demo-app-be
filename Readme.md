# Listing Platform

A Django REST API for managing property listings.

## Features

- List model with title, description, price, location, created/updated timestamps
- Filtering by title (case-insensitive)
- RESTful endpoints for CRUD operations
- Admin interface
- CORS support for frontend integration

## Project Structure

- `backend/List/` - Django app for listings
- `backend/listing_platform/` - Django project settings and URLs
- `backend/manage.py` - Django management script
- `requirements.txt` - Python dependencies

## Setup

1. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

2. **Run migrations**

   ```sh
   cd backend
   python manage.py migrate
   ```

3. **Create superuser (optional)**

   ```sh
   python manage.py createsuperuser
   ```

4. **Start development server**
   ```sh
   python manage.py runserver
   ```

## API Endpoints

- `GET /api/lists/` - List all listings
- `POST /api/lists/` - Create a new listing
- `GET /api/lists/{id}/` - Retrieve a listing
- `PUT /api/lists/{id}/` - Update a listing
- `DELETE /api/lists/{id}/` - Delete a listing

## Filtering

- Filter by title: `/api/lists/?title=apartment`

## Deployment

- Configured for Vercel with [vercel.json](vercel.json)
