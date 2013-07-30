#define _WIN32_WINNT 0x0500
#include <windows.h>
#include <stdio.h>

int main() {
  HWND hwnd;
  char *title;
  
  HWND dat = GetConsoleWindow();
  ShowWindow(dat, SW_MINIMIZE);
  ShowWindow(dat, SW_HIDE);
  
  if((hwnd = FindWindow("PX_WINDOW_CLASS", NULL)) == NULL) {
    printf("Error");
    return 0;
  }
  
  title = (char*)malloc(sizeof(char)*1024);
  GetWindowText(hwnd, title, 1024);

  printf("%s", title);

  return 0;
}