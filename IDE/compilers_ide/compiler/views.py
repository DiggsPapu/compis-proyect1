from django.shortcuts import render
from django.http import JsonResponse

def ide_home(request):
    return render(request, 'compiler/ide_home.html')

def compile_code(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        # Aquí llamas a tus scripts de Python/ANTLR para compilar el código
        # y devuelves el resultado
        result = run_compiler(code)
        return JsonResponse({'result': result})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def run_compiler(code):
    # Implementar la lógica de compilación utilizando ANTLR y tus scripts
    # Puedes llamar a tus scripts de Python aquí
    return "Compilación exitosa"
