// Ques 3
#include<bits/stdc++.h>
using namespace std;
class Node{
    public:
    int data;
    Node* next;
    Node(int val){
        data=val;
        next=NULL;
    }
   
};

void insertAtend(Node* head, int val){
    Node* n=new Node(val);
    Node* temp=head;
    while(temp->next!=NULL){
        temp=temp->next;
    }
    temp->next=n;
}
bool iscycle(Node *head){
    
    Node* slow=head;
    Node* fast=head;
    while(fast!=NULL && fast->next!=NULL){
        slow=slow->next;
        fast=fast->next->next;
        if(slow==fast){
            return true;
        }
    }
    return false;

}


int main(){
    int arr[]= {3,2,0,-4};
    int pos=1;
    Node* head=new Node(arr[0]);
    for(int i=1;i<4;i++){
        insertAtend(head,arr[i]);
    }
  
    // displayList(head);
    if(pos!=-1){
        Node* temp=head;
        Node* joinNode;
        int count=0;
        while(temp->next!=NULL){
            if(count==pos){
                joinNode=temp;
            }
            temp=temp->next;
            count++;
        }
        temp->next=joinNode;
    }

    if(iscycle(head)){
        cout<<"Cycle is present"<<endl;
    }
    else{
        cout<<"Cycle is not present"<<endl;
    }
    return 0;
       

}