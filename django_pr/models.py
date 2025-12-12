from django.db import models

class Auto(models.Model):
    brand = models.CharField(
        max_length=100,
        verbose_name="Марка",
        help_text="Название марки автомобиля (например, Toyota, BMW)"
    )
    model = models.CharField(
        max_length=100,
        verbose_name="Модель",
        help_text="Название модели автомобиля (например, Camry, X5)"
    )
    year = models.PositiveIntegerField(
        verbose_name="Год выпуска",
        help_text="Год выпуска автомобиля"
    )
    color = models.CharField(
        max_length=50,
        verbose_name="Цвет",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} ({self.color if self.color else 'нет цвета'})"

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"
        ordering = ['-year', 'brand', 'model']