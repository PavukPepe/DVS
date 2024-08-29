from django.shortcuts import render
from .models import CarBrand, CarModel, CarGeneration, Engine
from .models import Engine

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import OrderEngine

def index(request):
    engines = Engine.objects.all()  # Начинаем с получения всех двигателей
    brands = CarBrand.objects.all()  # Получаем все марки
    models = CarModel.objects.all()  # Получаем все модели
    generations = CarGeneration.objects.all()  # Получаем все поколения
    if request.method == 'GET':



        selected_brand_id = request.GET.get('brand')
        selected_model_id = request.GET.get('model')
        selected_generation_id = request.GET.get('generation')
        selected_conditions = request.GET.getlist('condition')
        name = request.GET.get('name')

        if selected_brand_id:
            models = CarModel.objects.filter(brand_id=selected_brand_id)

            if selected_model_id:
                # Если выбранная модель, фильтруем двигатели по выбранной модели
                engines = Engine.objects.filter(generations__model_id=selected_model_id).distinct()
            else:
                # Если модель не выбрана, выводим все двигатели, связанные с моделями выбранной марки
                engines = Engine.objects.filter(generations__model__brand_id=selected_brand_id).distinct()

        if selected_model_id:
            generations = CarGeneration.objects.filter(model_id=selected_model_id)
            engines = Engine.objects.filter(generations__model_id=selected_model_id).distinct()
        else:
            # Если модель не выбрана, выводим все двигатели, связанные с моделями выбранной марки
            if selected_brand_id:
                engines = Engine.objects.filter(generations__model__brand_id=selected_brand_id).distinct()

        # Если выбрано поколение, фильтруем двигатели по выбранному поколению
        if selected_generation_id:
            engines = engines.filter(generations=selected_generation_id).distinct()


        if selected_conditions:
            print(selected_conditions)
            engines = engines.filter(condition__in=selected_conditions)

        if name:
            engines = engines.filter(name__icontains=name)
        context = {
            'engines': engines,
            'brands': brands,
            'models': models,
            'generations': generations,
            'selected_brand_id': selected_brand_id,
            'selected_model_id': selected_model_id,
            'selected_generation_id': selected_generation_id,
            'selected_conditions': selected_conditions,
        }
    if request.method == "POST":
        context = {
            'engines': engines,
            'brands': brands,
            'models': models,
            'generations': generations}
        print("EEEEEEEEEEEEEE")
        phone = request.POST.get('phone')
        engine = request.POST.get('engine')
        # Создание экземпляра Order и сохранение в базе данных
        new_order = OrderEngine(engine=engine, phone=phone)
        new_order.save()
        # Возвращаем ответ о успешном создании заказа
        return render(request, 'index.html', context=context)

    # Передаем найденные двигатели в шаблон
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html')

def servises(request):
    return render(request, 'servises.html')