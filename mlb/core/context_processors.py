from django.conf import settings


def project_metadata(request):
    return {
        'project_title': settings.MLB_PROJECT_TITLE
    }
