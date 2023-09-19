/*******************************************************************************************************/
/*
Example program using Microsoft C V5.1 and the National Instruments GPIB card.
Connect the Sine Out to the A Input with a BNC cable.
Run this program by typing the program name followed by a space and the device name.
The device name is the name used in IBCONF to configure the National Instruments driver.
For example, if the program is called LIATEST and the above configuration is used,
then type LIATEST LIA.
Binary X and Y data will be transferred for 10 seconds to the PC using the FAST transfer command.
After the fast transfer is complete, the existing magnitude (R) data in the data buffer will be transferred
in IEEE floating point format as well as the LIA non-normalized floating point format (faster transfer) */
#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "decl.h"
#define SR830 argv[1]

/* function prototypes */

void main(int, char *[]);
void txLia(char *);
void initGpib(char *);
void setupLia(void);
void printOutBinaryResults(void);
void printOutIEEEResults(void);
void printOutLIAResults(void);


/* National Instruments Interface Function Prototypes (488.1 Calls - see the National software manual).
These are declared in "decl.h"
int
ibfind(char*);
void
ibwrt(int,char *,int);
void
ibrd(int,char *,unsigned long);
void
ibrsp(int,char *);
void
ibeos(int,int);
void
ibtmo(int,int);
*/
/* global variables */




int lia;
int rxBuf[660*2];
float rfBuf[1000];
/* SR830 handle */
/* FAST mode data buffer */
/* Floating point data buffer */
void main(int argc, char *argv[])
{
int nPts,i;
char tstr[20];
if (argc<2) {
    printf("\nUsage: liatest <devName>\n");
    exit(1);}

else
initGpib(SR830);

txLia("OUTX1"); /* Set the SR830 to output responses to the GPIB port */
setupLia(); /* Setup the SR830 */



printf("\nAcquiring Data\n");
ibtmo(lia,0);   /*  turn off timeout for lia or set the timeout longer than the scan (10 seconds). The
                    timeout measures the time to transfer the FULL number of bytes, not the time since
                    the most recent byte is received.*/


txLia("FAST2;STRD"); /* Turn FAST mode data transfer ON, then start scan using the STRD start
after delay command. The STRD command MUST be used if the scan is to
be started by this program! Do NOT use STRT. */


/* take data for 10 seconds and then stop */
ibrd(lia,(char *)rxBuf,2564L); /* get FAST mode data for 10 seconds.
10 seconds of data at 64 Hz sample rate has 64*10 + 1 points,
each point consists of X (2 bytes) and Y (2 bytes) for a total of
4*(64*10+1) = 2564 bytes. */

i=(int)ibcnt; /* save total number of bytes read */

i=(int)ibcnt; /* save total number of bytes read */

txLia("PAUS"); /* pause the data storage so no new points are taken */

printOutBinaryResults();/* format and print the results */

printf("\n%d bytes received.\nPress <Enter> to continue.",i);

getch(); printf("\n");

printf("Reading Results in IEEE Binary Format\n");

txLia("SPTS?"); /* how many points in CH1 (R) buffer? */
ibrd(lia,tstr,20L); /* get the answer */

sscanf(tstr,"%d",&nPts);/* convert from a string to an int */

printf ("SPTS?=%d\n",nPts);

sprintf(tstr,"TRCB?1,0,%d",nPts); /* use TRCB? to read the points in IEEE floating point format */

ibwrt(lia,tstr,strlen(tstr)); /* note that we cannot use txLia here because the IFC RDY bit will
not be set until the transfer is complete! */

ibrd(lia,(char *)rfBuf,(long)nPts*4L); /* read directly into a FLOAT array, 4 bytes per point */
printf ("\nReceived %d bytes in IEEE binary format\n",ibcnt);

printOutIEEEResults();
/* format and print results */
printf ("Press <Enter> to continue");
getch(); printf("\n");
printf("Reading Results in LIA Binary Format\n");
sprintf(tstr,"TRCL?1,0,%d",nPts);
/* use TRCL? to read the points in LIA floating point format */
ibwrt(lia,tstr,strlen(tstr));
/* note that we cannot use txLia here because the IFC RDY bit will
not be set until the transfer is complete! */


ibrd(lia,(char *)rfBuf,(long)nPts*4L); /* read into FLOAT array but the values are NOT floats! */
printf ("\nReceived %d bytes in LIA binary format\n",ibcnt);
printOutLIAResults();
/* format and print results */
printf ("End of Program");
}

void printOutBinaryResults(void)
{
/* calculates the first 10 values of R based on the X and Y values taken in FAST mode by the SR830 */
int i;
float x,y,r;
int *ptr;
printf("\n\n");
ptr = rxBuf; /* ptr points to the first X,Y pair of values. X and Y are each integers. */
for (i=0;i<10;i++)
{
x = (float) (*ptr++) /(float) 30000.0; /* 30000 is full scale which is 1 V in this case */
y = (float) (*ptr++) /(float) 30000.0; /* for other scales, multiply by the full scale voltage */
r = (float) sqrt(x*x + y*y);
/* compute R from X and Y */
printf("%d %e\n",i,r);
}
}

void printOutIEEEResults(void)
{
/* prints the first 10 values of R transferred in IEEE floating point format by the SR830 */
int i;
printf("\n\n");
for (i=0;i<10;i++)
printf("%d %e\n",i,rfBuf[i]);
/* this is simple since the values are already IEEE floats */
}

void printOutLIAResults(void)
{
/* calculates the first 10 values of R transferred in LIA float format by the SR830 */
int i,mant,exp;
int *ptr;
float val;
printf("\n\n");
ptr =(int *) rfBuf;
/* ptr points to integers in rfBuf, not floats! */
for (i=0;i<10;i++)
{
mant = *ptr++;
/* first comes the mantissa (16 bits) */
exp = *ptr++ - 124;
/* then the binary exponent (16 bits) offset by 124 */
val = (float) mant * (float) pow(2.0,(double) exp);
printf("%d %e\n",i,val);
}
}
void initGpib(char *devName)
{
if ((lia=ibfind(devName))<0) {
printf("\nCannot Find SR830 \n\a");
exit(1);
}
}




void txLia(char *str)
{
char serPol;
ibwrt(lia,str,strlen(str));
do {
ibrsp(lia,&serPol); /* now poll for IFC RDY */
} while ((serPol&2)==0); /* until the command finishes executing */
}
void setupLia(void)
{
txLia("*RST");
/* initialize the lock-in */
txLia("SRAT10; SEND0"); /* set 64 Hz sample rate, stop at end */
txLia("DDEF1,1,0; DDEF2,1,0");
/* set CH1=R, CH2=theta. Buffers store CH1 and CH2 */
printf("Scan is Initialized, Press <Enter> to Begin Scan...");
getch();
}