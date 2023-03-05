from pomegranate import *


Antecedentes = Node(DiscreteDistribution({
    "Ratero": 0.06,
    "Asesino": 0.001,
    "Neutro": 0.939
}), name="Antecedentes")


# Relación con el muerto
Relacion = Node(DiscreteDistribution({
    "Madre": 0.08,	
    "Padre": 0.08,	 
    "Hijo": 0.1,	
    "Hermano": 0.08,	
    "Amigo": 0.16,	
    "Abuelo": 0.08,	
    "Nieto": 0.14,	
    "Pareja": 0.04,	
    "Ninguna": 0.24
}), name="Relacion")


Consumo = Node(DiscreteDistribution({
    "Alcohol": 0.04,	
    "Droga": 0.01 ,
    "Normal": 0.95
}), name="Consumo")


# Benecios obtenidos del muerto, ya sea gracias a su muerte o en vida

Beneficios = Node(ConditionalProbabilityTable([
    ["Madre","Sostenimiento",0.2],
    ["Madre","Herencia",0.25],
    ["Madre","Sostenimiento y Herencia",0.15],
    ["Madre","Nada",0.4],

    ["Padre","Sostenimiento",0.2],
    ["Padre","Herencia",0.25],
    ["Padre","Sostenimiento y Herencia", 0.15],
    ["Padre","Nada", 0.4],

    ["Hijo","Sostenimiento",0.3],
    ["Hijo","Herencia",0.1],
    ["Hijo","Sostenimiento y Herencia",0.45],
    ["Hijo","Nada",0.15],

    ["Hermano","Sostenimiento",0.2],
    ["Hermano","Herencia",0.1],
    ["Hermano","Sostenimiento y Herencia",0.05],
    ["Hermano","Nada",0.65],

    ["Amigo","Sostenimiento",0.08],
    ["Amigo","Herencia",0.03],
    ["Amigo","Sostenimiento y Herencia",0.02],
    ["Amigo","Nada",0.87],

    ["Abuelo","Sostenimiento",0.14],
    ["Abuelo","Herencia",0.06],
    ["Abuelo","Sostenimiento y Herencia",0.04],
    ["Abuelo","Nada",0.76],

    ["Nieto","Sostenimiento",0.05],
    ["Nieto","Herencia",0.3],
    ["Nieto","Sostenimiento y Herencia",0.15],
    ["Nieto","Nada",0.5],

    ["Pareja","Sostenimiento",0.2],
    ["Pareja","Herencia",0.3],
    ["Pareja","Sostenimiento y Herencia",0.4],
    ["Pareja","Nada",0.1],

    ["Ninguna","Sostenimiento",0.02],
    ["Ninguna","Herencia",0.015],
    ["Ninguna","Sostenimiento y Herencia",0.005],
    ["Ninguna","Nada",0.96]

],[Relacion.distribution]), name="Beneficios")

#Emociones hacia el muerto

Emociones = Node(ConditionalProbabilityTable([
    ["Madre","Odio",0.1],
    ["Madre","Amor",0.75],
    ["Madre","Celos",0.01],
    ["Madre","Ninguno",0.14],

    ["Padre","Odio",0.1],
    ["Padre","Amor",0.75],
    ["Padre","Celos", 0.01],
    ["Padre","Ninguno", 0.14],

    ["Hijo","Odio",0.25],
    ["Hijo","Amor",0.6],
    ["Hijo","Celos",0.01],
    ["Hijo","Ninguno",0.14],

    ["Hermano","Odio",0.15],
    ["Hermano","Amor",0.5],
    ["Hermano","Celos",0.2],
    ["Hermano","Ninguno",0.15],

    ["Amigo","Odio",0.15],
    ["Amigo","Amor",0.35],
    ["Amigo","Celos",0.25],
    ["Amigo","Ninguno",0.25],

    ["Abuelo","Odio",0.1],
    ["Abuelo","Amor",0.55],
    ["Abuelo","Celos",0.03],
    ["Abuelo","Ninguno",0.32],

    ["Nieto","Odio",0.25],
    ["Nieto","Amor",0.6],
    ["Nieto","Celos",0.01],
    ["Nieto","Ninguno",0.14],

    ["Pareja","Odio",0.03],
    ["Pareja","Amor",0.65],
    ["Pareja","Celos",0.3],
    ["Pareja","Ninguno",0.02],

    ["Ninguna","Odio",0.1],
    ["Ninguna","Amor",0.1],
    ["Ninguna","Celos",0.2],
    ["Ninguna","Ninguno",0.6]

],[Relacion.distribution]), name="Emociones")

# Tiene motivos para matarlo?

Motivo = Node(ConditionalProbabilityTable([
    ["Ratero"  ,"Odio"  ,  "Sostenimiento", "Si",0.5175],
    ["Ratero"  ,"Odio"  ,  "Sostenimiento", "No",0.4825],
    ["Ratero"  ,"Odio"  ,  "Herencia", "Si",0.83375],
    ["Ratero"  ,"Odio"  ,  "Herencia", "No",0.16625],
    ["Ratero"  ,"Odio"  ,  "Sostenimiento y Herencia", "Si",0.71875],
    ["Ratero"  ,"Odio"  ,  "Sostenimiento y Herencia", "No",0.28125],
    ["Ratero"  ,"Odio"  ,  "Nada", "Si",0.618125],
    ["Ratero"  ,"Odio"  ,  "Nada", "No",0.381875],
    ["Asesino" ,"Odio"  ,  "Sostenimiento", "Si",0.585],
    ["Asesino" ,"Odio"  ,  "Sostenimiento", "No",0.415],
    ["Asesino" ,"Odio"  ,  "Herencia", "Si",0.9425],
    ["Asesino" ,"Odio"  ,  "Herencia", "No",0.0575],
    ["Asesino" ,"Odio"  ,  "Sostenimiento y Herencia", "Si",0.8125],
    ["Asesino" ,"Odio"  ,  "Sostenimiento y Herencia", "No",0.1875],
    ["Asesino" ,"Odio"  ,  "Nada", "Si",0.69875],
    ["Asesino" ,"Odio"  ,  "Nada", "No",0.30125],
    ["Neutro"  ,"Odio"  ,  "Sostenimiento", "Si",0.4275],
    ["Neutro"  ,"Odio"  ,  "Sostenimiento", "No",0.5725],
    ["Neutro"  ,"Odio"  ,  "Herencia", "Si",0.68875],
    ["Neutro"  ,"Odio"  ,  "Herencia", "No",0.31125],
    ["Neutro"  ,"Odio"  ,  "Sostenimiento y Herencia", "Si",0.59375],
    ["Neutro"  ,"Odio"  ,  "Sostenimiento y Herencia", "No",0.40625],
    ["Neutro"  ,"Odio"  ,  "Nada", "Si",0.510625],
    ["Neutro"  ,"Odio"  ,  "Nada", "No",0.489375],

    ["Ratero"  ,"Amor"  ,  "Sostenimiento", "Si",0.0828],
    ["Ratero"  ,"Amor"  ,  "Sostenimiento", "No",0.9172],
    ["Ratero"  ,"Amor"  ,  "Herencia", "Si",0.1334],
    ["Ratero"  ,"Amor"  ,  "Herencia", "No",0.8666],
    ["Ratero"  ,"Amor"  ,  "Sostenimiento y Herencia", "Si",0.115],
    ["Ratero"  ,"Amor"  ,  "Sostenimiento y Herencia", "No",0.885],
    ["Ratero"  ,"Amor"  ,  "Nada", "Si",0.0989],
    ["Ratero"  ,"Amor"  ,  "Nada", "No",0.9011],
    ["Asesino" ,"Amor"  ,  "Sostenimiento", "Si",0.0936],
    ["Asesino" ,"Amor"  ,  "Sostenimiento","No",0.9064],
    ["Asesino" ,"Amor"  ,  "Herencia", "Si",0.1508],
    ["Asesino" ,"Amor"  ,  "Herencia", "No",0.8492],
    ["Asesino" ,"Amor"  ,  "Sostenimiento y Herencia", "Si",0.13],
    ["Asesino" ,"Amor"  ,  "Sostenimiento y Herencia", "No",0.87],
    ["Asesino" ,"Amor"  ,  "Nada", "Si",0.1118],
    ["Asesino" ,"Amor"  ,  "Nada", "No",0.8882],
    ["Neutro"  ,"Amor"  ,  "Sostenimiento", "Si",0.0684],
    ["Neutro"  ,"Amor"  ,  "Sostenimiento", "No",0.9316],
    ["Neutro"  ,"Amor"  ,  "Herencia", "Si",0.1102],
    ["Neutro"  ,"Amor"  ,  "Herencia", "No",0.8898],
    ["Neutro"  ,"Amor"  ,  "Sostenimiento y Herencia", "Si",0.095],
    ["Neutro"  ,"Amor"  ,  "Sostenimiento y Herencia", "No",0.905],
    ["Neutro"  ,"Amor"  ,  "Nada", "Si",0.0817],
    ["Neutro"  ,"Amor"  ,  "Nada", "No",0.9183],

    ["Ratero"  ,"Celos" ,	 "Sostenimiento", "Si",0.5382],
    ["Ratero"  ,"Celos" ,	 "Sostenimiento", "No",0.4618],
    ["Ratero"  ,"Celos" ,	 "Herencia", "Si",0.8671],
    ["Ratero"  ,"Celos" ,	 "Herencia", "No",0.1329],
    ["Ratero"  ,"Celos" ,	 "Sostenimiento y Herencia", "Si",0.7475],
    ["Ratero"  ,"Celos" ,	 "Sostenimiento y Herencia", "No",0.2525],
    ["Ratero"  ,"Celos" ,	 "Nada", "Si",0.64285],
    ["Ratero"  ,"Celos" ,	 "Nada", "No",0.35715],
    ["Asesino" ,"Celos" ,  "Sostenimiento", "Si",0.6084],
    ["Asesino" ,"Celos" ,  "Sostenimiento", "No",0.3916],
    ["Asesino" ,"Celos" , "Herencia", "Si",0.9802],
    ["Asesino" ,"Celos" , "Herencia", "No",0.0198],  
    ["Asesino" ,"Celos" ,  "Sostenimiento y Herencia", "Si",0.845],
    ["Asesino" ,"Celos" ,  "Sostenimiento y Herencia", "No",0.155],
    ["Asesino" ,"Celos" ,  "Nada", "Si",0.7267],
    ["Asesino" ,"Celos" ,  "Nada", "No",0.2733],
    ["Neutro"  ,"Celos" , "Sostenimiento", "Si",0.4446],
    ["Neutro"  ,"Celos" , "Sostenimiento", "No",0.5554],
    ["Neutro"  ,"Celos" ,  "Herencia", "Si",0.7163],
    ["Neutro"  ,"Celos" ,  "Herencia", "No",0.2837],
    ["Neutro"  ,"Celos" ,  "Sostenimiento y Herencia", "Si",0.6175],
    ["Neutro"  ,"Celos" ,  "Sostenimiento y Herencia", "No",0.3825],
    ["Neutro"  ,"Celos" ,  "Nada", "Si",0.53105],
    ["Neutro"  ,"Celos" ,  "Nada", "No",0.46895],

    ["Ratero"  ,"Ninguno", "Sostenimiento", "Si",0.284625],
    ["Ratero"  ,"Ninguno", "Sostenimiento", "No",0.715375],
    ["Ratero"  ,"Ninguno", "Herencia", "Si",0.4585625],
    ["Ratero"  ,"Ninguno", "Herencia", "No",0.5414375],
    ["Ratero"  ,"Ninguno", "Sostenimiento y Herencia", "Si",0.3953125],
    ["Ratero"  ,"Ninguno", "Sostenimiento y Herencia", "No",0.6046875],
    ["Ratero"  ,"Ninguno", "Nada", "Si",0.33996875],
    ["Ratero"  ,"Ninguno", "Nada", "No",0.66003125],
    ["Asesino" ,"Ninguno", "Sostenimiento", "Si",0.32175],
    ["Asesino" ,"Ninguno", "Sostenimiento", "No",0.67825],
    ["Asesino" ,"Ninguno", "Herencia", "Si",0.518375],
    ["Asesino" ,"Ninguno", "Herencia", "No",0.481625],
    ["Asesino" ,"Ninguno", "Sostenimiento y Herencia", "Si",0.446875],
    ["Asesino" ,"Ninguno", "Sostenimiento y Herencia", "No",0.553125],
    ["Asesino" ,"Ninguno", "Nada", "Si",0.3843125],
    ["Asesino" ,"Ninguno", "Nada", "No",0.6156875],
    ["Neutro"  ,"Ninguno", "Sostenimiento", "Si",0.235125],
    ["Neutro"  ,"Ninguno", "Sostenimiento", "No",0.764875],
    ["Neutro"  ,"Ninguno", "Herencia", "Si",0.3788125],
    ["Neutro"  ,"Ninguno", "Herencia", "No",0.6211875],
    ["Neutro"  ,"Ninguno", "Sostenimiento y Herencia", "Si",0.3265625],
    ["Neutro"  ,"Ninguno", "Sostenimiento y Herencia", "No",0.6734375],
    ["Neutro"  ,"Ninguno", "Nada", "Si",0.28084375],
    ["Neutro"  ,"Ninguno", "Nada", "No",0.71915625]


],[Antecedentes.distribution, Emociones.distribution, Beneficios.distribution]), name="Motivo")

Asesino = Node(ConditionalProbabilityTable([

    ["Si" ,	"Alcohol", "Culpable", 0.9],
    ["Si" ,	"Alcohol", "Inocente",0.1],
    ["Si" ,	"Droga", "Culpable", 0.95],
    ["Si" ,	"Droga", "Inocente", 0.05],
    ["Si" ,	"Normal", "Culpable", 0.8],
    ["Si" ,	"Normal", "Inocente",0.2],
    ["No" ,	"Alcohol", "Culpable", 0.2],
    ["No" ,	"Alcohol", "Inocente",0.8],
    ["No" ,	"Droga", "Culpable", 0.35],
    ["No" ,	"Droga", "Inocente", 0.65],
    ["No"	, "Normal", "Culpable", 0.05],
    ["No"	, "Normal", "Inocente", 0.95]

],[Motivo.distribution, Consumo.distribution]), name="Asesino")


# Creamos una Red Bayesiana y añadimos estados
modelo = BayesianNetwork()
#modelo.add_states(Antecedentes, Relacion, Consumo, Beneficios, Emociones, Motivo, Asesino)
modelo.add_states(Antecedentes, Relacion, Consumo, Beneficios,Emociones, Motivo, Asesino)

# Añadimos bordes que conecten nodos
modelo.add_edge(Relacion, Emociones)
modelo.add_edge(Relacion, Beneficios)
modelo.add_edge(Antecedentes, Motivo)
modelo.add_edge(Emociones, Motivo)
modelo.add_edge(Beneficios, Motivo)
modelo.add_edge(Motivo, Asesino)
modelo.add_edge(Consumo, Asesino)

#Modelo Final
modelo.bake()
