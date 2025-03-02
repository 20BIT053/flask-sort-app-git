Flask Sort App
Overview
  This is a Flask-based web application that sorts data based on user input. It is containerized using Docker for easy deployment.
Features
  Accepts user input for sorting
  Sorts data using different algorithms (if applicable)
  Displays the sorted output on a web page
  Uses Flask for backend processing
  Deployable with Docker
Technologies Used
  Flask (Python web framework)
  HTML, CSS (for frontend)
  Docker (for containerization)
  GitHub (for version control)
Setup Instructions
1. Clone the Repository
  git clone https://github.com/20BIT053/flask-sort-app-git.git
  cd flask-sort-app-git
2. Install Dependencies
  pip install -r requirements.txt
3. Run the Application
  python app.py
4. Run with Docker (Optional)
  docker build -t flask-sort-app .
  docker run -p 5000:5000 flask-sort-app
5. Access the Web App
  Open your browser and go to: http://localhost:5000/
