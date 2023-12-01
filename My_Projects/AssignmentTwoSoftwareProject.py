#For this project, i created a Help Desk ticket System using Python.It covers various aspects, including ticket submission, generation of passwords, responding to tickets, reopening resolved tickets, and displaying ticket statistics. This project demonstrates object-oriented programming concepts, user input handling, and basic data management. In the future, you can build upon this foundation by adding more features, implementing user authentication, integrating with databases, or even creating a web-based interface for a more comprehensive help desk system.


import random
import string

class HelpDeskTicketSystem:
    def __init__(self):
        # Initialize ticket system with empty lists and counters
        self.tickets = []
        self.ticket_counter = 2000
        self.resolved_tickets = 0
        self.open_tickets = 0

    def submit_ticket(self, staff_id, creator_name, contact_email, description, auto_password=None):
        # Submit a new ticket with provided information
        ticket_number = self.ticket_counter
        self.ticket_counter += 1
        ticket = {
            'ticket_number': ticket_number,
            'staff_id': staff_id,
            'creator_name': creator_name,
            'contact_email': contact_email,
            'description': description,
            'status': 'open',
            'auto_password': auto_password
        }
        self.tickets.append(ticket)
        self.open_tickets += 1
        print(f"Ticket submitted successfully. Your ticket number is {ticket_number}.")
        if auto_password:
            print(f"Your new password is: {auto_password}")

    def generate_password(self, staff_id, creator_name):
        # Generate a password based on staff ID and creator name
        return staff_id[:2] + creator_name[:3]

    def respond_to_ticket(self, ticket_number, response):
        # Respond to a ticket and update its status
        for ticket in self.tickets:
            if ticket['ticket_number'] == ticket_number:
                ticket['response'] = response
                ticket['status'] = 'closed'
                self.resolved_tickets += 1
                self.open_tickets -= 1
                print(f"Response to ticket {ticket_number} submitted successfully.")
                return
        print(f"Ticket number {ticket_number} not found.")

    def reopen_ticket(self, ticket_number):
        # Reopen a resolved ticket and update its status
        for ticket in self.tickets:
            if ticket['ticket_number'] == ticket_number:
                if ticket['status'] == 'closed':
                    ticket['status'] = 'open'
                    self.resolved_tickets -= 1
                    self.open_tickets += 1
                    print(f"Ticket {ticket_number} has been reopened.")
                    return
                else:
                    print("Ticket is already open.")
                    return
        print(f"Ticket number {ticket_number} not found.")

    def display_ticket_statistics(self):
        # Display statistics on submitted, resolved, and open tickets
        submitted_tickets = len(self.tickets)
        print(f"Submitted tickets: {submitted_tickets}")
        print(f"Resolved tickets: {self.resolved_tickets}")
        print(f"Open tickets: {self.open_tickets}")

    def display_tickets(self):
        # Display detailed information for all tickets
        print("----------------------------------------------------------")  
        for ticket in self.tickets:
            print(f"Ticket Number: {ticket['ticket_number']}")
            print(f"Staff ID: {ticket['staff_id']}")
            print(f"Ticket Owner Name: {ticket['creator_name']}")
            print(f"Email: {ticket['contact_email']}")
            print(f"Description: {ticket['description']}")
            print(f"Status: {ticket['status']}")
            print(f"Response: {ticket.get('response', 'No response yet')}")
            print("----------------------------------------------------------")  

    def run(self):
        # Main program loop for user interaction
        while True:
            print("----------------------------------------------------------") 
            print("Select from the following choices:")
            print("0: Exit")
            print("1: Submit helpdesk ticket")
            print("2: Show all tickets")
            print("3: Respond to ticket by number")
            print("4: Re-open resolved ticket")
            print("5: Display ticket stats")
            print("----------------------------------------------------------") 

            choice = input("Enter menu selection (0 - 5): ")

            if choice == '0':
                print("Exiting the program.")
                break
            elif choice == '1':
                # User submits a new helpdesk ticket
                staff_id = input("Enter your staff ID: ")
                creator_name = input("Enter your name: ")
                contact_email = input("Enter your email address: ")
                issue_description = input("If you require a password change, type 'password change'. Please describe your issue: ")
                auto_password = None
                if issue_description.lower() == 'password change':
                    auto_password = self.generate_password(staff_id, creator_name)
                    issue_description = "Password change requested."
                self.submit_ticket(staff_id, creator_name, contact_email, issue_description, auto_password)
                another_ticket = input("Do you have another ticket to submit (Y/N)? ")
                if another_ticket.lower() != 'y':
                    break
            elif choice == '2':
                # Display all tickets
                self.display_tickets()
            elif choice == '3':
                # User responds to a specific ticket
                try:
                    ticket_number = int(input("Please enter the ticket number: "))
                    response = input(f"Response to ticket {ticket_number}: ")
                    self.respond_to_ticket(ticket_number, response)
                except ValueError:
                    print("Invalid ticket number. Please enter a numeric value.")
            elif choice == '4':
                # User reopens a resolved ticket
                try:
                    ticket_number = int(input("Please enter the ticket number to reopen: "))
                    self.reopen_ticket(ticket_number)
                except ValueError:
                    print("Invalid ticket number. Please enter a numeric value.")
            elif choice == '5':
                # Display ticket statistics
                self.display_ticket_statistics()
            else:
                print("Invalid choice. Please enter a valid menu option (0 - 5).")

if __name__ == "__main__":
    # Initialize and run the HelpDeskTicketSystem
    help_desk = HelpDeskTicketSystem()
    help_desk.run()

#In this HelpDeskTicketSystem project, several design principles and patterns are evident. The use of a class, encapsulating ticket-related functionalities, adheres to the Object-Oriented Programming (OOP) design principle, promoting code organization and modularity. The implementation of an initialization method (__init__) initializes the system's state, aligning with the Constructor design pattern. Additionally, the program employs the Command design pattern in the run method, creating an interactive loop where user choices trigger specific actions. The separation of concerns is demonstrated through methods like submit_ticket and respond_to_ticket, adhering to the Single Responsibility Principle. Overall, the project showcases a blend of OOP principles and design patterns, enhancing maintainability and readability.