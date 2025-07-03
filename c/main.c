#include <stdio.h>

struct element{
    int mass;
    float v;
};

void calc_vels(struct element *aElem1,struct element *aElem2);

int main(){
    struct element iElem1={1,-5};
    struct element iElem2={1,0};
    int counter=0;

    while(1){
        if(iElem1.v>iElem2.v){
            calc_vels(&iElem1,&iElem2);
            counter++;
        }

        if(iElem2.v<0){
            iElem2.v=-iElem2.v;
            counter++;
        }

        if(iElem1.v<iElem2.v && iElem1.v>=0) break;
    }

    printf("\nTotal number of impacts: %d",counter);
    
    return 0;
}


void calc_vels(struct element *aElem1,struct element *aElem2){
    float v1=aElem1->v;
    float v2=aElem2->v;

    aElem1->v=((aElem1->mass-aElem2->mass)*v1+2*aElem2->mass*v2)/(aElem1->mass+aElem2->mass);
    printf("aElem1.v --> %f\n",aElem1->v);

    aElem2->v=((aElem2->mass-aElem1->mass)*v2+2*aElem1->mass*v1)/(aElem1->mass+aElem2->mass);
    printf("aElem2.v --> %f\n",aElem2->v);
}
