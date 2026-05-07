from django.shortcuts import render


def main_page(request):
    data = {
        'title': 'Главная страница',
    }

    return render(request, 'images/main_page.html', data)


def db_model(request):
    data = {
        'title': 'Модель базы данных',
        'inf': 'База данных была описана следующим образом',
    }

    return render(request, 'images/db_model.html', data)


def not_found(request):
    return render(request, 'images/not_found.html')


def success_add(request):
    return render(request, 'images/success_add.html')
