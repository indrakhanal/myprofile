from django.urls import path
from .views import home as x1
from .views import project as x2
from .views import gallery as x3
from .views import contact as x4
from .views import send_message as x5
from .views import complete_project as x6
from .views import videos as x7
# from .views import GeneratePDF as x7


urlpatterns = [
    path('', x1, name='home'),
    path('project', x2, name='project'),
    path('gallery', x3, name='gallery'),
    path('contact', x4, name='contact'),
    path('message', x5, name='message'),
    path('project_detail', x6, name='project_detail'),
    path('video', x7, name='video'),
    # path('bio_data', x7.as_view(), name='bio_data'),
]
