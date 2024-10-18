// My hello world in C, it took me 3 hours to write it and mostly to understand it.

#include <stdio.h>
#include <windows.h>

int main() {
    char hostname[MAX_COMPUTERNAME_LENGTH + 1];
    DWORD size = sizeof(hostname);

    if (GetComputerNameA(hostname, &size)) {
        printf("Hello! From: %s hostname\n", hostname);
    } else {
        printf("Error: %lu\n", GetLastError());
    }

    return 0;
}
