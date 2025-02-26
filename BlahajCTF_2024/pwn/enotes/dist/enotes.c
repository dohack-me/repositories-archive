//gcc enotes.c -o enotes -no-pie
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>
#include <signal.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define MAX_MESSAGES 256
#define MESSAGE_SIZE 1024

void *notes[MAX_MESSAGES];
int isadmin = 0;

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    char buffer[1032];
    int index;

    fprintf(stdout, "Welcome to Enotes, private edition!\nCollaborate with your friends to take notes!\n");
    fprintf(stdout, "Commands: new/read/write/delete/quit/shutdown.\n");

    while (1) {
        if (fscanf(stdin, "%1024s", buffer) == EOF) break;
        if (strcmp(buffer, "read") == 0) {
            if (fscanf(stdin, "%d", &index) == EOF) break;
            if (index >= MAX_MESSAGES || index < 0)
                fprintf(stdout, "ERROR!!!\n");
            else{
                if (notes[index]) {
                    fprintf(stdout, "NOTE: ");
                    fwrite((char*)notes[index], 1, MESSAGE_SIZE, stdout);
                } else {
                    fprintf(stdout, "NOTE: (empty)\n");
                }
            }
        } else if (strcmp(buffer, "new") == 0) {
            if (fscanf(stdin, "%d", &index) == EOF) break;
            if (index >= MAX_MESSAGES || index < 0)
                fprintf(stdout, "ERROR!!!\n");
            else{
                notes[index] = malloc(MESSAGE_SIZE);
            }
        } else if (strcmp(buffer, "write") == 0) {
            if (fscanf(stdin, "%d", &index) == EOF) break;
            if (index >= MAX_MESSAGES || index < 0)
                fprintf(stdout, "ERROR!!!\n");
            else{
                char *target = notes[index] ? notes[index] : buffer;
                fscanf(stdin, "%1024s", target);
            }
        } else if (strcmp(buffer, "delete") == 0) {
            if (fscanf(stdin, "%d", &index) == EOF) break;
            if (index >= MAX_MESSAGES || index < 0)
                fprintf(stdout, "ERROR!!!\n");
            else{
                if (notes[index]) {
                    free(notes[index]);
                    notes[index] = 0;
                }
            }
        } else if (strcmp(buffer, "shutdown") == 0) {
            if(isadmin)
                exit(0);
            else
                fprintf(stdout, "Admin not here, we cannot shut down!\n");
        } else if (strcmp(buffer, "quit") == 0) {
            break;
        } else {
            fprintf(stdout, "Unrecognized choice!\n");
        }
    }
    return 0;
}