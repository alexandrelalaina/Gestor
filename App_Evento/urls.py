from django.urls import path
from .views import home, home2, EventoKanbanList, EventoKanbanUpdate

urlpatterns = [
    path('', home),
    # path('Evento_Kanban_List', home2),
    path('Evento_Kanban_List', EventoKanbanList.as_view()),
    path('Evento_Kanban_Update/<int:pk>/', EventoKanbanUpdate.as_view(), name='EventoKanbanUpdate'),
]
