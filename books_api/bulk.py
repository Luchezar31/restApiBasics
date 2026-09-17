import os
import sys
import django

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Replace 'RestfulExersice.settings' with your actual settings module path if different
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restBasics.settings')
django.setup()

# Django setup MUST happen before importing models
from books_api.models import Book

# Note: .create() automatically saves to the database—book.save() is not required
book = Book.objects.create(
    title='shogun',
    description='Very nice book',  # Fixed typo: 'description'
    pages=400,                      # Ensure field name matches models.py (e.g., 'page' or 'pages')
    author='Japanese'
)

