package com.github.dozaza;

//给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
//
// 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
//
// 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
//
// 示例：
//
// 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
//输出：7 -> 0 -> 8
//原因：342 + 465 = 807
//
//

public class Question_0002 {

    private static class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }

    public static void main(String[] args) {
        ListNode l1 = new ListNode(5);
        l1.next = new ListNode(4);
        l1.next.next = new ListNode(5);

        ListNode l2 = new ListNode(9);
        l2.next = new ListNode(9);
        l2.next.next = new ListNode(9);
        l2.next.next.next = new ListNode(9);


        ListNode res = addTwoNumbers(l1, l2);
        System.out.println(res.val);
    }

    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode l1Head = l1;
        ListNode l2Head = l2;

        ListNode ptr = new ListNode(0);
        ListNode res = ptr;
        int carry = 0;
        while(l1Head != null && l2Head != null) {
            int sum = l1Head.val + l2Head.val + carry;
            carry = sum / 10;

            ptr.val = sum % 10;

            l1Head = l1Head.next;
            l2Head = l2Head.next;

            if (l1Head != null && l2Head != null) {
                ptr.next = new ListNode(0);
                ptr = ptr.next;
            }
        }

        if (l1Head != null || l2Head != null) {
            ptr.next = new ListNode(0);
            ptr = ptr.next;
        }

        while(l1Head != null) {
            int l1Val = l1Head.val;

            int sum = l1Val + carry;
            carry = sum / 10;

            ptr.val = sum % 10;

            l1Head = l1Head.next;

            if (l1Head != null) {
                ptr.next = new ListNode(0);
                ptr = ptr.next;
            }
        }

        while(l2Head != null) {
            int l2Val = l2Head.val;

            int sum = l2Val + carry;
            carry = sum / 10;

            ptr.val = sum % 10;

            l2Head = l2Head.next;
            if (l2Head != null) {
                ptr.next = new ListNode(0);
                ptr = ptr.next;
            }
        }

        if (carry > 0) {
            ptr.next = new ListNode(carry);
        }

        return res;
    }

}
