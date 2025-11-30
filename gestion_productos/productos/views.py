from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, DetalleProducto, Categoria, Etiqueta
from .forms import ProductoForm, CategoriaForm, EtiquetaForm
from django.db.models import Count, Avg


def index(request):
    return render(request, 'index.html')


def lista_productos(request):
    productos = Producto.objects.select_related('categoria').prefetch_related('etiquetas')
    return render(request, 'productos/lista.html', {
        'productos': productos
    })


def detalle_producto(request, id):
    producto = get_object_or_404(Producto.objects.select_related('categoria'), pk=id)
    # detalle puede no existir aún
    detalle = getattr(producto, 'detalle', None)
    return render(request, 'productos/detalle.html', {
        'producto': producto,
        'detalle': detalle,
    })


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()

    return render(request, 'productos/crear.html', {
        'form': form
    })


def editar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    # si ya hay detalle, precargamos datos
    detalle = getattr(producto, 'detalle', None)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        # precargar iniciales de detalle en save() ya se maneja
        if form.is_valid():
            form.save()
            return redirect('detalle_producto', id=producto.id)
    else:
        initial = {}
        if detalle:
            initial['dimensiones'] = detalle.dimensiones
            initial['peso'] = detalle.peso
        form = ProductoForm(instance=producto, initial=initial)

    return render(request, 'productos/editar.html', {
        'form': form,
        'producto': producto,
    })


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)

    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')

    return render(request, 'productos/eliminar.html', {
        'producto': producto
    })



# -----------------------------
# CRUD DE CATEGORÍAS
# -----------------------------
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/lista.html', {
        'categorias': categorias
    })


def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()

    return render(request, 'categorias/formulario.html', {
        'form': form,
        'titulo': 'Crear categoría',
    })


def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'categorias/formulario.html', {
        'form': form,
        'titulo': 'Editar categoría',
    })


def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)

    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')

    return render(request, 'categorias/eliminar.html', {
        'categoria': categoria,
    })




# -----------------------------
# CRUD DE ETIQUETAS
# -----------------------------
def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'etiquetas/lista.html', {
        'etiquetas': etiquetas
    })


def crear_etiqueta(request):
    if request.method == 'POST':
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm()

    return render(request, 'etiquetas/formulario.html', {
        'form': form,
        'titulo': 'Crear etiqueta',
    })


def editar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, pk=id)

    if request.method == 'POST':
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm(instance=etiqueta)

    return render(request, 'etiquetas/formulario.html', {
        'form': form,
        'titulo': 'Editar etiqueta',
    })


def eliminar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, pk=id)

    if request.method == 'POST':
        etiqueta.delete()
        return redirect('lista_etiquetas')

    return render(request, 'etiquetas/eliminar.html', {
        'etiqueta': etiqueta,
    })




def consultas_productos(request):
    productos_caros = Producto.objects.filter(precio__gt=100)
    productos_no_baratos = Producto.objects.exclude(precio__lt=50)
    categorias_con_conteo = Categoria.objects.annotate(num_productos=Count('productos'))
    precio_promedio = Producto.objects.all().aggregate(precio_promedio=Avg('precio'))['precio_promedio']

    sql = """
        SELECT * 
        FROM productos_producto 
        WHERE precio > 100 
        ORDER BY precio DESC
    """
    productos_raw = Producto.objects.raw(sql)


    return render(request, 'productos/consultas.html', {
        'productos_caros': productos_caros,
        'productos_no_baratos': productos_no_baratos,
        'categorias_con_conteo': categorias_con_conteo,
        'precio_promedio': precio_promedio,
    })
