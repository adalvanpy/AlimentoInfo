from django.db import models

class Alimento(models.Model):
    idAlimento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    kcal = models.DecimalField(max_digits=5, decimal_places=2)
    carboidratos = models.DecimalField(max_digits=5, decimal_places=2)
    proteinas = models.DecimalField(max_digits=5, decimal_places=2)
    gordurasTotais = models.DecimalField(max_digits=5, decimal_places=2)
    gorduraSaturada = models.DecimalField(max_digits=5, decimal_places=2)
    Ig = models.DecimalField(max_digits=5, decimal_places=2)
    cg = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade_gramas = models.DecimalField(max_digits=5, decimal_places=2)
    fibras = models.DecimalField(max_digits=5, decimal_places=2)

    

    class Meta:
        db_table = 'alimento'
        managed = False   
