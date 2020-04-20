
#include <stdio.h>
#include "pin.H"
#include<stdint.h>
FILE * trace;

uint64_t tmp_rax,tmp_rbx,tmp_rcx,tmp_rcx1,tmp_rdx,tmp_rdi,tmp_rsi;
// This function is called before every instruction is executed
// and prints the IP
VOID printip(VOID *ip,ADDRINT rdi,ADDRINT rsi,ADDRINT rax,ADDRINT rbx,ADDRINT rcx,ADDRINT rdx) {
    switch((__uint64_t)ip){
        //4
        case 0x040C05F:
            fprintf(trace, "array1[%ld]=array2[%ld] %ld\n", rcx,tmp_rax,rdx); 
            break;
        case 0x040C039:
            tmp_rax=rax;
            break;
        //1
        case 0x40C0BC:
            fprintf(trace, "array2[%ld]=%ld\n", rcx,rdx); 
            break;
        //3
        case 0x40C17C:
            fprintf(trace, "array2[%ld]=array1[%ld] %ld\n", rcx,tmp_rax,rdx); 
            break;
        case 0x040C118:
            tmp_rax=rax;
            break;
        //2
        case 0x040C20B:
            fprintf(trace, "array2[%ld]=array2[%ld] %ld\n", rcx,tmp_rax,rdx); 
            break;
        case 0x40C1C5:
            tmp_rax=rax;
            break;
        //5
        case 0x040C2CF:
            fprintf(trace, "push array2[%ld] %ld\n", rcx,rdx); 
            break;
        //6
        case 0x040C362:
            fprintf(trace, "pop array2[%ld] %ld\n", rcx,rdx); 
            break;
        
        //7
        case 0x40C6A8:
            fprintf(trace, "array2[%ld]+= %ld\n", rcx,tmp_rcx); 
            break;
        case 0x040C677:
            tmp_rcx=rcx;
            break;
        //8
        case 0x040C76B:
            fprintf(trace, "array2[%ld]+= array[%ld]\n", rcx,tmp_rcx); 
            break;
        case 0x40C6F4:
            tmp_rcx=rcx;
            break;
        //9
        case 0x40C803:
            fprintf(trace, "array2[%ld]-= %ld\n", rcx,tmp_rdx); 
            break;
        case 0x040C7D3:
            tmp_rdx=rcx;
            break;
        //10
        case 0x40C8C9:
            fprintf(trace, "array2[%ld]-= array[%ld]\n", rcx,tmp_rcx); 
            break;
        case 0x040C84F:
            tmp_rcx=rcx;
            break;

        //17
        case 0x40C926:
            fprintf(trace, "array2[%ld]^= %ld\n", rdx,rcx); 
            break;
        //18
        case 0x040C9C0:
            fprintf(trace, "array2[%ld]^=array[%ld]\n", rdx,tmp_rcx); 
            break;
        case 0x40C976:
            tmp_rcx=rcx;
            break;
        //r19
        case 0x040CA1D:
            fprintf(trace, "array2[%ld]|= %ld\n", rdx,rcx); 
            break;
        //20
        case 0x040CAB7:
            fprintf(trace, "array2[%ld]|=array[%ld]\n", rdx,tmp_rcx); 
            break;
        case 0x040CA6D:
            tmp_rcx=rcx;
            break;
        
        //21
        case 0x040CB18 :
            fprintf(trace, "array2[%ld]&= %ld\n", rdx,rcx); 
            break;

        //22
        case 0x40CBAA:
            fprintf(trace, "array2[%ld]&=array[%ld]\n", rdx,tmp_rcx); 
            break;
        case 0x040CB64:
            tmp_rcx=rcx;
            break;
        //11
        case 0x040CC46:
            fprintf(trace, "array2[%ld]*=%ld\n", rcx,tmp_rdx); 
            break;
        case 0x040CC16:
            tmp_rdx=rdx;
            break;

        //12
        case 0x040CD0C:
            fprintf(trace, "array2[%ld]*=array[%ld]\n", rcx,tmp_rcx); 
            break;
        case 0x040CC92:
            tmp_rcx=rcx;
            break;
        
        //13
        case 0x040CDC1:
            fprintf(trace, "array2[%ld]<<=%ld\n", rcx,tmp_rcx); 
            break;
        case 0x040CD95:
            tmp_rcx=rcx&0xff;
            break;
        //14
        case 0x040CEA4:
            fprintf(trace, "array2[%ld]<<=(array[%ld]&0x3f)\n", rcx,tmp_rcx); 
            break;
        case 0x40CE0D:
            tmp_rcx=rcx;
            break;

        //15
        case 0x40CF4A:
            fprintf(trace, "array2[%ld]>>=%ld\n", rcx,tmp_rcx); 
            break;
        case 0x40CF27:
            tmp_rcx=rcx&0xff;
            break;
        
        //16
        case 0x040D00F:
            fprintf(trace, "array2[%ld]>>=(array[%ld]&0x3f)\n", rcx,tmp_rcx); 
            break;
        case 0x040CF90:
            tmp_rcx=rcx;
            break;


        //26
        case 0x040C47B:
            fprintf(trace, "judge array2[%ld]==%ld\n", rcx,tmp_rcx); 
            break;
        case 0x0040BED4:
            tmp_rcx=rcx;
            break;
        
        //27
        case 0x040C52F:
            fprintf(trace, "judge array2[%ld]==array[%ld]\n", rcx,tmp_rcx); 
            break;
        
        //stdin
        case 0x040D115:
            fprintf(trace, "input array2[%ld]= '%c'\n", rsi,(char)rcx); 
            break;
    }   
}

// Pin calls this function every time a new instruction is encountered
VOID Instruction(INS ins, VOID *v)
{
    // Insert a call to printip before every instruction, and pass it the IP
    INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)printip, IARG_INST_PTR,IARG_REG_VALUE, REG_RDI,IARG_REG_VALUE, REG_RSI, IARG_REG_VALUE, REG_RAX , \
                    IARG_REG_VALUE, REG_RBX,IARG_REG_VALUE, REG_RCX,IARG_REG_VALUE, REG_RDX,IARG_END);
}

// This function is called when the application exits
VOID Fini(INT32 code, VOID *v)
{
    fprintf(trace, "#eof\n");
    fclose(trace);
}

/* ===================================================================== */
/* Print Help Message                                                    */
/* ===================================================================== */

INT32 Usage()
{
    PIN_ERROR("This Pintool prints the IPs of every instruction executed\n" 
              + KNOB_BASE::StringKnobSummary() + "\n");
    return -1;
}

/* ===================================================================== */
/* Main                                                                  */
/* ===================================================================== */

int main(int argc, char * argv[])
{
    trace = fopen("itrace.out", "w");
    
    // Initialize pin
    if (PIN_Init(argc, argv)) return Usage();

    // Register Instruction to be called to instrument instructions
    INS_AddInstrumentFunction(Instruction, 0);

    // Register Fini to be called when the application exits
    PIN_AddFiniFunction(Fini, 0);
    
    // Start the program, never returns
    PIN_StartProgram();
    
    return 0;
}
