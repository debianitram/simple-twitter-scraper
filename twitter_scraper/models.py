from django.db import models
from django.db.models.signals import post_save

from . import tasks


### Define Querysets
class TwitterProfileQuerySet(models.QuerySet):
    def search(self, query):
        return self.filter(name__icontains=query)



class TaskQuerySet(models.QuerySet):
    def search(self, query):
        return self.filter(query__icontains=query)

    def pending(self):
        return self.filter(status='PD')

    def done(self):
        return self.filter(status='DN')



### Define Models
class TwitterProfile(models.Model):
    class Meta:
        ordering = ('popularity', 'name')

    tw_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    popularity = models.PositiveIntegerField(blank=True, default=0)

    objects = models.Manager()
    custom = TwitterProfileQuerySet.as_manager()

    __str__ = lambda self: self.name


    def update_(self, tw_user):
        update_fields = []
        if self.name != tw_user.name:
            self.name = tw_user.name
            update_fields.append('name')

        if self.description != tw_user.description:
            self.description = tw_user.description
            update_fields.append('description')

        if self.image != tw_user.profile_image_url:
            self.image = tw_user.profile_image_url
            update_fields.append('image')

        if self.popularity != tw_user.followers_count:
            self.popularity = tw_user.followers_count
            update_fields.append('popularity')

        if update_fields:
            self.save(update_fields=update_fields)



class Task(models.Model):
    class Meta:
        ordering = ('query', )

    PENDING = 'PD'
    DONE = 'DN'

    STATUS = (
        (PENDING, 'Pending'),
        (DONE, 'Done')
    )

    query = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS, default=PENDING)

    objects = models.Manager()
    custom = TaskQuerySet.as_manager()


    def __str__(self):
        return "%s -> Status: %s" % (self.query, self.get_status_display())

    def update_to_done(self):
        if self.status is not self.DONE:
            self.status = self.DONE
            self.save()

    @staticmethod
    def run(**kwargs):
        if kwargs.get('created', False) or 'from_view' in kwargs:
            tasks.twitter_scraper.delay(kwargs['instance'].id)



# Signals
post_save.connect(Task.run, Task)