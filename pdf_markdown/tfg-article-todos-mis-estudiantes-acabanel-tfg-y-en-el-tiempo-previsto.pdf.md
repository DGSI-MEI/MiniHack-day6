Artículo invitado Todos mis estudiantes acaban el TFG, y en el tiempo previsto
Fermín Sánchez, Jaume Moral y David López Facultat d’ Informàtica de Barcelona
Universitat Politècnica de Catalunya Barcelona fermin@ac.upc.edu,
jaumem@ﬁb.upc.edu, david@ac.upc.edu Resumen Los Trabajos de Fin de Grado (TFG)
deben ser evaluados a partir de competencias, como el resto de las asignaturas
de la titulación. La Guía de Evaluación de los trabajos de Fin de Grado y
Master en las Ingenierías recomienda que esta evaluación se realice en 3 hitos
(Inicial, de Seguimiento y Final) mediante 5 acciones de evaluación. Cada
hito/acción puede ser evaluado mediante rúbricas por un agente evaluador
distinto a partir de indicadores objetivos. Este planteamiento es
considerablemente distinto al que tenían los Proyectos de Final de Carrera que
eran evaluados, nor- malmente sólo a su ﬁnalización, por un tribunal que ponía
una única nota que contemplaba todos los aspectos del proyecto. La complejidad
de la evaluación de los TFG puede provocar que muchas escuelas traten de
simpliﬁcarla para reducir el tiempo dedicado a su gestión, lo que sin duda
repercutirá negativamente en la calidad del TFG y de su evaluación. Para
evitar este fenómeno, en la Facultat d’Informàtica de Barcelona hemos diseñado
una aplicación que facilita la gestión de la evaluación de los TFG, de forma
que, pese a usar los tres hitos y las cinco acciones de evaluación que
recomienda la Guía, con un total de 26 indicadores objetivos (con sus
respectivas rúbricas) y agentes evaluadores diferentes para cada hito, la
evaluación resulta sencilla y rápida y al profesorado le ha resultado fácil
adaptarse a la nueva metodología. Este diseño ha permitido mejorar la ratio de
proyectos presentados y reducido considerablemente la duración de los
proyectos. Los datos que disponemos de dos años (2013–14 y 2014–15) indican
que se han presentado el 97 % de los TFG y que sólo un 1 % de los TFG ha
invertido más de 12 meses desde su matriculación hasta su lectura. En este
trabajo se presentan las ideas que han guiado el diseño de la aplicación y los
resultados de dos años de aplicación. Palabras clave: Evaluación TFG, Software
evaluación TFG, Evaluación por competencias. 1\. Motivación El EEES deﬁne que
los planes de estudios han de ser dise- ñados a partir de las competencias de
la titulación. Este diseño debe reﬂejarse en las estrategias de
enseñanza/aprendizaje y en los métodos de evaluación y también en el Trabajo
Final de Grado (TFG): aprendizaje y evaluación han de estar orien- tados,
ambos, a competencias. En la Facultat d’Informàtica de Barcelona de la
Universi- tat Politècnica de Catalunya (FIB) se ha hecho un gran esfuer- zo
por cumplir con estas directivas, pero uno de los aspectos donde más se ha
notado el cambio ha sido, sin duda, en los TFG. En los planes de estudios
anteriores a la implantación del EEES, los Proyectos de Fin de Carrera (PFC)
tenían en la FIB las siguientes características: No existían directivas
respecto a las fases y objetivos más allá del criterio del director. Cada
director deﬁnía el alcance del PFC. La evaluación se realizaba en un único
acto al ﬁnal del proyecto y se hacía a partir de la memoria del proyec- to y
de una defensa oral del mismo. No había entregas parciales ni ningún tipo de
seguimiento más allá que el que decidiese realizar motu proprio el director.
El tribunal que evaluaba el proyecto estaba formado por tres miembros: un
Presidente (propuesto por el direc- tor), un secretario (el propio director) y
un vocal es- cogido por sorteo entre los profesores del centro. Nor- ReVisión
vol. 8, núm. 3. Septiembre 2015 ISSN 1989-1199 31 32 ReVisión. Vol. 8, núm. 3
malmente, tanto el presidente como el secretario eran “expertos” en el tema
abordado por el PFC. La nota del PFC se ponía después de una delibera- ción
del tribunal. Esta deliberación era libre y no esta- ba pautada de forma
alguna. Las competencias técnicas y transversales se evaluaban de forma
conjunta, con la ponderación que el tribunal considerase conveniente en cada
caso, y que podía variar de un PFC a otro y de un tribunal a otro. El
porcentaje de sobresalientes y Matrículas de Honor era muy superior al que se
daba en cualquier otra asig- natura. Para no desvirtuar el sentido de una
Matrícula de Honor, y teniendo en cuenta que en la FIB están li- mitadas al 5
% de cada asignatura, se decidió que los tribunales sólo podrían hacer
«propuestas de Matrícula de Honor» y que una comisión seleccionada por el cen-
tro evaluaría anualmente estas propuestas y determina- ría cuáles de ellas
eran merecedoras de la Matrícula de Honor. Como consecuencia de esta
metodología para el desarrollo y la evaluación del PFC, se detectaron los
siguientes proble- mas: Los alumnos estaban poco formados para hacer un pro-
yecto en el momento de comenzar su PFC y la calidad de su formación ﬁnal en
proyectos dependía mucho de la formación en dirección de proyectos del
director del PFC. El director, por su parte, tenía que formar a todos sus
proyectistas una y otra vez, en cada nuevo proyecto. El papel del director era
determinante: había directores que exigían una clara planiﬁcación inicial y el
cumpli- miento de plazos estrictos, mientras que otros actuaban de una manera
más caótica o relajada. Algunos direc- tores se preocupaban de tener un buen
estudio del es- tado del arte o de la viabilidad del proyecto, mientras que
otros poco menos que ignoraban estos apartados. Unos directores hacían
seguimiento del proyecto, mien- tras que otros dejaban el seguimiento en manos
de la proactividad del estudiante. Diferentes tribunales podrían haber puesto
diferentes notas al mismo proyecto, tanto por establecer una pon- deración
diferente entre competencias técnicas y trans- versales como por evaluar de
forma poco objetiva las competencias. Por ejemplo, algunos tribunales daban
mucha importancia a la memoria del proyecto y a su presentación, mientras
otros consideraban que lo impor- tante era fundamentalmente la calidad técnica
del pro- yecto. No había un criterio claro de evaluación, lo que llevaba a
caliﬁcaciones arbitrarias. Algunos proyectos recibían notas muy inferiores a
las de otros proyectos que parecían claramente peores, simplemente porque al
no haber criterios establecidos cada tribunal aplicaba los que consideraba
oportunos en cada caso. La duración del proyecto dependía de los intereses del
director. Pese a que el tiempo de dedicación de un estu- diante a su PFC
estaba claramente estipulado en el plan de estudios, y era diferente para un
proyecto de inge- niería que para un proyecto de ingeniería técnica, a los
profesores les costaba diferenciarlos y tendían a propo- ner proyectos para la
ingeniería independientemente de si el estudiante estudiaba la Ingeniería en
Informática o una de las dos ingenierías técnicas que impartía la FIB
(informática de sistemas e informática de gestión). Es- to provocaba que los
estudiantes de ingenierías técnicas dedicasen a su PFC más tiempo del que
deberían. Incluso los estudiantes de ingeniería dedicaban más tiempo del
estipulado. Ya fuera porque no sabían cuán- to tiempo debían dedicar, por
exceso de celo o por la presión del director, el caso es que muchos de los
pro- yectos de ingeniería tenían una dedicación mayor de las 900 horas
previstas (1 semestre). Este hecho provocaba, en muchas ocasiones, que los
proyectos durasen mucho más de 6 meses e incluso más de 1 año, como puede
observarse en el apartado 4. Los estudiantes no necesitaban hacer el PFC para
en- contrar trabajo. De hecho, la mayoría de ellos compa- ginaba sus últimos
años de estudios con un trabajo re- munerado, por lo que una vez acababan de
cursar las asignaturas de la carrera se dedicaban a trabajar y “ol- vidaban”
que tenían que hacer el PFC para obtener el título. De hecho, algunos ni
siquiera intentaban comen- zarlo. Sólo cuando el título era preciso para su
puesto de trabajo, o cuando un cambio de plan de estudios se avecinaba, se
decidían a hacer ﬁnalmente el PFC. En es- te caso, y dado que ya tenían varios
años de experiencia en la industria, normalmente escogían un proyecto en el
que hubiesen participado y se limitaban a documentarlo y presentarlo. La
existencia de una bolsa de estudiantes que estaban pendientes de acabar su PFC
para obtener el título repercutía negativamente en las estadísticas de la FIB
(el porcentaje de titulados respecto a los alum- nos ingresados era menor que
el de otras titulaciones similares de la universidad) y también en su
capacidad económica, ya que una parte del presupuesto ordinario del centro
depende del número y porcentaje de egresa- dos anuales. El EEES supuso una
oportunidad para tratar de solventar, o al menos reducir, todos estos
problemas. La implantación del Grado en Ingeniería Informática se llevó los
PFC y trajo consigo los TFG, y aprovechando el cambio se decidió dise- ñar un
modelo de seguimiento y evaluación que subsanase los inconvenientes
detectados. El apartado 2 muestra brevemente las ideas principales del modelo
que se ha implantado en la FIB. En el apartado 3 se describe la herramienta
que se dise- ñó para gestionar de forma eﬁcaz el modelo de seguimiento y
evaluación de los TFG. El apartado 4 presenta los resultados 33 obtenidos
durante los dos primeros años que se han producido egresados y los compara con
los de años anteriores. 2\. Modelo de seguimiento y evaluación del TFG Para
diseñar el modelo de seguimiento y evaluación del TFG se usó el esquema
propuesto en la Guía para la evalua- ción de competencias en los trabajos de
Fin de Grado y Master de las Ingenierías [1]. En la Guía se deﬁne que la
evaluación del TFG debe realizarse en 3 hitos: el Hito Inicial, el Hito de
Seguimiento y el Hito Final. Las competencias a evaluar en el TFG se deﬁnen en
forma de indicadores que se distribuyen entre los 3 hitos y se evalúan
mediante una rúbrica especíﬁca para cada indicador en cada hito. En nuestro
caso, se tomaron una serie de decisiones para tratar de resolver los problemas
detectados en los PFC, deta- llados en el apartado 1. Con el objeto de uniﬁcar
la forma- ción en gestión de proyectos de los estudiantes se diseñó un TFG de
18 créditos, de los cuales 3 se dedican a esta forma- ción cuando se inicia el
TFG. Los otros 15 corresponden al proyecto en sí y permiten la movilidad de
los estudiantes, ya que la mayoría de las escuelas de informática en Europa
tie- nen proyectos de 15 créditos. Los 3 créditos de formación se cursan en un
módulo denominado GEP (GEstión de Proyec- tos [2]) que se realiza al inicio de
cada semestre y que cursan todos los estudiantes que han matriculado el TFG.
GEP tiene un formato semipresencial (sólo la evaluación es presencial), es
intensivo (se realiza en un mes) y su evaluación es también la del Hito
Inicial del TFG. Esta evaluación es realizada tanto por los profesores de GEP
como por el director del TFG. Los detalles del modelo de seguimiento y
evaluación de los TFG en la FIB pueden encontrarse en escritos anteriores [2,
3]. A continuación se describen brevemente las características prin- cipales
del modelo de seguimiento y evaluación de los TFG usado en la FIB: GEP
garantiza que el proyecto se ha puesto en marcha en un tiempo razonable (1
mes) y con un planteamiento adecuado. El Hito de Seguimiento es evaluado por
el di- rector del TFG hacia la mitad del proyecto. En caso de que el proyecto
no haya avanzado como se esperaba, se programa una nueva evaluación del Hito
de Seguimien- to. La última evaluación realizada es la que se considera como
evaluación del hito. Las evaluaciones previas son descartadas, pero el
director puede tenerlas en cuenta a la hora de evaluar el Hito de Seguimiento.
El Hito Final es evaluado por un tribunal que está for- mado por tres
miembros: dos expertos en la especiali- dad del proyecto y un miembro escogido
por sorteo en- tre los profesores del centro. Para minimizar el posible efecto
del tribunal en la nota del TFG, se decidió que un mismo tribunal evaluaría
varios proyectos en una mis- ma sesión, con un máximo de 4 proyectos por
sesión (una mañana o una tarde), y que no podía ser miembro del tribunal el
director de ninguno de los TFG evalua- dos. Como en la FIB se imparten las 5
especialidades del Grado en Ingeniería Informática, y el TFG debe es- tar
asociado a una especialidad, los 5 tribunales pueden evaluar hasta 20 TFG en
sólo una sesión de cada uno. Para distribuir en el tiempo la lectura de los
TFG, y no obligar a los estudiantes a evaluarse únicamente al ﬁnal del curso,
cada proyecto puede escoger entre tres turnos de evaluación durante el año
académico (desde el mes 5 hasta el mes 12).1 Esto facilita la distribución de
los TFG entre los tres turnos y permite que, en muchos ca- sos, un único
tribunal evalúe todos los TFG de la espe- cialidad de un turno. Como hay 4
turnos de evaluación cada año (aunque un mismo TFG sólo puede acceder a tres
de ellos porque el cuarto está fuera de su ran- go de lectura), y 5 tribunales
(uno por especialidad), se puede garantizar en media que cada año se pueden
leer 80 TFG con un solo tribunal por especialidad en cada turno. La
experiencia nos ha demostrado que en algu- nas especialidades necesitamos 2
tribunales por turno (para no sobrecargar de trabajo a los miembros de un
tribunal), pero no se ha considerado un problema da- do que cada tribunal
evalúa hasta 4 estudiantes y así se garantiza una cierta ecuanimidad. En el
TFG se evalúan 7 competencias transversales (ac- titud emprendedora e
innovación, sostenibilidad y com- promiso social, comunicación efectiva oral y
escrita, uso solvente de los recursos de información, aprendi- zaje autónomo,
actitud adecuada frente al trabajo y ra- zonamiento) a través de 26
indicadores: 8 indicadores en los hitos Inicial y De Seguimiento y 10
indicadores en el Hito Final. Cada indicador tiene asociada una rú- brica con
4 notas posibles (no conseguido, conseguido pero no con el nivel esperado,
conseguido con el nivel esperado y conseguido con excelencia) para uniﬁcar el
criterio de los agentes evaluadores. Las competencias técnicas se evalúan de
forma conjunta a criterio del pro- pio tribunal. Somos conscientes de que esta
decisión permite una cierta arbitrariedad en la evaluación de las competencias
técnicas, pero varios factores apoyan que es un modelo correcto en este caso:
(1) los proyectos de Ingeniería Informática son muy distintos entre sí, in-
cluso dentro de una misma especialidad; (2) deﬁnir una rúbrica para estas
competencias restringiría mucho la evaluación y muy probablemente no cubriría
todos los casos posibles, y (3) el hecho de que un mismo tribu- nal formado
por expertos en el área evalúe en la misma sesión varios proyectos (a veces
todos los matriculados en la especialidad en un curso determinado) minimiza
1El director del proyecto debe dar el visto bueno a la memoria para que el
proyecto sea evaluado, lo que garantiza que el TFG cumple los requisitos
mínimos de calidad. 34 ReVisión. Vol. 8, núm. 3 la inﬂuencia del tribunal en
la evaluación del Hito Final. El 40 % de la nota ﬁnal proviene de la
evaluación de las competencias transversales y el 60 % restante de las
competencias técnicas. En el Hito Final, el tribunal pue- de consultar los
resultados de la evaluación de los hitos anteriores (en escritos anteriores
[2, 3] pueden encon- trarse más detalles sobre la forma de calcular la nota).
Pese a que los estudiantes siguen sin necesitar el TFG para encontrar trabajo,
ya que muchos compatibilizan sus estudios con un trabajo remunerado los
últimos cur- sos, perciben GEP como una asignatura más y la cur- san. Cuando
se dan cuenta están lanzados en su proyec- to, por lo que les resulta más
difícil abandonarlo (y de hecho los resultados prueban que no lo hacen). En la
gestión de la inscripción, seguimiento y evaluación del TFG intervienen muchos
actores y procesos distintos por lo que, si no se dispone de un sistema eﬁcaz,
esta gestión pue- de resultar muy complicada. Si este es el caso, los
profesores que intervienen en el proceso buscarán vías para simpliﬁcar- lo,
probablemente desvirtuándolo y reduciendo la probabili- dad de alcanzar los
objetivos deﬁnidos por el centro. Para evi- tar que esto suceda, hemos
desarrollado una aplicación infor- mática que gestiona todo el proceso y
facilita enormemente a profesores, estudiantes y personal de administración su
tra- bajo. La siguiente sección describe el funcionamiento de esta aplicación,
que está integrada en El Racó, el Campus Virtual de la FIB. 3\. La aplicación
Creemos que la herramienta que aquí describimos es im- prescindible para poder
aplicar de forma efectiva el modelo de seguimiento y evaluación descrito en el
apartado 2. La aplica- ción reduce el salto en complejidad evaluadora de los
TFG con respecto a los PFC, que se evalúan en un único acto al ﬁnal. Se ha
duplicado el número de personas implicadas en la evaluación, triplicado el
número de actos evaluativos y se ha pasado de evaluar con una nota única todo
el proyecto a una nota calculada a partir de 26 indicadores en tres hitos y
cinco acciones de evaluación, basada en competencias y gestionada por medio de
rúbricas e informes. La mejor manera de entender el funcionamiento de la apli-
cación es entender el proceso general que sigue un TFG en la FIB, que es el
siguiente: 1\. El estudiante selecciona un proyecto de su especialidad (a
propuesta suya, de una empresa o de un profesor) y lo inscribe a través del
campus virtual. Para ello, debe indicar qué competencias técnicas de la
especialidad se van a trabajar en el proyecto. Esta selección será poste-
riormente validada por el director y por el responsable de la especialidad. La
ﬁgura 1 presenta un diagrama de ﬂujo de esta fase. 2\. El estudiante matricula
el TFG y cursa GEP [2], don- de recibe formación no presencial durante tres
semanas que aplica directamente a su TFG. Realiza varias entre- gas de
documentación, que deben ser validadas por el director del proyecto y por el
profesor de GEP, y ha- ce una presentación ﬁnal la cuarta semana. Es evaluado
por el profesor de GEP (que evalúa 8 indicadores) y por el director del
proyecto (que evalúa 4 indicadores, un subconjunto de los evaluados por el
profesor de GEP). Esta evaluación es la nota del Hito Inicial. En la ﬁgura 2
se presenta la pantalla que usa el director para evaluar el Hito Inicial. Como
puede observarse, para realizar la evaluación de los 4 indicadores sólo tiene
que hacer 4 clics en la opción seleccionada de la rúbrica. 3\. Una vez
superado el Hito Inicial, el estudiante deﬁne la fecha del Hito de Seguimiento
y escoge el turno de lectura (hay tres turnos posibles). En la fecha acordada
para el Hito de Seguimiento el estudiante presenta el in- forme de
seguimiento, el director lo valida y realiza la evaluación del hito, que puede
implicar (o no) una en- trevista presencial con el estudiante. En caso de que
el estudiante no haya llegado al punto del proyecto esta- blecido en el Hito
Inicial para el Hito de Seguimiento, acuerda con el director una nueva fecha
para la evalua- ción. Este proceso se repite tantas veces como sea ne- cesario
y sólo se realiza la evaluación la última vez. El director puede considerar en
esta evaluación, si lo con- sidera conveniente, los anteriores Hitos de
Seguimiento fallidos. 4\. Al menos dos semanas antes del turno acordado para
la presentación del TFG, el estudiante sube al campus virtual la memoria del
proyecto, que debe ser validada por el director antes de estar accesible al
tribunal. El día de la lectura el estudiante hace la presentación oral de su
proyecto y contesta a las preguntas del tribunal. Al ﬁnalizar la lectura de
todos los proyectos del turno (un máximo de 4), el tribunal delibera y los
evalúa uno a uno. Los estudiantes pueden consultar su nota a partir del
momento en que el tribunal la introduce en la apli- cación, normalmente menos
de 24 horas después de la lectura. La ﬁgura 3 muestra el diagrama de ﬂujo del
proceso des- crito en los puntos 2, 3 y 4. El tribunal evalúa los 10
indicadores del Hito Final (con simplemente 10 clics), cada uno de ellos por
consenso o por mayoría, y pone una nota conjunta (entre 0 y 10) a las com-
petencias técnicas. Si lo desea, puede consultar la evaluación de los hitos
anteriores. En caso de que un TFG sea de excep- cional calidad, el tribunal
puede decidir poner hasta un punto extra (justiﬁcando el motivo por el que lo
hace). Esto permite compensar el hecho de que cuando la nota ﬁnal se calcula a
partir de un conjunto elevado de notas parciales es difícil ob- tener la
caliﬁcación máxima. Una vez el tribunal ha realizado la evaluación, la
aplicación calcula automáticamente la nota 35 Figura 1: Diagrama de ﬂujo de la
fase de inscripción y matrícula del TFG. del TFG y de cada una de las
competencias transversales y la muestra a título informativo (describir el
algoritmo usado para calcular la nota está fuera de los objetivos de este
traba- jo, y puede consultarse en obras anteriores [2, 3]). La ﬁgura 4 muestra
cómo se presenta al tribunal la evaluación conjunta de los indicadores una vez
evaluados. Nótese que alguno de los indicadores se evalúa en más de un hito y
existe en este caso una rúbrica especíﬁca del indicador para cada uno de los
hitos. En ningún caso el tribunal puede modiﬁcar la nota cal- culada por la
aplicación o rehacer la evaluación. En caso de que la nota sea igual o
superior a 9,5, la aplicación ofrece al tribunal la posibilidad de poner una
Matrícula de Honor. Para veriﬁcar que la nota propuesta por la aplicación era
adecuada, durante 1 año se pidió a todos los tribunales que sugiriesen una
nota ﬁnal única para el proyecto antes de ver la nota propuesta por la
aplicación. Esto permitió detectar al- guna pequeña disfunción del algoritmo
de cálculo de la nota y ajustarlo. En prácticamente todos los casos, no
obstante, la diferencia entre la nota propuesta por la aplicación y la pro-
puesta por el tribunal variaba apenas unas décimas. Por otra parte, el
estudiante puede consultar en el campus virtual el es- tado de su TFG en cada
momento. Un código de colores le permite identiﬁcar rápidamente las partes ya
ﬁnalizadas y los procesos pendientes, así como acceder a los informes de eva-
luación ya realizados. La ﬁgura 5 muestra la información tal y como la ve el
estudiante. En verde se muestran los procesos terminados y en azul el
siguiente proceso que está pendien- te de realizar. Finalmente, los procesos a
realizar en el futuro están sombreados en gris. Los procesos están ordenados
tem- poralmente de arriba abajo. En el caso de la ﬁgura 5, el es- tudiante
está pendiente de entregar el informe de seguimiento para ser evaluado del
Hito de Seguimiento. 4\. Resultados Para presentar los resultados de este
trabajo hemos deci- dido incluir sobre todo resultados cuantitativos, pero
también alguno cualitativo. Con respecto a estos últimos, se han reali- zado
encuestas a los estudiantes para conocer su opinión so- bre el proceso de
seguimiento y evaluación del TFG (espe- cialmente sobre el impacto de GEP) y
sobre el aprendizaje de las competencias transversales. En la mayoría de los
casos los estudiantes consideran que GEP les ha orientado a la hora de
plantear el TFG y opinan que sin GEP probablemente ha- brían tardado más
tiempo en acabar el proyecto. Los resulta- dos cuantitativos demuestran que
esta apreciación es del todo correcta. Con respecto a las competencias
transversales, es notable la opinión de los profesores que han ejercido de
miembros de un tribunal o de directores de un TFG. Pese a que la metodolo- gía
descrita en este trabajo despertó al principio reticencias en algunos
profesores (tanto por la existencia de GEP como por 36 ReVisión. Vol. 8, núm.
3 Figura 2: Rúbrica de evaluación del Hito Inicial del director del TFG. 37
Figura 3: Diagrama de evaluación del TFG. 38 ReVisión. Vol. 8, núm. 3 Figura
4: Resultado de la Evaluación del TFG. 39 Figura 5: Pantalla del TFG del
estudiante. 40 ReVisión. Vol. 8, núm. 3 la aparente complejidad del sistema de
evaluación del TFG), después de dos años de experiencia es prácticamente
unánime la opinión de que los estudiantes están mejor formados que antes en
gestión de proyectos y que hacen unas presentacio- nes excelentes. El sistema
de evaluación, por otra parte, no ha resultado en absoluto complejo gracias a
que la aplicación di- señada dirige el proceso en todo momento y avisa por
correo electrónico con tiempo suﬁciente a profesores y estudiantes de los
próximos pasos a seguir, ofreciendo el enlace a la pá- gina a la que se debe
acceder y la información pertinente para continuar con el proceso. Con
respecto a los resultados cuantitativos, presentamos a continuación una
comparación del tiempo que tardaban los estudiantes de los anteriores planes
de estudio en terminar su TFG frente a lo que tardan los actuales, así como el
núme- ro de estudiantes que no realizan el PFC/TFG pese a estar en disposición
de hacerlo. Los datos presentados corresponden a: El plan de estudios de 1991,
en el que se ofrecían las titulaciones de Ingeniería Informática (II),
Ingeniería Técnica en Informática de Gestión (ITIG) e Ingeniería Técnica en
Informática de Sistemas (ITIS), El plan de estudios de 2003, que consistió en
una revi- sión del plan de 1991 para adaptar las 3 titulaciones al EEES y que
nos ayudó a evitar errores en el diseño del plan de estudios del Grado en
Ingeniería Informática que diseñaríamos años más tarde, y El plan de estudios
de Grado en Ingeniería Informática de 2009 que se ofrece actualmente en la
FIB. Los pla- nes de estudios del 1991 y 2003 se han ido extinguiendo poco a
poco, pese a que algunos alumnos han esperado al último momento para presentar
su PFC, como puede verse en los resultados de la ﬁgura 6. La ﬁgura 6 muestra
en el eje vertical de cada gráﬁca el nú- mero de estudiantes que representa
cada barra, mientras que el eje horizontal indica el número de meses
transcurridos des- de la inscripción del proyecto hasta su lectura. La ﬁgura
6(a) presenta los resultados de la Ingeniería Informática del plan de 1991 y
la 6(b) la Ingeniería Informática del 2003; la ﬁgura 6(c) presenta los
resultados de la Ingeniería Técnica en Informáti- ca de Gestión del plan de
1991 y la 6(d) los del plan 2003; ﬁnalmente, la ﬁgura 6(e) presenta los
resultados de la Inge- niería Técnica en Informática de Sistemas del plan de
1991 y la 6(f) los del plan 2003. Como puede observarse en las ﬁguras 6(a) y
6(b), los PFC de la Ingeniería Informática del plan 91 duraban hasta 50 me-
ses, mientras que algunos PFC del plan de 2003 llegaron a tardar 64 meses en
leerse. Con respecto a las ingenierías téc- nicas, cuyos PFC deberían haber
tardado menos en general por tratarse de carreras de 3 años y PFC de 18
créditos (equi- valentes ECTS) frente a los 30 de los PFC de la Ingeniería
Informática, llegaron a tardar entre 72 y 90 meses en el caso de la Ingeniería
Informática de Gestión y entre 66 y 78 en el caso de la Ingeniería Informática
de Sistemas. Creemos que esto es debido a que estos estudiantes estaban más
motivados para comenzar antes su vida laboral, y por ello se “olvidaban” de la
realización de su TFG hasta que les resultaba impres- cindible presentarlo, ya
que no lo necesitaban para encontrar trabajo. Los estudiantes de Ingeniería
Informática, pese a en- contrar también trabajo mucho antes de acabar sus
estudios, parecen más motivados por obtener su título, aunque como se ve en
las gráﬁcas tampoco tenían mucha prisa. Pero más allá de la larga duración de
algunos casos pun- tuales, es interesante ver que una gran parte de los
proyectos se leían en un plazo de 12 meses en el caso de la Ingeniería
Informática (con picos signiﬁcativos en 5, 7 y 12 meses2), y que el plan de
estudios del 2003 consiguió mejorar estos re- sultados notablemente (con picos
en los mismos meses). No obstante, el tiempo previsto de lectura para estos
proyectos era de 6 meses, y en ese plazo puede comprobarse que el por- centaje
de proyectos leídos era pequeño. Además, en ambos casos existe un número
importante de PFC que tardan más de 12 meses en leerse. En las ingenierías
técnicas el resultado es similar (si no peor), con picos en los mismos meses.
La ﬁgura 7 muestra los resultados obtenidos en el Grado en Ingeniería
Informática durante los últimos dos años. Pue- de observarse que ha
desaparecido el pico del mes 12 y que prácticamente todos los estudiantes
acaban en un máximo de un año. Sólo un 1 % de los estudiantes ha tardado más
de 12 meses en acabar el TFG. Por otra parte, la ﬁgura también evi- dencia que
menos de la mitad de los proyectos se acaban en los 6 meses previstos, pese a
que el pico se halla en los 5 me- ses. Creemos que es debido a que la
normativa UPC permite extender el plazo de lectura del TFG hasta casi 1 año
pagan- do sólo las tasas después del sexto mes y eso hace que los estudiantes
se relajen. Tan importante como saber el tiempo que tardan los es- tudiantes
en acabar su proyecto es saber cuántos de ellos no llegan a acabarlo. Las
Figuras 8 y 9 muestran estos datos. La ﬁgura 8(a) muestra el número de
estudiantes de cada semestre del plan 2003 que han acabado el PFC (barras
verdes) y los que estaban en condiciones de hacerlo pero no lo presentaron
(barras amarillas). La ﬁgura 8(b) muestra los mismos datos en porcentaje. Para
cada semestre se representan 3 barras, una para cada titulación (Ingeniería
Informática, Ingeniería Téc- nica en Informática de Gestión e Ingeniería
Técnica en Infor- mática de Sistemas). Puede observarse que el porcentaje de
estudiantes que en cada semestre está en condiciones de leer el proyecto y no
lo hacía es considerablemente alto. La ﬁgura 9 muestra los mismos datos que la
ﬁgura 8 pa- ra el Grado en Ingeniería Informática. En este caso dispone- mos
de información de 4 semestres completos. El curso 2013– 2014 leyeron su TFG 24
de los 26 estudiantes que estaban en disposición de hacerlo. Durante los tres
turnos del curso 2Los estudiantes debían inscribir el proyecto antes de
matricularlo. La matrícula se realizaba a principio de semestre (febrero y
julio), y la lectura al ﬁnal (julio y febrero). Ese es el motivo de los picos
de 5 meses (febrero-julio) y 7 meses (julio-febrero). El pico de 12 meses
corresponde a estudiantes que no conseguían leer en el semestre de
matriculación y lo hacían en el siguiente (tenían dos años de tiempo desde la
inscripción). 41 Figura 6: Número de meses que han requerido para terminar el
PFC los estudiantes de (a) II91 (b) II2003 (c) ITIG91 (d) ITIG2003 (e) ITIS91
y (f) ITIS2003 Figura 7: Número de meses para terminar el TFG en el Grado en
Inge- niería Informática. 42 ReVisión. Vol. 8, núm. 3 Figura 8: Número (a) y
porcentaje (b) de estudiantes que presentan el PFC cada semestre (plan 2003).
43 Figura 9: Número (a) y porcentaje (b) de estudiantes que presentan el TFG
cada semestre (Grado). 44 ReVisión. Vol. 8, núm. 3 2014–2015 han leído 72 de
los 75 estudiantes que podían ha- cerlo (incluyendo los 2 que no lo hicieron
el curso anterior). Esto nos da un 93 % de estudiantes que podían presentar el
TFG y lo han hecho durante el curso 2013–2014 y un 96 % durante el curso
2014–2015. Estos números corresponden exclusivamente a estudian- tes que
comenzaron directamente en los estudios de Grado (a diferencia de los
presentados en la ﬁgura 7, que incluyen también los estudiantes procedentes de
convalidaciones de los anteriores planes de estudios: la Ingeniería
Informática y las Ingenierías Técnicas en Informática del 91 y del 2003). Los
estudiantes procedentes de convalidaciones no se incluyen en la ﬁgura 9 para
evitar considerar estudiantes que se habían en- quistado en el sistema. No
obstante, si consideramos también los estudiantes provenientes de
convalidaciones, en el curso 2013–2014 había 11 estudiantes que estaban en
condiciones de matricular el TFG y no lo hicieron (por 161 que ya se han
titulado), y de los 11 sólo 1 había comenzado directamente el grado. Los
resultados con este colectivo son, por lo tanto, también buenos. Se observa
que el porcentaje de estudiantes que no hacen el TFG en el Grado es muy
pequeño (3 % de los que empe- zaron directamente en el Grado y casi el 7 % si
se consideran también los procedentes de convalidaciones de las ingenierías
informáticas de los planes de estudios anteriores), lo que pa- rece indicar
que los objetivos planteados cuando se diseñó el modelo de seguimiento y
evaluación del TFG se han cumpli- do. Con respecto a la duración temporal del
TFG, la ﬁgura 10 muestra una comparación de lo que tardaban los estudiantes de
la Ingeniería Técnica en Informática de Gestión y la In- geniería Técnica en
Informática de Sistemas frente al tiempo que tardan los actuales estudiantes
de Grado. Comparamos a los estudiantes de Grado con estos colectivos porque el
tiem- po de dedicación a su PFC es similar al de un TFG. En el caso de los
estudiantes de Ingeniería Informática, el PFC era equivalente a 30 ECTS, y por
lo tanto no comparable. La ﬁgura 10 muestra el porcentaje de estudiantes de
Grado que leen el TFG (eje vertical) en función del tiempo transcu- rrido
entre la matriculación y la lectura (eje horizontal). Como puede verse en la
ﬁgura, el porcentaje de estudiantes que lee en los primeros 6–7 meses es
aproximadamente del 50 %, tal como sucedía en las ingenierías técnicas. Sin
embargo, tanto en la ITG como en la ITS se producía a partir de este momento
una importante debacle que llevaba a los estudiantes a eterni- zarse en su
PFC. Los que no lo leían en 6 meses era porque lo habían abandonado (muchas
veces por motivos laborales) o trabajaban en él de forma esporádica. Un
porcentaje de ellos, algo más de un 30 % del total, lo leían en un año más (18
me- ses en total) porque no se habían desvinculado del todo de la Facultad,
pero el resto podían tardar hasta 5 o 6 años en leerlo, y muchos de ellos aún
están pendientes de lectura. De hecho, hay 106 estudiantes de Ingeniería
Informática que aún no han leído su PFC y 62 estudiantes de alguna ingeniería
técnica que también están pendientes de hacerlo. De estos, sólo 34 han
matriculado el PFC en el caso de la Ingeniería Informática y 24 en el caso de
las ingenierías técnicas. No sabemos cuántos de los matriculados leerán. Los
112 no matriculados, sin em- bargo, sabemos a ciencia cierta que no leerán su
proyecto este curso. En el Grado, por el contrario, se observa como la gráﬁca
mantiene su pendiente, lo que sugiere que los estudiantes no abandonan,
simplemente a algunos de ellos el TFG les cuesta más que a otros por diversas
razones; probablemente la princi- pal de ellas sea compaginar su vida laboral
con la realización del TFG. Aun así, el 97 % de los estudiantes de Grado ha
con- seguido leer en menos de un año (que, por cierto, es el tiempo que la UPC
les concede para leer sin tener que matricular de nuevo el TFG y pagando los
créditos a precio de repetidor. Es- to no es, obviamente, una casualidad). Los
datos sugieren, por lo tanto, que la metodología empleada no sólo ha
conseguido que prácticamente todos los estudiantes hagan su TFG, sino que
además lo hagan en un tiempo razonable. No obstante, aún es pronto para sacar
conclusiones deﬁ- nitivas, ya que los estudiantes que han acabado estos prime-
ros cuatro semestres son los que han sido capaces de acabar el Grado en 4 o 5
años, y por lo tanto son sin duda los estudiantes más brillantes. Al menos,
sabemos que para esos estudiantes el sistema diseñado funciona. De no haber
sido así, claramente nos habríamos equivocado. 5\. Conclusiones La
implantación del EEES ha supuesto cambiar el modelo de enseñanza-aprendizaje
para implantar un sistema basado en competencias. Las competencias deben
trabajarse y eva- luarse en todas las asignaturas, y en particular en el TFG.
En este trabajo hemos presentado un modelo de segui- miento y evaluación del
TFG basado en competencias que trata de solucionar los problemas detectados en
los PFC de los planes de estudios previos al EEES: la falta de formación de
los estudiantes en temas de gestión de proyectos, la falta de trazabilidad de
la nota, la falta de seguimiento del trabajo realizado, la inﬂuencia del
tribunal en la nota y, ﬁnalmente, la cantidad de PFC que duraban mucho más
tiempo del esperado o que simplemente no llegan a presentarse. Para solventar
estos problemas se ha diseñado un modelo de seguimiento y evaluación basado en
3 hitos y una aplica- ción para facilitar a profesores, estudiantes y personal
de ad- ministración la gestión del modelo. Los resultados obtenidos, pese a
ser todavía preliminares, parecen apuntar que los obje- tivos han sido
plenamente alcanzados. Agradecimientos Este trabajo ha sido posible gracias a
la gran labor del In- Lab de la FIB, responsable del diseño de la aplicación
descrita en este trabajo. Queremos agradecer a Albert Obiols la ayuda prestada
para recopilar los datos aquí presentados. En el dise- ño de la metodología de
evaluación han participado también 45 Figura 10: Tiempo invertido en hacer el
TFG por los estudiantes del Grado en Ingeniería Informática frente al tiempo
invertido en el PFC por los estudiantes de Ingeniería Técnica en informática
de Gestión (ITG) e Ingeniería Técnica en Informática de Sistemas (ITS). los
profesores de la FIB Joan Climent, Julita Corbalán, Pau Fonseca, Jordi Garcia,
Josep Ramon Herrero, Xavier Llinàs, Horacio Rodriguez y Maria-Ribera Sancho. A
todos ellos, nuestra más sincera gratitud. Finalmente, queremos agrade- cer a
los miembros de AENUI presentes en las XXI Jornadas sobre la Enseñanza
Universitaria en Informática que otorga- sen a este trabajo el premio al mejor
artículo presentado en JENUI 2015. Referencias [1] Agència per a la Qualitat
del Sistema Universitari de Catalunya. Guia per a l’avaluació de competències
als treballs de ﬁnal de grau i de màster a les Enginyeries. 2009\. Disponible
en http://www.aqu.cat/doc/doc_ 21214293_1.pdf [2] Fermín Sánchez, Joan
Climent, Julita Corbalán, Pau Fon- seca, Jordi García, Josep-Ramon Herrero,
Xavier Llinàs, Horacio Rodriguez y Maria-Ribera Sancho. Evaluación del trabajo
Final de Grado. En Actas de las XIX Jorna- das de Enseñanza Universitaria de
la Informática, Jenui 2013, pp. 303-310. Castelló de la Plana, julio de 2013.
[3] Fermín Sánchez, Juan Climent, Julita Corbalán, Pau Fon- seca, Jordi
García, José R. Herrero, Xavier Llinàs, Ho- racio Rodriguez, Maria-Ribera
Sancho, Marc Alier, Jo- se Cabré y David López. Evaluation and assessment of
professional skills in the Final Year Project. En Actas del IEEE Frontiers in
Education Conference (FIE). Madrid, España, octubre de 2014. Dr. Fermín
Sánchez Carracedo (Barce- lona, 1962) es Técnico Especialista en Electrónica
Industrial por la E.A. SEAT (Barcelona, España, 1981), Licenciado en
Informática desde 1987 y Doctor en Informática desde 1996, los dos últimos
títulos obtenidos en la Universitat Poli- tècnica de Catalunya (UPC Barcelona-
Tech, Barcelona, España). Sus campos de estudio son la arquitectura de
computadores, la innovación docente y la educación para la sostenibilidad.
Desde 1987 trabaja como profesor en el Departament d’Arquitectura de
Computadors de la UPC, donde es pro- fesor Titular de Universidad desde 1997.
Ha sido consultor de la Universitat Oberta de Catalunya (UOC) desde 1997 hasta
2010 y Vicedecano de innovación de la Facultat d’Informàtica de Barcelona
(FIB) desde mayo de 2007 hasta junio de 2013. Desde julio de 2013 ocupa el
cargo de Adjunto de Innovación en la FIB. Tiene varias decenas de
publicaciones relaciona- das con sus temas de investigación, es revisor de
numerosas conferencias y revistas nacionales e internacionales y autor y
coautor de varios libros y capítulos de libro. Actualmente tra- baja en el
desarrollo de nuevas arquitecturas multihebra para procesadores VLIW, la
sostenibilidad en las Tecnologías de la Información y la innovación en la
educación universitaria. El Dr. Sánchez es miembro de AENUI, ha sido miembro
del Comité Directivo de JENUI desde septiembre de 2006 hasta julio de 2015 y
fue su presidente las ediciones 2011 a 2013, ha sido miembro del Comité de
Organización y Programa de diversas conferencias y otros eventos nacionales e
internacio- nales, es miembro de la ONG TxT (Tecnologia per Tothom) desde 2004
y ocupa la vicepresidencia desde 2013, es director del MAC (Museo de
Arquitectura de Computadores) desde Febrero de 2006 y miembro de la junta
directiva del Cercle Fiber-FIB Alumni desde Noviembre de 2002. 46 ReVisión.
Vol. 8, núm. 3 Jaume Moral es ingeniero informático por la FIB. Lleva desde el
año 97 tra- bajando en temas de aplicaciones web utilitzando diversas
tecnologías, espe- cialmente las basadas en Java y Oracle. Le interesa todo lo
relacionado con la seguridad en las aplicaciones web, mé- todos de
autenticación de usuarios e in- tegración de sistemas. Actualmente se ocupa
del desarrollo de la intranet de la FIB (el Racó) y ase- sora a otros
proyectos web dentro del inLab. David López (Barcelona, 1967) es pro- fesor
titular de la Universitat Politècnica de Catalunya (UPC). Licenciado y doc-
tor en informática (UPC 1991 y 1998 respectivamente), imparte clases desde
1991\. Aunque su tesis versó sobre compila- ción y arquitecturas para códigos
numé- ricos, en 2004 dio un giro radical a su in- vestigación dedicándose a la
educación, la ética y la sostenibi- lidad en la informática, habiendo
publicado más de 80 artícu- los cientíﬁcos y divulgativos en esta nueva etapa.
Ha imparti- do más de un centenar de talleres y conferencias en el tema de
competencias transversales, especialmente en temas de soste- nibilidad y
comunicación. Es responsable de la competencia Comunicación en la Facultat
d’Informàtica de Barcelona. En la actualidad, es presidente de la ONG
Tecnología para Todos (TxT) y director del Instituto de Ciencias de la
Educación de la UPC. El Dr. López es miembro de las asociaciones AENUI, SEFI y
ASEE. 2015 F. Sánchez, J. Moral, D. López Esta obra está bajo una licencia de
Creative Commons Reconocimiento-NoComercial- SinObraDerivada 4.0 Internacional
que permite copiar, distribuir y comunicar públicamente la obra en cualquier
medio, sólido o elec- trónico, siempre que se acrediten a los autores y
fuentes originales y no se haga un uso comercial.

