package dataStructures.stackImplementationArrayList;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Demo {

    public static void main(String[] args) {
        int choice,x;
        StackArray stackArray;

        Scanner scanner = new Scanner(System.in);
        System.out.println("Choose the Size of Stack: ");
        System.out.println("1. Custom Size ");
        System.out.println("2. Default Size: 10.");
        try {
            x = scanner.nextInt();
            if (x == 1){
                System.out.println("Enter The size of the Stack: ");
                x = scanner.nextInt();
                stackArray = new StackArray(x);

            }
            else if(x==2){
                System.out.println("The Stack has been created with Size 10.");
                stackArray = new StackArray();
            }
            else {
                System.out.println("The Input Not Allowed.");
                System.out.println("The Stack has been created with Size 10.");
                stackArray = new StackArray();
            }
        }catch (InputMismatchException inputMismatchException){
            System.out.println("The Input Not Allowed.");
            System.out.println("The Stack has been created with Size 10.");
            stackArray = new StackArray();
        }



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
                    stackArray.push(x);
                    break;
                case 2:
                    stackArray.pop();
                    break;
                case 3:
                    stackArray.peek();
                    break;
                case 4:
                    stackArray.display();
                    break;
                case 5:
                    System.out.println("The size of the stack is : " + stackArray.size());
                    break;
                default:
                    System.out.println("Wrong Input. Please Try Again.");

            }
        }

    }

}
