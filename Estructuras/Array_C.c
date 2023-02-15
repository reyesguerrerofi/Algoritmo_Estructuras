#include <stdio.h>


/* Un array es una estructura que almacena de forma
contigua los datos. Por ejemplo:

[10,23,4,6,7] 

Tiene varias operaciones:

-Insert [random]-@ O(n) ya que tiene que recorrer el arreglo de tamaño n para desplazar a la derecha
-Insert [front]-@ O(n) tiene que recorrer el arreglo de n tamaño para recorrer todo el contenido a la derecha
-Insert [back]-@ O(1) cte porque solamente tiene que insertar al final del arreglo
-Delete [front]-@O(n) por su desplazamiento a la izquierda
-Delete [back]-@O(1) por solo eliminar al final. No podemos enviar a NULL debido a que es un array con un tipo de dato especifico. Esto se tendria que hacer con apuntadores. Esto se hace en las listas ligadas
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

int DeleteBack(int array[], int size);
int DeleteFront(int array[], int size);

int main(){

//Creación de un array 
	printf("Número de elementos: ");
	scanf("%i",&size);

	for (i=0; i<=size; i++){
		scanf("%i", &array1[i]);
	}
	
	//Operaciones
	Imprime(array1,size);
	size = BackInsert(array1,size);
	size = FrontInsert(array1,size);
	size = RandInsert(array1,size);
	Imprime(array1,size);
	printf("\nNuevo size %i",size);
	size = DeleteBack(array1,size);
	Imprime(array1,size);
	printf("\nNuevo size %i",size);
	size = DeleteFront(array1,size);
	Imprime(array1,size);
	printf("\nNuevo size %i",size);
	
	return 0;
}

/*Insert e impresion*/

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

/*-----------------------------------------------------------*/
/*Eliminacion de elementos*/

int DeleteBack(int array[], int size){
	
	size--;
	
	for (i=0; i<=size; i++){
		array[i] = array[i];
	}
	return size;

}

int DeleteFront(int array[], int size){
	
	size--;
	for(i=0;i<=size;i++){
		array[i] = array[i+1];
	}
	
	return size;

}
