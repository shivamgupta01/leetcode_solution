package dataStructures.binaryTree;

public class BinaryTree {
    private Node root;
    public BinaryTree(){
        root = null;
    }

    public void display(){
        display(root,0);
        System.out.println();
    }

    private void display(Node p, int level) {
        int i ;
        if (p==null){
            return;
        }
        display(p.rchild,level+1);
        System.out.println();

        for(i =0;i<level;i++)
            System.out.print("    ");
        System.out.print(p.info);
        display(p.lchild,level+1);

    }
    public void preOrder(Node p){}
    public void inOrder(Node p){}
    public void postOrder(Node p){}
    public void levelOrder(){}
    public int height(){return 0;}
    public void createTree(){
        root = new Node('p');
        root.lchild = new Node('Q');
        root.rchild = new Node('R');
        root.lchild.lchild = new Node('A');
        root.lchild.rchild = new Node('B');
        root.rchild.lchild= new Node('X');
    }

}
