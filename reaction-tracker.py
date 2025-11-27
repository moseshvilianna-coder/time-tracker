# დავაიმპორტოთ დრო, რენდომიზაცია და csv.
import time  # გაზომავს  დროს და დააპაუზებს პროგრამას
import random  # დააგენერირებს რენდომულ რიცხვებს
import csv  # გვაძლევს csv ფაილების დაწერისა და წაკითხვის უფლებას


# __________________________________
# ცდის გაშვების ფუნქცია
# __________________________________
def run_trial(trial_number):
    """თითო რეაქციის დროს ცდის გაშვება და შედეგის დაბრუნება"""

    print(f"\n trial {trial_number}:")

    # ვაჩერებთ პროგრამას და ველოდებით თუ როდის დააჭერს მომხმარებელი ENTERS-ს
    input("Press ENTER when you are ready...")

    print("Get Ready!!!")

    # დაყოვნება უნდა იყოს არაპროგნოზიორებადი, რათა მომხვარებელმა ვერ მოატყუოს
    delay = random.uniform(0.7, 5.0)

    # პროგრამა შეჩერდება ზემოთ მოცემული დროის განმავლობაში
    time.sleep(delay)

    # ვზომავთ დროს მომხმარებლის რეაგირებამდე
    start = time.time()

    input("GO!!! Press ENTER As Fast As You Can!!!")

    # ვაფიქსირებთ დროს მაშინვე, როცა დააჭერს ENTER-ს.
    end = time.time()

    # გამოკლება, დროის ინტერვალის გასარკვევათ
    reaction_time = end - start

    # ფალც-სტარტის პრევენცია
    if reaction_time < 0.1:
        print("That's Sus! Too Early!")
        return None
    elif reaction_time > 10.0:
        print("Too Slow!")

    #:.4f - ვაჩვენებთ რეაქციის დროს 4 ათობითი ნიშნით
    print(f"Your Reaction Time: {reaction_time:.4f} seconds")

    # ვაბრუნებთ მნიშვნელობას
    return reaction_time


# __________________________________
# შედეგების შენახვის ფუნქცია- ყველა რეაქცია შეინახება csv ფაილში
# __________________________________


def save_results(times, filename="reaction_times.csv"):
    """ყველა რეაქციის დრო შეინახება CSV ფაილში"""
    # open() ხსნის ან ქმინს ფაილს
    # "w" ქმინს ახალ ფაილს ან გადაწერს არსებულს
    # newline="" ხელს შეუშლის დამატებით ცარიელ სტრიქონებს
    # "with" ფაილი ავტომატურად დაიხურება, როცა მოვრჩებით
    valid_times = [t for t in times if t is not None]

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["trial", "reaction time (sec)"])

        for trial_num, reaction_time in enumerate(valid_times, start=1):
            writer.writerow([trial_num, f"{reaction_time:.4f}"])


# __________________________________
# მთავარი ფუნქცია
# __________________________________


def main():
    """მთავარი ფუნქცია- გაუშვებს მთელ პროგრამას"""

    print("*******Reaction Time Tracker*******")
    print("You Have To Go Through 5 Trials")

    trials = 5

    # ლისტი- ყველა რეაქციის დროის შესანახად
    reaction_times = []

    # for ლუპი გაუშვებს კოდს შიგნით ერთხელ თითიოეული ერთეულისთვის
    for trial_num in range(1, trials + 1):
        #
        result = run_trial(trial_num)

        if result is not None:
            reaction_times.append(result)
        else:
            print("This Trial Was Not Counted! Try Again!")
    # შეჯამება
    print("\n *******Summary*******")

    if not reaction_times:
        print("No Valid Results Were Recorded!")
        return

    # ვატრიალებთ სიას და ვდებთ თითოეულ შედეგს
    for trial_num, reaction_time in enumerate(reaction_times, start=1):
        print(f"Trial {trial_num}: {reaction_time:.4f} seconds")

    # ვთვლით საშუალო არტითმეტიკულს
    avg_time = sum(reaction_times) / len(reaction_times)
    print(f"\n Average Reaction Time: {avg_time:.4f} წამი")

    # შედეგების შენახვა
    save_results(reaction_times)
    print("Your Results Are Saved To reaction_times.csv file.")


# __________________________________
# პროგრამის შესვლის წერტილი
# __________________________________

if __name__ == "__main__":
    main()
