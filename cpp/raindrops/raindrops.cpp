#include "raindrops.h"
#include <string>

namespace raindrops {
    std::string convert(int drop) {
        std::string result = "";

        if (drop % 3 == 0) {
            result.append("Pling");
        }
        if (drop % 5 == 0) {
            result.append("Plang");
        }
        if (drop % 7 == 0) {
            result.append("Plong");
        }
        if (result.length() == 0){
            result = std::to_string(drop);
        }

        return result;
    }
}  // namespace raindrops
