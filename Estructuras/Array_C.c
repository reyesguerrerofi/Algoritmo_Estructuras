#include <stdio.h>


/* Un array es una estructura que almacena de forma
contigua los datos. Por ejemplo:

[10,23,4,6,7] 

Tiene varias operaciones:

-Insert [random]-@
-Insert [front]-@
-Insert [back]-@
-Delete [front]
-Delete [back]
-Search [unsorted]
-Search [sorted]
*/

#define MAX_SIZE 100

int array1[MAX_SIZE];//Se aparta un espacio de memoria equivalente a 100, puede no ser usado en su totalidad
int size,i,nuevo,indice; //Aqui va lo que requiera la trama

int BackInsert(int array[],int size);
int FrontInsert(int array[], int size);
int RandInsert(int array[], int size);
void Imprime(int array[], int size);

int main(){

//Creación de un array 
	printf("Número de elementos: ");
	scanf("%i",&size);

	for (i=0; i<=size; i++){
		scanf("%i", &array1[i]);
	}
	Imprime(array1,size);
	size = BackInsert(array1,size);
	size = BackInsert(array1,size);
	size = FrontInsert(array1,size);
	size = RandInsert(array1,size);
	Imprime(array1,size);
	printf("Nuevo size %i",size);
	return 0;
}

int BackInsert(int array[], int size){

	size++;
	printf("Valor insertar: \n");
	scanf("%i",&nuevo);
	array[size] = nuevo;
	return size;
}

int FrontInsert(int array[], int size){
	
	size++;
	printf("Valor insertar: \n");
	scanf("%i",&nuevo);
	for (i=size; i>=1;i--){
		array[i] = array[i-1];
	}
	array[0] = nuevo;
	return size;
}

int RandInsert(int array[],int size){

	size++;
	printf("Valor insertar: \n");
	scanf("%i",&nuevo);
	printf("Indice: \n");
	scanf("%i",&indice);
	for (i=size;i>=indice+1;i--){
		array[i] = array[i-1];
	}
	array[indice] = nuevo;
	return size;
}

void Imprime(int array[], int size){

	printf("Imprime array \n");//Se recorre el array y se imprime su contenido uno a la vez
	for (i=0;i<=size; i++){
		printf("%i ",array1[i]);
	}
}
