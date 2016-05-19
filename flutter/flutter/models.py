from django.db import models


class Flutt(models.Model):
    user = models.TextField(default='elfough')
    text = models.TextField(max_length=140, default='start typing')
    date_n_time = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return 'object has(Date = {}, ID = {}, User = {}, Flutt = {})'.format(
            self.id, self.date_n_time, self.user, self.text
        )

    def __repr__(self):
        return 'flutt:({}, {}, {}, {})'.format(
            self.date_n_time, self.id, self.user, self.text
        )
