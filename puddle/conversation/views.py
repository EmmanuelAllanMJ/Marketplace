from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Conversation, ConversationMessage
from .forms import NewConversationMessageForm

# Create your views here.
@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')

    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation:details', conversation_pk=conversations.first().id)   
    
    if request.method == 'POST':
        form = NewConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:details', pk=item_pk)
    else:
        form = NewConversationMessageForm()
    
    return render(request, 'conversation/new.html', {
        'form': form,
        'item': item
    })

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })

@login_required
def details(request, conversation_pk):
    conversation = get_object_or_404(Conversation, pk=conversation_pk)

    if request.user not in conversation.members.all():
        return redirect('dashboard:index')

    if request.method == 'POST':
        form = NewConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('conversation:details', conversation_pk=conversation_pk)
    else:
        form = NewConversationMessageForm()
    
    return render(request, 'conversation/details.html', {
        'conversation': conversation,
        'form': form
    }
)