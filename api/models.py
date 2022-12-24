from django.db import models

# Create your models here.
class Category(models.Model):
    description = models.CharField(
        max_length=100, 
        help_text="Descripcion de la categoria",
        unique=True
        )
    def __str__(self):
        return '{}'.format(self.description)
    
    class Meta:
        verbose_name_plural: "Categorias"

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(
        max_length=100,
        help_text='Descripción de la subcategoría'
    )
    
    def __str__(self):
        return '{}:{}'.format(self.category.description, self.description)
    
    class Meta:
        verbose_name_plural = "Sub Categorías"
        unique_together = ("category", "description")
        
class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    description = models.CharField(
        max_length=100,
        help_text="Descripción del Producto",
        unique=True
    )
    fecha_creado = models.DateTimeField()
    vendido = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.description)
    
    class Meta:
        verbose_name_plural = "Productos"
        
