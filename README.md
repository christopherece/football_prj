# Football Academy Website

A modern and professional website for a football academy built with Django and Bootstrap.

## Features

- Responsive design that works on all devices
- Professional football academy branding
- Multiple training programs (Youth, Advanced, Elite)
- Interactive training schedule
- Player achievements showcase
- Modern UI with animations and effects
- Contact forms and booking system

## Tech Stack

- Backend: Django (Python)
- Frontend: HTML5, CSS3, JavaScript
- Framework: Bootstrap 5
- Animations: AOS (Animate On Scroll)
- Icons: Bootstrap Icons
- JavaScript Libraries: jQuery, AOS, PureCounter

## Getting Started

1. Clone the repository:
```bash
git clone [repository-url]
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Open your browser and visit `http://localhost:8000`

## Project Structure

```
football_prj/
├── football_prj/             # Django project settings
├── static/                  # Static files (CSS, JavaScript, images)
│   ├── assets/
│   │   ├── img/
│   │   ├── css/
│   │   └── js/
├── templates/              # HTML templates
│   ├── base.html          # Base template
│   ├── partials/          # Template partials
│   └── pages/             # Page templates
└── requirements.txt       # Python dependencies
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
