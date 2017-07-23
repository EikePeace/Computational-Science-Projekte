/* 	Praxis der Programmierung
	Hausaufgabe 2
	Abgabedatum: 23.07.2017

	Gruppennummer: 64
	Gruppenmitglieder:
	- Eike Olaf Pubantz
	- Max Wiedenhöft
	- Jan Heuer
*/

import java.util.ArrayList;

public class Node<T>{

  private String name;
  private T value;
  private ArrayList<Node> adj;

  public Node(String name){
    this.name = name;
    this.adj = new ArrayList<Node>();
  }

  public Node(String name, T value){
    this(name);
    this.value = value;
  }

  public String getName(){
    return name;
  }

  public T getValue(){
    return value;
  }

  public void setValue(T value){
    this.value = value;
  }

  public void connect(Node<T> node){
    if (!adj.contains(node)){ // Knoten noch nicht verbunden ?
      adj.add(node);
      node.connect(this);
    }
  }

  public void disconnect(Node<T> node){
    if (adj.contains(node)){ // Knoten verbunden ?
      adj.remove(node);
      node.disconnect(this);
    }
  }

  public ArrayList<Node> visitAll(Visitor<T> v){
    ArrayList<Node> queue = new ArrayList<Node>(); // Warteschlange
    ArrayList<Node> visited = new ArrayList<Node>(); // Speichert bereits besuchte Knoten
    queue.add(this); // Startknoten in Warteschlange
    Node curNode; // Wird aktuellen Knoten speichern
    while (!queue.isEmpty()){ // Solange noch Knoten in Warteschlange
      curNode = queue.remove(0); // Ersten Knoten der Warteschlange entnehmen
      v.process(curNode); // Visitor process für aktuellen Knoten aufrufen
      visited.add(curNode); // Aktuellen Knoten zur besucht Liste hinzufügen
      for (int i = 0 ; i < curNode.adj.size() ; i++){ // Durchlaufen der Adjazenzliste des aktullen Knoten
        if (!visited.contains(curNode.adj.get(i))){ // Knoten noch nicht besucht
          if (!queue.contains(curNode.adj.get(i))){ // Knoten noch nicht in Warteschlange
            queue.add((Node)curNode.adj.get(i)); // Knoten zur Warteschlange hinzufügen
          }
        }
      }
    }
    return visited; // Zurückgeben aller besuchter Knoten
  }

  boolean isConnected(Node<T> node){
    // Ausrufen von visitAll mit Visitor-Implementierung Pass (macht nichts)
    // visited speichert dann alle Knoten die erreichbar sind
    ArrayList<Node> visited = this.visitAll(new Pass<T>());
    if (visited.contains(node)){ // Falls gesuchter Knoten in visited
      return true;
    }
    return false;
  }

}
