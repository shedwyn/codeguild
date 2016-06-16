from django.shortcuts import render

from . import logic


def render_index(request):
    tasks = logic.get_all_tasks()
    items = logic.get_all_items()
    items_by_task = logic.get_all_items_for_task(task)

    template_args = {
        'tasks': tasks,
        'items': items,
        'items_by_task': item_by_task,
    }
    return render(request, 'todo/index.html', template_args)
