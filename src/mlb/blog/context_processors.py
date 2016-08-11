from django.conf import settings


def project_metadata(request):
    return {
        'project_metadata': {
            'title': settings.PROJECT_TITLE
        }
    }
