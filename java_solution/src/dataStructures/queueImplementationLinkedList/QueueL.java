package dataStructures.queueImplementationLinkedList;

import dataStructures.singleLinkedList.Node;

public class QueueL {
    Node front;
    Node rear;
    int size;

    public QueueL() {
        front =null;
        rear = null;
        size = 0;
    }
    public boolean isEmpty(){
        return (front==null);
    }
    public void enQueue(int data){
//        Node temp = new Node(data);
        if (rear == null){
            rear = new Node(data);
            front = rear;
            System.out.println("Node Inserted.");
            size = size +1;
            return;
        }
        rear.link = new Node(data);
        rear=rear.link;
        System.out.println("Node Inserted.");
        size = size +1;
    }
    public void peek(){
        if(isEmpty()){
            System.out.println("List is Empty");
            return;
        }
        System.out.println("The Top Most Element is : "+ front.info);
    }
    public void deQueue(){
        if(isEmpty()){
            System.out.println("the list is Empty");
            return;
        }else {
            front = front.link;
            System.out.println("The Item is deleted.");
            size = size-1;
            if (front == null){
                rear =null;
                return;
            }
            return;

        }
    }
    public void display(){
        if(isEmpty()){
            System.out.println("The list is Empty");
            return;
        }else {
            Node p = front;
            System.out.println("The Elements in the Queue are: ");
            while (p!=null){
                System.out.println(p.info+" ");
                p = p.link;
            }
        }


    }
    public int getSize(){
        return size;
    }

}
