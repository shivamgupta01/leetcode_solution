package dataStructures.stackImplementattionLinkedList;

import java.util.Scanner;

public class Demo {
    public static void main(String[] args) {
        StackL stackL = new StackL();
        int choice,x;
        Scanner scanner = new Scanner(System.in);
        while (true){
            System.out.println("1. Push An element on the stack");
            System.out.println("2. Pop An element on the stack");
            System.out.println("3. Display the Top Element");
            System.out.println("4. Display all Stack Elements");
            System.out.println("5. Display Size of the stack");
            System.out.println("6. Quit");
            System.out.println("Enter Your Choice.");
            choice = scanner.nextInt();

            if (choice == 6){
                break;
            }
            switch (choice){
                case 1:
                    System.out.println("Enter the Element to be Pushed.");
                    x= scanner.nextInt();
                    stackL.push(x);
                    break;
                case 2:
                    stackL.pop();
                    break;
                case 3:
                    stackL.peek();
                    break;
                case 4:
                    stackL.display();
                    break;
                case 5:
                    System.out.println("The size of the stack is : " + stackL.getSize());
                    break;
                default:
                    System.out.println("Wrong Input. Please Try Again.");

            }
        }
    }

}
