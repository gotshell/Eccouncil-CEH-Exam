import json
import random
import time

def load_questions(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        questions = json.load(file)
    return questions

def run_quiz(questions):
    try:
        total_questions = 0
        correct_answers = 0
        start_time = time.time()
        while True:
            question = random.choice(questions)
            print(f"\nQuestion # {total_questions} | " + question["question"] + "\n")
            answers = question["answers"]
            for key, answer in answers.items():
                print(f"{key}) {answer}")
            user_answer = input("\nChoose the right one ('z' to exit): ").upper().strip()
            if user_answer == 'Z': break
            correct_index = question["correct_answer"]
            correct_letter = chr(65 + correct_index)
            correct_answer = answers[correct_letter]
            total_questions += 1
            if user_answer == correct_letter:
                print("\n✅✅✅ Correct!\n")
                correct_answers += 1
            else:
                print("\n❌❌❌ Wrong!\n")
                print(f"ℹ️ The right option is {correct_letter}) {correct_answer}\n")
            print(f"📖 Explanation: {question['explanation']}")
            print("_" * 120)
        end_time = time.time() 
        elapsed_time = end_time - start_time 
        if total_questions > 0: accuracy = (correct_answers / total_questions) * 100
        else: accuracy = 0.0
        print("\n📊 Quiz Statistics:")
        print(f"📅 Total questions answered: {total_questions}")
        print(f"✅ Correct answers: {correct_answers}")
        print(f"❌ Incorrect answers: {total_questions - correct_answers}")
        print(f"🎯 Accuracy: {accuracy:.2f}%")
        print(f"⏳ Time spent: {elapsed_time:.2f} seconds\n")

    except KeyboardInterrupt:
        print("\n\nManually interrupted, thanks for playing!\n")

if __name__ == "__main__":
    questions_json_path = 'dump_no_duplicates.json' 
    questions = load_questions(questions_json_path)
    run_quiz(questions)
