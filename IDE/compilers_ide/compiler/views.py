import json
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import os

def ide_home(request):
    return render(request, 'compiler/ide_home.html')

@csrf_exempt
def compile_code(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            code = data.get('code', '')

            # Llamar a la función run_compiler con el código del usuario
            result = run_compiler(code)

            return JsonResponse({'result': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def run_compiler(code):
    try:
        # Subir dos niveles desde 'IDE/compilers_ide/compiler/views.py' para llegar a la raíz del proyecto
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        driver_path = os.path.join(project_root, 'compiler', 'Driver.py')

        # Imprimir la ruta para verificar
        print(f"Ruta al archivo Driver.py: {driver_path}")

        process = subprocess.Popen(
            ['python', driver_path],  # Usar la ruta completa al archivo Driver.py
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        # Pasar el código como entrada estándar al proceso
        stdout, stderr = process.communicate(input=code)

        if process.returncode != 0:
            return f"Error al ejecutar el compilador: {stderr}"

        return stdout  # Devuelve la salida del compilador
    except Exception as e:
        return str(e)
