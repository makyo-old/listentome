from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.db.models import Q
from django.http import HttpResponse
from listentome.catalog.models import *
from listentome.catalog.forms import *
import json

def show_record(request, record_id):
    record = get_object_or_404(Record, pk = record_id)
    return render_to_response("catalog/record_show.html", context_instance = RequestContext(request, {'record': record}))

def show_performer(request, performer_id):
    performer = get_object_or_404(Performer, pk = performer_id)
    return render_to_response("catalog/show_performer.html", context_instance = RequestContext(request, {'performer': performer}))

def show_piece(request, piece_id):
    piece = get_object_or_404(Piece, pk = piece_id)
    return render_to_response("catalog/show_piece.html", context_instance = RequestContext(request, {'piece': piece}))

def show_composer(request, composer_id):
    composer = get_object_or_404(Composer, pk = composer_id)
    return render_to_response("catalog/show_composer.html", context_instance = RequestContext(request, {'composer': composer}))

def create_record(request):
    if request.user.is_authenticated() and request.user.has_perm("record.can_create"):
        form = RecordForm()
        if request.method == "GET":
            return render_to_response("catalog/edit_record.html", context_instance = RequestContext(request, {'form': form}))
        else:
            form = RecordForm(request.POST)
            if form.is_valid():
                record = form.save()
                return render_to_response("catalog/edit_record.html", context_instance = RequestContext(request, {'form': form, 'instance': record}))
            else:
                return render_to_response("catalog/edit_record.html", context_instance = RequestContext(request, {'form': form}))
    else:
        return render_to_response("403.html", context_instance = RequestContext(request))

def ajax_autocomplete(request, model):
    search_term = request.GET.get('q', '')
    search_results = dict()
    if request.is_ajax() and len(search_term) > 3:
        if model == 'performer' or model == 'any':
            search_results['performer'] = []
            for performer in Performer.objects.get(Q(name__istartswith = search_term) | Q(name__icontains = " %s" % search_term)):
                search_results['performer'].append({"text": performer.name, "url": performer.get_absolute_url()})
        if model == 'piece' or model == 'any':
            search_results['piece'] = []
            for piece in Piece.objects.get(Q(title__istartswith = search_term) | Q(name__icontaints = " %s" % search_term)):
                search_results['piece'].append({"text": piece.title, "url": piece.get_absolute_url()})
        if model == 'composer' or model == 'any':
            search_results['composer'] = []
            for composer in Composer.objects.get(Q(name__istartswith = search_term) | Q(name__icontains = " %s" % search_term)):
                search_results['composer'].append({"text": composer.name, "url": composer.get_absolute_url()})
    return HttpResponse(json.dumps(search_results), mimetype = 'text/plain')

def ajax_create_performer(request):
    to_return = False
    if request.is_ajax() and request.method == 'POST' and request.user.has_perm('performer.can_create'):
        form = PerformerForm(request.POST)
        if form.is_valid():
            form.save()
            to_return = True
    return HttpResponse(json.dumps(to_return), mimetype = 'text/plain')

def ajax_create_piece(request):
    to_return = False
    if request.is_ajax() and request.method == 'POST' and request.user.has_perm('piece.can_create'):
        form = PieceForm(request.POST)
        if form.is_valid():
            form.save()
            to_return = True
    return HttpResponse(json.dumps(to_return), mimetype = 'text/plain')

def ajax_create_movement(request):
    to_return = False
    if request.is_ajax and request.method == 'POST' and request.user.has_perm('movement.can_create'):
        form = MovementForm(request.POST)
        if form.is_valid():
            form.save()
            to_return = True
    return HttpResponse(json.dumps(to_return), mimetype = 'text/plain')

def ajax_create_component(request):
    to_return = False

def ajax_create_composer(request):
    pass
