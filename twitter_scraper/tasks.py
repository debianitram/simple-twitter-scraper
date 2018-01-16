from celery import shared_task

from . import models
from .utils import api_twitter


@shared_task
def twitter_scraper(task_id):
    task = models.Task.objects.get(id=task_id)
    users = api_twitter.GetUsersSearch(task.query, include_entities=True)

    for user in users:
        profile, created = models.TwitterProfile.objects.get_or_create(
            tw_id=user.id,
        )

        profile.update_(user)

    task.update_to_done()