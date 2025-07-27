import os
import sys
import django

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lionsfootball.settings')
django.setup()

from django.core.management import call_command
from django.db import connection

def fix_migration_order():
    print("Starting migration fix process...")
    
    # Get the database path
    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db.sqlite3')
    print(f"\nDatabase path: {db_path}")
    
    # Ensure we have write permissions
    if os.path.exists(db_path):
        print("\nChecking database permissions...")
        if not os.access(db_path, os.W_OK):
            print("Database file is read-only. Please make it writable and try again.")
            print("You can make it writable using: chmod +w db.sqlite3")
            return
        
        # Delete the existing database
        print("\nDeleting existing database...")
        os.remove(db_path)
    
    # Create new migrations
    print("\nCreating migrations...")
    call_command('makemigrations')
    
    # Apply migrations in correct order
    print("\nApplying migrations in correct order...")
    call_command('migrate', 'auth')  # Apply auth migrations first
    call_command('migrate', 'accounts')  # Then accounts
    call_command('migrate', 'admin')  # Finally admin
    
    # Create a superuser if needed
    print("\nCreating superuser if needed...")
    from django.contrib.auth.models import User
    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create_superuser(
            'admin',
            'admin@example.com',
            'admin123'  # Change this in production!
        )
        print("Created superuser with username 'admin'")
    
    print("\nMigration fix completed!")

if __name__ == '__main__':
    fix_migration_order()
