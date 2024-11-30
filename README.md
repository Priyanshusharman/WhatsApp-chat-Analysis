# WhatsApp-chat-Analysis
url = https://whatsapp-chat-analysis-priyanshu-sharman.streamlit.app/

WhatsApp Chat Analyzer

WhatsApp Chat Analyzer is a Python-based project designed to analyze WhatsApp chat data. It provides various insights into chat usage patterns, including peak activity times, most frequently used emojis, and user activity heatmaps.

Features
Time Analysis: Identify peak usage times to determine when users are most active.
Emoji Analysis: Determine the most commonly used emojis in the chat.
User Activity Heatmap: Visualize user activity throughout the day with a heatmap.
User Filter: Filter chat data based on specific users for personalized analysis.

Certainly! Here's a more detailed explanation of the installation and usage instructions, along with additional context on how to run the Streamlit app:

## Installation

1. Clone the Repository: This step downloads the project files to your local machine. Open a terminal and run the following command:

   
   git clone [https://github.com/yourusername/whatsapp-chat-analyzer.git](https://github.com/Priyanshusharman/WhatsApp-chat-Analysis/tree/main/__pycache__)
   

2. Install Dependencies: Navigate into the project directory and install the required Python packages by running:

   
   cd whatsapp-chat-analyzer
   pip install -r requirements.txt
   

   This command installs all the necessary dependencies listed in the `requirements.txt` file.

## Usage

1. Export WhatsApp Chat Data: Before using the app, you need to export your WhatsApp chat data as a text file. You can do this directly from WhatsApp by accessing the chat you want to analyze, tapping on the menu button (three dots), and selecting the "Export chat" option.

2. Run the Streamlit App: Once you have your chat data exported, you can run the Streamlit app. In your terminal, navigate to the project directory and run the following command:

   
   streamlit run app.py
   

   This command starts the Streamlit server and launches the app in your default web browser.

3. Explore the App: After opening the app in your web browser, you'll see an interface where you can upload your WhatsApp chat data file. Once uploaded, you can explore various analysis features provided by the app, such as time analysis, emoji analysis, and user activity heatmap.

4. Interact with the Visualizations: The app provides interactive visualizations that allow you to gain insights into your WhatsApp chat data. You can filter data based on specific users, view trends over time, and identify patterns in emoji usage.

## Examples

The app generates several types of visualizations to help you understand your WhatsApp chat data better:

- Time Analysis: Visualizes chat activity over time, showing peak usage times and trends.
  
- Emoji Analysis: Analyzes the frequency and distribution of emojis used in the chat.

- User Activity Heatmap: Displays a heatmap of user activity throughout the day, helping you identify when users are most active.

## Contributing

Contributions to the project are welcome! If you encounter any issues, have suggestions for new features, or want to contribute improvements, feel free to open issues or submit pull requests on the project's GitHub repository.

## License

This project is open-source and licensed under the Priyanshu sharman, which allows you to use, modify, and distribute the code for both personal and commercial purposes. See the `LICENSE` file in the project repository for more details.
