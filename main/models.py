from django.db import models

class CarBrand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    logo = models.ImageField(upload_to='car_logos/')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Марку"
        verbose_name_plural = "Марки"

class CarModel(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name="Название")
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, null=False, verbose_name="Марка")

    def __str__(self):
        return f"{self.brand.name} {self.name}"

    class Meta():
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

class CarGeneration(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name="Модель")

    def __str__(self):
        return f"{self.model.brand.name} {self.model.name} {self.name}"

    class Meta():
        verbose_name = "Поколение"
        verbose_name_plural = "Поколения"

class Engine(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    photo = models.ImageField(upload_to='engine_photos/', verbose_name="Фото")
    fuel_type = models.CharField(max_length=50, choices=[('Бензин', 'Бензин'), ('Дизель', 'Дизель')], verbose_name="Тип топлива", default="Бензин")
    volume = models.FloatField(verbose_name="Объем двигателя")
    generations = models.ManyToManyField(CarGeneration, verbose_name="Поколения в которых устанавливался")
    state_of_origin = models.CharField(max_length=100, verbose_name="Страна производитель")
    condition = models.CharField(max_length=50, choices=[('Новый', 'Новый'), ('Б/у', 'Б/у')], verbose_name="Состояние")
    price = models.FloatField(default=0, verbose_name="Цена")
    price_order = models.FloatField(default=0, verbose_name="Цена под заказ")

    def __str__(self):
        return f"{self.name} - {', '.join([str(gen) for gen in self.generations.all()])}hp"

    class Meta:
        ordering = ['condition', 'state_of_origin']
        verbose_name = "Двигатель"
        verbose_name_plural = "Двигатели"

class OrderEngine(models.Model):
    engine = models.CharField(max_length=100, verbose_name="Двигатель")
    phone = models.CharField(max_length=15, verbose_name="Номер телефона")
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Заказы"
        verbose_name_plural = "Заказ"

