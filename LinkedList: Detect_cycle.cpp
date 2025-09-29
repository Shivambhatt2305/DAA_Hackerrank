

/*
Detect a cycle in a linked list. Note that the head pointer may be 'NULL' if the list is empty.

A Node is defined as: 
    struct Node {
        int data;
        struct Node* next;
    }
*/

bool has_cycle(Node* head) {
    Node* pre=head;
    Node* nxt=head;
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

