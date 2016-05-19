from . import models

def create_and_save_new_task(task_name):
    new_task = models.Task(task_name=task_name)
    new_task.save()

def create_and_save_new_item(item_name, task):
    new_ie = models.Item(
        item_name = item_name,
        task = task,
        )
    new_ie.save()


def get_all_tasks():
    return models.Task.objects.all()


def get_all_items():
    return models.Item.objects.all()


def get_all_items_for_task(task):
    return models.Item.objects.filter(task=task)
