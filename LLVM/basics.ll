; ModuleID = basics

; Exploring the basics in the LLVM documentation - https://llvm.org/docs/LangRef.html#abstract
; Author: Andrew Jarombek
; Date: 2/18/2020

@formatString = private constant [4 x i8] c"%d\0A\00"

declare i32 @printf(i8* noalias nocapture, ...)

define i32 @add31(i32) #0 {
    ; alloca allocates memory on the stack frame of the currently executing function.   This memory is automatically
    ; released when the function retuns (the stack frame is popped off the programs execution stack).
    ; https://llvm.org/docs/LangRef.html#alloca-instruction
    ; yields i32*:ptr
    %2 = alloca i32, align 4
    ; store writes data to memory.  The following command stores the function argument %0 to the memory allocated
    ; in the prior alloc command.
    store i32 %0, i32* %2, align 4
    ; load is used to read from memory.
    %3 = load i32, i32* %2, align 4
    ; nsw stands for 'No Signed Wrap', meaning that a signed integer overflow is not allowed.  There is a corresponding
    ; nuw (No Unsigned Wrap) command as well.
    ; https://llvm.org/docs/LangRef.html#id96
    %4 = add nsw i32 %3, 31
    ret i32 %4
}

define i32 @main() {
entry:
    ; Print the result of 1 + 2
    %x = add i32 1, 0
    %y = add i32 2, 0
    %z = add i32 %x, %y
    %call = call i32 (i8*, ...)
                @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @formatString, i32 0, i32 0), i32 %z)

    ; Integers can be varying sizes, including a single bit.
    %bit = add i1 0, 0
    call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @formatString, i32 0, i32 0), i1 %bit)

    %bit2 = add i1 %bit, 1
    call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @formatString, i32 0, i32 0), i1 %bit2)

    ; Perform arithmetic 12 + 31
    %mem = alloca i32, align 4
    store i32 12, i32* %mem, align 4
    %mnth = load i32, i32* %mem, align 4
    %res = call i32 @add31(i32 %mnth)
    call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @formatString, i32 0, i32 0), i32 %res)

    ret i32 0
}