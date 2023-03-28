package _983_Min_Cost_For_Tickets;
// Problem link: https://leetcode.com/problems/minimum-cost-for-tickets/description/

/*
// Leetcode Template:
class Solution {
    public int mincostTickets(int[] days, int[] costs) {

    }
}
*/



// Leetcode Solution:
//  NOTE: I changed the class name for convenience
class _983 {
    public static int getMin(int[] args){
        int ans = args[0];
        for(int num : args) {
            ans = (num < ans ? num : ans);
        }
        return ans;
    }
    // This function is proven to work
    public static int getEarliestIndex(int[] days, int iCur, int numDays){
        // iCur is the index of ans we are trying to fill in
        // numDays is the number of days the ticket is valid for
        //int ans = iCur;
        for(int i = iCur-1; i >= 0; i--){
            if (days[iCur] - days[i] >= numDays) {
                return i; // i or ++i ?
            }
        }
        return -1;
    }
    public static int getBest(int[] days, int[] costs, int[] ans, int iCur){
        assert 0 <= iCur && iCur < days.length;
        int[] arrI = {getEarliestIndex(days, iCur, 1), getEarliestIndex(days, iCur, 7), getEarliestIndex(days, iCur, 30)};
        int[] arr = new int[3];
        for(int i = 0; i < arrI.length; i++) {
            if(arrI[i] == -1) arr[i] = costs[i];
            else arr[i] = ans[arrI[i]] + costs[i];
        }
        //printArr(arrI, "  arrI");
        //printArr(arr,  "  arr ");
        return getMin(arr);
    }
    public int mincostTickets(int[] days, int[] costs) {
        int[] ans = new int[days.length];
        for(int i = 0; i < days.length; i++){
            //printArr(ans, "ans");
            ans[i] = getBest(days, costs, ans, i);
        }
        //printArr(ans, "ans");
        return ans[ans.length-1];
    }

    // -----------------------------------------------------------------
    // -----------------------------------------------------------------
    // -----------------------------------------------------------------

    // Extra code I need to make this work
    public static void printArr(int[] arr, String arrName){
        System.out.print(arrName + ": { ");
        for(int num : arr) System.out.print(num + " ");
        System.out.println("}");
    }
    public static void main(String[] args){
        // Replace these with any length of array desired
        int[] days = {1,2,5,6,7,8,10,12,15,16,29,31,33,36,38,39};
        int[] costs = {2,3,5};
        // Enforce constrants on test cases
        assert 1 <= days.length && days.length <= 365;
        for(int day : days) assert 1 <= day && day < 365;
        for(int i = 1; i < days.length; i++) assert days[i] > days[i-1];
        assert costs.length == 3;
        for(int cost : costs) assert 1 <= cost && cost <= 1000;
        // Retrieve and display answer
        _983 obj = new _983();
        System.out.println("Input is:");
        printArr(costs, "  costs");
        printArr(days, "  days");
        int ans = obj.mincostTickets(days, costs);
        System.out.print("The minimum number of dollars needed");
        System.out.println(" to travel every day in days is: " + ans);
    }
}

