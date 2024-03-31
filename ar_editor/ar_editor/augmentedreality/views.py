
from django.shortcuts import render, redirect
from django.conf import settings
import os
from datetime import datetime, timedelta
from .models import ModelStats
from users.models import User
from .forms import EditModelForm

from augmentedreality.models import ModelStats


def upload_view(request):
    if request.user.username == '':
        return redirect('index')

    user = request.user

    if request.method == 'POST':
        if user.free_models_count > 0:
            glb_file = request.FILES.get('glb_file')

            #проверка на размер файла
            max_size = 10 * 1024 * 1024  # 10 МБ в байтах
            if glb_file.size > max_size:
                return render(request, 'augmentedreality/upload.html',
                                  {'error_message': 'Слишком большой размер файла, загрузите файл размером до 10МБ или купите подписку.'})

            project_name = request.POST.get('project_name')
            description = request.POST.get('description')

            #логика создания модели
            if glb_file and project_name:
                save_path = os.path.join('augmentedreality','static', 'projects', request.user.username, project_name)

                if os.path.exists(save_path):
                    return render(request, 'augmentedreality/upload.html',
                                  {'error_message': f'Проект с именем "{project_name}" уже существует.'})

                os.makedirs(save_path, exist_ok=True)
                file_name = 'model.glb'
                file_path = os.path.join(save_path, file_name)

                with open(file_path, 'wb') as f:
                    for chunk in glb_file.chunks():
                        f.write(chunk)

                user.free_models_count -= 1
                user.save()

                # Создаем запись в ModelStats
                display_stats = ModelStats.objects.create(
                    user=user,
                    project_name=project_name,
                    description=description,
                )

                context = {}
                context['user_name'] = request.user.username
                context['description'] = description
                context['project_name'] = project_name
                context['remaining_displays'] = display_stats.remaining_displays

                return render(request, 'augmentedreality/success.html',
                              context=context)
            else:
                # Обработка случая, если glb_file или project_name равны None
                return render(request, 'augmentedreality/upload.html',
                              {'error_message': 'Загрузите файл .glb и укажите имя проекта.'})
        else:
            return render(request, 'augmentedreality/upload.html',
                          {'error_message': 'У вас нет доступных бесплатных загрузок. Но вы можете их приобрести:',
                           'buy_models': True})

    return render(request, 'augmentedreality/upload.html')


from django.shortcuts import  get_object_or_404
from django.http import Http404
def open_place_ar(request, username, projectname):
    context = {'username': username, 'projectname': projectname}

    try:
        user = get_object_or_404(User, username=username)
        display_stats = get_object_or_404(ModelStats, user=user, project_name=projectname)
    except Http404:
        return redirect('error')

    # Проверка на наличие доступных показов
    if display_stats.remaining_displays > 0:
        # Обновление счетчиков показов
        display_stats.remaining_displays -= 1
        display_stats.displays_all_time += 1
        display_stats.displays_today += 1
        display_stats.displays_this_week += 1

        display_stats.save()

        # Ваш текущий код отображения страницы
        return render(request, 'ar_assets/place_ar.html', context=context)
    else:
        # Если доступных показов нет
        return render(request, 'augmentedreality/no_displays_available.html', context=context)


# def edit_model(request, get_project_name):
#     if request.user.username == '':
#         return redirect('index')
#
#     user = request.user  # Предполагается, что у вас есть аутентифицированный пользователь
#     now_model = ModelStats.objects.get(user=user.username, name=get_project_name)
#
#     if request.method == 'POST':
#         glb_file = request.FILES.get('glb_file')
#         project_name = request.POST.get('project_name')
#         description = request.POST.get('description')
#
#         # Найдите проект по имени пользователя и имени проекта
#
#
#         if now_model.project_name != project_name:
#
#         # Измените атрибуты проекта
#         now_model.description = description
#
#
#     else:
#         form = EditModelForm(instance=now_model)
#
#     return render(request, 'edit_project.html', {'form': form, 'project': project})