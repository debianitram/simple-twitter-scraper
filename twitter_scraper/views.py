from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from . import forms
from .models import TwitterProfile, Task


@csrf_exempt
def twitter_profile_api(req):
    if req.method != 'POST':
        return JsonResponse({'data': 'Method %s not allowed' % req.method}, status=405)
    
    form = forms.TaskForm(req.POST)
    
    if form.is_valid():
        tasks = Task.custom.search(form.data['query'])

        if not tasks.exists():
            form.save()
            return JsonResponse({'data': 'processing request'}, status=200)
        
        else:
            if tasks.done().exists():
                # Update followers_count, short_description, name.
                # [Task.run(instance=task, form_view=True) for task in tasks.done()]
                Task.run(instance=tasks.first(), from_view=True)

            else:
                return JsonResponse({'data': 'processing request'}, status=200)


        profiles = TwitterProfile.custom.search(tasks.first().query).values()
        return JsonResponse({'data': list(profiles)}, status=200, safe=False)

    else:
        return JsonResponse(form.errors)




            