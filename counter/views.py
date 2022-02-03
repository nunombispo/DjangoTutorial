from django.shortcuts import render
from .models import Counter


def counter(request):
    counter_value = Counter.objects.last()

    if counter_value is None:
        counter_value = Counter(count=0)
        counter_value.save()

    if request.method == 'POST':
        counter_value.count += 1
        counter_value.save()

    return render(request, 'counter.html', {'counter': counter_value.count})
