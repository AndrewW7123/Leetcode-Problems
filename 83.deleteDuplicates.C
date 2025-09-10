// Include is used for local testing only
#include <cstddef>

// ListNode structure definition
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* deleteDuplicates(struct ListNode* head) {
    if (head == NULL) {
        return NULL;
    }

    struct ListNode* result = head;
    struct ListNode* prev = head;
    head = head -> next;

    while (head != NULL) {
        if (prev -> val == head -> val) {
            head = head -> next;
            prev -> next = head;
        }
        else {
            prev = head;
            head = head -> next;
        }
    }
    
    return result;
}