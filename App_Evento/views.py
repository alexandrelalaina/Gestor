from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, UpdateView

from App_Evento.models import Evento
from apps.caract.models import CaractRel
from apps.util.models import CgRefCodes


def home(request):
    return HttpResponse('Ola => views.py home')


def home2(request):
    return HttpResponse('Ola 222222 => views.py home')


class EventoKanbanList(ListView):
    # model = Evento
    template_name = 'App_Evento/EventoKanbanList.html'

    def get(self, request):
        # p_param_id = self.id
        # print('--VIEWS.PY GET - fazendo RawQuery')
        # TODO: ver se consigo fazer sem ser rawquery
        w_lista = Evento.objects.raw('select e.id, e.descricao as evento_descr, e.dt_evento, car.id as fluxo_id, car.valor as fluxo_valor, cg.rv_meaning as fluxo_descr ' +
                                     'from evento e ' +
                                     '   , caract_rel car ' +
                                     '   , cg_ref_codes cg ' +
                                     'where car.fk_evento_id = e.id ' +
                                     '  and car.valor = cg.rv_low_value ' +
                                     '  and car.fk_caract_tipo_id = 1 ' +  # Fluxo Fotografia
                                     '  and car.valor <> 10 ' + # Entregue
                                     '  and cg.rv_domain = %s '
                                     ' order by car.valor, e.dt_evento'
                                     , ['EVENTO.FLUXO'])
        # for reg in w_lista:
        #     return reg.rv_meaning
        return render(request, 'App_Evento/EventoKanbanList.html', {'data_view': w_lista})


        # def getQtLanctos(self):
        # fk_caract_tipo = 1 = Fluxo de Eventos (Fotografia)
        # data = CaractRel.objects.filter(fk_caract_tipo_id=1)
        # for reg in data:
            # data['cg_ref_codes_valor']
            # w_aux_valor = data['valor']
            # x = CgRefCodes.objects.filter(rv_domain='EVENTO.FLUXO').filter(valor=float(1))
            # data['cg_ref_codes_descr'] = x
            # print('loop valor encontrado: ' + str(x))
        # eventos = Evento.objects.all()
        # return render(request, 'App_Evento/EventoKanbanList.html', {'data_view': data})


class EventoKanbanUpdate(UpdateView):
    model = CaractRel
    fields = {'id', 'fk_evento_id', 'valor', 'valor_alfa', 'data'}

    # def form_valid(self, form):
    #     CaractRel = form.save(commit=False)
    #     CaractRel.save()
    #     return super(EventoKanbanUpdate, self).form_valid(form)