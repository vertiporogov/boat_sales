from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Owner(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя владеллца')
    email = models.EmailField(verbose_name='почта владельца', unique=True)

    def __str__(self):
        return f'{self.email} ({self.name})'

    class Meta:
        verbose_name = 'владелец'
        verbose_name_plural = 'владельцы'


class Boat(models.Model):
    name = models.CharField(max_length=50, verbose_name='название лодки')
    year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='год выпуска')

    price = models.IntegerField(**NULLABLE, verbose_name='цена')

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name='владелец лодки')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'лодка'
        verbose_name_plural = 'лодки'


class BoatHistory(models.Model):
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE, verbose_name='лодка')
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, verbose_name='владелец лодки', **NULLABLE)

    start_year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='владел с')
    stop_year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='владел по')

    def __str__(self):
        return f'{self.boat} {self.start_year}-{self.stop_year}'

    class Meta:
        verbose_name = 'история'
        verbose_name_plural = 'история'
