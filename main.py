
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_pr.settings')
django.setup()

from django_pr.models import Auto  # импорт после setup()

def main():
    auto = Auto(brand="Toyota", model="Camry", year=2020, color="Белый")
    print(auto)

if __name__ == '__main__':
    main()
