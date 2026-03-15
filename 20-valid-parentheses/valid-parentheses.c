#include <string.h>

int isValid(char* s) {
    char stack[10000];
    int top = -1;

    for(int i = 0; s[i] != '\0'; i++) {

        if(s[i]=='(' || s[i]=='{' || s[i]=='[')
            stack[++top] = s[i];

        else {
            if(top == -1) return 0;

            if((s[i]==')' && stack[top]=='(') ||
               (s[i]=='}' && stack[top]=='{') ||
               (s[i]==']' && stack[top]=='['))
                top--;
            else
                return 0;
        }
    }

    return top == -1;
}