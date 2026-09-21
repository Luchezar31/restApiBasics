import os
import sys
import django


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restBasics.settings')
django.setup()


from books_api.models import Book


book = Book.objects.create(
    title='shogun',
    description='Very nice book',  # Fixed typo: 'description'
    pages=400,                      # Ensure field name matches models.py (e.g., 'page' or 'pages')
    author='Japanese'
)

