<h4>Objective</h4>
In this challenge, we're going to learn about the difference between a class and an instance; because this is an Object Oriented concept, it's only enabled in certain languages.

<h4>Task</h4>
Write a Person class with an instance variable, age, and a constructor that takes an integer, initialAge, as a parameter. The constructor must assign initialAge to age after confirming the argument passed as initialAge is not negative; if a negative argument is passed as initialAge, the constructor should set age to 0 and print Age is not valid, setting age to 0.. In addition, you must write the following instance methods:
<br>
1. yearPasses() should increase the age instance variable by 1.<br>
2. amIOld() should perform the following conditional actions:<br>
If age<13 >, print You are young..<br>
If age>=13 and age<18>, print You are a teenager..<br>
Otherwise, print You are old..<br>
To help you learn by example and complete this challenge, much of the code is provided for you, but you'll be writing everything in the future. The code that creates each instance of your Person class is in the main method. Don't worry if you don't understand it all quite yet!
<br>
Note: Do not remove or alter the stub code in the editor.<br>

<h4>Input Format</h4>

Input is handled for you by the stub code in the editor.<br>

The first line contains an integer, T (the number of test cases), and the T subsequent lines each contain an integer denoting the age of a Person instance.

<h4>Output Format</h4>

Complete the method definitions provided in the editor so they meet the specifications outlined above; the code to test your work is already in the editor. If your methods are implemented correctly, each test case will print 2 or 3 lines (depending on whether or not a valid initialAge was passed to the constructor).

<h4>Sample Input</h4>

4<br>
-1<br>
10<br>
16<br>
18<br>
<h4>Sample Output</h4>

Age is not valid, setting age to 0.<br>
You are young.<br>
You are young.<br>
<br>
You are young.<br>
You are a teenager.<br>
<br>
You are a teenager.<br>
You are old.<br>
<br>
You are old.<br>
You are old.<br>