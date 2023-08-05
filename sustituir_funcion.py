import re

def sustituir(p): #función que sustituye algunas palabras de un párrafo con otras
    nuevo_p = p
    
    #testigos
    nuevo_p = re.sub(r"[Tt]estigos",'tipos que conozco',nuevo_p)      
    nuevo_p = re.sub(r"[Uu]n testigo|[Tt]estigo ",'uno que conozco ',nuevo_p)      
    
    #estudio
    nuevo_p = re.sub(r"[Ee]studio científico|[Ee]studio ",'post de tumblr ',nuevo_p)   

    #investigadores
    nuevo_p = re.sub(r"[Ll]os [Ii]nvestigadores|[Ii]nvestigador[es]|[Ii]nvestigador ",'mi tía Claudia ',nuevo_p)   

    #científicos
    nuevo_p = re.sub(r"[Ll]os científicos|[Cc]ientíficos",'Nik gaturro',nuevo_p)   

    #elecciones
    nuevo_p = re.sub(r"[Ll]as elecciones|[Ee]lecciones",'la competencia nacional de discapacitados',nuevo_p)   

    #candidato
    nuevo_p = re.sub(r"[Cc]andidato ",'malabarista ',nuevo_p) 
    nuevo_p = re.sub(r"[Cc]andidatos",'malabarista',nuevo_p)    

    #jugador
    nuevo_p = re.sub(r"[Jj]ugador ",'tarotista ',nuevo_p)   
    nuevo_p = re.sub(r"[Jj]ugadores",'tarotistas',nuevo_p)   

    #encuesta
    nuevo_p = re.sub(r"[Ee]ncuestas",'tiradas de cartas',nuevo_p)   
    nuevo_p = re.sub(r"[Ee]ncuesta ",'tirada de cartas ',nuevo_p)   

    #fútbol
    nuevo_p = re.sub(r"[Ff]útbol",'cricket',nuevo_p)   

    #gobernador
    nuevo_p = re.sub(r"[Gg]obernador ",'emperador ',nuevo_p)   

    #polémica
    nuevo_p = re.sub(r"[Pp]olémica ",'partida de tejo ',nuevo_p)
    nuevo_p = re.sub(r"[Pp]olémicas",'partidas de tejo',nuevo_p)

    #conductor
    nuevo_p = re.sub(r"[Cc]onductor ",'jugador profesional de League of Legends ',nuevo_p)
    nuevo_p = re.sub(r"[Cc]onductores",'jugadores profesionales de League of Legends',nuevo_p)   

    #condenado
    nuevo_p = re.sub(r"[Cc]ondenado ",'cordialmente invitado ',nuevo_p)   
    nuevo_p = re.sub(r"[Cc]ondenada ",'cordialmente invitada ',nuevo_p)   

    #libertadores
    nuevo_p = re.sub(r"[Ll]ibertadores",'campeonato internacional de ruleta (va mi abuela)',nuevo_p) 

    #calentamiento global
    nuevo_p = re.sub(r"[Cc]alentamiento global",'calorcito global',nuevo_p) 

    #temperaturas
    nuevo_p = re.sub(r"[Tt]emperaturas",'formas geométricas',nuevo_p)
    nuevo_p = re.sub(r"[Tt]emperatura ",'forma geométrica ',nuevo_p)

    #prisión 
    nuevo_p = re.sub(r"[Pp]risión",'ver gran hermano',nuevo_p) 

    #PASO
    nuevo_p = re.sub(r"PASO",'SAPO',nuevo_p)   

    #partido
    nuevo_p = re.sub(r" [Pp]artido ",' server de discord ',nuevo_p)
    nuevo_p = re.sub(r" [Pp]artidos",'servers de discord',nuevo_p)

    #detuvieron
    nuevo_p = re.sub(r"[Dd]etuvieron",'dieron un besito',nuevo_p)

    #detenido
    nuevo_p = re.sub(r"[Dd]etenido ",'célebre y ejemplar ciudadano ',nuevo_p)
    nuevo_p = re.sub(r"[Dd]etenidos",'célebres y ejemplares ciudadanos',nuevo_p)

    #sospechoso
    nuevo_p = re.sub(r"[Ss]ospechoso ",'presidente ',nuevo_p)
    nuevo_p = re.sub(r"[Ss]ospechosos",'ejecutivos',nuevo_p)

    #debate
    nuevo_p = re.sub(r"[Dd]ebate ",'competencia de zumba ',nuevo_p)
    nuevo_p = re.sub(r"[Ll]os debates|[Dd]ebates",'las competencias de zumba',nuevo_p)

    #experto/s
    nuevo_p = re.sub(r"[Ee]xpertos",'curadores del empacho',nuevo_p)
    nuevo_p = re.sub(r"[Ee]xperto ",'curador del empacho ',nuevo_p)

    #precios
    nuevo_p = re.sub(r"[Pp]recios",'animes',nuevo_p)

    #economía
    nuevo_p = re.sub(r"[Ee]conomía ",'trama del anime que estoy viendo ',nuevo_p)

    #ciencia
    nuevo_p = re.sub(r" [Cc]iencia ",' astrología ',nuevo_p)

    #millones/miles de pesos/dólares
    nuevo_p = re.sub(r"[Mm]illones de pesos|[Mm]illones de dólares|[Mm]iles de pesos|[Mm]iles de dólares",'50 (cincuenta) pesos',nuevo_p)

    #medicinal
    nuevo_p = re.sub(r"[Mm]edicinal ",'astral ',nuevo_p)

    #mitos y verdades
    nuevo_p = re.sub(r"[Mm]itos y verdades",'lo primero que se me viene a la cabeza',nuevo_p)

    #duro
    nuevo_p = re.sub(r"[Dd]uro ",'rico ',nuevo_p)

    #actor
    nuevo_p = re.sub(r" [Aa]ctor ",' duendólogo libanés ',nuevo_p)

    #cantante
    nuevo_p = re.sub(r"[Cc]antante ",'mod de reddit ',nuevo_p)
    nuevo_p = re.sub(r"[Cc]antantes",'mods de reddit',nuevo_p)

    #netflix
    nuevo_p = re.sub(r"[Nn]etflix",'Taringa',nuevo_p)

    #serie
    nuevo_p = re.sub(r"[Ss]erie ",'dibujito chino ',nuevo_p)
    nuevo_p = re.sub(r"[Ss]eries",'dibujitos chinos',nuevo_p)

    #película
    nuevo_p = re.sub(r"[Pp]elícula ",'ova de Code Geass ',nuevo_p)
    nuevo_p = re.sub(r"[Pp]elículas",'ovas de Code Geass',nuevo_p)

    #Alberto Fernández
    nuevo_p = re.sub(r"Alberto Fernández",'Taylor Swift',nuevo_p)

    #Larreta
    nuevo_p = re.sub(r"Horacio Larreta|Larreta",'El Pelado',nuevo_p)

    #deportista
    nuevo_p = re.sub(r"[Dd]eportista ",'repartidor de Rappi ',nuevo_p)
    nuevo_p = re.sub(r"[Dd]eportistas",'repartidores de Rappi',nuevo_p)

    #votos
    nuevo_p = re.sub(r"[Vv]otos",'ojotas en un balde',nuevo_p)
    nuevo_p = re.sub(r"[Vv]oto ",'ojota en un balde',nuevo_p)

    #IA
    nuevo_p = re.sub(r"[Ii]nteligencia artificial|IA",'comadreja',nuevo_p)

    #tecnología
    nuevo_p = re.sub(r"[Tt]ecnología ",'obra de Nik Gaturro ',nuevo_p)
    nuevo_p = re.sub(r"[Tt]ecnologías",'obras de Nik Gaturro',nuevo_p)

    #Mauricio Macri
    nuevo_p = re.sub(r"Mauricio Macri",'Tini Stoessel',nuevo_p)

    #gol/goles/golear

    #plantel

    #boca
    nuevo_p = re.sub(r"Boca Juniors|Boca",'colectivo de actrices argentinas',nuevo_p)
    
    #river
    nuevo_p = re.sub(r"River Plate|River",'asociación colombófila profesional',nuevo_p)

    #tucumán
    nuevo_p = re.sub(r"[Tt]ucumano ",'tucumono',nuevo_p)
    nuevo_p = re.sub(r"Tucumán",'micumán',nuevo_p)

    #club

    #crimen
    #nuevo_p = re.sub(r"[Cc]rimen ",'travesura',nuevo_p)

    #criminal
    nuevo_p = re.sub(r"[Cc]riminal ",'distinguido CEO',nuevo_p)

    #prófugo

    #iphone
    nuevo_p = re.sub(r"Iphone ",'Blackberry 8520',nuevo_p)

    #monotributista

    #masterchef
    nuevo_p = re.sub(r"[Mm]asterchef",'Cocinando con Dross',nuevo_p)

    #argentina

    #dólar
    nuevo_p = re.sub(r"[Dd]ólar ",'Baht tailandés',nuevo_p)
    nuevo_p = re.sub(r"[Dd]ólares",'Bahts tailandeses',nuevo_p)

    #propuesta/s
    nuevo_p = re.sub(r"[Pp]ropuesta ",'lectura de borra',nuevo_p)
    nuevo_p = re.sub(r"[Pp]ropuestas",'lecturas de borra',nuevo_p)

    #televisión
    #nuevo_p = re.sub(r"[Tt]elevisión",'',nuevo_p)
    
    #film

    #cine

    #libro

    #porteño

    #barrio

    #desarrolladores

    #vecinos

    #empleo

    #campeón

    #celular
    nuevo_p = re.sub(r"[Cc]elular",'máquina de fax',nuevo_p)

    #redes

    #internet

    #PRO

    #campaña

    #estados unidos
    nuevo_p = re.sub(r"Estados Unidos|EEUU",'Tiroteos Unidos',nuevo_p)

    #apple

    #coronavirus
    #nuevo_p = re.sub(r"[Cc]oronavirus",'',nuevo_p)

    #libro/s

    #padrón
    #nuevo_p = re.sub(r"[Pp]adrón",'',nuevo_p)

    #plataforma

    #amazon

    #instagram
    nuevo_p = re.sub(r"Instagram ",'Fotolog',nuevo_p)

    #spotify
    nuevo_p = re.sub(r"Spotify",'Ares',nuevo_p)

    #tendencia

    #furor

    #usuarios


    return(nuevo_p) 

