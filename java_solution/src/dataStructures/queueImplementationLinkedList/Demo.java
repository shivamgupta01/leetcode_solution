package dataStructures.queueImplementationLinkedList;

import java.util.Scanner;

public class Demo {
    public static void main(String[] args) {
        QueueL queueL = new QueueL();
        int choice, x;
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("1. Push An element on the Queue");
            System.out.println("2. Pop An element on the Queue");
            System.out.println("3. Display the Top Element");
            System.out.println("4. Display all Queue Elements");
            System.out.println("5. Display Size of the Queue");
            System.out.println("6. Quit");
            System.out.println("Enter Your Choice.");
            choice = scanner.nextInt();

            if (choice == 6) {
                break;
            }
            switch (choice) {
                case 1:
                    System.out.println("Enter the Element to be Pushed.");
                    x = scanner.nextInt();
                    queueL.enQueue(x);
                    break;
                case 2:
                    queueL.deQueue();
                    break;
                case 3:
                    queueL.peek();
                    break;
                case 4:
                    queueL.display();
                    break;
                case 5:
                    System.out.println("The size of the stack is : " + queueL.getSize());
                    break;
                default:
                    System.out.println("Wrong Input. Please Try Again.");

            }

        }
    }}
