#include <array>
#include <string>
#include <vector>

// Round down all provided student scores.
std::vector<int> round_down_scores(std::vector<double> student_scores) {
    // TODO: Implement round_down_scores
    std::vector<int> int_student_scores;
    for (double score : student_scores){ int_student_scores.push_back(static_cast<int>(score)); }
    return int_student_scores;
}


// Count the number of failing students out of the group provided.
int count_failed_students(std::vector<int> student_scores) {
    // TODO: Implement count_failed_students
    int count{0};
    for (int score : student_scores) {
        if (score <= 40) {count++;}
    }
    return count;
}

// Determine how many of the provided student scores were 'the best' based on the provided threshold.
std::vector<int> above_threshold(std::vector<int> student_scores, int threshold) {
    // TODO: Implement above_threshold
    std::vector<int> the_best{};
    for (int score : student_scores) {
        if (score >= threshold) {the_best.emplace_back(score);}
    }
    return the_best;
}

// Create a list of grade thresholds based on the provided highest grade.
std::array<int, 4> letter_grades(int highest_score) {
    // TODO: Implement letter_grades
    std::array<int, 4> result = {};
    int interval = (highest_score - 40) / 4;
    for (int i : {0, 1, 2, 3}){ result[i] = 41 + interval * i; }
    return result;
}

// Organize the student's rank, name, and grade information in ascending order.
std::vector<std::string> student_ranking(std::vector<int> student_scores, std::vector<std::string> student_names) {
    // TODO: Implement student_ranking
    std::vector<std::string> result = {};
    for (int i = 0; i < student_scores.size(); ++i){
        result.emplace_back(std::to_string(i + 1) + ". " 
            + student_names[i] + ": "
            + std::to_string(student_scores[i]));
    }
    return result;
}

// Create a string that contains the name of the first student to make a perfect score on the exam.
std::string perfect_score(std::vector<int> student_scores, std::vector<std::string> student_names) {
    // TODO: Implement perfect_score
    auto result = std::find(student_scores.begin(), student_scores.end(), 100);
    return student_names[result];
}
