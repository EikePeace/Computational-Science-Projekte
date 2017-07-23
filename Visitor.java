/* 	Praxis der Programmierung
	Hausaufgabe 2
	Abgabedatum: 23.07.2017

	Gruppennummer: 64
	Gruppenmitglieder:
	- Eike Olaf Pubantz
	- Max Wiedenhöft
	- Jan Heuer
*/

public interface Visitor<T>{

  public void process(Node<T> node);
  
}
