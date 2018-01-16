from django.urls import reverse
from django.test import TestCase, Client

from . import models, forms


class TaskTest(TestCase):
    def setUp(self):
        self.payload = {'query': 'twitter'}
        models.Task.objects.create(query='facebook')

    def test_form_valid(self):
        form = forms.TaskForm(data=self.payload)
        self.assertTrue(form.is_valid())


    def test_create_task_with_status_pending(self):
        task = models.Task.objects.create(**self.payload)
        self.assertEqual(task.status, task.PENDING)
        

    def test_method_update_to_done(self):
        task = models.Task.objects.get(query='facebook')
        task.update_to_done()
        self.assertEqual(task.status, task.DONE)



class TwitterProfileAPITest(TestCase):
    def setUp(self):
        self.url = reverse('twitter-profiles')
        self.payload = {'query': 'twitter'}
        self.client = Client()

    def create_fake_twitter_profiles(self):
        profiles = [
            {'tw_id': 100, 'name': 'Fake 1', 'popularity': 100},
            {'tw_id': 101, 'name': 'Fake 2', 'popularity': 101},
            {'tw_id': 102, 'name': 'Fake 3', 'popularity': 102},
        ]

        models.TwitterProfile.objects.bulk_create(
            [models.TwitterProfile(**profile) for profile in profiles]
        )

    def create_fake_task_done(self):
        task = models.Task.objects.create(query='fake')
        task.update_to_done()


    def test_first_request(self):
        res = self.client.post(self.url, data=self.payload)
        task = models.Task.objects.get(**self.payload)

        # Test Success call
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), {'data': 'processing request'})

        # Test Success create task
        self.assertEqual(task.query, self.payload['query'])
        self.assertEqual(task.status, task.PENDING)

    def test_second_request(self):
        self.create_fake_twitter_profiles()
        self.create_fake_task_done()
        queryset_profiles = models.TwitterProfile.custom.search('fake').values()

        res = self.client.post(self.url, data={'query': 'fake'})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), {'data': list(queryset_profiles)})