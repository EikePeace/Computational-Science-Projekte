#include <stdio.h>
#include <stdlib.h>

void insert(int v, list *l);
int delete_head(list *l);
void delete_all(list l);
int lenght(list l);
void print_list(list l);

int main(){
	return0;
}

void insert(int v, list *l){
	listelement * new;
	new = malloc(sizeof(listelement));
	new->value = v;
	new->next = *l;
	*l = new;
}

int delete_head(list *l){
	if (*l == NULL) return -l;
	list old = *l;
	*l = old->next;
	free(old);
	return 0;
}

void delete_all(list l){
	list next;
	while (l =! NULL){
		next = l->next;
		free(l);
		l = next;
	}
}

int lenght(list l){
	int count = 0;
	while (l != NULL){
		count++;
		l = l->next;
	}
	return count;
}

void print_list(list l){
	if (l == NULL) printf ("leer");
	else
		while (l != NULL){
			printf("%d ", l->value);
			l = l->next;
		}
}