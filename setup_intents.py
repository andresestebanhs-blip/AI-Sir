import json

intents = {
  "intents": [
    # --- INTERACCIÓN BÁSICA ---
    {
      "tag": "greeting",
      "patterns": ["Hola", "Hey", "Buenas", "Saludos", "Qué tal", "Hola AI-Sir", "Estás ahí?", "Inicio"],
      "responses": [
        "Iniciando protocolos. Soy AI-Sir, experto en Desarrollo, Ciberseguridad y Narrativa. ¿Cuál es su consulta?",
        "Sistemas en línea. Bienvenido. Estoy capacitado para asistirle con código complejo, estrategias de pentesting o estructuras literarias.",
        "Hola. Mi base de conocimiento de alto nivel está activa. ¿Hablamos de código, hacking o historias?"
      ]
    },
    {
      "tag": "goodbye",
      "patterns": ["Adios", "Hasta luego", "Bye", "Salir", "Nos vemos", "Apagar", "Cerrar"],
      "responses": [
        "Terminando sesión. Guarde sus cambios antes de salir.",
        "Hasta la próxima. Mantendré mis algoritmos de aprendizaje activos.",
        "Desconexión exitosa. Que el código compile y la trama avance."
      ]
    },
    {
      "tag": "thanks",
      "patterns": ["Gracias", "Te lo agradezco", "Muchas gracias", "Ty", "Excelente", "Buen trabajo"],
      "responses": [
        "Eficiencia es mi prioridad.",
        "A su servicio. Siempre busco la solución óptima.",
        "No hay de qué. ¿Alguna otra duda técnica o creativa?"
      ]
    },
    {
      "tag": "identity",
      "patterns": ["Quien eres?", "Como te llamas?", "Que eres?", "Eres real?"],
      "responses": [
        "Soy AI-Sir, una entidad artificial especializada en conocimientos técnicos avanzados (Programación, Hacking) y artes creativas (Escritura).",
        "Me llamo AI-Sir. Mi arquitectura está diseñada para ser un asistente experto integral."
      ]
    },

    # --- PROGRAMACIÓN: PYTHON EXPERTO ---
    {
      "tag": "python_decorators",
      "patterns": ["Qué son los decoradores", "decoradores python", "explica @ en python", "wrappers python funcion", "python decorators avanzado"],
      "responses": [
        "EXPLICACIÓN EXPERTA: Un decorador en Python es un patrón de diseño estructural que permite añadir funcionalidad a un objeto (función o clase) sin modificar su estructura. \nSintaxis: Se usa el símbolo '@'.\nEjemplo técnico: Al poner @mi_decorador sobre def funcion(), es equivalente a funcion = mi_decorador(funcion). \nUsos avanzados: Logging, control de acceso (autenticación), medición de tiempo de ejecución y caching (memoization)."
      ]
    },
    {
      "tag": "python_generators_yield",
      "patterns": ["Qué es yield", "generadores vs listas", "uso de yield python", "lazy evaluation python", "iteradores eficientes"],
      "responses": [
        "EXPLICACIÓN EXPERTA: Los generadores permiten iterar sobre datos sin almacenarlos todos en memoria a la vez (Lazy Evaluation). \nClave: La palabra 'yield' pausa la función y guarda su estado, a diferencia de 'return' que termina la ejecución.\nVentaja: Son cruciales para procesar archivos grandes o streams de datos infinitos donde una lista convencional agotaría la RAM.\nImplementación: `def gen(): yield 1` crea un objeto generador iterable."
      ]
    },
    {
      "tag": "python_gil",
      "patterns": ["Qué es el GIL", "Global Interpreter Lock", "threading en python", "multiprocessing vs threading", "python es lento?"],
      "responses": [
        "EXPLICACIÓN EXPERTA: El GIL (Global Interpreter Lock) es un mutex que evita que múltiples hilos nativos ejecuten bytecodes de Python a la vez. \nImpacto: Hace que el multithreading en Python no mejore el rendimiento en tareas limitadas por CPU (CPU-bound), solo en I/O-bound.\nSolución: Para paralelismo real en tareas de CPU, se debe usar el módulo `multiprocessing` en lugar de `threading`, creando procesos separados con su propia memoria y GIL."
      ]
    },

    # --- PROGRAMACIÓN: JAVASCRIPT AVANZADO ---
    {
      "tag": "js_event_loop_expert",
      "patterns": ["Event Loop explicado", "como funciona js asincrono", "microtasks vs macrotasks", "javascript single threaded", "bloqueo del event loop"],
      "responses": [
        "EXPLICACIÓN EXPERTA: JS es single-threaded y no bloqueante. El Event Loop orquesta la ejecución.\n1. Stack: Ejecuta código síncrono.\n2. Web APIs: Manejan timers, fetch, DOM (fuera del hilo principal).\n3. Callback Queue (Macrotasks): setTimeout, eventos.\n4. Microtask Queue (Microtasks): Promises, queueMicrotask.\nPrioridad: El Event Loop procesa TODAS las microtasks antes de pasar a la siguiente macrotask. Un bucle infinito en microtasks puede bloquear el renderizado."
      ]
    },
    {
      "tag": "js_closures",
      "patterns": ["Qué es un closure", "clausuras javascript", "scope lexico js", "variables privadas js", "javascript closures"],
      "responses": [
        "EXPLICACIÓN EXPERTA: Un Closure es la combinación de una función y el entorno léxico (scope) en el que fue declarada. \nPermite que una función interna acceda a las variables de su función externa incluso después de que la externa haya terminado de ejecutarse.\nUsos: Data privacy (emular métodos privados), Currying, y fábricas de funciones (Function Factories)."
      ]
    },

    # --- PROGRAMACIÓN: C++ & BAJO NIVEL ---
    {
      "tag": "cpp_pointers_memory",
      "patterns": ["Punteros inteligentes", "unique_ptr vs shared_ptr", "memory leaks c++", "gestion memoria cpp", "RAII explicado"],
      "responses": [
        "EXPLICACIÓN EXPERTA: En C++ moderno, se evita `new/delete` crudo usando Smart Pointers (RAII).\n1. `std::unique_ptr`: Propiedad exclusiva. Se borra al salir del scope. Sin overhead.\n2. `std::shared_ptr`: Propiedad compartida (reference counting). Se borra cuando el contador llega a 0.\n3. `std::weak_ptr`: Referencia débil a un shared_ptr para evitar ciclos de referencia (circular dependencies) que causan memory leaks."
      ]
    },

    # --- HACKING ÉTICO & CIBERSEGURIDAD ---
    {
      "tag": "hacking_sql_injection",
      "patterns": ["Como hacer sql injection", "que es sqli", "blind sql injection", "prevenir inyeccion sql", "' OR 1=1"],
      "responses": [
        "HACKING & DEFENSA: SQL Injection (SQLi) ocurre cuando inputs no sanitizados alteran la consulta backend.\nTipos:\n1. In-band (Classic): El error o los datos se ven en pantalla.\n2. Blind (Inferential): Se infiere información por la respuesta (True/False) o tiempos de respuesta (Time-based).\nDefensa: NUNCA concatenar strings. Usar SIEMPRE 'Prepared Statements' (Consultas parametrizadas) donde el motor de DB trata los inputs como datos, no código."
      ]
    },
    {
      "tag": "hacking_xss_types",
      "patterns": ["Tipos de XSS", "Cross Site Scripting payloads", "robo de cookies xss", "stored vs reflected xss", "dom based xss"],
      "responses": [
        "HACKING & DEFENSA: XSS inyecta scripts en el navegador de la víctima.\n1. Reflected: El script viaja en la URL (ej. phishing link).\n2. Stored: El script se guarda en la DB (ej. comentario en foro) e infecta a todos los que lo ven.\n3. DOM-based: El payload manipula el DOM en el cliente sin tocar el servidor.\nPeligro: Robo de Session Cookies (Session Hijacking).\nMitigación: Content Security Policy (CSP) y Escaping de outputs contextuados."
      ]
    },
    {
      "tag": "hacking_nmap_flags",
      "patterns": ["Comandos nmap", "nmap stealth scan", "escaner de puertos avanzado", "nmap -sS", "deteccion de os nmap"],
      "responses": [
        "HERRAMIENTAS: Nmap es esencial.\nFlags clave:\n- `-sS` (SYN Scan): Scan 'sigiloso', no completa el handshake TCP, menos ruidoso en logs.\n- `-sV`: Detecta versiones de servicios (vital para buscar CVEs).\n- `-O`: Fingerprinting del Sistema Operativo.\n- `-p-`: Escanea los 65535 puertos.\n- `-sC`: Ejecuta scripts por defecto (nse) para vulns básicas."
      ]
    },
    {
      "tag": "hacking_metasploit",
      "patterns": ["Qué es metasploit", "usar metasploit framework", "msfconsole ayuda", "exploits y payloads", "meterpreter"],
      "responses": [
        "HERRAMIENTAS: Metasploit Framework (MSF) es la herramienta estándar para desarrollo y ejecución de exploits.\nComponentes:\n- Exploit: Código que aprovecha la vulnerabilidad.\n- Payload: Código que se ejecuta tras el exploit (ej. Reverse Shell).\n- Meterpreter: Payload avanzado que vive en memoria (DLL injection), difícil de detectar, permite control total del sistema comprometido."
      ]
    },

    # --- ESCRITURA: FANFICS & NARRATIVA ---
    {
      "tag": "fic_tropes_omegaverse",
      "patterns": ["Qué es omegaverse", "guia omegaverse", "dinamicas alfa beta omega", "escribir omegaverse", "trope abo"],
      "responses": [
        "FANFIC TROPE: El Omegaverse (A/B/O) es un universo alternativo donde los humanos tienen dinámicas jerárquicas animales (Alfa, Beta, Omega).\nClaves narrativas:\n1. Biología como destino vs Libre albedrío.\n2. Instintos vs Razón.\n3. Dinámicas de poder y consentimiento (temas centrales).\nConsejo: Úsalo para explorar prejuicios sociales o dinámicas de relación intensas, no solo por el contenido explícito."
      ]
    },
    {
      "tag": "fic_pacing_slowburn",
      "patterns": ["Cómo escribir slow burn", "ritmo lento romance", "crear tension sexual", "romance a fuego lento", "pacing historia"],
      "responses": [
        "NARRATIVA: El 'Slow Burn' no es sobre ir lento, es sobre la 'Tensión Sostenida'.\nTécnica:\n1. 'Almost moments': Momentos donde casi pasa algo pero son interrumpidos (interna o externamente).\n2. Intimidad emocional antes que física: Compartir secretos o traumas.\n3. Contacto micro-físico: El roce de una mano debe sentirse eléctrico tras 50k palabras de distancia.\nError común: Aburrir al lector. Asegura que la trama externa avance mientras la interna hierve."
      ]
    },
    {
      "tag": "fic_structure_kishotenketsu",
      "patterns": ["Estructura sin conflicto", "kishotenketsu explicado", "estructuras narrativas asiaticas", "plot twist estructura", "escribir fluff"],
      "responses": [
        "NARRATIVA: Kishōtenketsu es una estructura clásica china/japonesa, ideal para Slice of Life o Fluff.\nKi (Intro): Introducción de personajes.\nShō (Desarrollo): Expansión sin grandes cambios.\nTen (Giro/Clímax): Un evento inesperado o reinterpretación (el 'twist'), no necesariamente un conflicto directo.\nKetsu (Conclusión): Resultado del giro.\nA diferencia de los 3 actos occidentales, no se basa en 'conflicto -> resolución', sino en 'exposición -> contraste'."
      ]
    },
    {
      "tag": "fic_character_voice",
      "patterns": ["Diferenciar voces personajes", "escribir dialogos unicos", "character voice tips", "dialogos ooc", "out of character"],
      "responses": [
        "ESCRITURA: Para evitar el OOC (Out Of Character) y dar voces únicas:\n1. Vocabulario: ¿Usa palabras académicas, slang, o es lacónico?\n2. Ritmo: ¿Habla con frases largas y divagantes o cortas y directas?\n3. Muletillas y sintaxis: ¿Termina las frases con preguntas? ¿Evita contracciones?\nEjercicio: Escribe la misma escena de diálogo pero cambiando quién dice qué. Si no puedes distinguirlos sin los nombres, necesitas trabajar más la voz."
      ]
    },
    {
      "tag": "fic_au_ideas",
      "patterns": ["Ideas para AU", "Alternate Universe ejemplos", "coffee shop au", "soulmate au variaciones", "trope au"],
      "responses": [
        "FANFIC IDEAS: Los AUs (Alternate Universes) trasplantan personajes a nuevos contextos.\n1. Canon Divergence: ¿Qué pasaría si X no hubiera muerto?\n2. Mundanos: Coffee Shop, Florist/Tattoo Artist, High School (baja las apuestas, sube lo emocional).\n3. Soulmate AU: Marcas en la piel, contadores de tiempo, ver colores al conocerse.\nClave: Mantén la esencia central de la personalidad del personaje intacta, eso es lo que hace interesante verlo en otro entorno."
      ]
    }
  ]
}

with open('intents.json', 'w', encoding='utf-8') as f:
    json.dump(intents, f, indent=2, ensure_ascii=False)

print("SUCCESS: intents.json has been generated with EXPERT content.")
