## Answers to Lab Exercise 3 Part 2 - SeiP 2024
Name: Kyriaki Darivaki
### Task 1
**Answer:** 
From a total of 3 saved crashes, using gdb, hex and looking through the code & crash files I got the following notes:
1. Most crashes were detected at around 150 test cases executed.
2. Inputs starting with 0x00 are frequently detected causing the call of the abort function:
```
if(str[0] == 0 || str[str.length() - 1] == 0) {
    abort();
}
```
3. In some cases I found that a part of the input had a sequence of consecutive increasing digits between 48 and 57 ASCII (so digits 0-9), causing the condition inside the loop to become true:
```
while (count != str.length() - 1) {
    char c = str[count];
    if(c >= 48 && c <= 57) { // If c is a digit (0-9)
        if(c == prev_num + 1) { // If c is one greater than prev_num
            abort();
        }
        prev_num = c;
    }
    count++;
}
```
<p>Note: most hexademical representations i got from hexdump -C were translated to non-printable ASCII characters, so these asumptions are not necessarily a rule, also considering the small number of saved crash files.</p> 

### Task 2
**Answer:**
Using the same methods as the first exercise, with 7 saved crashes i got the following input descriptions:
1. All the inputs involving the character 'l', when the crew number is zero cause a crash, as shown in this code snippet:
```
} else if (input[i] == 'l') {
    if (crew.num == 0) {
        abort();
    }
    land();
}
```
2. All inputs with a total of crew members different from zero (where total crew members= initial crew number + number of 'h' chars) and 'f' chars as many as the crew, followed by 'l' are certain crashes.   

<p>Suggestion: In some cases, I noticed 't' as the last char of the input, so the absence of the 'l' could be handled by some abortion logic, as the plane can't fly eternally and will eventually crash.</p>

### Task 3
**Answer:**
