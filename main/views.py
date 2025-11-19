from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ItemForm
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_http_methods
import requests
from django.utils.html import strip_tags
import json
# from main.forms import CarForm

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    
    if filter_type == "all":
        item_list = Item.objects.all()
    else:
        item_list = Item.objects.filter(user=request.user)

    context = {
        'npm': '2406439091',
        'name': request.user.username,
        'class': 'PBP D',
        'item_list': item_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'form': ItemForm(),
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        item_entry = form.save(commit=False)
        item_entry.user = request.user
        item_entry.save()

        # Tambahan untuk handle AJAX
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'status': 'success',
                'message': 'Item created successfully!'
            })
        
        return redirect('main:show_main')

    # Kalau form invalid dan request AJAX
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'error',
            'errors': form.errors
        }, status=400)

    context = {
        'form': form
    }
    return render(request, "create_item.html", context)

@login_required(login_url='/login')
def show_item(request, id):
    item = get_object_or_404(Item, pk=id)

    context = {
        'item': item
    }

    return render(request, "item_detail.html", context)

def show_xml(request):
     item_list = Item.objects.all()
     xml_data = serializers.serialize("xml", item_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    item_list = Item.objects.all()
    data = [
        {
            'id': str(item.id),
            'name': item.name,
            'price': item.price,
            'price_formatted': f"{item.price:,}".replace(",", "."),
            'description': item.description,
            'category': item.category,
            'thumbnail': item.thumbnail,
            'is_featured': item.is_featured,
            'user_id': item.user_id,
        }
        for item in item_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, item_id):
   try:
       item_item = Item.objects.filter(pk=item_id)
       xml_data = serializers.serialize("xml", item_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Item.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, item_id):
    try:
        # ambil item berdasarkan primary key (UUID)
        item = Item.objects.select_related('user').get(pk=item_id)
        data = {
            'id': str(item.id),
            'name': item.name,
            'price': item.price,
            'description': item.description,
            'thumbnail': item.thumbnail,
            'category': item.category,
            'is_featured': item.is_featured,
            'user_id': item.user_id,
            'user_username': item.user.username if item.user_id else None,
        }
        return JsonResponse(data)
    except Item.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Balas sukses kalau request-nya AJAX
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        else:
            # Kirim error JSON kalau AJAX
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = JsonResponse({
                'success': True,
                'redirect_url': reverse('main:show_main')
            })
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            # Kalau invalid, kirim JSON error
            return JsonResponse({
                'success': False,
                'error': 'Invalid username or password.'
            }, status=400)
    
    # Kalau GET, render halaman biasa
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login') + '?logged_out=1')
    response.delete_cookie('last_login')
    return response

def edit_item(request, id):
    item = get_object_or_404(Item, pk=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == 'POST':
        form.save()

        # 🔹 Kalau request datang dari AJAX
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'status': 'success',
                'message': 'Item updated successfully!'
            })
        
        # 🔹 Kalau bukan AJAX (fallback normal)
        return redirect('main:show_main')

    # 🔹 Kalau form invalid (tapi AJAX)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'error',
            'errors': form.errors
        }, status=400)

    context = {'form': form}
    return render(request, "edit_item.html", context)

@csrf_exempt
@require_http_methods(["POST","GET"])
def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == 'POST':
        item.delete()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success'})
        return HttpResponseRedirect(reverse('main:show_main'))
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'error', 'detail': 'Invalid method'}, status=405)
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_item_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # handling checkbox

    # kalau user belum login, biarkan kosong (karena kamu hapus login_required)
    user = request.user if request.user.is_authenticated else None

    # buat item baru
    new_item = Item(
        user=user,
        name=name,
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
    )
    new_item.save()

    return HttpResponse(b"CREATED", status=201)

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    
@csrf_exempt
def create_item_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = strip_tags(data.get("name", ""))
        description = strip_tags(data.get("description", ""))
        category = data.get("category", "")
        thumbnail = data.get("thumbnail", "")
        is_featured = data.get("is_featured", False)
        price = data.get("price", 0)
        user = request.user

        new_item = Item(
            name=name,
            description=description,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            price=price,
            user=user,
        )
        new_item.save()

        return JsonResponse({"status": "success"}, status=200)
    return JsonResponse({"status": "error"}, status=401)