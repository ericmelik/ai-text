// Main function that handles sending questions to the AI
// This is an async function because it needs to wait for the server response
async function askQuestion() {
    // Get references to HTML elements we need to interact with
    const input = document.getElementById('questionInput');  // The text input field
    const button = document.getElementById('askButton');  // The send button
    const chatContainer = document.getElementById('chatContainer');  // The message container
    
    // Get the question text and remove any extra whitespace
    const question = input.value.trim();
    
    // If the question is empty, do nothing and return early
    if (!question) return;
    
    // Create a new div element for the user's message
    const userMsg = document.createElement('div');
    // Add CSS classes to style it as a user message
    userMsg.className = 'message user-message';
    // Set the text content to the user's question
    userMsg.textContent = question;
    // Add the message to the chat container
    chatContainer.appendChild(userMsg);
    
    // Clear the input field for the next question
    input.value = '';
    // Disable the button while we wait for response (prevent duplicate requests)
    button.disabled = true;
    // Change button text to show it's processing
    button.textContent = 'Thinking...';
    
    // Create a temporary loading message to show the bot is "typing"
    const loadingMsg = document.createElement('div');
    loadingMsg.className = 'message bot-message loading';
    loadingMsg.textContent = 'Typing...';
    chatContainer.appendChild(loadingMsg);
    
    // Scroll to the bottom of the chat to show the latest messages
    chatContainer.scrollTop = chatContainer.scrollHeight;
    
    // Try-catch block to handle any errors that might occur
    try {
        // Send a POST request to our backend API
        const response = await fetch('/ask', {
            method: 'POST',  // Use POST method to send data
            headers: {
                'Content-Type': 'application/json',  // Tell server we're sending JSON
            },
            // Convert our question object to JSON string and send it
            body: JSON.stringify({ question: question })
        });
        
        // Parse the JSON response from the server
        const data = await response.json();
        
        // Remove the "Typing..." loading message
        chatContainer.removeChild(loadingMsg);
        
        // Create a new div for the bot's response
        const botMsg = document.createElement('div');
        botMsg.className = 'message bot-message';
        // Set the text to the AI's answer from the response
        botMsg.textContent = data.answer;
        // Add the bot's message to the chat
        chatContainer.appendChild(botMsg);
        
    } catch (error) {
        // If anything goes wrong, remove the loading message
        chatContainer.removeChild(loadingMsg);
        
        // Create an error message to show the user
        const errorMsg = document.createElement('div');
        errorMsg.className = 'message bot-message';
        errorMsg.textContent = 'Sorry, something went wrong. Please try again.';
        chatContainer.appendChild(errorMsg);
    }
    
    // Re-enable the send button
    button.disabled = false;
    // Change button text back to "Send"
    button.textContent = 'Send';
    
    // Scroll to bottom again to show the new bot message
    chatContainer.scrollTop = chatContainer.scrollHeight;
}