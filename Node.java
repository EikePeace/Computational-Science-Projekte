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

  public void visitAll(Visitor<T> v){
    ArrayList<Node> queue = new ArrayList<Node>();
    ArrayList<Node> visited = new ArrayList<Node>();
    queue.add(this);
    Node curNode;
    while (!queue.isEmpty()){
      curNode = queue.remove(0);
      v.process(curNode);
      visited.add(curNode);
      for (int i = 0 ; i < curNode.adj.size() ; i++){
        if (!visited.contains(curNode.adj.get(i))){
          if (!queue.contains(curNode.adj.get(i))){
            queue.add((Node)curNode.adj.get(i));
          }
        }
      }
    }
  }

  boolean isConnected(Node<T> node){
    return true;
  }

}
