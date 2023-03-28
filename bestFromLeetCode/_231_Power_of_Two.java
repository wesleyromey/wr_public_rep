/*
// Leetcode Template:
class Solution {
    public boolean isPowerOfTwo(int n) {

    }
}
*/


// Leetcode Solution:
//  NOTE: I changed the class name for convenience
/*
class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n <= 0) return false;
        while(n % 2 == 0) n /= 2;
        return (n == 1);
    }
}
*/

// Extra code I need to make this work
import java.util.Scanner;

class _231_Power_of_Two {
    public static void main(String[] args) {
        // Generate the input
        System.out.print("Enter an integer: ");
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        input.close();
        boolean ans = false;

        // This is the solution I wrote
        if (n <= 0) {
            ans = false;
        } else {
            while(n % 2 == 0) n /= 2;
            ans = (n == 1);
        }

        // Report the answer
        System.out.print("isPowerOfTwo(" + n + "): ");
        System.out.print(ans);
    }

}