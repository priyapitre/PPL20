flight(paris,united,toulouse,35,120).
flight(toulouse,united,paris,35,120).
flight(toronto,aircanada,london,500,360).
flight(london,aircanada,toronto,500,360).
flight(toronto,united,london,650,420).
flight(london,united,toronto,650,420).
flight(toronto,aircanada,madrid,900,480).
flight(madrid,aircanada,toronto,900,480).
flight(toronto,united,madrid,950,540).
flight(madrid,united,toronto,950,540).
flight(toronto,iberia,madrid,800,480).
flight(madrid,iberia,toronto,800,480).
flight(madrid,aircanada,barcelona,100,60).
flight(barcelona,aircanada,madrid,100,60).
flight(madrid,iberia,barcelona,120,65).
flight(barcelona,iberia,madrid,120,65).
flight(barcelona,iberia,london,220,240).
flight(london,iberia,barcelona,220,240).
flight(barcelona,iberia,valencia,110,75).
flight(valencia,iberia,barcelona,110,75).
flight(madrid,iberia,valencia,40,50).
flight(valencia,iberia,madrid,40,50).
flight(madrid,iberia,malaga,50,60).
flight(malaga,iberia,madrid,50,60).
flight(malaga,iberia,valencia,80,120).
flight(valencia,iberia,malaga,80,120).

airport(toronto,50,60).
airport(london,75,80).
airport(madrid,75,45).
airport(barcelona,40,30).
airport(valencia,40,20).
airport(malaga,50,30).
airport(paris,50,60).
airport(toulouse,40,30).

pathflight(X,Z) :- flight(X,_,Z,_,_).
pathflight(X,Z) :- flight(X,_,Y,_,_) , pathflight(Y,Z).


checkcheap(A,C,B) :- flight(A,C,B,D,_),
			D<400.

twoflights(X,Y) :- flight(X,_,Z,_,_) , flight(Z,_,Y,_,_).


prefered(A,C,B) :- checkcheap(A,C,B); C==aircanada.



displayflight():-forall(flight(P,Q,R,S,T),(write(P),write("\t"),write(Q),write("\t"),write(R),write("\t"),write(S),write("\t"),writeln(T))).

displayairport():-forall(airport(P,Q,R),(write(P),write("\t"),write(Q),write("\t"),writeln(R))).


checkimplication(A,B) :- not(flight(A,united,B,_,_)) ; flight(A,aircanada,B,_,_).
