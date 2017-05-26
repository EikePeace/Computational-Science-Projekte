#include <stdio.h>
#include <stdlib.h>

struct le{
	int value;
	struct le * next;
};
typedef struct le listelement;

typedef listelement * list;

void insert(int v, list *l);
int delete_head(list *l);
void delete_all(list l);
int length(list l);
void print_list(list l);
int insert_pos(int v, int pos, list l);


	
int main(){
	list l = NULL;
	insert(10, &l);
	print_list(l);
	printf("%d\n", length(l));
	insert_pos(2,0,l);
	print_list(l);
	return 0;
}
//Wert am Anfang einfügen
void insert(int v, list *l){
	listelement * new;
	new = malloc(sizeof(listelement));
	new->value = v;
	new->next = *l;
	*l = new;
}
//Ersten Wert löschen
int delete_head(list *l){
	if (*l == NULL) return -1;
	list old = *l;
	*l = old->next;
	free(old);
	return 0;
}
//Ganze Liste löschen
void delete_all(list l){
	list next;
	while (l != NULL){
		next = l->next;
		free(l);
		l = next;
	}
}
//Länge der Liste
int length(list l) { 
	int count = 0;
	while (l != NULL) { 
		count++;
		l = l->next; 
	} 
	return count;
}
//Elemente der Liste drucken
void print_list(list l){
	if (l == NULL) printf ("leer");
	else
		while (l != NULL){
			printf("%d ", l->value);
			l = l->next;
		}
}
//Element an Position pos einfügen.
int insert_pos(int v, int pos, list l){
	int count = 0;
	while (count < pos){
		count++;
		l = l->next;
		if (l == NULL) break;
	}
	if (count < pos) return -1;
	insert (v, &l);
	return 0;
}
/*Alle Vorkommen von Element e löschen.
int delete_elem(int e, list *l){
	if (*l == NULL) return -1;
	while (l != NULL){
		if (e == value){
			list old = *l;
			*l = old->next;
			free (old);
		}
		l = l->next;
	}
	return 0;
}*/
