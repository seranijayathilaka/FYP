# MyProjects
#FYP - Team work
#GUI for the real time monitoring system of power grids with increased renewable energy penetration for cyber attacks

The layout of the GUI is designed using a tabbed interface that is available in the ttk.Notebook widget in Tkinter. The created interface consists of four tabs: Home, Process, Info, and Our Team. 
The Home tab displays the project overview and objectives along with the background information and the significance of cybersecurity in power grids. The Process tab is the main functional tab where the user can connect, feed data to the model from the external system, and start the prediction process. It contains buttons for feeding data beginning and stop predictions. The Info tab provides information about the project, such as methodology and usage instructions. The Our Team Tab displays information about the team members involved in the project. Considering the user experiences, the design focuses on ease of use and clear navigation. Large buttons, clear labels, and a consistent color scheme were used to enhance user experience. The background color and fonts were chosen to provide good contrast and readability. 

#Data Handling and Real-Time Prediction 
Users can load data from external systems. Here, for the demonstration purpose an Excel file containing multiple sheets as the external data source is used, and using a file dialog those data are fed to the model as a real-time data sequence. Only the first four columns of each sheet are considered for further processing. Data from all sheets are read and concatenated into a single sequence. This ensures that the entire dataset is utilized for prediction. The GUI displays the loaded data in a text widget, showing each row one by one. This is achieved by iterating over the data and updating the display every 30 seconds along with the prediction and graphs. 
For real-time prediction, here it is used moving window approach. A sliding window with a width of 30 timesteps is used where the model will analyze sequences of 30 consecutive data points at a time. That window moves forward one timestep at a time. That ensures the continuous monitoring of the data stream. As the window moves, it generates sequences of 30 timesteps, which are then fed into the model for prediction. The model's output will be a prediction indicating whether a cyber-attack is detected or not for each 30-timestep window. The model outputs a probability value between 0 and 1, where: 
•	Probability > 0.5: Indicates an attack is detected ("Attack Detected").
Probability <= 0.5: Indicates no attack is detected ("No Attack").

Note: - Use the Excel file along with this for demonstration purposes.

