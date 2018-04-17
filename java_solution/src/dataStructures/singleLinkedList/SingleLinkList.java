package dataStructures.singleLinkedList;

import java.util.Scanner;

public class SingleLinkList {
    public Node start;

    public SingleLinkList() {
        start = null;
    }
    //Working as Expected.
    public void displayList(){
        Node p;
        if (start ==null){
            System.out.println("list is empty");
            return;
        }
        p = start;
        System.out.println("List is ");
        while (p!=null){
            System.out.println(p.info+" ");
            p = p.link;
        }
        System.out.println();
    }
    //Working as Expected.
    public void countNodes(){
        int n = 0;
        Node p = start;
        while (p!=null){
            n++;
            p = p.link;
        }
        System.out.println("No of element in the list : " + n);

    }
    //Working as Expected.
    public boolean search(int x){

        Node p = start;

        int position = 1;
        while(p!=null){
            if (p.info == x){
                break;
            }
            position++;
            p = p.link;

        }
        if (p == null){
            System.out.println("Element not found in the list");
            return false;
        }
        else {
            System.out.println("the Element was found on Position: " + position);
            return true;
        }
    }
    //Working as Expected.
    public void insertInBegining(int data){
        Node temp = new Node(data);
        temp.link = start;
        start = temp;
    }
    //Working ss Expected.
    public void insertAtEnd(int data){
        Node p = start;
        Node temp = new Node(data);
        if (start == null){
            start = temp;
            return;
        }

        while(p.link!=null){
            p = p.link;
        }
        p.link = temp;
    }
    //Working as Expected.
    public void createList(){
        int i,n,data;
        Scanner scan = new Scanner(System.in);

        System.out.println("Enter the Number of Nodes: ");

        n = scan.nextInt();
        if (n ==0)
            return;

        for(i = 0;i<n;i++){
            System.out.println("Enter the Number to be Inserted: ");
            data = scan.nextInt();
            insertAtEnd(data);
        }
    }
    //Working as Expected
    public void insertAfter(int data,int x){
        Node p = start;

        while (p!=null){
            if (p.info == x){
                break;
            }
            p=p.link;

        }
        if (p ==null){
            System.out.println(x +": Element is not found in the list");
        }
        else {
            Node temp = new Node(data);
            temp.link = p.link;
            p.link = temp;
        }
    }
    ///Working as Expected
    public void insertBefore(int data,int x){
        Node p =start;
        if (start == null){
            System.out.println("The Node is not present in the list");
            return;
        }
        if (x == start.info){
            Node temp = new Node(data);
            temp.link = start;
            start = temp;
            return;
        }
        while(p.link!=null){
            if (p.link.info == x)
            break;

            p = p.link;
        }
        if (p.link == null){
            System.out.println("The Element is not present in the list");
        }
        else {
            Node temp = new Node(data);
            temp.link = p.link;
            p.link = temp;
        }

    }
    //Working as Expected.
    public void insertAtPosition(int data,int k){
       Node p = start;
       if (k ==1){
           Node temp = new Node(data);
           temp.link = start;
           start = temp;
           return;
       }
       /*In case you do not need to define Variable i
//       if (k == 2 && start!=null){
//           Node temp = new Node(data);
//           temp.link = start.link;
//           start.link = temp;
//           return;
     }
     while(k>2&&p!=null){
        p = p.link;
     }
     */
        int i = 1;
       while (i <k-1 && p!=null){
           i = i +1;
           p = p.link;
       }
       if (p == null){
           System.out.println("The List is too small");
           return;
       }
       else {
           Node temp = new Node(data);
           temp.link = p.link;
           p.link = temp;
       }

    }
    public void deleteFirstNode(){
        if (start == null){
            System.out.println("The list is empty, no Node deleted");
            return;
        }
        else {
            start = start.link;
        }
    }
    public void deleteLastNode(){
        if (start == null){
            System.out.println("The List is emplty, No Node Deleted");
            return;
        }
        else if(start.link == null){
            start = null;
        }
        else {
            Node p = start;
            while(p.link.link != null){
                p = p.link;
            }
            p.link = null;

        }
    }
    public void deleteNode(int x){
        Node p = start;
        if (start == null){
            System.out.println("The list is Empty");
            return;
        }
        if(start.info == x){
            start = null;
            return;
        }
        while(p.link!=null){
            if(p.link.info == x)
                break;
            p= p.link;
        }
        if (p.link == null){
            System.out.println("The Elemnt not Found in the List");
            return;
        }
        p.link = p.link.link;
    }
    //Working as expected
    public void reversingList(){
        Node prev,p,next;
        if (start==null || start.link == null){
            System.out.println("The linked list is reversed");
            return;
        }
        prev  = null;
        p = start;
        while(p!=null){
             next = p.link;
             p.link = prev;
             prev = p;
             p = next;
        }
        start = prev;
    }
    public void sortTwoList(){
    }
    public void bubbleSortExData(){
        Node p=start;
        Node q=p.link;
        Node end=null;
        if (start==null){
            System.out.println("Empty List cannot be sorted.");
            return;
        }
        while (start.link!=end){
            p=start;
            while (p.link!=end){
                q=p.link;
                if(p.info>q.info){
                    int temp = p.info;
                    p.info = q.info;
                    q.info = temp;
                }
                p = p.link;
            }
            end = q;

        }
    }
    public void bubbleSortExNode(){
        Node p=start;
        Node r = null;
        Node q=p.link;
        Node end=null;
        r.link = p;
        if (start==null){
            System.out.println("Empty List cannot be sorted.");
            return;
        }
        while (start.link!=end){
            p=start;
            while (p.link!=end){
                q=p.link;
                if(p.info>q.info){
                    p.link=q.link;
                    r.link = q;
                    q.link = p;
                    p=q;
                }
                p = p.link;

            }
            end = q;

        }

    }

}
