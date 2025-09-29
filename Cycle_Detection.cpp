

// Complete the has_cycle function below.

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode* next;
 * };
 *
 */
bool has_cycle(SinglyLinkedListNode* head) {
    SinglyLinkedListNode* pre=head;
    SinglyLinkedListNode* nxt=head;
    if(!head){return false;}
    while(nxt!=nullptr && nxt->next!=nullptr){
        pre=pre->next;
        nxt=nxt->next->next;
        if(pre==nxt){
            return true;
        }
    }
    return false;

}

