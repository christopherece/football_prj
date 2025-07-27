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
    
    # First reset migrations
    print("\nResetting migrations...")
    call_command('migrate', 'accounts', 'zero')
    call_command('migrate', 'admin', 'zero')
    
    # Then apply in correct order
    print("\nApplying migrations in correct order...")
    call_command('migrate', 'accounts')
    call_command('migrate', 'admin')
    
    print("\nMigration fix completed!")

if __name__ == '__main__':
    fix_migration_order()
