import customtkinter as ctk
from PIL import Image

# Initialize the app
ctk.set_appearance_mode("System")  # Default to system theme
ctk.set_default_color_theme("green")  # Default color theme

class ExpenseManagerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Initialize default user name
        self.user_name = "User"  # Default value

        # Configure the main window
        self.title("Budget Buddy")
        self.geometry("1000x500")  # Landscape layout
        self.resizable(0, 0)
        self.iconbitmap("./assets/app_logo.ico")

        # Create a main frame
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True)

        # Add a header
        self.header_label = ctk.CTkLabel(self.main_frame, text="Home", font=("Arial", 24, "bold"))
        self.header_label.pack(pady=20)

        # Add a content frame
        self.content_frame = ctk.CTkFrame(self.main_frame)
        self.content_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Add a bottom navigation menu
        self.bottom_nav = ctk.CTkFrame(self, height=80)
        self.bottom_nav.pack(side="bottom", fill="x")

        # Load icons for navigation buttons
        self.icons = {
            "Home": ctk.CTkImage(Image.open("./assets/home_icon.png").resize((32, 32))),
            "Investment": ctk.CTkImage(Image.open("./assets/savings_icon.png").resize((32, 32))),
            "Expenses": ctk.CTkImage(Image.open("./assets/expenses_icon.png").resize((32, 32))),
            "Support": ctk.CTkImage(Image.open("./assets/support_icon.png").resize((32, 32))),
            "Profile": ctk.CTkImage(Image.open("./assets/profile_icon.png").resize((32, 32))),
            "Light": ctk.CTkImage(Image.open("./assets/sun_icon.png").resize((32, 32))),
            "Dark": ctk.CTkImage(Image.open("./assets/moon_icon.png").resize((32, 32))),
            "Plus": ctk.CTkImage(Image.open("./assets/plus_icon.png").resize((20, 20))),
            "Minus": ctk.CTkImage(Image.open("./assets/minus_icon.png").resize((20, 20))),
            "Address": ctk.CTkImage(Image.open("./assets/address_icon.png").resize((16, 16))),
            "Phone": ctk.CTkImage(Image.open("./assets/phone_icon.png").resize((16, 16))),
            "Email": ctk.CTkImage(Image.open("./assets/email_icon.png").resize((16, 16))),
            "Pencil": ctk.CTkImage(Image.open("./assets/pencil_icon.png").resize((16, 16))),
            "Dustbin": ctk.CTkImage(Image.open("./assets/dustbin_icon.png").resize((16, 16))),

        }

        # Add navigation buttons
        self.nav_buttons = {}
        self.create_nav_button("Home", self.show_home)  # First Home button (keep this)
        # self.create_nav_button("Savings", self.show_savings)  # This line is commented out
        self.create_nav_button("Investment", self.show_investment)
        self.create_nav_button("Expenses", self.show_expenses)
        self.create_nav_button("Support", self.show_support)
        # self.create_nav_button("Profile", self.show_profile)

        self.active_tab = "Home"
        self.show_home()  # Set default tab

        
        # Add theme toggle button
        self.theme_button = ctk.CTkButton(
            self.bottom_nav, 
            text="Light", 
            image=self.icons["Light"], 
            command=self.toggle_theme, 
            hover_color="gray"
        )
        self.theme_button.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        
        self.active_tab = "Home"
        self.show_home()  # Set default tab
    
    def create_nav_button(self, text, command):
        """Create a navigation button with hover effect."""
        button = ctk.CTkButton(
            self.bottom_nav, 
            text=text, 
            image=self.icons[text],
            compound="top",
            command=command,
            hover_color="gray"
        )
        button.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.nav_buttons[text] = button
    
    def show_investment(self):
        """Display the Investment tab with separate sections for Stocks, Mutual Funds, etc."""
        self.header_label.configure(text="Investment")
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Scrollable Frame for Investment Content
        investment_frame = ctk.CTkScrollableFrame(self.content_frame)
        investment_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Title for Investment Section
        ctk.CTkLabel(investment_frame, text="Investment Options", font=("Arial", 20, "bold")).pack(pady=10)

        # Investment Subsections (Stocks, Mutual Funds, etc.)
        investment_sections = [
            {"title": "Stocks", "items": [
                {"name": "Tesla", "description": "Innovative electric car company", "price": "$2500", "ticker": "TSLA"},
                {"name": "Apple", "description": "Tech giant with consistent growth", "price": "$150", "ticker": "AAPL"},
                {"name": "Google", "description": "Search engine leader", "price": "$2800", "ticker": "GOOGL"}
            ]},
            {"title": "Mutual Funds", "items": [
                {"name": "Vanguard 500 Index Fund", "description": "Tracking the S&P 500", "returns": "7% annually"},
                {"name": "Fidelity Growth Fund", "description": "Growth-focused fund", "returns": "9% annually"},
                {"name": "T. Rowe Price Equity Fund", "description": "Large-cap equity fund", "returns": "8% annually"}
            ]},
            {"title": "Bonds", "items": [
                {"name": "US Government Bond", "description": "Low-risk, fixed return", "returns": "3% annually"},
                {"name": "Corporate Bond", "description": "Bonds issued by corporations", "returns": "5% annually"}
            ]}
        ]

        # Creating sections for each investment type
        for section in investment_sections:
            section_title = section["title"]
            ctk.CTkLabel(investment_frame, text=section_title, font=("Arial", 18, "bold")).pack(anchor="w", padx=20, pady=(20, 5))

            # Create individual investment items under each section
            for item in section["items"]:
                investment_widget = ctk.CTkFrame(investment_frame, width=600, height=150, corner_radius=10)
                investment_widget.pack(pady=10, fill="x", padx=5)

                # Grid layout for better control of the widget's content
                investment_widget.grid_columnconfigure(0, weight=1)  # Allow the text to expand
                investment_widget.grid_columnconfigure(1, weight=0)  # Keep the button fixed

                # Add investment details in the widget
                ctk.CTkLabel(investment_widget, text=item["name"], font=("Arial", 16, "bold")).grid(row=0, column=0, sticky="w", padx=20, pady=5)
                if section_title == "Stocks":
                    ctk.CTkLabel(investment_widget, text=f"Ticker: {item['ticker']}", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=20)
                    ctk.CTkLabel(investment_widget, text=f"Price: {item['price']}", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=20, pady=5)
                else:
                    ctk.CTkLabel(investment_widget, text=f"Description: {item['description']}", font=("Arial", 12), wraplength=500).grid(row=1, column=0, sticky="w", padx=20)
                    ctk.CTkLabel(investment_widget, text=f"Expected Returns: {item['returns']}", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=20, pady=5)

                # Add the "Invest Now" button in the second column, right-aligned
                invest_button = ctk.CTkButton(investment_widget, text="Invest Now", font=("Arial", 14), command=lambda name=item["name"]: self.invest_now(name))
                invest_button.grid(row=0, column=1, rowspan=3, padx=20, pady=5, sticky="e")

    def invest_now(self, investment_name):
        """Handle the Invest Now button click."""
        print(f"Investing in {investment_name} now!")


    
    def toggle_theme(self):
        """Toggle between light and dark themes."""
        current_mode = ctk.get_appearance_mode()
        new_mode = "Light" if current_mode == "Dark" else "Dark"
        ctk.set_appearance_mode(new_mode)
        
        # Update theme icon and text
        self.theme_button.configure(
            image=self.icons[new_mode],
            text=new_mode
        )
    
    def show_home(self):
        """Display the Home tab."""
        self.header_label.configure(text="Home")
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Scrollable frame for the Home content
        scrollable_frame = ctk.CTkScrollableFrame(self.content_frame)
        scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Get the user name from profile (default to "User" if not set)
        user_name = getattr(self, "user_name", "User")
        greeting = f"Hi, {user_name}!"

        # Greeting Label
        ctk.CTkLabel(
            scrollable_frame,
            text=greeting,
            font=("Arial", 20, "bold"),
            anchor="w"
        ).pack(pady=10, padx=10, anchor="w")

        # Monthly Income Widget
        income_frame = ctk.CTkFrame(scrollable_frame, height=80, corner_radius=10)
        income_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(
            income_frame,
            text="Monthly Income",
            font=("Arial", 16),
            anchor="w"
        ).pack(pady=5, padx=10, anchor="w")
        ctk.CTkLabel(
            income_frame,
            text="$0.00",  # Placeholder for monthly income
            font=("Arial", 24, "bold"),
            anchor="w"
        ).pack(pady=5, padx=10, anchor="w")

        # Total Expenses Widget
        expenses_frame = ctk.CTkFrame(scrollable_frame, height=80, corner_radius=10)
        expenses_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(
            expenses_frame,
            text="Total Expenses (This Month)",
            font=("Arial", 16),
            anchor="w"
        ).pack(pady=5, padx=10, anchor="w")
        ctk.CTkLabel(
            expenses_frame,
            text="$0.00",  # Placeholder for total expenses
            font=("Arial", 24, "bold"),
            anchor="w"
        ).pack(pady=5, padx=10, anchor="w")

        # Savings Goal Widget
        savings_frame = ctk.CTkFrame(scrollable_frame, height=80, corner_radius=10)
        savings_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(
            savings_frame,
            text="Savings Goal (This Month)",
            font=("Arial", 16),
            anchor="w"
        ).pack(pady=5, padx=10, anchor="w")
        ctk.CTkLabel(
            savings_frame,
            text="$500.00",  # Placeholder for savings goal
            font=("Arial", 24, "bold"),
            anchor="w"
        ).pack(pady=5, padx=10, anchor="w")

        # Money Saved Till Now Widget
        saved_frame = ctk.CTkFrame(scrollable_frame, height=80, corner_radius=10)
        saved_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(
            saved_frame,
            text="Money Saved Till Now",
            font=("Arial", 16),
            anchor="w"
        ).pack(pady=5, padx=10, anchor="w")
        ctk.CTkLabel(
            saved_frame,
            text="$0.00",  # Placeholder for money saved
            font=("Arial", 24, "bold"),
            anchor="w"
        ).pack(pady=5, padx=10, anchor="w")



    
    def show_savings(self):
        """Display the Savings tab."""
        self.update_content("Savings", "Track your savings here.")
    
    def show_expenses(self):
        """Display the Expenses tab."""
        self.header_label.configure(text="Expenses")
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Dictionary to store categories and their total expenses
        self.categories = getattr(self, "categories", {})
        
        # Add Category Section
        add_category_frame = ctk.CTkFrame(self.content_frame, corner_radius=10)
        add_category_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(add_category_frame, text="Add Category", font=("Arial", 16)).pack(side="left", padx=10)
        category_entry = ctk.CTkEntry(add_category_frame, placeholder_text="Enter category name", width=200)
        category_entry.pack(side="left", padx=10)

        def add_category():
            category_name = category_entry.get().strip()
            if category_name and category_name not in self.categories:
                self.categories[category_name] = 0  # Initialize with 0 expense
                self.update_category_widgets()
                category_entry.delete(0, "end")
        
        add_button = ctk.CTkButton(add_category_frame, text="Add", command=add_category, width=100)
        add_button.pack(side="left", padx=10)

        # Category Widgets Section
        self.categories_frame = ctk.CTkFrame(self.content_frame)
        self.categories_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Add Expense Section
        add_expense_frame = ctk.CTkFrame(self.content_frame, corner_radius=10)
        add_expense_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(add_expense_frame, text="Add Expense", font=("Arial", 16)).pack(side="left", padx=10)
        
        expense_entry = ctk.CTkEntry(add_expense_frame, placeholder_text="Enter amount", width=100)
        expense_entry.pack(side="left", padx=10)
        
        category_dropdown = ctk.CTkOptionMenu(add_expense_frame, values=list(self.categories.keys()))
        category_dropdown.pack(side="left", padx=10)

        def add_expense():
            try:
                amount = float(expense_entry.get().strip())
                selected_category = category_dropdown.get()
                if selected_category in self.categories:
                    self.categories[selected_category] += amount
                    self.update_category_widgets()
                    expense_entry.delete(0, "end")
            except ValueError:
                print("Invalid amount entered!")

        add_expense_button = ctk.CTkButton(add_expense_frame, text="Add Expense", command=add_expense)
        add_expense_button.pack(side="left", padx=10)

        self.update_category_widgets()

    def update_category_widgets(self):
        """Update the category widgets based on the current list of categories."""
        for widget in self.categories_frame.winfo_children():
            widget.destroy()

        for category_name, total in self.categories.items():
            category_widget = ctk.CTkFrame(self.categories_frame, corner_radius=10)
            category_widget.pack(fill="x", padx=10, pady=5)
            
            # Category Name and Total
            ctk.CTkLabel(
                category_widget,
                text=f"{category_name} - ${total:.2f}",
                font=("Arial", 14),
                anchor="w"
            ).pack(side="left", padx=10, expand=True, fill="both")

            # Edit Button
            edit_button = ctk.CTkButton(
                category_widget,
                text="",
                image=self.icons["Pencil"],
                width=20,
                command=lambda cat=category_name: self.rename_category(cat)
            )
            edit_button.pack(side="right", padx=5)
            
            # Delete Button
            delete_button = ctk.CTkButton(
                category_widget,
                text="",
                image=self.icons["Dustbin"],
                width=20,
                command=lambda cat=category_name: self.delete_category(cat)
            )
            delete_button.pack(side="right", padx=5)

    def delete_category(self, category_name):
        """Delete a category."""
        if category_name in self.categories:
            del self.categories[category_name]
            self.update_category_widgets()

    def rename_category(self, category_name):
        """Rename a category."""
        def save_new_name():
            new_name = rename_entry.get().strip()
            if new_name and new_name != category_name and new_name not in self.categories:
                self.categories[new_name] = self.categories.pop(category_name)
                self.update_category_widgets()
                rename_window.destroy()

        # Create a popup window for renaming
        rename_window = ctk.CTkToplevel(self)
        rename_window.title("Rename Category")
        rename_window.geometry("300x150")
        
        ctk.CTkLabel(rename_window, text="Enter new name:", font=("Arial", 14)).pack(pady=10)
        rename_entry = ctk.CTkEntry(rename_window, placeholder_text="New category name", width=200)
        rename_entry.pack(pady=10)
        rename_button = ctk.CTkButton(rename_window, text="Save", command=save_new_name)
        rename_button.pack(pady=10)

    
    def show_support(self):
        """Display the Support tab."""
        self.header_label.configure(text="Support")
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Scrollable Frame for Support Content
        support_frame = ctk.CTkScrollableFrame(self.content_frame)
        support_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Add Support Details
        ctk.CTkLabel(support_frame, text="Address:", image=self.icons["Address"], compound="left", font=("Arial", 16)).pack(anchor="w", pady=5, padx=5)
        ctk.CTkLabel(support_frame, text="123 Expense St, Budget City", font=("Arial", 16)).pack(anchor="w", pady=5)
        ctk.CTkLabel(support_frame, text="Phone:", image=self.icons["Phone"], compound="left", font=("Arial", 16)).pack(anchor="w", pady=5, padx=5)
        ctk.CTkLabel(support_frame, text="+1-800-EXPENSE", font=("Arial", 16)).pack(anchor="w", pady=5)
        ctk.CTkLabel(support_frame, text="Email:", image=self.icons["Email"], compound="left", font=("Arial", 16)).pack(anchor="w", pady=5, padx=5)
        ctk.CTkLabel(support_frame, text="support@example.com", font=("Arial", 16)).pack(anchor="w", pady=5)

        # Add Dropdown for Terms and Conditions
        self.terms_button = ctk.CTkButton(
            support_frame, 
            text="Terms and Conditions", 
            image=self.icons["Plus"], 
            compound="left",
            command=self.toggle_terms, 
            anchor="w"
        )
        self.terms_button.pack(fill="x", pady=10)

        # Container for terms text (hidden initially)
        self.terms_text = ctk.CTkFrame(support_frame, fg_color="transparent")
        self.terms_text.pack(fill="x", pady=5)
        self.terms_text.pack_forget()  # Hide by default

        # Add Detailed Terms Content
        terms_content = (
            "1. **Usage of Application**:\n"
            "   By using this application, you agree to comply with all terms outlined herein. "
            "Unauthorized use is strictly prohibited.\n\n"
            "2. **Privacy Policy**:\n"
            "   We value your privacy. All data provided is stored securely and used solely for improving your experience.\n\n"
            "3. **Limitations of Liability**:\n"
            "   The app and its services are provided 'as-is'. We are not responsible for any inaccuracies or issues arising from its use.\n\n"
            "4. **Termination**:\n"
            "   We reserve the right to terminate access to the app for violation of these terms or misuse.\n\n"
            "5. **Contact**:\n"
            "   For any concerns, please contact support at support@example.com."
        )

        self.terms_label = ctk.CTkLabel(
            self.terms_text, 
            text=terms_content, 
            font=("Arial", 18),  # Increased font size
            justify="left",
            anchor="w",
            wraplength=800  # Line wrapping for cleaner alignment
        )
        self.terms_label.pack(padx=20, pady=10)


    def toggle_terms(self):
        """Toggle the visibility of terms and conditions."""
        if self.terms_text.winfo_viewable():
            self.terms_text.pack_forget()  # Hide
            self.terms_button.configure(image=self.icons["Plus"])
        else:
            self.terms_text.pack(fill="x", pady=5)  # Show
            self.terms_button.configure(image=self.icons["Minus"])


    def show_profile(self):
        """Display the Profile tab."""
        self.header_label.configure(text="Profile")
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Create Profile Form
        profile_frame = ctk.CTkFrame(self.content_frame)
        profile_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Input fields
        ctk.CTkLabel(profile_frame, text="Name", font=("Arial", 14)).grid(row=0, column=0, pady=10, sticky="w")
        name_entry = ctk.CTkEntry(profile_frame, placeholder_text="Enter your name", width=300)
        name_entry.grid(row=0, column=1, pady=10, padx=10, sticky="e", ipady=5, ipadx=5)
        
        ctk.CTkLabel(profile_frame, text="Email", font=("Arial", 14)).grid(row=1, column=0, pady=10, sticky="w")
        email_entry = ctk.CTkEntry(profile_frame, placeholder_text="Enter your email", width=300)
        email_entry.grid(row=1, column=1, pady=10, padx=10, sticky="e", ipady=5, ipadx=5)
        
        # ctk.CTkLabel(profile_frame, text="Phone", font=("Arial", 14)).grid(row=2, column=0, pady=10, sticky="w")
        # phone_entry = ctk.CTkEntry(profile_frame, placeholder_text="Enter your phone number")
        # phone_entry.grid(row=2, column=1, pady=10, padx=10, sticky="e", ipady=5, ipadx=5)
        
        # Submit Button
        def submit_data():
            name = name_entry.get()
            email = email_entry.get()
            self.user_name = name if name.strip() else "User"  # Update user name
            print(f"Name: {name}, Email: {email}")

        
        submit_button = ctk.CTkButton(profile_frame, text="Save Data", command=submit_data, width=300)
        submit_button.grid(row=3, column=0, columnspan=2, pady=20, ipady=5, ipadx=5)

    def update_content(self, tab_name, message):
        """Update the content frame based on the active tab."""
        if self.active_tab != tab_name:
            self.active_tab = tab_name
            self.header_label.configure(text=tab_name)
            for widget in self.content_frame.winfo_children():
                widget.destroy()
            label = ctk.CTkLabel(self.content_frame, text=message, font=("Arial", 18))
            label.pack(expand=True)

# Run the app
if __name__ == "__main__":
    app = ExpenseManagerApp()
    app.mainloop()
