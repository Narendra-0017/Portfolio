# Personal Portfolio Website

A modern, responsive personal portfolio website built with Flask, HTML, and CSS.

## Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI**: Clean, professional design with smooth animations
- **Contact Form**: Functional contact form with Flask backend
- **Interactive Navigation**: Smooth scrolling navigation with mobile menu
- **Skills Showcase**: Display your technical skills and technologies
- **Project Portfolio**: Showcase your featured projects
- **Flash Messages**: User feedback for form submissions

## Project Structure

```
Task6/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   └── css/
│       └── style.css    # CSS styles
└── README.md            # This file
```

## Installation & Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask application:**
   ```bash
   python app.py
   ```

3. **Open your browser and visit:**
   ```
   http://localhost:5000
   ```

## Customization

### Personal Information
Edit the following in `templates/index.html`:
- Name: Replace "John Doe" with your name
- Title: Update "Full-Stack Developer & UI/UX Designer"
- About section: Modify the about text
- Contact information: Update email, phone, and location
- Social links: Add your social media profiles

### Skills & Projects
- Update the skills section with your technologies
- Modify the projects section with your actual projects
- Add real project links and descriptions

### Styling
- Colors: Modify the CSS variables in `static/css/style.css`
- Fonts: Change the Google Fonts import
- Layout: Adjust grid layouts and spacing

## Features Explained

### Flask Routing
- `/` - Home page with portfolio content
- `/contact` - Handles contact form submissions (POST)

### Contact Form
- Validates required fields (name, email, message)
- Shows success/error messages using Flask flash
- Redirects to home page after submission

### Responsive Design
- Mobile-first approach
- Hamburger menu for mobile devices
- Flexible grid layouts
- Touch-friendly navigation

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with Flexbox and Grid
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Inter)

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Development

To run in development mode:
```bash
export FLASK_ENV=development
python app.py
```

The application will run with debug mode enabled and auto-reload on file changes.

## Deployment

For production deployment:
1. Set `debug=False` in `app.py`
2. Use a production WSGI server like Gunicorn
3. Configure environment variables for secret keys
4. Set up proper database for contact form submissions

## License

This project is open source and available under the MIT License.
