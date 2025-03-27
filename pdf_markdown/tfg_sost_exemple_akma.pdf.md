Universitat Politècnica de Catalunya BarcelonaTECH Informe de Sostenibilitat
Índex Page 1 Descripció del projecte 1 2 Matriu de sostenibilitat 1 3 Projecte
Posat en Producció 2 3.1 Ambiental . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . 2 3.2 Econòmic . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . 4 3.3 Social . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . 5 4 Vida útil 6 4.1 Ambiental . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . 6 4.2 Econòmic . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . 7 4.3 Social . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . 8 5 Riscs 9 5.1 Ambiental
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 5.2
Econòmic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
5.3 Social . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. 10 Índex de figures 11 Índex de taules 11 Bibliografia 11 1 Descripció del
projecte AKMA Housing és un projecte que té per objectiu proveir allotjament
per a tot tipus d’inquilins, especialment aquells que són nouvinguts a les
localitats. La plataforma AKMA Housing proveeix un rànquing d’allotjaments
basat en di-ferents opcions utilitzant algoritmes de multi-criteria decision.
Aquests algoritmes tenen en compte el tipus d’allotjament, els llocs que vol
visitar o freqüenta l’inquilí, les preferències de transport i temps de
transport, el pressupost total (que inclou des-peses externes a les
directament derivades de l’allotjament) i altres característiques i serveis
urbans. 2 Matriu de sostenibilitat La matriu de sostenibilitat presenta el
resultat de l’avaluació del projecte AKMA Housing en tres grans blocs:
Projecte Posat en Producció, Vida Útil i Riscs. Per cada un dels blocs s’ha
realitzat una valoració de l’impacte ambiental, econòmic i social tant per la
fita inicial i final del projecte. PPP Vida Útil Riscs Ambiental Consum del
diseny Emprempta ecològica Ambientals Econòmic Factura Pla de viabilitat
Econòmics Social Impacte personal Impacte social Socials Figura 1: Matriu
sostenibilitat En els següents apartats de l’informe es descriu l’avaluació de
cada un dels blocs. Per cada una de les avaluacions es descriuen els aspectes
que s’han valorat i la seva justificació. La ponderació de cada un dels
apartats s’ha fet en relació a les solucions que existeixen actualment i en
els riscs o alternatives que poden tenir cada un dels aspectes. 3 Projecte
Posat en Producció El Projecte Posat en Producció o PPP avalua el projecte
AKMA Housing durnat la seva planificació, desenvolupament i implantació. 3.1
Ambiental Fita Inicial S’ha realitzat una previsió dels recursos necessaris
per desenvolupar el projecte amb un equip de 4 desenvolupadors i tenint en
compte els requeriments tecnològics propis de les característiques del
projecte i també s’ha tingut en compte l’impacte mediambiental d’aquests
recursos. Per desenvolupar el projecte AKMA Housing, cada un dels quatre
desenvolupa- dors necessita un ordinador i per desplegar el projecte fa falta
un servidor cloud com Google Cloud. A l’hora d’escollir el model d’ordinador
han entrat en joc dos variables importants: el tipus d’ordinador i la
possibilitat de ser reutilitzat. La reutilització d’ordinadors s’ha descartat,
ja que pels propis requeriments de les tecnologies amb les quals es treballa i
les infraestructures Big Data que s’han de crear, es necessiten ordinadors amb
unes característiques tecnològiques d’alt nivell; a més, es requereix un temps
de vida útil llarg, per poder utilitzar els ordinadors durant el màxim temps
possible. Per tant, els ordinadors nous amb els quals es treballarà podran ser
reutilitzats per altres persones quan esgotin la seva vida útil dins el nostre
projecte. D’aquesta manera, també ens estalviem el cost en reparacions
resultant de l’alta intensitat de les tasques computacionals que han de
realitzar. Pel que fa al model d’ordinador existeixen dues opcions: ordinador
de sobretaula i ordinador portàtil. Per tal d’escollir la més adient pel
nostre projecte s’ha valorat l’impacte mediambiental de totes dues i les
facilitats que aporten a l’usuari. Segons l’informe de Megan Bray[1]: un
ordinador portàtil necessita entre 12W i 22W quan està actiu, entre 1.5W i 6W
quan està en mode estalvi i entre 1.5W i 2W quan està apagat amb la bateria
carregada al 100%; i un ordinador de sobre taula necessita 70W quan està
actiu, 25W en mode estalvi i 1.5W quan està apagat. Si suposem un ús intensiu
de 6 h de feina, 2 h de baix consum i 16 hores que l’ordinador està apagat,
obtenim els següents consums diaris: Ordinador portàtil: 6h x 22W + 2h x 6W +
16h x 2W = 176W h Ordinador de sobretaula: 6h x 70W + 2h x 25W + 16h x 1.5W =
494W h Com podem observar els ordinadors portàtils es presenten com la millor
opció de baix consum i a més, ofereixen llibertat de moviment als
treballadors. Per tant aquest model és el que escollim tant pel
desenvolupament del projecte com per la seva futura implantació. La
infraestructura de servidors necessària per la realització i explotació del
pro-jecte no es pot desestimar, ja que és la que més consum energètic té i pot
tenir un impacte major en el medi ambient. Com que el volum d’accessos,
informació i processament que ha de ser capaç de suportar la infraestructura
és variable en el temps, optem per utilitzar una arquitectura elàstica. Les
arquitectures elàstiques permeten dotar al sistema dels recursos necessaris en
cada moment, és a dir quan el sistema necessita més recursos l’arquitectura és
capaç de proveir-ne i quan necessita menys recursos l’arquitectura és capaç de
treure’ls. D’aquesta manera sempre s’utilitzen els recursos necessaris a cada
moment i no es fa un malbaratament ni de recursos ni d’energia. Per tal de
garantir l’elasticitat del sistema s’opta per serveis de CaaS (Cloud as a
Service) com Google Cloud o IBM Bluemix. Ambdós permeten utilitzar una
arquitectura elàstica, però fa molt difícil la mesura del consum energètic del
nostre projecte. Tot i així, podem garantir que els recursos que s’utilitzen
en el nostre siste-ma sempre seran els adequats i necessaris, per tant mai hi
haurà un malbaratament de recursos pel que fa a la infraestructura. Fita Final
L’impacte ambiental del desenvolupament del projecte fins a l’estat actual, es
pot quantificar mesurant el consum energètic dels recursos destinat a cada un
dels membres de l’equip. En aquest cas, cada membre de l’equip ha destinat 600
hores a la realització del projecte. Per tant, tenint en compte els costos
energètics dels ordinadors portàtils que es van calcular en la fita inicial el
consum energètic al llarg de tot el procés de desenvolupament és equivalent al
següent: Consum energètic per treballador: (22W x 0.75 + 6W x 0.25) x 600h +
75dies x 16h x 2W = 13200W h Consum energètic total: 13.2KW h x 4treballadors
= 52.8KW h Per tal de reduir el consum energètic s’ha portat a terme
pràctiques d’estalvi ener- gètic com el consum responsable. S’ha evitat tenir
els ordinadors encesos quan no s’està treballant, utilitzar les interfícies
gràfiques dels softwares que menys consu- meixen (les que utilitzen colors més
foscos o negres) i adequar la lluminositat de la pantalla a les necessitats de
l’entorn. En tractar-se d’ordinadors portàtils també s’ha intentat treballar
sense bateria quan hi havia una font de corrent disponible. No es pot
quantificar directament l’impacte d’aquestes mesures dins del consum dels
ordinadors portàtils, per això que s’ha estimat que una quarta part de l’ús
dels ordinadors ha estat feta en baix consum. Pel que fa a l’ús de la
infraestructura Cloud, aquesta no s’ha utilitzat fins a les últimes etapes del
desenvolupament del projecte, quan era indispensable. D’aquesta manera s’ha
evitat consumir recursos abans d’hora i retardar la seva explotació, ja que
mentre que no es desplega ni es crea, no té cap cost ni consumeix re perquè no
existeix. Durant tot moment s’han ajustat els recursos als requeriments,
evitant així el malbaratament d’aquests. Per tant, sempre s’han utilitzat els
recursos necessaris i en cas de tornar a realitzar el projecte no es podria
realitzar amb menys recursos. 3.2 Econòmic Fita Inicial Per realitzar el
projecte es compta amb un equip de 4 persones, 4 ordinadors portàtils, un
compte de Cloud estimada en 300 e i material d’oficina (papers i bolis) i
impressions. Per cada desenvolupador s’ha estimat 600 hores de treball a
14€/h. Cost d’un desenvolupador: 14€ x 600h = 8400€ Cost de l’equip: 8400€ x
4persones = 33600€ Per cada ordinador portàtil s’estima un cost de 750 €: Cost
ordinadors portàtils: 750€ x 4 = 3000€ El cost total del projecte suposant 20
€ en material d’oficina i impressions, dels quals s’estimen 15 € per material
i 5 € per impressions: Concepte Cost Sous 33600 € Ordinadors 3000 € Cloud 300
€ Material oficina 20 € Total 36920 € Taula 1: Cost total PPP - Fita Inicial
Fita Final La previsió econòmica feta en la fita inicial s’ha ajustat
correctament i no ha aparegut imprevistos durant el desenvolupament del
projecte. Tot i així, s’han aportat mesures per tal de reduir els costos, les
quals han estat: • Reduir el nombre d’impressions a 0, optant així per
utilitzar material digital. D’aquesta manera s’ha aconseguit un estalvi de 5
€. • Optar per una compta gratuïta de Cloud per a desenvolupadors, la qual ens
proporciona 60 dies de prova sense cap cost. Optant per aquesta compta, s’ha
estalviat 300 €. Per tant, el cost real del projecte ha estat de 36615 €. 3.3
Social Fita Inicial A nivell d’equip i personal aquest projecte aportarà
coneixements de les noves tecnologies que s’utilitzaran i del desenvolupament
de solucions Big Data i Business Intelligence. Alhora que aporta coneixements
de gestió i creació de projectes. Per tant, a nivell personal podem situar
aquest projecte com a font de coneixement professional i tècnic. Fita Final
Durant la realització del projecte s’han assolit els coneixements
professionals i tècnics previstos; aquests també s’han enriquit gràcies a les
dificultats tècniques que s’han trobat. Tot i així, han aparegut noves
qüestions i coneixements que no s’havien contemplat, com ara: • S’ha obtingut
una visió més acurada de l’estat del parc immobiliari de la ciutat de
Barcelona, sobretot pel que fa a pisos de lloguer i pisos buits. • S’han
obtingut coneixements del funcionament dels contractes de lloguer i
arranjament. • S’ha creat un debat sobre l’ús de les dades que s’obtenen i com
tractar- les, per tal de garantir una ètica i bon ús d’aquestes. • S’ha obert
un debat sobre quina implicació pot tenir el projecte dins el negoci
immobiliari i si aquesta resultarà positiva i afavorirà la igualtat
d’oportunitats o l’empitjorarà. • En l’àmbit personal se segueix reflexionant
si aquesta és una bona solució per resoldre els problemes d’habitatge digne de
la ciutat o només aporta un canvi en el model de cerca d’habitatge. 4 Vida
útil La Vida Útil avalua el projecte AKMA Housing un cop implantat i durant el
seu procés d’execució. No es preveu el seu desmantellament, ja que aquest
projecte té per objectiu construir una empresa i no es preveu en cap cas la
seva venda o tancament. 4.1 Ambiental Fita Inicial El projecte planteja una
nova manera de buscar allotjament i de mostrar la informació, utilitzant
ordenació per múltiples criteris. Actualment les solucions que es plantegen
estan orientades al filtratge dels allotjaments i utilitzen una arquitectura
semblant a la utilitzada en aquest projecte. La nova aproximació que s’ha
plantejat requereix una mateixa arquitectura que les solucions existents, però
afegint un nivell de complexitat superior, ja que requereix més recursos
computacionals. Aquest augment de recursos computacionals respecte de les
solucions existents implica un major consum energètic. No obstant això, es
pren consciència d’aquest major consum i es busca utilitzar mesures que
permetin reduir l’impacte mediambiental en altres àmbits i accions. Fita Final
Durant el primer any de vida útil del projecte, un cop aquest s’ha
desenvolupat i constituït com empresa farà falta la següent infraestructura: •
Oficina • Mobiliari d’oficina • 6-8 ordinadors portàtils • Infraestructura de
Servidors Cloud (PaaS) El consum dels ordinadors portàtils, equivaldria a
316.8KWh, com es descriu a continuació. Consum energètic anual per
treballador: (22W x 0.75 + 6W x 0.25) x 1800h + 225dies x 16h x 2W = 39600W h
Consum energètic total: 39.6KW h x 8treballadors = 316.8KW h En aquest cas no
s’està contemplat el consum de la infraestructura de servidors, ja que és molt
complicat trobar informació precisa i verídica. Tot i així, sabem que el
consum més gran està en els servidors. Prenent consciència que la nostra
solució, pel que fa a infraestructura, no és més eficient que les solucions
actuals hem decidit prendre mesures en altres àmbits que permeten ser
sostenibles amb el medi ambient i fer prendre consciència als nostres
proveïdors, clients i treballadors. Com a empresa hem pres consciència del
problema global que implica l’e- Waste[2], per tant, seguint les Directives
Europees de RoHS[3] i WEEE [4] hem definit i fet públic un pla de gestió dels
nostres residus electrònics. També som sensibles amb les guerres i conflictes
bèlics relacionats amb el Coltan[5], també hem fet nostres els reptes de Cool
IT Challenge[6] i Greener Electronics[7] promoguts per GreenPeace com a bones
pràctiques. Per aquesta raó anualment farem públics els informes de
sostenibilitat i els sol·licitarem als nostres proveïdors i stakeholders. A
més, només treballem amb allotjaments que comptin amb un certificat oficial
d’eficiència energètica[8] o equiva-lent. També posem la sostenibilitat com a
factor decisiu en qualsevol acció o decisió que hagi de pendre AKMA Housing.
D’aquesta manera tot i sabent que la nostra solució no millorarà la petjada
eco- lògica, volem intentar reduir el màxim el nostre impacte i fer prendre
consciència. Tot i això, s’ha de tenir amb compte que amb la nostra solució
l’usuari veu tota la informació en una sola plataforma, en comptes d’haver-la
de buscar en altres serveis, cosa que fa que l’impacte de la manera de fer
actual es redueixi. 4.2 Econòmic Fita Inicial Actualment existeixen moltes
plataformes de cerca en línia d’allotjaments a la web, totes elles
constituïdes per empreses. Algunes d’aquestes empreses operen com a negocis
P2P i altres com a classificadors d’anuncis. Totes elles tenen un denominador
comú, que utilitzen filtratge envers l’ordenació de múltiples criteris que
nosaltres plantegem. En l’àmbit econòmic el nostre plantejament està en la
línia del ja existent i per tant no aportem una millora econòmica, tot i que
intentem operar amb el mínim cost possible per l’usuari, sense utilitzar
publicitat en el nostre lloc web. Fita Final En cost estimat del projecte
durant el seu primer any, s’ha contemplat una parti-da de 60000e
d’imprevistos, on s’inclouen les reparacions, possibles actualitzacions i
qualsevol imprevist o desviament. Tot i així, la despesa més important del
pri-mer any és el màrqueting, el qual es podria reduir destinant- hi menys
capital i amb conseqüència es reduiria el cost de l’assessorament extern i
altres treballadors. El desglossament de les despeses del primer any es poden
veure a la següent taula. Concepte Preu Registre de l’empresa i patents 6000€
Màrqueting inicial 1000000€ Mobiliari oficina 5000€ Hardware i PC 5000€ Domini
i Servidors Cloud (PaaS) 3000€ Sou Desenvolpadors 120000€ Assesorament extern
10000€ Altres treballadors 120000€ Lloguer oficina 15000€ Serveis 10000€
Imprevistos 60000€ Total 1354000€ Taula 2: Despeses durant el primer any 4.3
Social Fita Inicial Les plataformes web per trobar allotjament que existeixen
actual treballen uti- litzant algoritmes de filtratge, els quals només
utilitzen paràmetres com ara: nom- bre d’habitacions, barri, mobiliari i
localització. La nostra aproximació planteja la utilització d’algoritmes
d’ordenació basats en múltiples criteris, utilitzant nous pa- ràmetres a més
del que ja són utilitzats per les solucions existents, com ara: temps de
transport, proximitat als punts d’interès, equipament urbà i despeses. Aquesta
nova manera de mostrar els allotjaments proporciona més informació als
usuaris, ajudant-los a trobar l’hàbitat que més s’ajusta a les seves
necessitats. A més, també facilita la informació que d’altra manera s’hauria
de contrastar utilitzant altres serveis webs. I per altra banda, també és molt
útil per aquella gent que no coneix o no té prou coneixement del medi. Per
tant, socialment millora la qualitat de vida, en la mesura que ajuda a la gent
a trobar i obtenir més informació del pis que millor s’adapta a les seves
necessitats. A més, es resol una problemàtica existent sobre el desconeixement
del medi per totes aquelles persones que són noves a la localitat o no tenen
la informació. Fita Final El principal beneficiari d’aquest projecte serà
l’inquilí, el qual trobarà un servei més fàcil i còmode, amb molta més
informació de valor i rellevància. Això li donarà més llibertat d’elecció i
capacitat de contrastar les diferents opcions existents al mercat segons les
seves preferències. Com a valors d’empresa tenim la integració i igualtat
d’oportunitat dels col·lectius més vulnerables. Per tant, qualsevol acció que
es porti a terme a AKMA Housing buscarà i potenciarà la integració d’aquest
col·lectius. Cuando hablamos de riesgos –que no de imprevistos- nos referimos
a aquellas 5 Riscs variables que, aun pudiendo condicionar el éxito o fracaso
del proyecto, podemos identificar pero no controlar. Els Riscs fan referència
a aquells riscs que són propis del projecte i es poden preveure durant tota la
seva construcció i vida útil. Així implica que durant la vida útil sempre es
buscarà l’integració d’aquest col·lectius i assolir que almenys un 30% del
personal formi part d’algun. 5.1 Ambiental Ambientalment existeix el risc
d’augmentar la petjada ecològica del projecte a mesura que l’empresa
s’expandeixi o creixi. Això és degut al fet que l’impacte ecològic més gran
resideix en els servidors i la infraestructura PaaS, per tant com més
informació, dades i usuaris més gran és aquesta i més consumeix. Tot i això,
s’ha de tenir amb compte que amb la nostra solució l’usuari veu tota la
informació en una sola plataforma, en comptes d’haver-la de buscar en altres
serveis, cosa que fa que l’impacte de la manera de fer actual es redueixi. 5.2
Econòmic Econòmicament existeix el risc de topar-se amb iniciatives dels
governs locals o estatals que estableixin taxes especials per aquest tipus de
projectes, com ha passat amb l’Ajuntament de Barcelona i l’empresa Airbnb[9].
Per altra banda, també existeix el risc que els usuaris gestionin els
contractes a través d’empreses alienes a nosaltres i per tant, perdem els
contractes d’arranjament, els quals són els que ens aporten els ingressos, en
facturar per contracte fet. 5.3 Social En l’àmbit social no es contempla cap
risc que pugui perjudicar a algun segment de la població. Al contrari, es
contempla crear feina per col·lectius vulnerables. Bibliografia [1] M. Bray,
Review of Computer Energy Consumption and Potential Savings. adr.:
https://www.dssw.co.uk/research/computer_energy_consumption.h tml. [2] G.
Peace, The e-Waste Problem. adr.: http://www.greenpeace.org/international/
en/campaigns/detox/electronics/the-e-waste-problem/. [3] E. Parliament i the
Council of the European Union, RoHS recast Directive 2011/65/EU. adr.:
http://eur- lex.europa.eu/legal- content/EN/TXT/ ? uri=CELEX:32011L0065. [4]
E. Parliament i the Council of the European Union, WEEE Directive. adr.: http
: / / eur - lex . europa . eu / legal - content / EN / TXT / ?uri = CELEX :
32012L0019. [5] U. Nations, Security Council Condemns Illegal Exploitation of
Democratic Re-public of Congo’s Natural Resources. adr.: www . un . org /
press / en / 2001 / sc7057.doc.htm. [6] G. Peace, Cool IT Challenge. adr.:
http://www.greenpeace.org/international/ en/campaigns/climate-change/cool-it/.
[7] G. Peace, Greener Electronics. adr.:
http://www.greenpeace.org/international/ en/campaigns/detox/electronics/. [8]
E. Parliament i the Council of the European Union, The energy performance of
buildings. adr.: http://eur- lex.europa.eu/legal-content/EN/TXT/?uri=
celex:32010L0031. [9] Barcelona multa a Airbnb y Homeway con 600.000 euros por
seguir anunciando pisos sin licencia. adr.:
http://www.lavanguardia.com/local/barcelona/ 20161124/412132887490/barcelona-
multa- airbnb- homeway- pisos- sin-licencia.html.

