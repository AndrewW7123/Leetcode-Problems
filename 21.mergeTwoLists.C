// Include is used for local testing only
#include <cstdlib>

// ListNode structure definition
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    if (list1 == NULL) {
        return list2;
    }
    if (list2 == NULL) {
        return list1;
    }

    struct ListNode* result = (struct ListNode*) malloc(sizeof(struct ListNode));
    result -> val = 0;
    result -> next = NULL;
    struct ListNode* head = result;

    while ((list1 != NULL) && (list2 != NULL)) {
        if (list1 -> val <= list2 -> val) {
            result -> val = list1 -> val;
            list1 = list1 -> next;
        }
        else {
            result -> val = list2 -> val;
            list2 = list2 -> next;
        }
        result -> next = (struct ListNode*) malloc(sizeof(struct ListNode));
        result = result -> next;
    }
    while (list1 != NULL) {
        result -> val = list1 -> val;
        list1 = list1 -> next;
        if (list1 != NULL) {
            result -> next = (struct ListNode*) malloc(sizeof(struct ListNode));
            result = result -> next;
        }
        else {
            result -> next = NULL;
        }
    }
    while (list2 != NULL) {
        result -> val = list2 -> val;
        list2 = list2 -> next;
        if (list2 != NULL) {
            result -> next = (struct ListNode*) malloc(sizeof(struct ListNode));
            result = result -> next;
        }
        else {
            result -> next = NULL;
        }
    }
    return head;
}