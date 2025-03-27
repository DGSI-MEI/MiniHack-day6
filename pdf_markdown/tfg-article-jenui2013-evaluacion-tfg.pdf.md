Evaluación del Trabajo de Fin de Grado Fermín Sánchez, Joan Climent, Julita
Corbalán, Pau Fonseca, Jordi García, Josep-Ramon Herrero, Xavier Llinàs,
Horacio Rodriguez y Maria-Ribera Sancho Facultat d’Informàtica de Barcelona.
Universitat Politècnica de Catalunya, UPC-Barcelona Tech Barcelona fermin @
ac.upc.edu, juan.climent @ upc.edu, juli @ ac.upc.edu, pau @ fib.upc.edu.
jordig @ ac.upc.edu, josepr @ ac.upc.edu, xavier.llinas @ ac.upc.edu, horacio
@ lsi,upc.edu, ribera @ essi.upc.edu Resumen Los Proyectos de Fin de Carrera
(PFC) se han eva- luado tradicionalmente a partir de una memoria y de una
presentación pública. Esta evaluación, en general, la realiza un tribunal
formado por varios profesores, que juzga de forma integral el proyecto a
partir de la documentación entregada y de su presentación públi- ca. Para
poner la nota final los centros no disponen, en general, de unos criterios
claros y precisos, por lo que cada tribunal usa su propia experiencia previa
para decidir la nota de cada proyecto. Los Trabajos de Fin de Grado (TFG)
substituyen en los nuevos planes de estudios de las ingenierías a los antiguos
PFC. La evaluación de los TFG debe consi- derar, de forma explícita, tanto las
competencias específicas como las genéricas, y es necesario que existan
criterios claros sobre la forma de evaluarlas. Para avanzar en este sentido,
el Ministerio de Ciencia e Innovación y la Agencia para la Calidad del Sistema
Universitario de Catalunya financiaron en 2008 y 2009 el proyecto “Guía para
la evaluación de compe- tencias en los Trabajos de Fin de Grado y de Máster en
las Ingenierías”. Esta guía es, en realidad, una guía para ayudar a que cada
centro/titulación defina su propio procedimiento de evaluación del TFG. En
este trabajo se presenta una implementación de las propuestas contenidas en la
guía y se define una metodología para evaluar los TFG a partir de las
competencias que se trabajan en la titulación de Grado en Ingeniería
Informática de la Facultat d’Informàtica de Barcelona. La metodología puede
ser fácilmente replicada o adaptada para otros centros y otras titulaciones,
lo que puede facilitar la realiza- ción de su propia guía de evaluación de los
TFG. Abstract Final Degree Projects (FDP) have traditionally been evaluated
from a project report and a public presenta- tion. This assessment is
generally performed by a panel of several teachers who judg comprehensively
the project from the documentation provided and analyze the public
presentation. In general, schools do not have clear and precise criteria to
set the final grade, as each panel uses its own previous experience to decide
the mark of each project. The Bachelor Degree Thesis (BDT) replaced the former
FDP in the new engineering curricula. Evalua- tion of FDP should consider
explicitly both specific and professional skills, and clear criteria on how to
assess competencies is required. To advance in this issue, the Ministry of
Science and Innovation and the Quality Agency for the University System in
Catalo- nia funded in 2008 and 2009 the project "Guía para la evaluación de
competencias en los Trabajos de Fin de Grado y de Master en las Ingenierías".
This guide is actually a guide to help each school / degree to define its own
procedure for assessing the BDT. This paper presents an implementation of the
sugges- tions contained in the guide and defines a methodol- ogy for assessing
the BDT considering the profes- sional skills trained in the Computer
Engineering Degree from the Barcelona School of Informatics. The methodology
can be easily replicated or adapted for other centres and degrees, which can
facilitate the realization of its own guidance for the BDT evalua- tion.
Palabras clave Trabajos de Fin de Grado, evaluación de TFG, eva- luación de
competencias genéricas, Proyectos de Fin de Carrera 1\. Introducción En curso
2012-2013 han comenzado a presentarse los primeros Trabajos de Fin de Grado
(TFG) en las titulaciones españolas de Grado. Los TFG deben ser evaluados de
forma diferente a como hasta ahora se han evaluado los Proyectos de Fin de
Carrera (PFC). Actas de las XIX Jenui. Castellón, 10-12 de julio 2013 ISBN:
978-84-695-8051-6 DOI: 10.6035/e-TIiT.2013.13 Páginas: 303-310 303 La
evaluación de los PFC considera de forma conjun- ta competencias específicas y
genéricas. Por ejemplo, la expresión oral y escrita se evalúa en todos los
proyectos, aunque generalmente no de forma explíci- ta ni siguiendo unos
criterios unificados. En general, los PFC son evaluados por un tribunal
formado por varios profesores, entre los cuales puede estar inclui- do el
director. La evaluación se realiza a partir de un informe y de una
presentación pública del proyecto. El informe y el trabajo del proyectista han
sido nor- malmente supervisados por el director del proyecto, y el tribunal
evalúa generalmente la calidad técnica del proyecto, la calidad del informe
escrito y la calidad de la presentación oral. Generalmente, estos tres
aspectos son evaluados de forma conjunta y dan lugar a una nota única, que es
la nota final del PFC. La mayoría de los centros no ofrece a sus estudian- tes
documentación que detalle lo que se espera del informe de un proyecto, de su
presentación o del propio contenido técnico. Estos aspectos quedan
generalmente supeditados a la experiencia y dedica- ción del director del
proyecto, que tiene la misión de formar a sus proyectistas en sus carencias a
la hora de realizar el PFC. Este hecho conduce a que, en la mayoría de casos,
la nota del proyecto no dependa sólo de la calidad del proyecto en sí, sino
también del tribunal que lo evalúa y de la experiencia del director. Distintos
tribunales podrían poner notas diferentes al mismo proyecto, ya que los
criterios de evaluación no están explícitamente definidos. En los TFG, por el
contrario, las competencias de- ben evaluarse de forma explícita, tanto las
específicas como las genéricas. En lugar de una única nota final, como en el
caso de los PFC, la calificación del TFG debería generarse a partir de un
conjunto de notas de las diferentes competencias trabajadas. Para resolver los
problemas de arbitrariedad detectados en la eva- luación de PFCs, deben
establecerse criterios claros que permitan evaluar cada una de las
competencias, de forma que exista una trazabilidad. Además, la publicación de
estos criterios servirá para guiar al estudiante sobre cómo realizar y
documentar su TFG. Con este propósito, entre 2008 y 2009 el Ministerio de
Ciencia e Innovación y la Agencia para la Calidad del Sistema Universitario de
Catalunya financiaron el proyecto “Guía para la evaluación de competencias en
los Trabajos de Fin de Grado y de Máster en las Ingenierías” [1,4]. Esta guía
es, en realidad, una guía para ayudar a que cada centro/titulación defina su
propio procedimiento de evaluación del TFG. El siguiente apartado describe
brevemente las ideas principales de la guía. 2\. La guía de evaluación de TFGs
Tal como se explica en [4], la guía establece un procedimiento de diseño en
seis etapas de la guía de evaluación del TFG en la titulación: 1\. Definir las
competencias asociadas al TFG y los indicadores objetivos de cada competencia
2\. Definir los hitos de evaluación, las acciones concretas de evaluación que
deben realizarse en cada hito y los agentes que llevarán a cabo di- chas
acciones. Se definen tres posibles hitos: • Hito inicial, con dos acciones de
evaluación: un informe escrito y una presentación oral, • Hito de seguimiento,
con una única acción de evaluación de un informe de progreso, • Hito final,
con dos acciones de evaluación: el in- forme del proyecto y su presentación
pública. 3\. Asignar indicadores objetivos a cada una de las acciones de
evaluación. 4\. Definir una rúbrica para cada indicador, estable- ciendo de
forma clara y objetiva los criterios de evaluación del indicador. 5\. Definir
los informes que deberán cumplimentar los agentes evaluadores. 6\. Definir el
criterio para asignar la nota final al TFG a partir de los informes de
evaluación. La Figura 1 (extraída de [4]) presenta gráficamente el
procedimiento descrito. Para definir la guía de evaluación del TFG de la
Facultat d’Informàtica de Barcelona (FIB), se nombró una comisión
multidisciplinar formada por los autores del presente trabajo. Los miembros de
la comisión se reunieron periódicamente entre febrero y julio de Definición
de competencias Definición de indicadores HITOS Y ACCIONES DE EVALUACIÓN
INICIAL Informe inicial Exposición SEGUIMIENTO Informe de progreso FINAL
Memoria Defensa Asignación de indicadores a las acciones de evaluación
Definición de niveles de cumplimiento Elaboración de los informes de
evaluación para cada hito Elaboración del informe de evaluación acumulativo,
por competencias CALIFICACIÓN Figura 1: Procedimiento propuesto en la guía
para definir el proceso de evaluación del TFG. 304 XIX Jornadas sobre la
Enseñanza Universitaria de la Informática 2011 y debatieron las distintas
etapas del proceso de definición de la guía, tomando decisiones sobre todos
aquellos aspectos que la guía deja abiertos. Desde julio de 2011 hasta julio
de 2012, la FIB ha seguido trabajando en la implementación de las recomenda-
ciones de la comisión. Las decisiones tomadas, que han dado lugar al
reglamento de evaluación del TFG de la FIB, se detallan en los siguientes
apartados. 3\. Marco de referencia El plan de estudios de la FIB contempla las
cinco especialidades del Real Decreto 1393/2007 [3] (Com- putación, Ingeniería
de Computadores, Ingeniería del Software, Sistemas de Información y
Tecnologías de la Información). Los estudiantes trabajan y son eva- luados de
nueve competencias genéricas: • Actitud emprendedora e innovación •
Sostenibilidad y compromiso social • Lengua extranjera • Comunicación eficaz
oral y escrita • Trabajo en equipo • Uso apropiado de los recursos de
información • Aprendizaje autónomo • Actitud adecuada frente al trabajo •
Razonamiento Se decidió que todas las competencias deben ser evaluadas en el
TFG, a excepción de la lengua extran- jera y trabajo en equipo (los TFG son
individuales en la FIB, salvo excepciones). La lengua extranjera se evalúa de
forma opcional y a petición del estudiante, ya que en nuestra universidad (la
UPC) los estudian- tes deben demostrar durante sus estudios de Grado que
poseen un nivel B2.2 o superior (en el caso del inglés). Si no lo han
acreditado con los mecanismos previstos para ello, pueden hacerlo escribiendo
y presentando el TFG en inglés. En cualquier caso, la nota de la competencia
“lengua extranjera” no afecta a la nota final del TFG. El plan de estudios de
la FIB prevé un TFG de 18 ECTS. El TFG puede realizarse en una universidad
extranjera a través de un programa de movilidad. La mayoría de las
universidades europeas establecen un TFG de 15 ECTS (también algunas
americanas y asiáticas con las que mantenemos convenios de cooperación), por
lo que para hacer compatible nues- tro TFG con un convenio de movilidad, los
18 crédi- tos se han dividido en dos bloques: • Un bloque de 15 créditos para
realizar un pro- yecto, similar en número de créditos a los que se realizan en
muchas universidades extranjeras. • Un bloque de 3 créditos en los que el
alumno se forma en aspectos de gestión de proyectos. Este bloque, que
denominamos GEP, se organiza co- mo una asignatura semipresencial y se detalla
en el Apartado 4. Los dos bloques tienen una única nota correspon- diente a
los 18 créditos. Muchas universidades ex- tranjeras tienen asignaturas
similares a GEP, por lo que resulta sencillo establecer convalidaciones. 4\.
GEP: Gestión de Proyectos GEP se organiza como un seminario intensivo se-
mipresencial de tres semanas de duración. Se cursa dos veces al año, en
febrero y en julio, coincidiendo con el final de los semestres de clase
regular. Las dos primeras semanas de GEP coinciden con las dos últimas semanas
del semestre, dedicadas fundamen- talmente a evaluaciones curriculares y
matrícula. En el semestre de otoño (septiembre-febrero) la tercera semana se
cursa simultáneamente con la primera semana de docencia de un curso regular.
En el semes- tre de primavera (marzo-julio) no existe solapamiento alguno con
otras asignaturas. Los motivos para esta distribución son varios: • Los
estudiantes que cursan GEP están acabando los estudios, por lo que
probablemente no cursa- rán ninguna asignatura simultáneamente con GEP o
cursarán unas pocas asignaturas optati- vas, que probablemente no requerirán
demasiada dedicación durante la primera semana de clase (caso del semestre de
otoño). • Cursar GEP al final de un semestre permite al estudiante hacer su
TFG en el siguiente semes- tre, por lo que el alumno recibe formación en
gestión de proyectos antes de realizar su TFG. Esto permite cursar el TFG el
octavo semestre de carrera, y por tanto acabar los estudios de Grado en los
cuatro años previstos. • Los créditos de TFG equivalen en nuestra uni-
versidad a 30 horas de trabajo del estudiante. Los 3 créditos de GEP
corresponden por lo tanto a 90 horas, o 30 horas por semana, lo que consi-
deramos un ratio razonable para un seminario in- tensivo, incluso durante la
última semana clase, en la que GEP podría simultanearse con alguna asignatura
optativa regular. • Permite el seguimiento de la asignatura a aque- llos
estudiantes que estén realizando movilidad y no dispongan de una asignatura
como GEP en el centro donde realizarán el TFG, y también a los que realizan el
TFG en una empresa, ya sea na- cional o extranjera. Con respecto a los
objetivos de GEP, se distribuyen en cuatro módulos, tres comunes para todos
los alumnos y uno específico de la especialidad en que están matriculados (el
TFG forma parte de la especia- lidad). En este módulo se tratan los aspectos
singula- res de la gestión de proyectos de la especialidad. Los cuatro módulos
se trabajan de forma no presencial. A medida que el estudiante avanza en GEP,
debe ir presentando diferentes informes en los que aplica los Trabajo ﬁn de
grado y Prácticum 305 conocimientos adquiridos a su TFG. Consideramos que el
50% del tiempo del estudiante debe dedicarse a estudiar los cuatro módulos de
GEP y el otro 50% a aplicar lo aprendido a la elaboración de su su TFG. Hacia
la mitad del curso, la documentación generada por cada estudiante es
presentada muy brevemente (tres minutos) en un video de cuerpo entero que se
envía al profesor, el cual proporciona realimentación. Al finalizar las tres
semanas del curso se realiza una presentación pública de 5 minutos en formato
presen- cial (o por videoconferencia o un sistema similar para los estudiantes
que están en el extranjero) de todo el trabajo realizado, y los estudiantes
reciben realimen- tación en directo del profesor. La evaluación de esta
presentación y de los informes elaborados durante el curso la realizan el
profesor de GEP y el director del proyecto, y el resultado es la evaluación
del Hito inicial. A continuación se describen brevemente los cuatro módulos de
GEP y los temas en que el estu- diante debe presentar documentación
acreditando que está aplicando a su TFG lo aprendido en GEP: • Módulo 1:
Herramientas TIC de soporte a la ges- tión de proyectos y equipos. En este
módulo se tratan los siguientes temas: (1) aplicaciones es- pecíficas de
gestión de proyectos, (2) recursos en Internet para la gestión y (3) gestión
del TFG a través de la red. • Módulo 2: Aspectos básicos de la gestión de
proyectos. En este módulo se tratan los siguien- tes temas: (1) gestión
integral de proyectos (2) gestión del alcance -entregable 1: definición del
alcance-, (3) gestión del tiempo -entregable 2: planificación temporal-, (4)
gestión económica - entregable 3: presupuesto-, (5) otras áreas de gestión. •
Módulo 3: Habilidades personales y profesiona- les para la gestión de
proyectos y equipos. En es- te módulo se tratan los siguientes temas: (1) ges-
tión de personas y equipos -entregable 4: presen- tación preliminar-, (2)
habilidades informaciona- les -entregable 5: contextualización y bibliogra-
fía-, (3) técnicas de comunicación eficientes. • El contenido del módulo 4
depende de la espe- cialidad, y en el módulo se detallan las caracte- rísticas
especiales y diferenciales que tienen los proyectos de cada especialidad. Al
finalizar los cuatro módulos, el estudiante debe entregar un documento que
recopile todos los entre- gables realizados hasta el momento (introducción y
estado del arte, alcance del proyecto, planificación temporal, presupuesto y
referencias bibliográficas consultadas), adaptados según los criterios
descritos en el módulo 4. Esta recopilación y su presentación pública es la
que será evaluada en el Hito Inicial. La forma de evaluación del TFG se
detalla en el siguiente apartado. 5\. Hitos de Evaluación/Indicadores Hemos
decidido evaluar el TFG mediante tres hitos y tres acciones de evaluación.
Tanto en el Hito inicial como en el Hito final, la evaluación de la documenta-
ción entregada y su presentación pública se realiza en una única acción de
evaluación. Cada hito tiene su propio agente evaluador y la evaluación se
realiza a partir de un conjunto de indicadores cuya valoración se define de
forma precisa mediante una rúbrica. Para facilitar los procesos de evaluación,
se ha di- señado una aplicación informática en la que los diferentes agentes
evaluadores pueden introducir de forma rápida y sencilla sus calificaciones,
seleccio- nando directamente su valoración sobre la rúbrica de cada indicador.
A partir de la información obtenida en los tres actos de evaluación, la
aplicación calcula de forma automática la nota final del TFG. 5.1. El Hito
inicial El Hito inicial se realiza durante el primer mes de trabajo del
estudiante en su TFG, mientras cursa GEP. En el Hito Inicial se evalúan los
informes presentados por el estudiante en GEP y la presentación pública
realizada a sus compañeros. La presentación se reali- za en el marco de la
asignatura GEP, y el agente evaluador es el profesor responsable de GEP. El
informe es evaluado tanto por el profesor de GEP como por el director del TFG,
que también actúa como agente evaluador. La rúbrica del Hito Inicial tiene
ocho indicadores, cuatro para evaluar la presentación pública y otros cuatro
para evaluar la documentación presentada. Los ocho indicadores (resumidos)
son: • la formulación del problema a resolver, • una planificación inicial del
trabajo a realizar, describiendo cómo se va a realizar el seguimien- to de
dicha planificación, y un análisis inicial de costes, • la descripción de la
metodología que va a usarse, las herramientas de seguimiento y el método de
validación de resultados, • un análisis inicial del posible impacto del pro-
yecto en términos sociales, ambientales y eco- nómicos (análisis de
sostenibilidad), • escribir de forma clara y correcta, • comunicación oral:
lenguaje verbal, • comunicación oral: lenguaje no verbal , • comunicación
oral: uso solvente de elementos de soporte. La presentación pública es
presencial para los estu- diantes matriculados en la FIB, pero puede
realizarse a través de un sistema de videoconferencia (por ejemplo a través de
Skype o de sistemas similares) para los estudiantes que están de movilidad.
Los estudiantes que realizan el proyecto en empresa 306 XIX Jornadas sobre la
Enseñanza Universitaria de la Informática pueden escoger realizar la
presentación de forma presencial o telemática. La presentación oral del
informe se realiza en gru- pos reducidos de 8-10 estudiantes, y cada
estudiante dispone de 5 minutos para realizar su presentación y 5 minutos para
contestar preguntas del profesor o de sus compañeros. El profesor da
realimentación de todas las presentaciones. El director o el profesor de GEP
pueden, si lo con- sideran conveniente, incluir comentarios en su eva- luación
sobre, por ejemplo, las posibles deficiencias en la definición de objetivos o
en la planificación, y eventuales propuestas para su corrección. En caso de
que el estudiante no supere satisfacto- riamente el Hito inicial, debe repetir
GEP el siguiente semestre, ya que el Hito inicial se considera funda- mental
para una correcta realización del Trabajo de Fin de Grado. Al finalizar el
Hito inicial, el estudiante propone y planifica en qué momento se realizará la
acción de evaluación correspondiente a su Hito de seguimiento, que debería
producirse más o menos cuando se ha realizado el 50% del TFG. Dado que se
estima que la duración de un proyecto estará entre 4 y 6 meses, el Hito de
seguimiento debería producirse dentro de los dos o tres meses siguientes a la
evaluación del Hito Inicial. 5.2. El Hito de seguimiento El Hito de
seguimiento se evalúa a partir del in- forme de seguimiento y de una
entrevista (opcional) con el director. El director/ponente del TFG actúa como
agente evaluador. La rúbrica del Hito de se- guimiento tiene ocho indicadores,
dos de los cuáles ya han sido previamente evaluados en el Hito inicial (aunque
no con la misma rúbrica): • la contextualización del proyecto, descripción de
los antecedentes y análisis de posibles solucio- nes y tecnologías, • el
seguimiento de la planificación justificando los eventuales ajustes
realizados, • si se han producido cambios en la metodología propuesta, la
justificación de los cambios y la descripción de la nueva metodología, • la
justificación de la opción seleccionada, • la capacidad del estudiante para
tomar iniciativas y decisiones, sopesando los riesgos y las oportu- nidades, •
la capacidad del estudiante de implicarse en el trabajo, mostrando una actitud
y comportamien- to profesional, • la integración de conocimientos y la
generación de soluciones creativas, • la identificación de las regulaciones
(leyes nor- mas, etc.) susceptibles de ser aplicadas en el proyecto. El
director/ponente puede proponer al estudiante cambios en lo que considere
incorrecto. Si considera que las desviaciones del estado actual del proyecto
respecto a lo previsto son muy grandes, puede propo- ner la realización de una
nueva acción de evaluación. La fecha de la nueva acción es acordada con el
estu- diante. En caso de que sea necesario repetir esta acción varias veces,
sólo se evalúa la última acción de seguimiento. En la evaluación se puede
premiar a los estudiantes que han hecho un trabajo adecuado (aun- que no se
ajuste a la planificación inicial) y se puede penalizar a aquellos que han
tenido que realizar varias acciones de evaluación de seguimiento no justifica-
das. 5.3. El Hito final En el Hito final se evalúan la memoria final y la
presentación pública del TFG. Ambas acciones son evaluadas por un tribunal,
como se hace en la mayo- ría de centros con los actuales PFC. El Hito final
debe celebrarse antes de que se cumpla un año desde que el estudiante
matriculó el proyecto. De no ser así, el estudiante debe matricular de nuevo
el proyecto (por normativa de la UPC). La rúbrica del Hito final tiene diez
indicadores: • resolución del problema formulado inicialmente y alcance de los
objetivos definidos, • el seguimiento de la planificación, justificando los
ajustes realizados, y la presentación de un análisis del coste del proyecto, •
La existencia de información suficiente para re- producir el procedimiento de
análisis, síntesis y evaluación. Si la evaluación es numérica, la pre-
sentación correcta y razonada de los números, • se analiza el impacto del
proyecto en términos sociales, ambientales y económicos (análisis de
sostenibilidad), • estructura y organización del trabajo, • escritura clara y
correcta, • el uso de recursos de información, • comunicación oral: lenguaje
verbal, • comunicación oral: lenguaje no verbal, • comunicación oral: uso
solvente de elementos de soporte. Las rúbricas de todos los hitos, así como la
infor- mación relativa a la evaluación del TFG, son accesi- bles desde la
página web de la FIB.1 No se ha definido un formato de memoria de TFG porque
consideramos que la casuística de trabajos es muy elevada y definir un
formato, aunque fuese un formato distinto para cada especialidad, limitaría la
creatividad de los estudiantes y probablemente no se ajustaría bien a algunos
proyectos. No obstante, se 1 http://www.fib.upc.edu/es/estudiar-enginyeria-
informatica/treball- final-grau.html Trabajo ﬁn de grado y Prácticum 307 exige
que todas las memorias comiencen con un resumen del proyecto de una o dos
páginas redactado en castellano y en inglés. Dado que el Real Decreto
1393/2007 [3] define que el TFG debe enmarcarse en una de las cinco
especialidades del Grado en Ingeniería Informática, parece adecuado que los
TFG se evalúen por especia- lidades. En la FIB, cada TFG es evaluado por un
tribunal específico de su especialidad. El tribunal puede consultar, si lo
desea, los infor- mes de evaluación de los hitos inicial y de seguimien- to.
El tribunal está formado por tres miembros: un presidente y dos vocales. Al
menos dos de los miem- bros del tribunal deben estar capacitados para evaluar
las competencias técnicas del proyecto. El direc- tor/ponente de un TFG no
puede ser miembro del tribunal que evalúa dicho TFG. Por ello, se nombra un
vocal suplente en cada tribunal para casos imprevis- tos o para suplir a uno
de sus miembros en caso de que éste sea director/ponente de uno de los
proyectos evaluados. Se definen dos períodos de evaluación cada semes- tre,
uno hacia mitad del semestre y otro al final (cua- tro periodos al año). Se
estima que cada período de evaluación puede durar uno o dos días. Los TFG se
agrupan en bloques de hasta cinco proyectos que son evaluados por un mismo
tribunal en una mañana o en una tarde. El estudiante dispone de 30 minutos
para realizar su presentación, y el tribunal puede realizar preguntas o
solicitar aclaraciones durante 15 minutos. En caso de que haya más de cinco
proyectos para evaluar, se agrupan en un nuevo bloque y son evalua- dos por un
tribunal distinto. Esta estructura facilita que los directores/ponentes no
evalúen los proyectos que dirigen, no sobrecarga excesivamente a los profe-
sores que forman parte de los tribunales (su trabajo se limita a una mañana o
una tarde más el tiempo de leer las memorias) y garantiza que al menos dos de
los miembros del tribunal tienen la capacidad de evaluar técnicamente el
proyecto. Para facilitar que los profesores se acostumbren al nuevo sistema de
evaluación, la primera vez que participen en un tribunal serán vocales. El
presidente debe haber estado previamente en algún tribunal. Este proceso
garantizará que siempre haya al menos un miembro del tribunal con experiencia
previa en la evaluación. 5.4. Indicadores Para definir los indicadores, se han
usado como punto de partida los indicadores identificados por la “Guía para la
evaluación de competencias en los Trabajos de Fin de Grado y de Máster en las
Ingenie- rías”. La guía se centra en las 30 competencias gené- ricas definidas
por el proyecto Tuning2, y define 2 http://www.unideusto.org/tuning/
indicadores específicos para evaluar el TFG (y el Trabajo Final de Master) en
cada una de ellas. La FIB, como se ha descrito en el Apartado 3, ha
seleccionado nueve competencias genéricas para ser trabajadas y evaluadas en
los estudios de Grado en Ingeniería Informática. Si bien alguna de estas com-
petencias puede identificarse claramente con alguna de las competencias Tuning
(como, por ejemplo, el trabajo en equipo o la comunicación oral y escrita), la
mayoría de ellas agrupan varias competencias Tuning o, al menos, aspectos de
varias competencias distin- tas. Por ello, el procedimiento que hemos usado
para seleccionar indicadores en cada hito de evaluación ha sido el siguiente:
• Revisar los indicadores de evaluación del TFG de todas las competencias
Tuning. • Seleccionar los indicadores relevantes para eva- luar las
competencias genéricas de la FIB. • Agrupar aquellos indicadores que son
similares o pueden evaluarse de forma conjunta. • Añadir los indicadores que
se consideren necesa- rios y no se hayan encontrado en la guía. • Redistribuir
los indicadores entre hitos a partir de la distribución propuesta por la guía,
como se muestra en el Cuadro 1. Algunos indicadores pueden aparecer en más de
un hito, y su descrip- ción se ha simplificado para hacer el cuadro más claro.
• Revisar los indicadores de cada hito con el obje- tivo que su número no sea
excesivo. • Asignar los indicadores a las competencias de la FIB, como se
muestra en el Cuadro 2. • Realizar la rúbrica para cada indicador. La rúbri-
ca puede ser distinta para un mismo indicador que aparezca en más de un hito.
El objetivo de este proceso ha sido disponer de un conjunto reducido de
indicadores capaz de evaluar las competencias genéricas del TFG. A partir de
una primera versión de los indicadores, realizada por los autores directamente
tomando como punto de partida los indicadores de la guía, un grupo de
profesores de la FIB, entre los que se encuentran algunos de los autores del
presente trabajo, han reali- zado un trabajo de revisión general y reescritura
de los indicadores para darle coherencia a todo el con- junto y han definido
el contenido de las rúbricas. El resultado final de todo este trabajo es el
que se pre- senta en esta ponencia. 6\. Evaluación final El proceso descrito
hasta el momento se ha aplica- do a la evaluación de las competencias
genéricas. Dada la enorme casuística de los TFG, hemos consi- derado que este
proceso no podía aplicarse a las competencias específicas de la titulación o
de la 308 XIX Jornadas sobre la Enseñanza Universitaria de la Informática
especialidad. De hecho, la “Guía para la evaluación de competencias en los
Trabajos de Fin de Grado y de Máster en las Ingenierías” se centra en la
evaluación de competencias genéricas y deja a criterio del centro la forma de
evaluar las competencias específicas. El criterio que la FIB ha adoptado para
evaluar las competencias específicas ha sido hacerlo durante el Hito final de
forma conjunta. Es decir, que los miem- bros del tribunal competentes para
evaluar técnica- mente el proyecto decidan, con los criterios que consideren
oportunos para cada proyecto (y para cada proyecto podrían ser distintos), la
nota correspondien- te a las competencias específicas del TFG. Pensamos que,
con una casuística tan elevada de TFGs, es preciso confiar en la experiencia
de los miembros del tribunal para evaluar la parte técnica del proyecto. Somos
conscientes de que esto repite los mismos errores detectados en la evaluación
del actual PFC, pero no vemos una forma mejor de hacerlo. Por otra parte,
creemos que el hecho de evaluar varios TFGs en el mismo momento y con el mismo
tribunal facili- tará una evaluación más equitativa. En cuanto al porcentaje
en la nota final, hemos considerado que las competencias específicas de la
titulación deberían valer un 60% de la nota y las competencias genéricas un
40%. Una forma de justi- ficar este porcentaje sería hacerse la siguiente
pregun- ta: ¿Qué nota le pondría usted a un proyecto excelen- te que ha
presentado una memoria horrorosa y ha hecho una presentación pública para
olvidar? Según nuestra ponderación, ese proyecto obtendría un 6. Hemos
determinado que todos los indicadores de- ben tener el mismo peso dentro de
cada hito, y para los hitos hemos definido los siguientes pesos: 25% para el
Hito inicial, 25% para el Hito de seguimiento y 50% para el Hito final. Dado
que este porcentaje corresponde a la evaluación de las competencias genéricas,
que supone el 40% de la nota total del TFG, el resultado es que el Hito
inicial vale un 10% de la nota final, el Hito de seguimiento otro 10% y el
Hito final un 80%: el 20% de la nota destinada a evaluar competencias
genéricas y el 60% restante a competencias específicas. Dado que algunos
indicadores son evaluados en más de un hito de evaluación, como puede verse en
el Cuadro 1, pensamos que es conveniente no considerar para la nota final las
notas de los tres o cuatro peores indicadores, siempre que estos hayan sido
evaluados en más de un hito y se haya detectado que su evalua- ción ha
mejorado con el avance del proyecto. Esto permite tener en cuenta que el
estudiante ha corregido de forma adecuada las posibles deficiencias detecta-
das durante la realización del TFG. Finalmente, en el informe del Hito final
se da al tribunal la opción de indicar que el TFG es de excep- cional calidad
o tiene un valor añadido, ya sea por la calidad del trabajo, por la
aplicabilidad de los resulta- dos o por cualquier otra causa que el tribunal
conside- re. Se debe justificar el motivo y en ningún caso puede coincidir con
uno de los indicadores ya evalua- dos. A estos TFG se les puede llegar a sumar
hasta un punto a la nota final (el tribunal puede escoger entre medio punto y
un punto). El objetivo de estas medidas es poder detectar aquellos TFG
excepcionalmente buenos y cuya evaluación sobresalga con respecto a los demás,
consiguiendo incluso la Matrícula de Honor, que el Cuadro 2: Ejemplo de
distribución de indicadores entre competencias genéricas. Cuadro 1:
Distribución de indicadores entre hitos. Trabajo ﬁn de grado y Prácticum 309
tribunal puede otorgar según su criterio a aquellos proyectos que hayan
obtenido una nota final superior a 9. Todas estas medidas son necesarias
porque, cuando una evaluación se produce como la suma de muchos actos
evaluativos (como es el caso del TFG, dada la gran cantidad de indicadores
involucrados), el resultado suele ser que las notas sufren una distribu- ción
normal alejada de las notas más altas, que son muy difíciles de obtener. Todo
el proceso descrito en este apartado es reali- zado de forma muy sencilla
usando la aplicación informática descrita al inicio del Apartado 5. El trabajo
del tribunal durante el Hito final consiste en que el tribunal (por medio de
su presidente) seleccio- na en las rúbricas de los indicadores la evaluación
de cada indicador y decide si el TFG es de excepcional calidad. En caso de
desacuerdo entre los miembros del tribunal, la decisión se toma por mayoría.
Para los TFG realizados en empresas se usa tam- bién el sistema de evaluación
descrito. Para los TFG realizados en universidades extranjeras se acepta la
calificación de la universidad en la que se realizó el proyecto. Finalmente, a
partir de los indicadores evaluados en los tres hitos se puede extraer una
nota para cada competencia genérica de la titulación. Esta nota puede servir
como nota final de la competencia o puede complementar la nota que haya
obtenido hasta el momento el estudiante en dicha competencia en caso de que el
centro evalúe de forma independiente las competencias genéricas (como es
nuestro caso). 7\. Guía para el estudiante Las rúbricas son muy útiles para
orientar a los agentes evaluadores y unificar criterios. El caso de la
evaluación del TFG, donde actúan diferentes agentes evaluadores formados por
diferentes personas, es muy importante disponer de rúbricas precisas que
permitan evaluar a los estudiantes eliminando en la medida de lo posible el
grado de subjetividad existen- te en cualquier acto de evaluación. Sin
embargo, las rúbricas precisas tienen un incon- veniente: contienen demasiada
información para poder servir de orientación al estudiante. Por ello, de cara
a orientar al estudiante, un grupo de profesores de la FIB elaboraron una
propuesta basada en el método socrático. Esta propuesta fue presentada en
Jenui 2012 [2], y consiste en que la orientación al estudiante se establezca
mediante un conjunto de preguntas que los estudiantes deben plantearse durante
la realización de su TFG. La res- puesta a alguna de estas preguntas debe
plasmarse en la memoria final del TFG, mientras que otras pregun- tas sirven
simplemente para que el estudiante se plantee cuestiones que le permitan
avanzar en la dirección correcta. 8\. Conclusiones El cambio de los Proyectos
de Fin de Carrera (PFC) por los Trabajos de Fin de Grado (TFG) repre- senta
una excelente oportunidad para replantear la evaluación de estos proyectos y
mejorar la forma como se había realizado hasta ahora. Tradicionalmen- te, la
evaluación se realizaba siguiendo criterios poco precisos basados en la
experiencia previa de los agentes evaluadores. Es necesario replantear la
forma de realizar la eva- luación para los TFG, de forma que exista una traza-
bilidad de la evaluación y que los criterios de evalua- ción sean claros y
públicos. En este artículo se presenta una propuesta para la evaluación de los
TFG realizada a partir de las reco- mendaciones de la “Guía para la Evaluación
de Competencias de los Trabajos de Fin de Grado y Máster en las Ingenierías”.
La evaluación está basada en tres hitos de evaluación: el Hito inicial, el
Hito (o Hitos) de seguimiento y el Hito final. La evaluación en cada uno de
los hitos se realiza a partir de un conjunto de indicadores. Los criterios de
evaluación de cada indicador están definidos median- te una rúbrica que el
estudiante conoce con anteriori- dad a la realización de su TFG.
Agradecimientos A todo el equipo de Elena Valderrama, por el gran trabajo
realizado en la “Guía para la Evaluación de Competencias de los Trabajos de
Fin de Grado y Master en las Ingenierías”, y a todos los profesores de la FIB
que han participado en la implementación final de la normativa del TFG además
de los autores, en particular a Marc Alier, Jose Cabré y David López.
Referencias [1] Guia per a l'avaluació de competències als tre- balls de final
de grau i de màster a les Enginye- ries, 2009\.
http://www.aqu.cat/doc/doc_21214293_1.pdf Última consulta, mayo 2013. [2] Marc
Alier, Jose Cabré, Jordi García, David López y Fermín Sánchez, Preguntas para
guíar el Trabajo Final de Grado. Jenui 2012 [3] Real Decreto 1393/2007, de 29
de Octubre, por el que se establece la ordenación de las ense- ñanzas
universitarias oficiales. BOE 30 de Oc- tubre de 2007, pág 44037-44048. [4] E.
Valderrama, M. Rullán, F. Sánchez, J. Pons, F. Cores, J. Bisbal. La evaluación
de compe- tencias en los Trabajos de Fin de Estudios. Je- nui 2009. 310 XIX
Jornadas sobre la Enseñanza Universitaria de la Informática

