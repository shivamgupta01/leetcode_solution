package dataStructures.queueImplementationArray;

import java.util.EmptyStackException;

public class QueueArray {
    int[] queue ;
    int front;
    int rear;
    int lengthofQueue;

    public QueueArray(int maxSize) {
        queue = new int[maxSize];
        rear=-1;
        front = -1;
        lengthofQueue = maxSize;
    }
    public QueueArray(){
        queue = new int[10];
        rear = -1;
        front = -1;
        lengthofQueue = 10;
    }
    public int size(){
        if(isEmpty()){
            return 0;
        }
        else if (rear>=front){
            return (rear-front+1);
        }else {
            return ((rear)+(queue.length-front)+1);
        }
            }
    public boolean isEmpty(){
        if(rear == -1){
            return true;
        }
        else return false;
    }
    public boolean isFull(){
        if (rear>=front){
            return ((rear-front+1)==queue.length);
        }else {
            return (((rear)+(queue.length-front)+1)==queue.length);
        }
    }
    public void enQueue(int item){
        if(isFull()){
            System.out.println("The Queue is full.");
            return;
        }else {
            if(front == -1){
                front = 0;
            }
            if (lengthofQueue-1-rear>0) {
                rear = rear + 1;
            }else if (lengthofQueue-1-rear ==0) {
                rear = 0;
            }
            }
            queue[rear] = item;
            System.out.println("Item Inserted.: " + item);
        }
    public void deQueue(){
        if(isEmpty()){
            System.out.println("The Queue is already Empty.");
            return;
        }else {
            if(front==rear){
                front=-1;
                rear = -1;
            }
            else if(front!=lengthofQueue-1){
                System.out.println("The Item is deleted.");
                front = front+1;
                return;
            }
            else {
                System.out.println("The Item is deleted: "+queue[front]);
                front = 0;
            }

        }
    }
    public void peek(){
        if (isEmpty()){
            System.out.println("The queue is Empty.");
            return;
        }else {
            System.out.println("The First Element in the queue is : " + queue[front]);
            return;
        }
    }
    public void display(){
        if(isEmpty()){
            System.out.println("The Queue is Empty.");
            return;
        }else if(rear>=front){
            System.out.println("The elements in the Queue are : ");
            for (int i = front;i<=rear;i++){
                System.out.println(queue[i]+" ");
            }
        }else {
            System.out.println("The element in the Queue are: ");
            for (int i = front;i<lengthofQueue;i++){
                System.out.println(queue[i] + " ");
            }
            for (int i = 0;i<=rear;i++){
                System.out.println(queue[i]+" ");
            }
        }
    }

}
