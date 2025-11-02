from django.shortcuts import render, redirect, get_object_or_404
from .models import Entry
from django.contrib.auth.decorators import login_required

@login_required
def entry_list(request):
    if request.method == 'POST':
        # 处理保存想做和完成状态
        for key, value in request.POST.items():
            if key.startswith('todo_'):
                entry_id = key.split('_')[1]
                entry = get_object_or_404(Entry, id=entry_id, user=request.user)
                entry.想做 = value
                entry.想做完成 = f'done_{entry_id}' in request.POST
                entry.save()
        return redirect('entry_list')

    # 未完成“想做”顶部
    todos_incomplete = Entry.objects.filter(user=request.user, 想做__isnull=False).exclude(想做='').filter(想做完成=False).order_by('-date')
    # 已完成“想做”下方
    todos_complete = Entry.objects.filter(user=request.user, 想做__isnull=False).exclude(想做='').filter(想做完成=True).order_by('-date')
    # 日记列表（所有日记）
    entries = Entry.objects.filter(user=request.user).order_by('-date')

    return render(request, 'entries/entry_list.html', {
        'todos_incomplete': todos_incomplete,
        'todos_complete': todos_complete,
        'entries': entries
    })

@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id, user=request.user)
    entry.delete()
    return redirect('entry_list')

@login_required
def edit_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id, user=request.user)
    if request.method == 'POST':
        entry.想做 = request.POST.get('想做', '')
        entry.所得 = request.POST.get('所得', '')
        entry.更好 = request.POST.get('更好', '')
        entry.生理 = request.POST.get('生理', '')
        entry.情绪 = request.POST.get('情绪', '')
        if 'image' in request.FILES:
            entry.image = request.FILES['image']
        if 'audio' in request.FILES:
            entry.audio = request.FILES['audio']
        entry.save()
        return redirect('entry_list')
    return render(request, 'entries/edit_entry.html', {'entry': entry})
def add_entry(request):
    if request.method == 'POST':
        Entry.objects.create(
            user=request.user,
            想做=request.POST.get('想做', ''),
            所得=request.POST.get('所得', ''),
            更好=request.POST.get('更好', ''),
            生理=request.POST.get('生理', ''),
            情绪=request.POST.get('情绪', ''),
            image=request.FILES.get('image'),
            audio=request.FILES.get('audio'),
        )
        return redirect('entry_list')
    return render(request, 'entries/add_entry.html')