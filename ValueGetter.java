public class ValueGetter<T> implements Visitor<T>{

  public void process(Node<T> node){
    System.out.println(node.getValue());
  }

}
