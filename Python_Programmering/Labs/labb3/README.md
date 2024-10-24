# Lab 3

## Funktioner
Programmet läser filen "unlabelled_data.csv" i funktionen readfile() som ligger i map "lab3" och sparar datan i en lista (data). 

Listan delas upp i par (x, y) där x körs igenom f(x)=kx+m ekvationen med fasta k, m-värden för att beräkna y.  
Om listans y-värde i paret överstiger beräknat y-värde får det paret en label om 0. Motsvarande händer om y understiger beräknat y, då paret får en label om 1. 
För varje iteration appendas resultatet i en lista (data_label) som därefter skrivs i en ny csv fil. Filen består nu av tre element (x,y,label) 

Funktionen line() räknar ut alla y genom alla x med fasta k,m värden för att få fram en linje ekvation som där efter plottas i plott().
Label_data konverteras till en array och varje kolumn får ett variabelnamn som  scatterplottas.  

## Instruktioner
Programmet kör läsning, klassifiering, skrivning av fil och plot vid start. 
Om man vill påverka linjen kan man ändra k för vinkeln och m för skärning genom y. 

mvh
Dev




