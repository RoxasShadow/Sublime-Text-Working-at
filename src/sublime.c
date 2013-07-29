#include <windows.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main() {
  HWND hwnd;
  char *title;
  
  if((hwnd = FindWindow("PX_WINDOW_CLASS", NULL)) == NULL) {
    printf("Error");
    return 0;
  }
  
  title = (char*)malloc(sizeof(char)*1024);
  GetWindowText(hwnd, title, 1024);

  printf("%s", title);

  return 0;
}