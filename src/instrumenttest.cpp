#include <iostream>
#include "ieee-c.h"
// #include <gpib/ib.h>

int main(){


    int dev = ibdev(0,1,0,T10s, 1, 0);
if(handle < 0){
std::cerr<< "failed to open"<<std::endl; 
return 1;}

const char* command = "OUTP?1\n";
ibwrt(dev,command,strlen(command));
char response[256];
ibrd(dev,response,sizeof(response));
std::cout<<response<<std::endl;
ibonl(dev,0);
return 0;
}