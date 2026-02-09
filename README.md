# ComputationalScience
 Assignment1
 Output:
<img width="1270" height="840" alt="Screenshot 2026-02-09 122501" src="https://github.com/user-attachments/assets/9d9f6c0a-79dd-4981-88ca-3cacedc6046e" />
<img width="1296" height="378" alt="Screenshot 2026-02-09 121817" src="https://github.com/user-attachments/assets/0a15b078-43c0-495c-a2f1-386369e008b4" />


 
 Summary Of the Findings:
1. Rounding is Consistently More Accurate than Truncation
The data proves that **rounding** is the superior method for approximating Pi.

* **The Evidence:** In every single test case (20th, 40th, 60th, and 100th decimal), the "Rounding Error" (Blue Line) was lower than the "Truncation Error" (Red Line).
* **The Reason:** Truncation always "chops down" the number (e.g., ), which creates a systematic error in one direction. Rounding goes to the nearest neighbor (e.g., ), which statistically keeps the average closer to the true value.

2. The "Accuracy Gap" Exists Even at High Precision
Even when using 100 decimal places—a level of precision far beyond what NASA uses—there is still a measurable difference.
 The `DIFF GAP` value in your table is always positive, meaning Truncation always resulted in a larger deviation from the "True Volume" than Rounding did.

3. Error Propagation behaves Exponentially

 Although the difference between the inputs (Truncated Pi vs. Rounded Pi) is tiny, the formula  magnifies this error.
 Your log-scale graph demonstrates that while both errors decrease as you add decimal places, the **gap** between them remains significant enough to be measured.

Conclusion for Lab Report:
This experiment demonstrates that method matters as much as precision. Simply adding more decimal places (precision) does not fix the systematic error introduced by truncation. To achieve the highest accuracy in scientific computing, rounding to the nearest digit is mathematically superior to simple truncation.
