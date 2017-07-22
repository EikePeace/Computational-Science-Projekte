public class Counter<T> implements Visitor<T>{

  private static int count = 0;

  public void process(Node<T> node){
    count++;
    System.out.println(count);
  }

}
