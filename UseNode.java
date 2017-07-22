public class UseNode{

  public static void main(String[] args){
    Node a = new Node<Integer>("A");
    System.out.println(a.getName());
    a.setValue(3);
    System.out.println(a.getValue());
    System.out.println();
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
    Node e = new Node<Integer>("E", 8);
    e.connect(d);
    e.connect(a);
    e.disconnect(a);

    a.visitAll(new Printer<Integer>());
    System.out.println();
    a.visitAll(new ValueGetter<Integer>());
    System.out.println();
    a.visitAll(new Counter<Integer>());
    System.out.println();
  }

}
