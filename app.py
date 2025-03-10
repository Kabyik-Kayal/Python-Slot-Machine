import tkinter as tk
from tkinter import messagebox, ttk
import random
from main import symbol_count, symbol_value, get_slot_machine_spin, check_winnings

class SlotMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Slot Machine")
        self.root.geometry("600x500")
        self.root.configure(bg="#2C3E50")
        
        self.balance = 0
        self.MAX_LINES = 3
        self.MAX_BET = 100
        self.MIN_BET = 1
        self.ROWS = 3
        self.COLS = 3
        
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_frame = tk.Frame(self.root, bg="#2C3E50")
        title_frame.pack(pady=10)
        
        title_label = tk.Label(
            title_frame, 
            text="PYTHON SLOT MACHINE", 
            font=("Arial", 20, "bold"),
            bg="#2C3E50",
            fg="white"
        )
        title_label.pack()
        
        # Balance display
        self.balance_var = tk.StringVar(value=f"Balance: ${self.balance}")
        balance_label = tk.Label(
            self.root, 
            textvariable=self.balance_var,
            font=("Arial", 14),
            bg="#2C3E50",
            fg="white"
        )
        balance_label.pack(pady=5)
        
        # Deposit section
        deposit_frame = tk.Frame(self.root, bg="#2C3E50")
        deposit_frame.pack(pady=10)
        
        deposit_label = tk.Label(
            deposit_frame, 
            text="Deposit amount: $",
            font=("Arial", 12),
            bg="#2C3E50",
            fg="white"
        )
        deposit_label.pack(side=tk.LEFT)
        
        self.deposit_entry = tk.Entry(deposit_frame, width=10, font=("Arial", 12))
        self.deposit_entry.pack(side=tk.LEFT, padx=5)
        
        deposit_button = tk.Button(
            deposit_frame, 
            text="Deposit",
            command=self.make_deposit,
            bg="#27AE60",
            fg="white",
            font=("Arial", 12),
            padx=10
        )
        deposit_button.pack(side=tk.LEFT, padx=5)
        
        # Betting section
        betting_frame = tk.Frame(self.root, bg="#2C3E50")
        betting_frame.pack(pady=10)
        
        # Lines selection
        lines_label = tk.Label(
            betting_frame, 
            text="Lines:",
            font=("Arial", 12),
            bg="#2C3E50",
            fg="white"
        )
        lines_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.lines_var = tk.IntVar(value=1)
        lines_spinbox = tk.Spinbox(
            betting_frame, 
            from_=1, 
            to=self.MAX_LINES,
            width=5,
            textvariable=self.lines_var,
            font=("Arial", 12)
        )
        lines_spinbox.grid(row=0, column=1, padx=5, pady=5)
        
        # Bet amount selection
        bet_label = tk.Label(
            betting_frame, 
            text="Bet per line: $",
            font=("Arial", 12),
            bg="#2C3E50",
            fg="white"
        )
        bet_label.grid(row=0, column=2, padx=5, pady=5)
        
        self.bet_var = tk.IntVar(value=5)
        bet_spinbox = tk.Spinbox(
            betting_frame, 
            from_=self.MIN_BET, 
            to=self.MAX_BET,
            width=5,
            textvariable=self.bet_var,
            font=("Arial", 12)
        )
        bet_spinbox.grid(row=0, column=3, padx=5, pady=5)
        
        # Slot machine display
        self.slot_frame = tk.Frame(
            self.root, 
            bg="#34495E",
            width=300,
            height=200,
            bd=3,
            relief=tk.RAISED
        )
        self.slot_frame.pack(pady=15)
        
        # Create slot symbols display (3x3 grid)
        self.slot_symbols = []
        for row in range(self.ROWS):
            row_symbols = []
            for col in range(self.COLS):
                symbol_label = tk.Label(
                    self.slot_frame,
                    text="",
                    width=5,
                    height=2,
                    font=("Arial", 16, "bold"),
                    bg="#2980B9",
                    fg="white",
                    relief=tk.SUNKEN
                )
                symbol_label.grid(row=row, column=col, padx=5, pady=5)
                row_symbols.append(symbol_label)
            self.slot_symbols.append(row_symbols)
            
        # Results section
        self.result_var = tk.StringVar(value="Make a deposit and spin!")
        result_label = tk.Label(
            self.root, 
            textvariable=self.result_var,
            font=("Arial", 12),
            bg="#2C3E50",
            fg="#F1C40F",
            wraplength=400
        )
        result_label.pack(pady=10)
        
        # Buttons
        button_frame = tk.Frame(self.root, bg="#2C3E50")
        button_frame.pack(pady=10)
        
        spin_button = tk.Button(
            button_frame, 
            text="SPIN",
            command=self.spin,
            bg="#E74C3C",
            fg="white",
            font=("Arial", 14, "bold"),
            padx=20,
            pady=10
        )
        spin_button.pack(side=tk.LEFT, padx=10)
        
        quit_button = tk.Button(
            button_frame, 
            text="CASH OUT",
            command=self.cash_out,
            bg="#3498DB",
            fg="white",
            font=("Arial", 14),
            padx=10,
            pady=10
        )
        quit_button.pack(side=tk.LEFT, padx=10)
        
    def make_deposit(self):
        try:
            amount = int(self.deposit_entry.get())
            if amount > 0:
                self.balance += amount
                self.update_balance()
                self.result_var.set(f"Successfully deposited ${amount}. Ready to play!")
            else:
                messagebox.showerror("Invalid Amount", "Amount must be greater than 0.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
    
    def update_balance(self):
        self.balance_var.set(f"Balance: ${self.balance}")
    
    def spin(self):
        lines = self.lines_var.get()
        bet = self.bet_var.get()
        total_bet = bet * lines
        
        if total_bet > self.balance:
            messagebox.showerror("Insufficient Funds", f"You need ${total_bet} to play. Your balance is ${self.balance}.")
            return
            
        # Deduct bet from balance
        self.balance -= total_bet
        self.update_balance()
        
        # Get spin result
        columns = get_slot_machine_spin(self.ROWS, self.COLS, symbol_count)
        
        # Update slot machine display with animation
        self.animate_spin(columns)
        
        # Calculate winnings
        winnings, winning_lines = check_winnings(columns, lines, bet, symbol_value)
        
        # Update balance with winnings
        self.balance += winnings
        self.update_balance()
        
        # Display result
        if winnings > 0:
            result_text = f"You won ${winnings}!\nWinning lines: {', '.join(map(str, winning_lines))}"
            self.highlight_winning_lines(winning_lines)
        else:
            result_text = "No win this time. Try again!"
            
        self.result_var.set(result_text)
    
    def animate_spin(self, final_columns):
        # Display the spinning animation
        self.root.update()
        
        # Convert columns to rows for display
        for row in range(self.ROWS):
            for col in range(self.COLS):
                symbol = final_columns[col][row]
                color = self.get_symbol_color(symbol)
                self.slot_symbols[row][col].config(
                    text=symbol, 
                    bg=color
                )
                self.root.update()
                self.root.after(100)  # Small delay for animation effect
    
    def highlight_winning_lines(self, winning_lines):
        # Reset all backgrounds first
        for row in range(self.ROWS):
            for col in range(self.COLS):
                symbol = self.slot_symbols[row][col]['text']
                self.slot_symbols[row][col].config(bg=self.get_symbol_color(symbol))
        
        # Highlight winning lines
        for line in winning_lines:
            row_idx = line - 1  # Convert to 0-based index
            for col in range(self.COLS):
                self.slot_symbols[row_idx][col].config(bg="#F1C40F")  # Highlight in gold
    
    def get_symbol_color(self, symbol):
        colors = {
            "A": "#E74C3C",  # Red
            "B": "#9B59B6",  # Purple
            "C": "#3498DB",  # Blue
            "D": "#2ECC71"   # Green
        }
        return colors.get(symbol, "#7F8C8D")  # Default gray
    
    def cash_out(self):
        if messagebox.askyesno("Cash Out", f"Are you sure you want to cash out ${self.balance}?"):
            messagebox.showinfo("Thank You", f"You cashed out ${self.balance}. Thanks for playing!")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SlotMachineApp(root)
    root.mainloop()
