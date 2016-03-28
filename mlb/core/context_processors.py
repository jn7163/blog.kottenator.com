from django.conf import settings


def project_metadata(request):
    return {
        'project_title': settings.PROJECT_TITLE
    }
