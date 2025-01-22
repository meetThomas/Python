from datetime import datetime
# Main program loop
while True:
    # Display available movies and get user's choice
    print("Available Movies:")
    print("1. Action")
    print("2. Drama")
    print("3. Comedy")

    # Get the movie choice from user
    movie_choice = int(input("Choose a movie (1-3): "))

    # Get the number of tickets and ticket type
    number_of_tickets = int(input("Enter the number of tickets: "))
    print("Ticket Types: 1. Normal ($10), 2. Premium ($20)")
    ticket_type = int(input("Choose ticket type (1 for Normal, 2 for Premium): "))

    # Display available showtimes as options
    print("Available Showtimes (in 24-hour format):")
    print("1. 10:00 AM")
    print("2. 14:00 PM (2 PM)")
    print("3. 18:00 PM (6 PM)")
    print("4. 22:00 PM (10 PM)")

    show_time_choice = int(input("Choose a showtime (1-4): "))

    # Map the user's choice to the corresponding showtime
    if show_time_choice == 1:
        show_time = 10
    elif show_time_choice == 2:
        show_time = 14
    elif show_time_choice == 3:
        show_time = 18
    elif show_time_choice == 4:
        show_time = 22
    else:
        print("Invalid choice! Defaulting to 10:00 AM.")
        show_time = 10  # Default to 10 AM if invalid input

    # Get current day of the week
    current_day = datetime.now().strftime("%A")  # Get current day name

    # Determine ticket price
    if ticket_type == 1:  # Normal Ticket
        ticket_price = 10
    elif ticket_type == 2:  # Premium Ticket
        ticket_price = 20

    # Calculate total cost
    total_cost = ticket_price * number_of_tickets

    # Initialize discount variable
    discount = 0

    # Apply discount for more than 5 tickets
    if number_of_tickets > 5:
        discount = 0.10  # 10% discount for more than 5 tickets

    # Apply the discount
    total_cost -= total_cost * discount  # Apply the discount to total cost (total_cost = total_cost - (total_cost * discount))

    # Display the booking summary
    if movie_choice == 1:
        movie_name = "Action"
    elif movie_choice == 2:
        movie_name = "Drama"

    elif movie_choice == 3:
        movie_name = "Comedy"

    print("\n--- Booking Summary ---")
    print(f"Movie: {movie_name}")
    print(f"Number of Tickets: {number_of_tickets}")
    print(f"Ticket Type: {'Normal' if ticket_type == 1 else 'Premium'}")
    print(f"Showtime: {show_time}:00")
    print(f"Day: {current_day}")
    print(f"Total Cost: ${total_cost:.2f}")

    # Ask if the user wants to continue booking
    continue_booking = input("\nDo you want to book another ticket? (yes/no): ").strip().lower()
    if continue_booking != "yes":
        print("Thank you for using the Online Movie Ticket Booking System. Goodbye!")
        break
