package dataStructures.stackImplementationArrayList;
import java.util.EmptyStackException;

public class StackArray {
    int top ;
    int[] stack ;
    public StackArray(int maxSize){
        stack = new int[maxSize];
        top = -1;
    }
    public StackArray(){
        stack = new int[10];
        top = -1;
    }
    public int size(){
        return (top+1);
    }
    public boolean isEmpty(){
        return (top ==-1);
    }
    public boolean isFull()
    {
        return (top == stack.length-1);
    }
    public void push(int item){

        if(isFull()){
            System.out.println("The Stack is already full");
            return;
        }

        top = top+1;
        stack[top] = item;
        System.out.println("Element is inserted at top.");

    }
    public void pop(){
        try {

        if(isEmpty()){
            System.out.println("Stack Underflow");
            throw new EmptyStackException();
        }
        else {
            System.out.println("Deleted Item: "  +stack[top]);
            stack[top] = 0;
            top -=1;

        }}
        catch (EmptyStackException emptyStackException){
            System.out.println(emptyStackException +"Try Again");
        }
    }
    public void peek(){
        try {
            if (isEmpty()) {
                System.out.println("The stack is empty.");
                return;
            } else {
                System.out.println("The top most element is : " + stack[top]);
            }
        }catch (EmptyStackException emptyStackException){
            System.out.println(emptyStackException + " Try Again");
        }
    }
    public void display(){
        try{
        if(isEmpty()){
            System.out.println("The stack is empty.");
            throw new EmptyStackException();
        }else {
            System.out.println("The Element is the Stack are");

            for (int i = top; i >= 0; i = i - 1) {
                System.out.print(stack[i] + " ");
            }
            System.out.println("");
            System.out.println("The Top At :" + stack[top]);
        }
    }catch (EmptyStackException emptyStackException){
            System.out.println(emptyStackException+" Try Again");
        }
    }
}
