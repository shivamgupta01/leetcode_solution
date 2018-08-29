package dataStructures.binaryTree;

public class Node {
    Node lchild;
    char info;
    Node rchild;

    public Node(char info) {
        this.info = info;
        lchild = null;
        rchild = null;
    }
}
