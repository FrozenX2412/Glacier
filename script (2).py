
# Create the HTML file for the portfolio website
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Professional Portfolio - Showcasing my work and skills">
    <title>My Portfolio | Web Developer</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar" id="navbar">
        <div class="nav-container">
            <a href="#home" class="logo">Portfolio<span class="dot">.</span></a>
            <button class="theme-toggle" id="themeToggle" aria-label="Toggle dark mode">
                <i class="fas fa-moon"></i>
            </button>
            <button class="mobile-menu-toggle" id="mobileMenuToggle" aria-label="Toggle menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-menu" id="navMenu">
                <li><a href="#home" class="nav-link">Home</a></li>
                <li><a href="#about" class="nav-link">About</a></li>
                <li><a href="#skills" class="nav-link">Skills</a></li>
                <li><a href="#projects" class="nav-link">Projects</a></li>
                <li><a href="#contact" class="nav-link">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="hero-content">
            <div class="hero-text">
                <h1 class="hero-title">
                    Hi, I'm <span class="gradient-text">Your Name</span>
                </h1>
                <p class="hero-subtitle typing-text">Full Stack Developer & Designer</p>
                <p class="hero-description">
                    I create beautiful, functional, and user-friendly web experiences that make a difference.
                </p>
                <div class="hero-buttons">
                    <a href="#projects" class="btn btn-primary">View My Work</a>
                    <a href="#contact" class="btn btn-secondary">Get In Touch</a>
                </div>
                <div class="social-links">
                    <a href="https://github.com" target="_blank" aria-label="GitHub"><i class="fab fa-github"></i></a>
                    <a href="https://linkedin.com" target="_blank" aria-label="LinkedIn"><i class="fab fa-linkedin"></i></a>
                    <a href="https://twitter.com" target="_blank" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
                    <a href="mailto:your.email@example.com" aria-label="Email"><i class="fas fa-envelope"></i></a>
                </div>
            </div>
            <div class="hero-image">
                <div class="image-placeholder">
                    <i class="fas fa-code"></i>
                </div>
            </div>
        </div>
        <a href="#about" class="scroll-down" aria-label="Scroll down">
            <i class="fas fa-chevron-down"></i>
        </a>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <h2 class="section-title">About Me</h2>
            <div class="about-content">
                <div class="about-image">
                    <div class="image-placeholder">
                        <i class="fas fa-user"></i>
                    </div>
                </div>
                <div class="about-text">
                    <h3>Hello! I'm a passionate developer</h3>
                    <p>
                        With a strong focus on creating intuitive and engaging digital experiences, I specialize in building responsive websites and web applications. My journey in web development started with a curiosity for how things work on the internet, and it has evolved into a career where I continuously learn and grow.
                    </p>
                    <p>
                        I believe in writing clean, maintainable code and creating designs that not only look great but also provide excellent user experiences. When I'm not coding, you can find me exploring new technologies, contributing to open-source projects, or enjoying a good cup of coffee.
                    </p>
                    <div class="about-stats">
                        <div class="stat-item">
                            <h4>50+</h4>
                            <p>Projects Completed</p>
                        </div>
                        <div class="stat-item">
                            <h4>3+</h4>
                            <p>Years Experience</p>
                        </div>
                        <div class="stat-item">
                            <h4>100%</h4>
                            <p>Client Satisfaction</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="skills">
        <div class="container">
            <h2 class="section-title">My Skills</h2>
            <p class="section-subtitle">Technologies and tools I work with</p>
            <div class="skills-grid">
                <div class="skill-card" data-skill="html">
                    <div class="skill-icon">
                        <i class="fab fa-html5"></i>
                    </div>
                    <h3>HTML5</h3>
                    <div class="skill-progress">
                        <div class="progress-bar" data-progress="95"></div>
                    </div>
                    <span class="skill-percentage">95%</span>
                </div>
                <div class="skill-card" data-skill="css">
                    <div class="skill-icon">
                        <i class="fab fa-css3-alt"></i>
                    </div>
                    <h3>CSS3</h3>
                    <div class="skill-progress">
                        <div class="progress-bar" data-progress="90"></div>
                    </div>
                    <span class="skill-percentage">90%</span>
                </div>
                <div class="skill-card" data-skill="js">
                    <div class="skill-icon">
                        <i class="fab fa-js"></i>
                    </div>
                    <h3>JavaScript</h3>
                    <div class="skill-progress">
                        <div class="progress-bar" data-progress="85"></div>
                    </div>
                    <span class="skill-percentage">85%</span>
                </div>
                <div class="skill-card" data-skill="react">
                    <div class="skill-icon">
                        <i class="fab fa-react"></i>
                    </div>
                    <h3>React</h3>
                    <div class="skill-progress">
                        <div class="progress-bar" data-progress="80"></div>
                    </div>
                    <span class="skill-percentage">80%</span>
                </div>
                <div class="skill-card" data-skill="node">
                    <div class="skill-icon">
                        <i class="fab fa-node-js"></i>
                    </div>
                    <h3>Node.js</h3>
                    <div class="skill-progress">
                        <div class="progress-bar" data-progress="75"></div>
                    </div>
                    <span class="skill-percentage">75%</span>
                </div>
                <div class="skill-card" data-skill="python">
                    <div class="skill-icon">
                        <i class="fab fa-python"></i>
                    </div>
                    <h3>Python</h3>
                    <div class="skill-progress">
                        <div class="progress-bar" data-progress="80"></div>
                    </div>
                    <span class="skill-percentage">80%</span>
                </div>
                <div class="skill-card" data-skill="git">
                    <div class="skill-icon">
                        <i class="fab fa-git-alt"></i>
                    </div>
                    <h3>Git</h3>
                    <div class="skill-progress">
                        <div class="progress-bar" data-progress="85"></div>
                    </div>
                    <span class="skill-percentage">85%</span>
                </div>
                <div class="skill-card" data-skill="figma">
                    <div class="skill-icon">
                        <i class="fab fa-figma"></i>
                    </div>
                    <h3>Figma</h3>
                    <div class="skill-progress">
                        <div class="progress-bar" data-progress="70"></div>
                    </div>
                    <span class="skill-percentage">70%</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="projects">
        <div class="container">
            <h2 class="section-title">My Projects</h2>
            <p class="section-subtitle">Showcasing my recent work</p>
            <div class="projects-grid">
                <div class="project-card">
                    <div class="project-image">
                        <div class="image-placeholder">
                            <i class="fas fa-laptop-code"></i>
                        </div>
                        <div class="project-overlay">
                            <a href="#" class="project-link" aria-label="View project"><i class="fas fa-external-link-alt"></i></a>
                            <a href="#" class="project-link" aria-label="View code"><i class="fab fa-github"></i></a>
                        </div>
                    </div>
                    <div class="project-content">
                        <h3>E-Commerce Platform</h3>
                        <p>A fully responsive e-commerce website with cart functionality, user authentication, and payment integration.</p>
                        <div class="project-tags">
                            <span class="tag">React</span>
                            <span class="tag">Node.js</span>
                            <span class="tag">MongoDB</span>
                        </div>
                    </div>
                </div>

                <div class="project-card">
                    <div class="project-image">
                        <div class="image-placeholder">
                            <i class="fas fa-mobile-alt"></i>
                        </div>
                        <div class="project-overlay">
                            <a href="#" class="project-link" aria-label="View project"><i class="fas fa-external-link-alt"></i></a>
                            <a href="#" class="project-link" aria-label="View code"><i class="fab fa-github"></i></a>
                        </div>
                    </div>
                    <div class="project-content">
                        <h3>Task Management App</h3>
                        <p>A productivity app featuring task scheduling, reminders, and team collaboration features.</p>
                        <div class="project-tags">
                            <span class="tag">JavaScript</span>
                            <span class="tag">Firebase</span>
                            <span class="tag">CSS3</span>
                        </div>
                    </div>
                </div>

                <div class="project-card">
                    <div class="project-image">
                        <div class="image-placeholder">
                            <i class="fas fa-chart-line"></i>
                        </div>
                        <div class="project-overlay">
                            <a href="#" class="project-link" aria-label="View project"><i class="fas fa-external-link-alt"></i></a>
                            <a href="#" class="project-link" aria-label="View code"><i class="fab fa-github"></i></a>
                        </div>
                    </div>
                    <div class="project-content">
                        <h3>Analytics Dashboard</h3>
                        <p>Real-time data visualization dashboard with interactive charts and comprehensive reporting features.</p>
                        <div class="project-tags">
                            <span class="tag">React</span>
                            <span class="tag">D3.js</span>
                            <span class="tag">API</span>
                        </div>
                    </div>
                </div>

                <div class="project-card">
                    <div class="project-image">
                        <div class="image-placeholder">
                            <i class="fas fa-blog"></i>
                        </div>
                        <div class="project-overlay">
                            <a href="#" class="project-link" aria-label="View project"><i class="fas fa-external-link-alt"></i></a>
                            <a href="#" class="project-link" aria-label="View code"><i class="fab fa-github"></i></a>
                        </div>
                    </div>
                    <div class="project-content">
                        <h3>Personal Blog Platform</h3>
                        <p>A modern blogging platform with markdown support, comments, and social sharing capabilities.</p>
                        <div class="project-tags">
                            <span class="tag">Next.js</span>
                            <span class="tag">TypeScript</span>
                            <span class="tag">Tailwind</span>
                        </div>
                    </div>
                </div>

                <div class="project-card">
                    <div class="project-image">
                        <div class="image-placeholder">
                            <i class="fas fa-gamepad"></i>
                        </div>
                        <div class="project-overlay">
                            <a href="#" class="project-link" aria-label="View project"><i class="fas fa-external-link-alt"></i></a>
                            <a href="#" class="project-link" aria-label="View code"><i class="fab fa-github"></i></a>
                        </div>
                    </div>
                    <div class="project-content">
                        <h3>Interactive Game</h3>
                        <p>Browser-based interactive game with engaging animations and multiplayer support.</p>
                        <div class="project-tags">
                            <span class="tag">JavaScript</span>
                            <span class="tag">Canvas</span>
                            <span class="tag">WebSocket</span>
                        </div>
                    </div>
                </div>

                <div class="project-card">
                    <div class="project-image">
                        <div class="image-placeholder">
                            <i class="fas fa-video"></i>
                        </div>
                        <div class="project-overlay">
                            <a href="#" class="project-link" aria-label="View project"><i class="fas fa-external-link-alt"></i></a>
                            <a href="#" class="project-link" aria-label="View code"><i class="fab fa-github"></i></a>
                        </div>
                    </div>
                    <div class="project-content">
                        <h3>Video Streaming Platform</h3>
                        <p>A custom video streaming solution with playlist management and quality adaptation.</p>
                        <div class="project-tags">
                            <span class="tag">React</span>
                            <span class="tag">Node.js</span>
                            <span class="tag">AWS</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <h2 class="section-title">Get In Touch</h2>
            <p class="section-subtitle">Let's work together on your next project</p>
            <div class="contact-content">
                <div class="contact-info">
                    <div class="contact-item">
                        <div class="contact-icon">
                            <i class="fas fa-envelope"></i>
                        </div>
                        <div>
                            <h3>Email</h3>
                            <p>your.email@example.com</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <div class="contact-icon">
                            <i class="fas fa-phone"></i>
                        </div>
                        <div>
                            <h3>Phone</h3>
                            <p>+1 (555) 123-4567</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <div class="contact-icon">
                            <i class="fas fa-map-marker-alt"></i>
                        </div>
                        <div>
                            <h3>Location</h3>
                            <p>New York, USA</p>
                        </div>
                    </div>
                </div>
                <form class="contact-form" id="contactForm">
                    <div class="form-group">
                        <input type="text" id="name" name="name" placeholder="Your Name" required>
                    </div>
                    <div class="form-group">
                        <input type="email" id="email" name="email" placeholder="Your Email" required>
                    </div>
                    <div class="form-group">
                        <input type="text" id="subject" name="subject" placeholder="Subject" required>
                    </div>
                    <div class="form-group">
                        <textarea id="message" name="message" rows="5" placeholder="Your Message" required></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary">Send Message</button>
                </form>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>Portfolio<span class="dot">.</span></h3>
                    <p>Creating digital experiences that inspire and engage.</p>
                    <div class="social-links">
                        <a href="https://github.com" target="_blank" aria-label="GitHub"><i class="fab fa-github"></i></a>
                        <a href="https://linkedin.com" target="_blank" aria-label="LinkedIn"><i class="fab fa-linkedin"></i></a>
                        <a href="https://twitter.com" target="_blank" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
                        <a href="mailto:your.email@example.com" aria-label="Email"><i class="fas fa-envelope"></i></a>
                    </div>
                </div>
                <div class="footer-section">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="#home">Home</a></li>
                        <li><a href="#about">About</a></li>
                        <li><a href="#skills">Skills</a></li>
                        <li><a href="#projects">Projects</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="#">Web Development</a></li>
                        <li><a href="#">UI/UX Design</a></li>
                        <li><a href="#">Consulting</a></li>
                        <li><a href="#">Maintenance</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 Portfolio. All rights reserved. Built with <i class="fas fa-heart"></i> and <i class="fas fa-coffee"></i></p>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>'''

# Save HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✓ index.html created successfully")
