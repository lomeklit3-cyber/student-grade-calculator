def print_header(title):
    print("\n" + "=" * 50)
    print(f" {title.upper()} ".center(50, "★"))
    print("=" * 50)


def get_letter_grade(score):
    if score >= 90:
        return "A", "🌟 Outstanding effort!"
    elif score >= 80:
        return "B", "👍 Great job! Solid understanding."
    elif score >= 70:
        return "C", "👌 Satisfactory performance."
    elif score >= 60:
        return "D", "⚠️ Needs improvement."
    else:
        return "F", "🚨 Critical: Immediate review required."


def render_progress_bar(percentage):
    # Renders a 20-character visual bar representing the score
    filled_length = int(20 * percentage // 100)
    bar = "█" * filled_length + "-" * (20 - filled_length)
    return f"[{bar}] {percentage:.1f}%"


def calculate_grades():
    print_header("Interactive Grade & Target Calculator")

    categories = []
    total_weight = 0.0

    print(
        "Enter your coursework categories (e.g., Homework, Quizzes, Midterm)."
    )
    print("Type 'done' when you have finished entering completed categories.\n")

    # Step 1: Input Completed Assignments
    while True:
        name = input("Category name (or 'done'): ").strip()
        if name.lower() == "done":
            if not categories:
                print("Please enter at least one category to proceed.")
                continue
            break

        try:
            score = float(input(f"  ➜ Score achieved in '{name}' (0-100): "))
            weight = float(input(f"  ➜ Weight of '{name}' (% of total grade): "))

            if not (0 <= score <= 100) or weight <= 0:
                print(
                    "  ❌ Invalid input. Score must be 0-100 and weight must be positive.\n"
                )
                continue

            categories.append({"name": name, "score": score, "weight": weight})
            total_weight += weight
            print(f"  ✓ Added. Current total weight allocated: {total_weight}%\n")

        except ValueError:
            print("  ❌ Please enter valid numerical values.\n")

    # Step 2: Calculate Current Weighted Average
    weighted_score_sum = sum(
        item["score"] * (item["weight"] / 100) for item in categories
    )
    current_avg = (weighted_score_sum / total_weight) * 100

    letter, feedback = get_letter_grade(current_avg)

    print_header("Current Status Report")
    print(f"Completed Weight Evaluated : {total_weight}%")
    print(f"Current Weighted Average   : {current_avg:.2f}%")
    print(f"Progress Bar               : {render_progress_bar(current_avg)}")
    print(f"Letter Grade Equivalent    : {letter}")
    print(f"Feedback                   : {feedback}")

    # Step 3: What-If / Remaining Goal Calculator
    remaining_weight = 100.0 - total_weight

    if remaining_weight > 0:
        print_header("Remaining Course Goal Analyzer")
        print(
            f"You have {remaining_weight:.1f}% of your total grade left unallocated (e.g., Final Exam).\n"
        )

        try:
            target_grade = float(
                input("Enter your desired target final course grade (%): ")
            )

            # Calculation: (Target - Current Weighted Points) / Remaining Weight Fraction
            required_score = (
                target_grade - weighted_score_sum
            ) / (remaining_weight / 100)

            print("\n" + "-" * 50)
            if required_score <= 0:
                print(
                    f"🎉 Great news! You've already locked in your target of {target_grade}%."
                )
                print("Even a 0% on the remaining work will keep you above target!")
            elif required_score > 100:
                print(
                    f"💔 Mathematically Unattainable: To reach {target_grade}%, you would need {required_score:.1f}%"
                )
                print(
                    f"The maximum overall grade you can achieve now is {(weighted_score_sum + remaining_weight):.2f}%."
                )
            else:
                print(
                    f"🎯 Target Goal: {target_grade}% final overall grade"
                )
                print(
                    f"📝 Required Score on remaining work ({remaining_weight}% weight): {required_score:.2f}%"
                )
                print(
                    f"Visual Target Bar: {render_progress_bar(required_score)}"
                )

        except ValueError:
            print("Invalid target grade entered.")
    else:
        print("\nAll 100% of course weight has been evaluated. No remaining exams!")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    calculate_grades()
