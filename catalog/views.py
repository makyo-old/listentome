from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError, Http404
from django.contrib.auth.decorators import login_required, permission_required
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

@permission_required("record.can_create")
def create_record(request):
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

@permission_required("record.can_edit")
def edit_record(request, record_id):
    record = get_object_or_404(Record, pk = record_id)
    form = RecordForm(instance = record)
    if request.method == "GET":
        return render_to_response("catalog/edit_record.html", 
                context_instance = RequestContext(request, 
                    {'form': form, 'instance': record}))
    else:
        form = RecordForm(request.POST, instance = record)
        if form.is_valid():
            record = form.save()
            return HttpResponseRedirect(record.get_absolute_url())
        else:
            return render_to_response("catalog/edit_record.html", 
                    context_instance = RequestContext(request, 
                        {'form': form, 'instance': record}))

@permission_required("performer.can_delete")
def merge_performers(request):
    if request.method == "GET" 
    and request.GET.get('performerA', None) is not None 
    and request.GET.get('performerB', None) is not None:
        performer_A = get_object_or_404(Performer, request.GET['performerA'])
        performer_B = get_object_or_404(Performer, request.GET['performerB'])
        return render_to_response("catalog/merge_performers.html", 
                context_instance = RequestContext(request, 
                    {'performer_A': performer_A, 'performer_B': performer_B}))
    elif request.method == "POST" 
    and request.POST.get('performerA', None) is not None 
    and request.POST.get('performerB', None) is not None 
    and request.POST.get('keep', None) is not None:
        keep = None
        drop = None
        if request.POST['keep'] == 'A':
            keep = get_object_or_404(Performer, request.POST['performerA'])
            drop = get_object_or_404(Performer, request.POST['performerB'])
        else:
            keep = get_object_or_404(Performer, request.POST['performerB'])
            drop = get_object_or_404(Performer, request.POST['performerA'])
        for record in drop.record_set.all():
            record.performers.remove(drop)
            record.performers.add(keep)
        drop.delete()
        return HttpResponseRedirect(keep.get_absolute_url())
    else:
        raise Http404

@permission_required("composer.can_delete")
def merge_composers(request):
    if request.method == "GET" 
    and request.GET.get('composerA', None) is not None 
    and request.GET.get('composerB', None) is not None:
        composer_A = get_object_or_404(Composer, request.GET['composerA'])
        composer_B = get_object_or_404(Composer, request.GET['composerB'])
        return render_to_response("catalog/merge_composers.html", 
                context_instance = RequestContext(request, 
                    {'composer_A': composer_A, 'composer_B': composer_B}))
    elif request.method == "POST" 
    and request.POST.get('composerA', None) is not None 
    and request.POST.get('composerB', None) is not None 
    and request.POST.get('keep', None) is not None:
        keep = None
        drop = None
        if request.POST['keep'] == 'A':
            keep = get_object_or_404(Composer, request.POST['composerA'])
            drop = get_object_or_404(Composer, request.POST['composerB'])
        else:
            keep = get_object_or_404(Composer, request.POST['composerB'])
            drop = get_object_or_404(Composer, request.POST['composerA'])
        for piece in drop.piece_set.all():
            piece.composer = keep
        drop.delete()
        return HttpResponseRedirect(keep.get_absolute_url())
    else:
        raise Http404

@permission_required("piece.can_delete")
def merge_pieces(request):
    if request.method == "GET" 
    and request.GET.get('pieceA', None) is not None 
    and request.GET.get('pieceB', None) is not None:
        piece_A = get_object_or_404(Piece, request.GET['pieceA'])
        piece_B = get_object_or_404(Piece, request.GET['pieceB'])
        return render_to_response("catalog/merge_pieces.html", 
                context_instance = RequestContext(request, 
                    {'piece_A': piece_A, 'piece_B': piece_B}))
    elif request.method == "POST" 
    and request.POST.get('pieceA', None) is not None 
    and request.POST.get('pieceB', None) is not None 
    and request.POST.get('keep', None) is not None:
        keep = None
        drop = None
        if request.POST['keep'] == 'A':
            keep = get_object_or_404(Piece, request.POST['pieceA'])
            drop = get_object_or_404(Piece, request.POST['pieceB'])
        else:
            keep = get_object_or_404(Piece, request.POST['pieceB'])
            drop = get_object_or_404(Piece, request.POST['pieceA'])
        if drop.movement_set.all().count() != keep.movement_set.all().count():
            return HttpResponseServerError()
        for drop_movement in drop.movement_set.all():
            keep_movement = keep.movement_set.get(movement_number__exact = drop_movement.movement_number)
            for component in drop_movement.component_set.all():
                component.movement = keep_movement
            drop_movement.delete()
        drop.delete()
        return HttpResponseRedirect(keep.get_absolute_url())
    else:
        raise Http404

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

@permission_required("performer.can_create")
def ajax_create_performer(request):
    to_return = False
    if request.is_ajax() and request.method == 'POST':
        form = PerformerForm(request.POST)
        if form.is_valid():
            form.save()
            to_return = True
    return HttpResponse(json.dumps(to_return), mimetype = 'text/plain')

@permission_required("composer.can_create")
def ajax_create_composer(request):
    to_return = False
    if request.is_ajax() and request.method == 'POST':
        form = ComposerForm(request.POST)
        if form.is_valid():
            form.save()
            to_return = True
    return HttpResponse(json.dumps(to_return), mimetype = 'text/plain')

@permission_required("piece.can_create")
def ajax_create_piece(request):
    to_return = False
    if request.is_ajax() and request.method == 'POST':
        form = PieceForm(request.POST)
        if form.is_valid():
            form.save()
            to_return = True
    return HttpResponse(json.dumps(to_return), mimetype = 'text/plain')

@permission_required("movement.can_create")
def ajax_create_movement(request):
    to_return = False
    if request.is_ajax and request.method == 'POST':
        form = MovementForm(request.POST)
        if form.is_valid():
            form.save()
            to_return = True
    return HttpResponse(json.dumps(to_return), mimetype = 'text/plain')

@permission_required("component.can_create")
def ajax_create_component(request):
    to_return = False
    if request.is_ajax and request.method == 'POST':
        form = ComponentForm(request.POST)
        if form.is_valid():
            form.save()
            to_return = True
    return HttpResponse(json.dumps(to_return), mimetype = 'text/plain')
