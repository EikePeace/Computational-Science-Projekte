/* 	Praxis der Programmierung
	Hausaufgabe 2
	Abgabedatum: 23.07.2017

	Gruppennummer: 64
	Gruppenmitglieder:
	- Eike Olaf Pubantz
	- Max Wiedenhöft
	- Jan Heuer
*/

public class Counter<T> implements Visitor<T>{

  private static int count = 0;

  public void process(Node<T> node){
    count++;
    System.out.println(count);
  }

}
