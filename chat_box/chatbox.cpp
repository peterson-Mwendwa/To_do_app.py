#include <iostream>
#include <string>
#include <algorithm> // For transforming strings to lowercase
using namespace std;

// Function to display a welcome message with coder credits
void displayWelcome() {
    cout << "👋 Hello! I'm ChatBot, your friendly virtual buddy! 😊\n";
    cout << "Coded with ❤️ by Valilian Peterson Mwendwa! 🌟\n";
    cout << "Let's have a fun chat! 🎉\n\n";
}

// Display the interactive menu
void displayMenu() {
    cout << "💬 Here are some things you can ask me:\n";
    cout << "  👉 'hello' - Just say hello!\n";
    cout << "  👉 'name' - Ask me about my name!\n";
    cout << "  👉 'time' - Ask for the current time!\n";
    cout << "  👉 'bye' - Say goodbye!\n";
    cout << "  👉 'help' - Show this menu again\n";
    cout << "Let's chat away! 🗨️ Type your message below!\n";
}

// Convert string to lowercase
string toLowerCase(string input) {
    transform(input.begin(), input.end(), input.begin(), ::tolower);
    return input;
}

// Process and respond to user input
void respondToUser(const string& input) {
    string userInput = toLowerCase(input);
    if (userInput == "hello") {
        cout << "👋 Hey there! Nice to see you! 😊\n";
    } else if (userInput == "name") {
        cout << "🤖 I'm ChatBot, your friendly assistant! 💻✨\n";
    } else if (userInput == "time") {
        cout << "⏰ I’d love to tell you the time, but I'm still learning that skill! 😅\n";
    } else if (userInput == "bye") {
        cout << "👋 Goodbye! It was great chatting with you! 😊 Have a wonderful day! 🌞\n";
    } else if (userInput == "help") {
        displayMenu();
    } else {
        cout << "🤔 Hmm, I'm not sure I understand that. Could you try something else? 💡\n";
    }
}

// Main program execution
int main() {
    displayWelcome();    // Show welcome message with coder's name
    displayMenu();       // Display available commands
    
    string userInput;
    do {
        cout << "\n📝 Your Message: ";
        getline(cin, userInput);
        
        respondToUser(userInput);
        
    } while (toLowerCase(userInput) != "bye");
    
    cout << "\n👋 See you next time! Thanks for chatting! 🎈\n";
    return 0;
}
