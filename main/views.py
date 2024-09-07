from django.shortcuts import render

def show_main(request):
    context = {
        'nama_aplikasi' : 'Closure Shop',
        'nama': 'Valentino Vieri ZHuo',
        'kelas': 'PBP E'
    }

    return render(request, "main.html", context)
