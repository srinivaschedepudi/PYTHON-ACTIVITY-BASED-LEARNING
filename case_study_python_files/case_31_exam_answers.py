"""Case 31: String-based examination answer evaluation."""

ANSWER_KEY = "ABCDC"
STUDENT_ANSWERS = ["ABXDC", "A-CD-", "BBCDA"]
MARKS_CORRECT = 2.0
PENALTY_WRONG = 0.5


def evaluate_answers(answer_key, answers, correct_marks, wrong_penalty):
    results = []
    print("EXAM ANSWER EVALUATION")
    print(f"Answer key: {answer_key}  ('-' means unanswered)")
    for student_number, response in enumerate(answers, start=1):
        if len(response) != len(answer_key):
            print(f"Student {student_number}: INVALID (answer count does not match key)")
            continue
        correct = 0
        wrong = 0
        blank = 0
        for index in range(len(answer_key)):
            if response[index] == "-":
                blank += 1
            elif response[index] == answer_key[index]:
                correct += 1
            else:
                wrong += 1
        score = correct * correct_marks - wrong * wrong_penalty
        results.append((student_number, correct, wrong, blank, score))
        print(f"Student {student_number}: correct={correct}, wrong={wrong}, blank={blank}, score={score:.2f}")
    return results


if __name__ == "__main__":
    evaluate_answers(ANSWER_KEY, STUDENT_ANSWERS, MARKS_CORRECT, PENALTY_WRONG)
