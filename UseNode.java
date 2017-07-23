/* 	Praxis der Programmierung
	Hausaufgabe 2
	Abgabedatum: 23.07.2017

	Gruppennummer: 64
	Gruppenmitglieder:
	- Eike Olaf Pubantz
	- Max Wiedenhöft
	- Jan Heuer
*/

public class UseNode{

  public static void main(String[] args){
    System.out.println("Aufbauen des Netwerks ohne Knoten 'E'.");
    Node a = new Node<Integer>("A", 3);
    Node f = new Node<Integer>("F", 17);
    f.connect(a);
    Node g = new Node<Integer>("G", 9);
    g.connect(a);
    g.connect(f);
    Node b = new Node<Integer>("B", 8);
    b.connect(g);
    b.connect(f);
    Node c = new Node<Integer>("C", 5);
    c.connect(f);
    Node d = new Node<Integer>("D", 1);
    d.connect(c);

    System.out.println();
    System.out.println("Erstellen von Knoten 'E'.");
    Node e = new Node<Integer>("E");
    System.out.println("Neuer Knoten: Name = " + e.getName());
    System.out.println("Setzen des Wertes.");
    e.setValue(8);
    System.out.println("Name = " + e.getName() + ", Wert = " + e.getValue());
    System.out.println();

    System.out.println("Nach Aufruf von e.connect(a):");
    e.connect(a);
    System.out.println("Sind Knoten 'E' und 'A' verbunden? " + e.isConnected(a));
    System.out.println("Nach Aufruf von e.disconnect(a):");
    e.disconnect(a);
    System.out.println("Sind Knoten 'E' und 'A' verbunden? " + e.isConnected(a));
    System.out.println();

    System.out.println("Vervollständigen des Netwerks.");
    e.connect(d);
    System.out.println();

    System.out.println("Besuchen aller Knoten (Startknoten = 'A'): ");
    System.out.println("mit Printer: ");
    a.visitAll(new Printer<Integer>());
    System.out.println();
    System.out.println("mit ValueGetter: ");
    a.visitAll(new ValueGetter<Integer>());
    System.out.println();
    System.out.println("mit Counter: ");
    a.visitAll(new Counter<Integer>());
    System.out.println();
  }

}
