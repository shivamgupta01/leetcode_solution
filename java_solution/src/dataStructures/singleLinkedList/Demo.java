package dataStructures.singleLinkedList;

import java.util.Scanner;

public class Demo {
    public static void main(String[] args) {
        int choice,data,k,x;

        Scanner scanner = new Scanner(System.in);
        SingleLinkList List = new SingleLinkList();
//        List.insertBefore(1,2);
//        List.insertAtPosition(1,1);
//        List.createList();
//        List.insertInBegining(0);
//        List.insertBefore(1,2);
//        List.insertBefore(4,5);
//        List.displayList();
//        List.countNodes();
//        List.insertAtPosition(2,2);
//        List.insertAtPosition(4,4);
//        List.insertAtPosition(8,8);
//        List.reversingList();
//        List.displayList();
//        List.countNodes();
//        List.countNodes();
//        System.out.println("If the Node is present: " + List.search(5));
//        System.out.println("If the Node is present: " + List.search(8));
//        List.insertAtPosition(10,5);
//        List.displayList();
        List.createList();
        System.out.println("Display list before Sorting");
        List.displayList();
        List.bubbleSortExData();
        System.out.println("Display list After Sorting");
        List.displayList();

    }
}
