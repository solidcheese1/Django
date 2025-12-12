
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from app.models import Auto  # импорт после setup()

def main():
    auto = Auto(brand="Toyota", model="Camry", year=2020, color="Белый")
    print(auto)

if __name__ == '__main__':
    main()
