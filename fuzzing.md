## Answers to Lab Exercise 3 Part 2 - SeiP 2024
Name: Kyriaki Darivaki
### Task 1
Answer: 
### Task 2
Backtrace:
#0  0x00007ffff7aef9fc in pthread_kill () from /lib/x86_64-linux-gnu/libc.so.6
#1  0x00007ffff7a9b476 in raise () from /lib/x86_64-linux-gnu/libc.so.6
#2  0x00007ffff7a817f3 in abort () from /lib/x86_64-linux-gnu/libc.so.6
#3  0x000055555555cd17 in Airplane::interact (this=0x5555557722c0)
    at /Users/kdari/Desktop/SEIP-assignments/Fuzzing-Module-SEiP/exercise2/airplane_object.cpp:68
#4  0x000055555555d0e3 in main (argc=<optimized out>, argv=<optimized out>)
    at /Users/kdari/Desktop/SEIP-assignments/Fuzzing-Module-SEiP/exercise2/main.cpp:26
Answer: 
...