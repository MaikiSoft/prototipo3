from django.shortcuts import render
from inventario.models import venta
import plotly.express as px
import pandas as pd
# Create your views here.
def interfas(request):

    ventas = venta.objects.all()

    df = pd.DataFrame({"mes": [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre",
        "Enero","Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre",
        "Enero","Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre",
        "Enero","Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ],
    "cantidad": [
        280, 410, 520, 690, 580, 720,
        480, 850, 620, 710, 390, 980,
        250, 690, 580, 720, 480, 850, 
        620, 710, 390, 980, 410, 520,
        432, 789, 256, 874, 193, 367, 
        548, 920, 467, 321, 812, 699, 
        245, 578, 354, 746, 182, 913, 
        537, 421, 655, 829, 178, 324
    ],
    "barrio": [
        "Candelaria", "Galerias", "Chapinero", "Rosales",
        "Candelaria", "Galerias", "Chapinero", "Rosales",
        "Candelaria", "Galerias", "Chapinero", "Rosales", 
        "Galerias","Chapinero", "Rosales","Candelaria",
        "Galerias","Chapinero", "Rosales","Candelaria",
        "Galerias","Chapinero", "Rosales","Candelaria",
        "Chapinero", "Rosales","Candelaria", "Galerias",
        "Chapinero", "Rosales","Candelaria", "Galerias",
        "Chapinero", "Rosales","Candelaria", "Galerias",
        "Rosales","Candelaria", "Galerias", "Chapinero",
        "Rosales","Candelaria", "Galerias", "Chapinero",
        "Rosales","Candelaria", "Galerias", "Chapinero",
        
    ]}

        #"mes":["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
        #"cantidad":[567, 312, 443, 715, 280, 922, 631, 499, 821, 387, 690, 245],
        #"barrio":["Candelaria", "Chapinero","San Francisco", "Rosales","Cabrera"]
    )
    suma_por_mes = df.groupby("mes")["cantidad"].sum().reset_index()
    grafico = px.bar(df,x = "mes", y ="cantidad", color = "barrio", title="Ventas mensuales")
    for i, row in suma_por_mes.iterrows():
        grafico.add_annotation(x=row["mes"], y=row["cantidad"]+ 70, text=str(row["cantidad"]), showarrow=False)
    mihtml = grafico.to_html(full_html=False)


    context = {
        "ventas":ventas,
        "grafica":mihtml
    }
    return render(request,"inventario/index.html", context)