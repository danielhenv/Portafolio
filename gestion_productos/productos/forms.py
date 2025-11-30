from django import forms
from .models import Producto, DetalleProducto
from .models import Categoria, Etiqueta

class ProductoForm(forms.ModelForm):
    dimensiones = forms.CharField(
        max_length=100,
        required=False,
        label="Dimensiones",
        help_text="Ej: 10x20x5 cm",
    )
    peso = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        required=False,
        label="Peso (kg)",
    )

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'etiquetas']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

    def save(self, commit=True):
        # Guardamos el producto
        producto = super().save(commit=commit)

        # Creamos o actualizamos el detalle
        dimensiones = self.cleaned_data.get('dimensiones')
        peso = self.cleaned_data.get('peso')

        from .models import DetalleProducto

        detalle, creado = DetalleProducto.objects.get_or_create(producto=producto)
        detalle.dimensiones = dimensiones
        detalle.peso = peso
        if commit:
            detalle.save()

        return producto
    

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']


class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = ['nombre']
