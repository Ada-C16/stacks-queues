package net.sophiale.deques;

import net.sophiale.linkedlists.SinglyList;
import net.sophiale.linkedlists.SinglyNode;

import java.util.ArrayList;
import java.util.List;

public class Stack<T extends Comparable>  extends  SinglyList<T> {
    SinglyNode<T> mHead;

    public void push(T value) {
        super.append(value);
    }

    public void pop() {
        super.removeHead();
    }

    public boolean empty() {
        return super.isEmpty();
    }

    public String toString() {
        SinglyNode<T> cur = mHead;
        if (cur == null) {
            return "";
        }
        StringBuilder builder = new StringBuilder();
        builder.append(cur.val.toString());
        while (cur.next != null) {
            builder.append(',');
            builder.append(cur.next.val.toString());
            cur = cur.next;
        }

        return builder.toString();
    }
}
