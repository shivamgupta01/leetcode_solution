package dataStructures.stackImplementattionLinkedList;
import dataStructures.singleLinkedList.Node;
import java.util.EmptyStackException;


public class StackL {
    Node top;
    int size;
    public StackL(){
        top = null;
        size = 0;
    }
    public int getSize() {
        return size;
    }
    public boolean isEmpty(){
        return (top==null);
    }
    public void push(int p){
        Node newNode = new Node(p);
        if (top==null){
            top = newNode;
            System.out.println("New Node Inserted");
            System.out.println("The Top is at:" + top.info);
            size = size +1;
            return;
        }
        else {
            newNode.link= top;
            top=newNode;
            System.out.println("New Node Inserted");
            System.out.println("The Top is at:" + top.info);
            size = size+1;
        }


    }
    public void pop(){

            if (isEmpty()){
                System.out.println(": The Node is Empty");
                throw new EmptyStackException();
            }
            else{
                top= top.link;
                System.out.println("Node Deleted");
                size = size-1;
            }
        }
    public void display(){
        Node p = top;
        System.out.println("The Items in the list are.");
        while (p!=null){
            System.out.print(p.info+" ");
            p = p .link;
        }
        System.out.println("Top at : "+ top.info);




    }
    public void peek(){
        if(isEmpty()){
            System.out.println(": The Node is Empty");
            throw new EmptyStackException();
        }else {
            System.out.println("The Top is at : " + top.info);
        }
    }
}
