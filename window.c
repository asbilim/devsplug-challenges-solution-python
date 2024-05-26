#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int largest_number(int* array,int size);

int* sliding_window(int* array,int size,int k);

int main(void){

    srand(time(NULL));

    int test_array[10];
    printf("initial array: ");

    for (int i = 0; i < 10; i++){
        int random_number = rand()%100;
        test_array[i] = random_number;
        printf("%d ", test_array[i]);
    }
    printf("\n");
    int* res = sliding_window(test_array,10,3);

    printf("result: ");

    for(int i = 0; i < 10-3+1; i++){
        printf("%d ", res[i]);     
    }


    return 0;
}

int largest_number(int* array,int size){

    /*
        @params size: the size of the array
        @params array: the array containing numbers

        function return an integer:the largest number in the array
    */

   int largest = 0;

   for(int i = 0; i < size; i++){
        printf("%d ",array[i]);
        if(array[i]>largest){
            largest=array[i];
        }
   }

    //   printf("the largest is %d\n",largest);

    return largest;

}

int* sliding_window(int* array,int size,int k){

    /*
        @params size: the size of the array
        @params array: the array containing numbers
        @params k: the parameter k from the challenge representing 
        the size of the window
    */

   int* result = (int*)malloc(sizeof(int)*size);


   if(k > size){
    printf("please enter a valid number for k");
    exit(1);
   }


    int outer_counter = 0;

   for(int i = 0; i < size-k+1; i++){

        int* new_array = (int*)malloc((k)*sizeof(int));
        int counter = 0;
        for(int j=i;j<i+k;j++){
            new_array[counter] = array[j];
            counter++;
        }

        int max_in_window = largest_number(new_array,k);
        printf("the largest number is %d",max_in_window);
        printf("\n");
        result[outer_counter] = max_in_window;
        outer_counter++;
   }

    return result;

}