from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Dish


def main(request):
    categories = Category.objects.all()
    dishes = Dish.objects.all()

    for item in categories:
        for dish in item:
            print(dish)

    res1 = f"Categories - {'; '.join(map(str, categories))}"
    res2 = f"Dishes - {'; '.join(map(str, dishes))}"
    return HttpResponse(
        res1 + '    ///     ' + res2
    )
