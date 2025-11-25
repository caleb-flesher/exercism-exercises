#include "difference_of_squares.h"

namespace difference_of_squares {
    int square_of_sum(int value)
    {
        int count{0}, result{0};
        while (count <= value) {
            result += count;
            count++;
        }
        return pow(result, 2);
    }

    int sum_of_squares(int value)
    {
        int result{0}, count{0};
        while (count <= value) {
            result += pow(count, 2);
            count++;
        }
        return result;
    }

    int difference(int diff)
    {
        return square_of_sum(diff) - sum_of_squares(diff);
    }

}  // namespace difference_of_squares
