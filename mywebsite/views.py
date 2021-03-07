from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse


class index(TemplateView):
    template_name="index.html"


def offline(request):
    return render(request, '../templates/offline.html')


class ServiceWorkerView(TemplateView):
    template_name = '../templates/sw.js'
    content_type = 'application/javascript'

    def get_context_data(self, **kwargs):
        return {
            'manifest_url': static('manifest.json'),
            'icon_url': static('icons/djangopwa512x512.png'),
            'style_url': static('css/style.css'),
            'offline_url': reverse('offline'),
        }
