from django.db import models


class Flutt(models.Model):
    user = models.TextField()
    text = models.TextField(max_length=140)
    date_n_time = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return '{}: [({}), ({}), ({})]'.format(
            self.id, self.date_n_time, self.user, self.text
        )

    def __repr__(self):
        return '(Date Stamp = {}, Unique ID = {}, User Name = {}, Flutt = {})'.format(
            self.date_n_time, self.id, self.user, self.text
        )
