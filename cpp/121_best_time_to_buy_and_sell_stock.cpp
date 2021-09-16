class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        int curr_profit = 0;
        int min_price;
        if (prices.size() > 0) {
            min_price = prices[0];
        } else {
            return 0;
        }
        for (int i=0; i<prices.size(); ++i) {
            if (prices[i] < min_price) {
                min_price = prices[i];
            }
            curr_profit = prices[i] - min_price;
            if (curr_profit > max_profit) {
                max_profit = curr_profit;
            }
        }
        return max_profit;
    }
};
