Richieste:
	- Vedi Word "PW_Consegna.rtf"

Scelta delle librerie:

	Viste le difficoltà nel progetto precedente (implementazione della fisica), è stato deciso un cambio delle librerie:		
		- Arcade per il terreno di "gioco" (finestre, rendering di mappa, modelli ecc...)
		- Pymunk per la fisica																					http://www.pymunk.org/en/latest/
		- [[-InfluxDB-Python per collegare un DB temporale a python -> analisi dati con grafici in real-time]] 			https://github.com/influxdata/influxdb-python
		- [[-MySQL-python per collegare un DB relazionale a python -> analisi dati massivi]]							https://pypi.org/project/MySQL-python/
		

Incrocio e terreno:
L'idea è creare una struttura 2D (l'incrocio) sfruttando dei "cubi":

	I cubi saranno di 6 tipologie:
		- Direzione semplice (avanti/indietro - DX/SX)
		- Direzione complessa (svoltaDX/svoltaSX)
		- Cubo centrale (verticale/orizzontale in combo)
		- Cubi di spawn (entrate incrocio)
		- Cubi di despawn (uscite incrocio)
		- Cubi decisionali
			- Sarà sufficiente "ruotarli" per ottenere una variazione della direzione (ruotare vagone merci)

All'interno dei cubi di direzione semplice cè una logica per la quale un veicolo può:
	- Cambiare corsia
	- Il cambio può essere fatto piu volte, anche se il cubo è occupato (distrazione)

Analisi dei cubi: Compiti, Logica e Criticità
	- Nella realtà un veicolo può:
		- Proseguire sul proprio percorso PRESTABILITO(A->B)
		- Proseguire sul proprio percorso facendo delle VARIAZIONI (volute o non volute) -> % di incidenza 
			(nella realtà quanto spesso cambio idea?, quale % rispecchia meglio questa possibilità?)
			- Come cambio percorso nella realtà?
				- Cambio corsia/uscita ecc...
				- Cambio strada del tutto, quindi non spawno nel programma
				- Faccio inversione
			- Perchè cambio ?
				- Strada chiusa/Necessità
				- Errore umano
					- Posso cambiare?
						- Si, e sono in sicurezza
						* - Si, e me la rischio
						* - No, ma non creo incidente/traffico
						- No, ma creo incidente
*queste due sono al confine

Come dovrebbe funzionare un cubo?
	- Cubo di spawn:
		- Ce ne sono 8: uno per ogni via (due vie per ogni direzione, vedi .png in allegato "cube_concept_spawn.png")
			- La % di spawnare è così suddivisa:
				- La giornata dura 24h, dunque dividiamo il tempo in fascie, nelle quali ci sara traffico piu o meno concentrato:
				  (ridotto (1) < sostenuto (2) < intenso (3)) - Scelta fatta prendendo come riferimento dati di diversi siti (aggiungere in seguito i link)
					- 00:00_05:59 1
					- 06:00_08:59 3
					- 09:00_11:59 2
					- 12:00_13:59 3
					- 14:00_15:59 1		Sti orari possono anche andare bene.
					- 16:00_16:59 2
					- 17:00_17:59 1
					- 18:00_18:59 3
					- 19:00_23:59 1
						- Con questi dati sapremo, a priori, come gestire lo spawn dei veicoli all'avanzare del tempo.
						- A seconda dell'ora in due strade (anche non "accoppiate") dovranno spawnare MOLTI più veicoli.
		- Crea i veicoli, non fa altro.
			- Non spawna un veicolo finchè l'ultimo generato non si è spostato
		
	- Cubo di despawn:
		- Sta fuori dal campo visivo della mappa
		- La macchina ci arriva, lo attraversa e, toccato il "bordo" del cubo, muore
		
	- Cubo di direzione semplice/complessa: funziona da guardrail e da guida, la macchina ci viaggia dentro (vedi con fede sta parte)
	
	- Cubo decisionale: in riferimento alla "scelta" che un veicolo può compiere, sto cubo gestisce le variazioni di percorso.
		- Il veicolo tocca il cubo, viene posto un controllo:
			- Vuoi andare dritto sulla tua strada? (n% di probabilità (n≈100))
			- Vuoi cambiare corsia? (m% di probabilità (m<<n!)) (sta cosa nella realtà simula il 
			  mona che cambia corsia per sorpassare (tipo in autostrada) o perchè sà dove andare 
			  ma non come arrivarci e magari la prima volta fà la strada sbagliata)
			- Vuoi cambiare corsia E percorso? (o% di probabilità (o<<m<<n!))
			- Adesso è necessario fare un ragionamento:
				- Il cubo decisionale che cosa comporta a livello di map design? Nel senso, io ho una fila di cubi, che nel programma indica la strada,
				  il cubo decisionale dove lo metto? O metto il cubo che gli dice vai avanti o metto quello che gli da input diversi da quello di spawn.
				  Quindi alcuni cubi saranno entrambi? oppure come li mettiamo? Possono coincidere? Li "marchiamo"? E come?
				  
			
Analisi del terreno:

	- Manto stradale -> quadrati 2D
		- Tiles per:
			- Corsia (standard, con strisce di corsia, stop, frecce)
			- Striscie pedonali
			- Erba (e magari do pini)
			- Segnaletica (pimpinot)
			- Manca altro? (vedé valtri)
	
	- Veicoli
		- 4 Sprites/macchina
		- 4 sprites/camion
		
	- Semaforo
		- 8 semafori (due per lato)
			- 8*3 (8 per le 3 combo di colori) = 24 Sprites
			
					
Veicolo:
L'idea è integrare la fisica usando la libreria "pymunk"

Cosa servirà:
	- Classe veicolo:
		- Tipo				
		- Dimensione
		- Coeff. attr. gomme
		- Velocità
		- CND freni
			- Oltre a questo sappiamo che dovrà anche ruotare e frenare 
			  realisticamente, la lista và dunque ampliata.
			  
Analisi sul veicolo:
	- Tipo: Diciamo 3 tipi
		- Macchina
		- Camion
		- Motorin
		
	- Dimensione: A conti fatti, se la dimensione della macchina è 2, allora camion è 4 e motorin 1. Quindi immaginando la cosa in uno sprite cio che abbiamo sarebbe: 
		- Macchina: 70*30
		- Camion: 140*60
		- Motorin: 35*15
			- Ovviamente ste misure sono approssimative e verranno modificate di sicuro. Questo perchè l'oggetto dipende dalla mappa e non il contrario.
			
	- Coefficiente di attrito:
		- Fisica in da houze: qua inizia il bello, i coefficienti di attrito variano a seconda di diversi fattori:
			- Terreno: Asciutto/Bagnato (possiamo approssimare le condizioni di asfalto sdrucciolevole a )
			- Gomme: Asciutte/Bagnate/Consumate (si, posso avere gomme bagnate e asfalto asciutto, xes. pozzanghera dopo pioggia)
			
				  μAS = 1.0
				  μAD = 0.8
				  μBS = 0.7
				  μBD = 0.6
				  
				- Come si legge sta roba?
					- μ è il coefficiente di attrito, non ha unità di misura, è un numero puro
					- A e B significano Asciutto e Bagnato
					- S e D significano Statico e Dinamico
					
						Physics 101: 
							- Attrito: si manifesta tra corpo e superficie, è di tipo vettoriale ed è opposta in verso alla direzione di moto (rema contro)
								- La formula, che se ne frega se l'attrito è statico o dinamico, è questa:
									- F(a) = μ * F(┴) dove F(┴) è la forza che spinge verso il terreno il corpo, ora convinti del fatto che F = m*a e che "a" se punto verso il basso è g (9.81m/s^2)
									  La formula diventa: F(a) = μ * m * g Not bad eh? Beh sta roba è costante. g non varia, m non varia, e μ pure. 
									  Ora, da questa formula otteniamo una verità: Se la forza con cui spingo il corpo in avanti non supera il valore della forza di attrito F(a) il corpo sta fermo. 
									  
									  """Sia chiaro che F(┴) può essere scritta come sopra fintanto che sto su un piano. 
										 In un piano inclinato conta anche il valore dell'angolo, ma a noi non interessa."""
	
	- Velocità: Qua son rogne. Come lo muoviamo un corpo in un programma? 
		http://programarcadegames.com/index.php?lang=en&chapter=lab_sprite_moving
		https://arcade-book.readthedocs.io/en/latest/chapters/19_moving_sprites/moving_sprites.html
	
	
Path dei veicoli:
		
		I veicoli dovranno avere:
		
			- Un path fisso:
				- Entrata Nord (A)
					- Corsia Nord-Sud (dritto)		NS
					- Corsia Nord-Est (sinistra)	NE
					- Corsia Nord-Ovest (destra)	NO
				- Entrata Sud (B)					
					- Corsia Sud-Nord				SN
					- Corsia Sud-Est				SE
					- Corsia Sud-Ovest				SO
				- Entrata Est (C)					
					- Corsia Est-Nord				EN
					- Corsia Est-Sud				ES
					- Corsia Est-Ovest				EO
				- Entrata Ovest (D)					
					- Corsia Ovest-Nord				ON
					- Corsia Ovest-Sud				OS
					- Corsia Ovest-Est				OE
					
			- Variazioni:
				- Cubi decisionali per ogni Corsia:
					- Tutti i path possono variare in altri path compatibili:
						- Cosa si intende per compatibili/quando lo sono?
							- I veicoli dovranno poter switchare lane al bisogno.
							- Un path è compatibile con un'altro solo se spawnano nella stessa entrata
								- La decisione viene presa sulla base del ragionamento fatto in "Ordine del programma"
								
I semafori: 
	- Come li gestiamo? 
		- Meccanica: Due semafori attivi in ogni istante:
			Vedi lights.png
							

Ordine del programma: 

	- Genero le finestre di gioco -> 	TERRENO [Fullscreen toggle, (px X * px Y) base da definire, così come vsync ecc., tasto per uscire] - 
										STATISTICS [macchine spawnate, macchine incidentate, macchine attuali, T/p/U%/h, #switch corsia]
										SETTINGS [Cursori per regolare parametri ingame]

	- Visualizzo negli schermi le informazioni, in particolare nel TERRENO:
		- La mappa di gioco + semafori (indipendenti?, la logica di cambio del colore è già fatta nel vecchio codice)
		- Dopo n secondi inizia lo spawn dei veicoli
		- Il gioco continua fino a quando non lo chiudo io.

			-Creo finestra
			-Carico la mappa
			-Carico i semafori
			-Genero la classe macchina
			-Spawno il veicolo:
				-Il veicolo picka una strada in cui spawnare (regolato da: 25% per le ore "scialle" della giornata, 75% in una sola via (a rotazione in 4 fasi della giornata))
				-Il veicolo picka una strada in cui despawnare (regolato da: 33.3% per le ore "scialle" della giornata, 85% in una sola via (a rotazione in 4 fasi della giornata))
					-Il veicolo ha una % di probabilità di cambiare corsia, minore è la distanza con il semaforo (< # di cubi) e minore la probabilità.
						-Quindi il veicolo può spawnare dove gli pare, e solo DOPO decide dove andare, ammettiamo che non sappia la strada? è un pò insensato, io so dove andare
							-Allora facciamo fare una scelta: spawno e so dove andare, oppure spawno e decido in un secondo momento (quando sono in un particolare cubo)
					-La % viene calcolata secondo un numero iniziale del 10% di fare il cambio, poi cè un secondo fattore -> il cubo a fianco è libero? 
						se SI -> ok vai
						se NO -> al 90% non cambio, al 10% cambio e creo incidente/ritardo (casualità)
							se il veicolo crasha -> rimosso, crash_counter+1, e si continua
				-Il veicolo arriva al semaforo: rispetta la logica del semaforo
				-Il veicolo frena se serve altrimenti prosegue, sempre attento alla distanza di sicurezza: se il "quadrato visivo" tocca un veicolo: 
					-Attento -> si ferma (95%)
					-Mona 	 -> non si ferma (5%) -> crasha -> rimosso, crash_counter+1, e si continua
				-Il veicolo arriva al cubo di despawn. Muore.
	- In ogni istante i dati dovranno essere monitorati, ci saranno dei counter