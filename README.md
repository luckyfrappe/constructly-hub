# Constructly Hub — A better way of Construction

Constructly Hub is a modern marketplace platform designed to simplify construction project management. Clients can post project requests, browse available subcontractors, and compare offers, while subcontractors can create profiles, showcase their expertise, and apply for relevant projects. The platform streamlines the entire process, making it easier for both sides to connect and collaborate effectively.

![alt text](documentation/showcase/landing.png "Mockup image of Constructly Hub website on different devices")

🔗 [**Live site**](https://constructly-hub-ee092254593a.herokuapp.com/)

---

## Contents

- [User Experience (UX)](#user-experience-ux)
  - [Business Goals](#business-goals)
  - [User Stories](#user-stories)
- [Design](#design)
  - [Color Scheme](#color-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
  - [Wireframes](#wireframes)
  - [Initial sitemap and Database Design](#initial-sitemap-and-database-design)
- [Features](#features)
  - [Common to All Pages](#common-to-all-pages)
  - [Page-Specific Features](#page-specific-features)
  - [Future Implementations](#future-implementations)
  - [Accessibility Considerations](#accessibility-considerations)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
- [Deployment](#deployment)
- [Local Development](#local-development)
  - [Cloning and Forking](#cloning-and-forking)
  - [Cloning](#cloning)
  - [Forking](#forking)
  - [Local vs Deployed Version](#local-vs-deployed-version)
- [Agile Development Process](#agile-development-process)
- [Testing](#testing)
- [Credits](#credits)
  - [Code Used](#code-used)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

### Business Goals

- Provide a streamlined marketplace where construction companies can showcase their services and receive project opportunities.

- Enable clients to easily create projects, compare bids, and choose the best contractor.

- Support subcontractors with a professional online presence to attract leads and increase visibility.

- Increase engagement by guiding users toward key actions such as creating a company profile, posting a project, or submitting a bid.

### User Stories

All user stories are listed in the [**GitHub Project board**](https://github.com/users/luckyfrappe/projects/6/views/1).

## Design

### Color Scheme

![alt text](documentation/showcase/adobe.jpeg "Color theme")

This project uses a custom color palette designed to create a clean, modern, and construction-inspired aesthetic.  
The light theme is built around neutral grays and white tones to maintain clarity and readability, complemented by vibrant lime accents that reinforce the brand’s energetic and professional identity.

A full dark theme is enabled through `prefers-color-scheme: dark`, replacing lighter backgrounds with deep blue-gray tones while maintaining high contrast text for accessibility.  

Both themes share the same accent colors to keep the branding consistent across all user environments.


### Typography

The website uses Tailwind CSS’s default sans-serif font stack for all headings and body text. Tailwind’s default typography is based on modern system fonts (such as Inter, San Francisco, and Segoe UI), ensuring excellent readability, performance, and a clean, professional interface across all devices.

### Imagery

Visual content across the platform is designed to reflect the scale, professionalism, and diversity of modern construction projects.

Images were sourced from royalty-free platforms such as **Pexels**, **Unsplash**, and **Freepik**, combined with additional visual elements created in **Canva** to support consistent branding throughout the site.  

All media assets used in this project are credited at the end.

### Wireframes

This project did not require traditional hand-drawn wireframes.  
Tailwind CSS and Tailwind Plus Elements provided ready-made structural patterns that acted as the foundation for the layout. Because Tailwind enables rapid prototyping directly in the browser, most wireframing was done live in code rather than through separate sketches.  

The following visuals show the initial layout concepts and structural flow used during development:

![alt text](documentation/wireframes/hero.png "Hero page initial draft")
![alt text](documentation/wireframes/main-app.png "Main app layout")
![alt text](documentation/wireframes/insights.png "Insights layout")
![alt text](documentation/wireframes/main-app-dropdown.png "Main app dropdown menu")
![alt text](documentation/wireframes/lost.png "404 Page wireframe")
![alt text](documentation/wireframes/sign-in.png "Sign In page")
![alt text](documentation/wireframes/companies-all.png "Browse all companies")
![alt text](documentation/wireframes/projects.png "Browse all projects")

### Initial sitemap and Database Design 

![alt text](documentation/flowcharts/logic/constructly-hub.jpg "Sitemap and User Flow Manifest")
See in PDF format **[Sitemap and User Flow Manifest](documentation/flowcharts/logic/constructly-hub.pdf)**
![alt text](documentation/flowcharts/logic/constructly-hub-erd.jpg)

---

## Features

### Common to All Pages
- Responsive layout using Tailwind CSS (mobile-first).
- Dark theme UI with consistent spacing, typography, and card design.
- Global navigation for signed-in users: **My Companies**, **All Companies**, **Projects**, **Profile**, **Settings**.
- Dynamic navigation for guests: **Home**, **Companies**, **Sign In**, **Sign Up**.
- Secure forms with CSRF protection and input validation.
- Flash messages for success/error feedback.
- Base template shared across all authenticated pages for visual consistency.

![alt text](documentation/showcase/all.png "Common to all pages")
![alt text](documentation/showcase/all-logged-in.png "Common to all pages logged-in")
![alt text](documentation/showcase/profile-dropdown.png "Profile dropdown")

### Page-Specific Features

#### Landing Page
- Hero section introducing the platform.
- CTAs to sign up or browse companies.
- Dynamic content depending on authentication state.

![alt text](documentation/showcase/landing.png "Landing page")

#### Companies (Public & Authenticated Views)
- Browse all registered construction companies.
- Company cards with logo, location, and short description.
- Company detail page showing full description, services, image, and owner.
- Owners can **edit** or **delete** their companies.
- “Create New Company” button (only for authenticated users and updated user profile).

![alt text](documentation/showcase/companies-guest.png "Companies guest page")
![alt text](documentation/showcase/my-companies.png "My Companies page")
![alt text](documentation/showcase/company-detail.png "Company detail page")
![alt text](documentation/showcase/create-company.png "Create Company page")
![alt text](documentation/showcase/company-crud.png "Company CRUD buttons")
![alt text](documentation/showcase/editing.png "Editing My Company page")
![alt text](documentation/showcase/profile-needed.png "Profile Needed view")

#### Projects
- Users can create projects with title, budget, location, and bidding deadline.
- Project details page showing full project info.
- Contractors can submit bids (authenticated only).
- Project owners can review and compare incoming bids.

![alt text](documentation/showcase/all-projects.png "All Projects page")
![alt text](documentation/showcase/my-projects.png "My Projects page")
![alt text](documentation/showcase/project-details.png "Project Details page")
![alt text](documentation/showcase/create-project.png "Create Project page")


#### Bids
- Companies can submit bid offers with price, duration, and a message.
- Bid list displayed for project owners.
- You need to have at least one company to leave a bid.

![alt text](documentation/showcase/my-bid.png "My Bid page")
![alt text](documentation/showcase/project-details.png "Project Details page")
![alt text](documentation/showcase/bids-received.png "Bids Received view")
![alt text](documentation/showcase/select-bid.png "Bid selected view")
![alt text](documentation/showcase/company-requirement.png "Company Requirement view")

#### Profile & User Settings
- Profile page showing user details and avatar.
- Settings page to update username, email, password, and profile image.
- Account deletion option.
- Direct navigation from profile → settings.

![alt text](documentation/showcase/user.png "User Profile Details page")
![alt text](documentation/showcase/settings.png "Settings page")
![alt text](documentation/showcase/delete-confirm.png "Delete Confirm page")

#### Authentication Pages
- Custom-styled Sign In, Sign Up, Email Verification, and Password Reset flows.
- Allauth integration with fully redesigned templates.
- Email templates customized with consistent branding.

![alt text](documentation/showcase/landing.png "Login page")
![alt text](documentation/showcase/sign-up.png "Sign Up page")
![alt text](documentation/showcase/reset.png "Reset page")
![alt text](documentation/showcase/reset-sent.png "Reset sent page")
![alt text](documentation/showcase/email-confirm.png "Confirm email message")
![alt text](documentation/showcase/password-reset.png "Password reset message")
![alt text](documentation/showcase/sign-out.png "Sign Out message")

#### 404 Page
- Custom 404 with navigation back to main pages.

![alt text](documentation/showcase/404.png "404 page")


### Future Implementations
- Dashboard with analytics for companies and project owners.
- Messaging/communication system between contractors and clients.
- Advanced search and filtering for companies and projects.
- Rating and review system for completed projects.
- AI-assisted bid generation and cost estimation.

---

### Accessibility Considerations
- Semantic HTML structure across all templates.
- Alt attributes for all images (company logos, profile images, placeholders).
- Keyboard-accessible forms and buttons.
- Sufficient color contrast in dark theme.
- Form field labels, ARIA roles, and descriptive helper text.

---

## Technologies Used

### Languages Used

- **HTML**
- **CSS**
- **JavaScript**
- **Python**

### Frameworks, Libraries & Programs Used

- **[Git & GitHub](https://github.com/)** – Version control and hosting.
- **[Google DevTools](https://developer.chrome.com/docs/devtools/)** – Development & debugging.
- **[FigJam](https://www.figma.com/figjam/)** - Flowcharts
- **[Font Awesome](https://fontawesome.com/)** – Icons via CDN.
- **[Favicon.io](https://favicon.io/)** – Favicon generation.
- **[TinyPNG](https://tinypng.com/)** – Image optimization.
- **[Polypane](https://polypane.app/)** – Responsive device previews.
- **[Autoprefixer](https://autoprefixer.github.io/)** – Vendor prefixes for CSS.
- **[HTML Validator](https://validator.w3.org/)** – Markup Validation Service.
- **[CSS Validator](https://jigsaw.w3.org/css-validator/)** – CSS Validation Service.
- **[WAVE](https://wave.webaim.org/)** – Web Accessibility Evaluation Tools.
- **[JSHint](https://jshint.com/)** – JavaScript validation.
- **[Tailwind CLI](https://tailwindcss.com/docs/installation/tailwind-cli)** – Tailwind CSS compiler.
- **[Jest](https://jestjs.io/)** – JavaScript testing framework.
- **[ESLint](https://eslint.org/)** – JavaScript linter for finding and fixing code issues, enforcing consistent style, and preventing bugs.
- **[Prettier](https://prettier.io/)** – Code formatter that ensures consistent style across your JavaScript, CSS, JSON, and other files.
- **[Canva](https://www.canva.com/create/logos/)** was used for creating the collage assets and favicon design.
- **[ChatGPT (OpenAI)](https://chat.openai.com/)** and **[Gemini (Google)](https://gemini.google.com/)** were used for generating service descriptions, debugging support, exploring different solutions, and clarifying code concepts.
- The virtual environment was installed following Code Institute’s setup instructions.
- **[Django](https://www.djangoproject.com/)** – High-level Python web framework powering the backend of the application.  
- **[Gunicorn](https://gunicorn.org/)** – Python WSGI HTTP server for running Django apps in production.
- **dj-database-url** – Simplifies database configuration in Django by allowing the database URL to be parsed and set as Django settings.  
- **psycopg2** – Adapter for Python, enabling Django to communicate with a PostgreSQL database.
- **[WhiteNoise](http://whitenoise.evans.io/en/stable/)** – Simplifies static file serving in Django for production environments.  
- **[PostgreSQL](https://www.postgresql.org/)** – Open-source relational database system used for storing structured application data.  
- **[django-allauth](https://django-allauth.readthedocs.io/en/latest/)** – Integrated Django app for authentication, registration, and account management with support for social logins and email verification.
- **[Namecheap](https://www.namecheap.com/)** – Domain register used for managing the custom business domain **constructlyhub.me**.
- **[Google Workspace (Gmail SMTP)](https://mail.google.com/)** – Configured to send transactional emails through Gmail’s secure SMTP service, used for account verification, password resets, and contact forms.
- **[Cloudinary](https://cloudinary.com/)** – Used to host images and manage media uploads.
- **[FilePond](https://pqina.nl/filepond/)** – Used for modern, user-friendly file uploads with drag-and-drop support, live image previews, and file validation. Configured to behave like a regular Django file input using `storeAsFile: true`, so uploaded files are submitted together with the form.

---

Here is a **clean, professional, CI-friendly Deployment section** written **specifically for your project**, matching the style of the example but simplified (since you worked entirely in VS Code, not Gitpod).
It includes Heroku, Cloudinary, your exact config vars, and local setup.

Everything is written in proper Markdown so you can paste directly into your README.

---

## Deployment

The live version of Constructly Hub is deployed on **Heroku**.

### Cloudinary API

This project uses **Cloudinary** to store uploaded images because Heroku does not persist static or media files.

To use Cloudinary in your own deployment:

1. Create a Cloudinary account.
2. Go to your Dashboard and copy the **API Environment Variable**.
3. In Heroku, add this value as a Config Var under the key:

```
CLOUDINARY_URL
```

*(Do not include `CLOUDINARY_URL=` in the value — use only the URL itself.)*

---

### Heroku Deployment

Constructly Hub is deployed using **Heroku**, which runs Django apps through Gunicorn.

#### Required Heroku Config Vars

Inside **Settings → Reveal Config Vars**, set the following:

| Key | Value |
|-----|-------|
| `CLOUDINARY_URL` | Your own Cloudinary URL |
| `DATABASE_URL` | Your own value |
| `SECRET_KEY` | Your own Django secret key |
| `EMAIL_HOST_PASSWORD` | Gmail App Password (for email verification) |
| `EMAIL_HOST_USER` | Your domain email address (if you want email functionality) |

These environment variables correspond to the Django settings:

```py
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
SECRET_KEY = os.environ.get('SECRET_KEY')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = 'your_email_here@gmail.com'
```

---

### Required Files for Heroku

Heroku requires two files:

1. **requirements.txt** (generated with `pip3 freeze > requirements.txt`)
2. **Procfile**

Your Procfile should contain:

```
web: gunicorn constructly_hub.wsgi
```

---

### Connecting Heroku to Your Repository

**Automatic Deploys**

* In Heroku → Deploy tab → Connect to GitHub → Choose your repo.
* Enable *Automatic Deploys*.

---

## Local Development

This project was fully developed in **VS Code**.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/constructly-hub.git
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip3 install -r requirements.txt
```

### 4. Create `env.py`

At the project root, create:

```py
import os

os.environ.setdefault("SECRET_KEY", "your_value_here")
os.environ.setdefault("CLOUDINARY_URL", "your_value_here")
os.environ.setdefault("DATABASE_URL", "your_value_here")

os.environ.setdefault("EMAIL_HOST_PASSWORD", "your_gmail_app_password")
os.environ.setdefault("EMAIL_HOST_USER", "your_email@gmail.com")

# Local only
os.environ.setdefault("DEBUG", "True")
```

Then add `env.py` to `.gitignore`.

### 5. Run Migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 6. Create Superuser (optional)

```bash
python3 manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python3 manage.py runserver
```

Your project will now run at:

```
http://127.0.0.1:8000/
```

---

## Cloning and Forking

### Cloning

```bash
git clone https://github.com/your-username/constructly-hub.git
```

### Forking

* Go to the repo on GitHub.
* Click **Fork**.
* This creates your own copy where you can make changes safely.

---

### Local vs Deployed Version

The **live Heroku version** includes full email verification and Cloudinary media storage.
The **local version** also supports email if valid `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` are set.

## Agile Development Process

This project followed an Agile-inspired workflow using **GitHub Projects** as the project management tool.  
While not a dedicated Agile platform, GitHub’s Kanban board was used effectively to structure and track development.

User stories, tasks, and issues were organized into columns such as **Ideas**, **To Do**, **In Progress**, and **Done**, allowing for clear visibility of priorities and weekly progress.  

The board also served as a central hub for refining features, and planning upcoming iterations throughout the development cycle.

The full list of user stories and tasks can be viewed in the  
[GitHub Project board](documentation/showcase/agile.png).

## Testing

See **[TESTING.md](TESTING.md)** for test cases, known issues, and resolved bugs.

---

## Credits

### Code Used

- **[Tailwind Plus UI Blocks](https://tailwindcss.com/plus)** – Tailwind Plus templates, built by the makers of Tailwind CSS.

- **[Tailwindtemplates.io](https://tailwindtemplates.io/templates?category=profile)** - Profile template.

- **[HyperUI](https://www.hyperui.dev/components/marketing/footers)** - Footer Component.

### Content

The textual content and platform descriptions for this fictional construction marketplace were created in collaboration with AI tools. Page copy, service descriptions, and general narrative elements were written with support from ChatGPT and Gemini. Inspiration for industry terminology, workflows, and tone was taken from real construction tendering platforms and public company websites, helping shape a realistic but fictional user experience for this educational project.

### Media

#### General Imagery
- **[404 Page Image](https://unsplash.com/id/foto/ekskavator-oranye-menggali-daerah-berbatu-RzwixD6C67s)** – Excavator working at a construction site.
- **[Building Inspector](https://www.freepik.com/free-photo/man-builder-uniform-holding-older-looking-building-plan_21298651.htm)** – Freepik.
- **[Modern Skyscrapers](https://www.freepik.com/free-photo/low-view-modern-skyscrapers-office-buildings_12396223.htm)** – Freepik.
- **[Tower Crane](https://www.pexels.com/photo/low-angle-shot-of-a-tower-crane-11654553/)** – Pexels.
- **[Yellow Excavator](https://www.pexels.com/photo/yellow-excavator-2101137/)** – Pexels.
- **[Mining Bulldozer](https://www.pexels.com/photo/heavy-duty-mining-bulldozer-in-quarry-31543919/)** – Pexels.
- **[Construction Equipment](https://www.pexels.com/photo/heavy-equipment-on-construction-site-10421763/)** – Pexels.
- **[Wheel Loader](https://www.pexels.com/sv-se/foto/sand-arbetssatt-fordon-hjullastare-12835355/)** – Pexels.
- **[Metal Grinding Sparks](https://www.pexels.com/photo/close-up-of-metal-grinding-sparks-in-workshop-30858409/)** – Pexels.
- **[Blueprint on Table](https://www.freepik.com/free-photo/eyeglasses-paper-plan-table_3716871.htm)** – Freepik.
- **Person holding tool** – Photo by Christopher Burns on Unsplash: https://unsplash.com/photos/person-holding-tool-during-daytime-8KfCR12oeUM

#### Icons & Placeholders
- **User profile placeholder** – https://www.flaticon.com/free-icon/profile_17446833  
- **Various avatar images:**
  - [Andrea Piacquadio – Businessman portrait](https://www.pexels.com/sv-se/foto/affarsman-man-oskarpa-ansikte-3778673/)
  - [Spolyakov – Creative portrait](https://www.pexels.com/sv-se/foto/man-konst-malning-kreativitet-16762332/)
  - [Tima Miroshnichenko – Architecture office](https://www.pexels.com/sv-se/foto/arkitektur-foretag-rum-staende-6474481/)
  - [𓇼 BABIX VISUALS 𓇼 – Portrait in hall](https://www.pexels.com/sv-se/foto/leende-man-i-vit-skjorta-i-elegant-hall-33344803/)
  - [Alax Matias – Woodworker portrait](https://www.pexels.com/sv-se/foto/portratt-av-en-leende-traarbetare-i-verkstad-28513049/)
  - [Unicons](https://iconscout.com/contributors/unicons)

#### Company Card Images
- [IslandHopper X – Construction Industry](https://www.pexels.com/sv-se/foto/konstruktion-industri-arbete-arbetare-15109993/)
- [Ahmet Çığşar – Factory Production](https://www.pexels.com/sv-se/foto/arbetssatt-fabrik-produktion-tillverkning-17406672/)
- [Brett Sayles – Construction lighting](https://www.pexels.com/sv-se/foto/lampor-byggnad-konstruktion-kontor-11051540/)
- [Vincent Photography – Rural landscape](https://www.pexels.com/sv-se/foto/landsbygden-plan-falt-lantlig-17034001/)
- [Iván Rivero – Construction scenery](https://www.pexels.com/sv-se/foto/1633970/)
- [Tobias Bjørkli – Industrial site](https://www.pexels.com/sv-se/foto/2058738/)
- [Jonathan Cooper – Winter truck machinery](https://www.pexels.com/sv-se/foto/sno-vinter-lastbil-maskin-11282087/)
- [Erik Mclean – Road and vehicles](https://www.pexels.com/sv-se/foto/bilar-vag-fordon-landskap-9146387/)
- [Daniel Adesina – Industrial scene](https://www.pexels.com/sv-se/foto/32427309/)

### Acknowledgments

I want to express my gratitude to my cat James, who provided emotional support throughout the project.

A huge thank you as well to my best friend in the construction industry. His guidance, feedback, and professional knowledge were essential in shaping the concept and making the project feel grounded in real industry needs. His support was a major inspiration.
