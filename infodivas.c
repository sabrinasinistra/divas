#include<stdio.h>
#include<stdlib.h>

//Modifica o arquivo dadosleitura.txt, um exemplo do que vamos usar para modificiar o arquivo
int main(void){
     /*Cria um ponteiro do tipo FILE e usa a função
       fopen passando como argumentos o nome do arquivo
       a ser aberto e o modo em que vai ser aberto
       (w+ significa write and read, escrita e leitura
     */
     FILE *fp = fopen("dadosleitura.txt", "w+");

     //Usa a função fprintf para escrever no arquivo
     //passa como argumento o ponteiro para o arquivo e a frase a ser escrita
     fprintf(fp, "Sabrina Diva");

     //Fecha o arquivo
     fclose(fp);

     return 0;
}

