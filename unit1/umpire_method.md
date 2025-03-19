# **Unit 1: Notes**

## **The UMPIRE Strategy**
The **UMPIRE** method is a methodology to problem-solving that enhances clarity and efficiency during technical interviews. It stands for:  

- **Understand** – Break down the problem, ask clarifying questions, and identify edge cases.  
- **Match** – Connect the problem to known patterns, data structures, or algorithms.  
- **Plan** – Outline your approach in logical steps before coding.  
- **Implement** – Translate the plan into Python code.  
- **Review** – Walk through your code line-by-line to verify correctness.  
- **Evaluate** – Optimize for time and space complexity where necessary.  

A great mental model to **establish flow and confidence when solving coding problems**.  

---

## **Step 1: Understand the Problem**
Before jumping into coding, it’s critical to **clarify the problem** by asking relevant questions.  

### **Key Actions in This Phase:**  
#### **Ask Clarifying Questions**  
- What inputs are allowed?  
- Are there constraints on the input size?  
- What should the function return or print?  
- Should we handle edge cases (empty input, negative numbers, large numbers)?  

#### **Generate Sample Inputs & Expected Outputs**  
- Helps define behavior in normal and edge cases.  
- Example: If the input is `"abc"`, what should the output be?  

#### **Consider Edge Cases**  
- What happens if the input is empty?  
- How does the function behave with extreme values?  

#### **Analyze Time & Space Complexity**  
- What is the expected runtime efficiency?  
- Can we optimize it further?  

**Rule of Thumb:** _Always choose the simplest approach that meets the problem’s requirements._  

---

## **Step 2: Planning Phase**
Once you understand the problem, **develop a step-by-step approach** before writing any code.  

### **How to Plan Effectively:**  
- **Write the overall approach in 1-2 sentences.**  
- **List out steps to solve the problem logically.**  
- **Ensure the approach follows constraints (time complexity, space complexity, etc.).**  
- **Always have a pen & paper to visualize the logic.**  

---

## **Step 3: Implementation Phase**
This is where you **translate your plan into Python code**.  

### **Best Practices for Writing Code:**  
- **Keep your code readable and structured.**  
- **Use Python’s built-in data structures (Lists, Dictionaries, Sets, etc.).**  
- **Simplify your logic where possible.**  
- **Walk through your logic as you code.**  
- **Use proper variable names.**  

### **During an Interview:**  
- **Be vocal about your thought process.**  
- **If stuck, walk through the code line-by-line.**  
- **If unsure about syntax, ask! It’s okay to look up syntax when necessary.**  
- **Focus on problem-solving, not just writing code that works.**  

---

## **Example Demo: Writing `nanana_batman()`**

### **Problem Statement:**  
Write a function `nanana_batman(x)` that **prints** `"nanana batman!"` where `"na"` is repeated **x times**.  
**Restriction:** Do **not** use the `*` operator for string repetition.  

### **Clarifying Questions to Ask:**  
- What if `x == 0` or `x` is negative?  
- What is the max value of `x`?  
- Should we handle non-integer inputs, or can we assume `x` will always be an integer?  
- Should `"na"` be spaced apart? (e.g., `"na na na"` vs. `"nanana"`)  
- Are there performance concerns for large `x` values?  

### **Planning the Solution:**  
1. Initialize an empty string `result`.  
2. Use a loop to append `"na"` to `result`, repeating `x` times.  
3. After the loop, append `" batman!"`.  
4. Print the final string.  

### **Implementation:**  
```python
def nanana_batman(x):
    if x <= 0:
        print("Batman!")
    result = ""
    for _ in range(x):
        result += "na"

    print(result + " batman!")

# Example Calls:
nanana_batman(3)  # Output: "nanana batman!"
nanana_batman(0)  # Output: "Batman!"
nanana_batman(-2) # Output: "Batman!"

# Optimized version using list comprehension
def nanana_batman(x):
    if x <= 0:
        print("Batman!")
    print("".join(["na" for _ in range(x)]) + " batman!")

```
## **Final Interview Tips from Instructor**
- Build rapport with your interviewer
- Stay engaged and confident on camera
- Walk through UPI effectively
- Focus on clear communication, rather than just a perfect solution

## **Key Takeaways from Unit 1**
- UMPIRE strategy is essential for structured problem-solving
- Clarifying questions help understand the problem and avoid ambiguity
- Planning before coding prevents confusion
- Readable, well-structured Python code is preferred
- Interviewers value thought process more than just final code