from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta
from api.models import Profile, Project, Skill, Education, Experience

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create/Update Profile
        profile, created = Profile.objects.get_or_create(pk=1, defaults={
            'name': 'Shazib Siddique',
            'title': 'AWS Cloud / Software Engineer',
            'bio': 'Designing secure, scalable cloud solutions and modern web applications',
            'home_image': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop&crop=face',
            'about_image': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop&crop=face',
            'about_heading': "Hi, I'm Shazib Siddique, based in Brooklyn, NY",
            'about_description': "I'm a Cloud and Software Engineer specializing in AWS infrastructure and full-stack development.",
            'years_experience': '3+ Years',
            'projects_completed': '20+ Projects',
            'support_availability': 'Available',
            'email': 'siddiqueshazib5@gmail.com',
            'phone': '3159759378',
            'messenger': 'shazib.siddique',
            'facebook_url': 'https://linkedin.com/in/shazibsiddique',
            'instagram_url': 'https://linkedin.com/in/shazibsiddique',
            'twitter_url': 'https://linkedin.com/in/shazibsiddique',
        })
        
        if created:
            self.stdout.write('✓ Created profile')
        else:
            self.stdout.write('✓ Profile already exists')
        
        # Create Projects
        sample_projects = [
            {
                'title': 'E-Commerce Platform',
                'description': 'A full-stack e-commerce platform built with React and Node.js, featuring user authentication, payment processing, and admin dashboard.',
                'url': 'https://example-ecommerce.com',
                'repo_url': 'https://github.com/yourusername/ecommerce-platform',
                'image_url': 'https://i.postimg.cc/43Th5VXJ/work-1.png',
                'tags': ['React', 'Node.js', 'MongoDB', 'Stripe'],
                'featured': True,
                'order': 1
            },
            {
                'title': 'Task Management App',
                'description': 'A collaborative task management application with real-time updates, team collaboration features, and project tracking.',
                'url': 'https://example-tasks.com',
                'repo_url': 'https://github.com/yourusername/task-manager',
                'image_url': 'https://i.postimg.cc/sXLjnC5p/work-2.png',
                'tags': ['Vue.js', 'Python', 'Django', 'WebSocket'],
                'featured': True,
                'order': 2
            },
            {
                'title': 'Weather Dashboard',
                'description': 'A responsive weather dashboard showing current conditions, forecasts, and location-based weather data.',
                'url': 'https://example-weather.com',
                'repo_url': 'https://github.com/yourusername/weather-dashboard',
                'image_url': 'https://i.postimg.cc/QNB1jXYZ/work-3.png',
                'tags': ['JavaScript', 'API', 'CSS3', 'HTML5'],
                'featured': True,
                'order': 3
            },
            {
                'title': 'Portfolio Website',
                'description': 'A modern portfolio website showcasing projects, skills, and experience with smooth animations and responsive design.',
                'url': 'https://example-portfolio.com',
                'repo_url': 'https://github.com/yourusername/portfolio',
                'image_url': 'https://i.postimg.cc/s2DGqyG8/work-4.png',
                'tags': ['HTML5', 'CSS3', 'JavaScript', 'Responsive'],
                'featured': False,
                'order': 4
            },
            {
                'title': 'Blog Platform',
                'description': 'A content management system for blogging with markdown support, comment system, and user authentication.',
                'url': 'https://example-blog.com',
                'repo_url': 'https://github.com/yourusername/blog-platform',
                'image_url': 'https://i.postimg.cc/TYVyPhrF/work-5.png',
                'tags': ['Django', 'Python', 'PostgreSQL', 'Bootstrap'],
                'featured': False,
                'order': 5
            },
            {
                'title': 'Social Media Dashboard',
                'description': 'A social media management dashboard for scheduling posts, analytics, and managing multiple social accounts.',
                'url': 'https://example-social.com',
                'repo_url': 'https://github.com/yourusername/social-dashboard',
                'image_url': 'https://i.postimg.cc/wMdqKcbv/work-6.png',
                'tags': ['React', 'Express', 'MongoDB', 'Chart.js'],
                'featured': False,
                'order': 6
            }
        ]
        
        for project_data in sample_projects:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f'✓ Created project: {project.title}')
        
        # Create Skills
        sample_skills = [
            # Languages
            {'name': 'JavaScript', 'category': 'language', 'level': 90, 'order': 1},
            {'name': 'Python', 'category': 'language', 'level': 85, 'order': 2},
            {'name': 'HTML5', 'category': 'language', 'level': 95, 'order': 3},
            {'name': 'CSS3', 'category': 'language', 'level': 90, 'order': 4},
            {'name': 'SQL', 'category': 'language', 'level': 80, 'order': 5},
            
            # Frameworks
            {'name': 'React', 'category': 'framework', 'level': 85, 'order': 1},
            {'name': 'Vue.js', 'category': 'framework', 'level': 80, 'order': 2},
            {'name': 'Django', 'category': 'framework', 'level': 90, 'order': 3},
            {'name': 'Express.js', 'category': 'framework', 'level': 75, 'order': 4},
            {'name': 'Bootstrap', 'category': 'framework', 'level': 85, 'order': 5},
            
            # Tools
            {'name': 'Git', 'category': 'tool', 'level': 90, 'order': 1},
            {'name': 'Docker', 'category': 'tool', 'level': 70, 'order': 2},
            {'name': 'AWS', 'category': 'tool', 'level': 65, 'order': 3},
            {'name': 'Figma', 'category': 'tool', 'level': 80, 'order': 4},
            {'name': 'Photoshop', 'category': 'tool', 'level': 75, 'order': 5},
            
            # Other
            {'name': 'Problem Solving', 'category': 'other', 'level': 95, 'order': 1},
            {'name': 'Team Leadership', 'category': 'other', 'level': 85, 'order': 2},
            {'name': 'Project Management', 'category': 'other', 'level': 80, 'order': 3},
        ]
        
        for skill_data in sample_skills:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f'✓ Created skill: {skill.name}')
        
        # Create Education
        sample_education = [
            {
                'institution': 'University of Technology',
                'degree': 'Bachelor of Science',
                'field_of_study': 'Computer Science',
                'start_date': date(2015, 9, 1),
                'end_date': date(2019, 6, 30),
                'description': 'Focused on software engineering, algorithms, and web development. Completed capstone project on machine learning applications.',
                'location': 'New York, NY',
                'order': 1
            },
            {
                'institution': 'Tech Academy',
                'degree': 'Certificate',
                'field_of_study': 'Full Stack Web Development',
                'start_date': date(2020, 1, 15),
                'end_date': date(2020, 6, 15),
                'description': 'Intensive bootcamp covering modern web technologies including React, Node.js, and cloud deployment.',
                'location': 'San Francisco, CA',
                'order': 2
            },
            {
                'institution': 'Online Learning Platform',
                'degree': 'Professional Certificate',
                'field_of_study': 'Cloud Computing',
                'start_date': date(2021, 3, 1),
                'end_date': date(2021, 8, 31),
                'description': 'Specialized training in AWS, Docker, and DevOps practices for scalable application deployment.',
                'location': 'Remote',
                'order': 3
            }
        ]
        
        for edu_data in sample_education:
            education, created = Education.objects.get_or_create(
                institution=edu_data['institution'],
                degree=edu_data['degree'],
                defaults=edu_data
            )
            if created:
                self.stdout.write(f'✓ Created education: {education.degree} - {education.institution}')
        
        # Create Experiences
        sample_experiences = [
            {
                'company': 'Tech Solutions Inc.',
                'role': 'Senior Full Stack Developer',
                'start_date': date(2022, 1, 1),
                'end_date': None,  # Current position
                'summary': 'Leading development of enterprise web applications using React, Node.js, and cloud technologies.',
                'highlights': ['Led a team of 5 developers', 'Improved application performance by 40%', 'Implemented CI/CD pipelines'],
                'order': 1
            },
            {
                'company': 'Digital Agency Co.',
                'role': 'Frontend Developer',
                'start_date': date(2020, 6, 1),
                'end_date': date(2021, 12, 31),
                'summary': 'Developed responsive web applications and maintained existing client websites.',
                'highlights': ['Built 20+ client websites', 'Reduced page load times by 50%', 'Mentored junior developers'],
                'order': 2
            },
            {
                'company': 'StartupXYZ',
                'role': 'Junior Web Developer',
                'start_date': date(2019, 3, 1),
                'end_date': date(2020, 5, 31),
                'summary': 'Contributed to the development of the company\'s main product and internal tools.',
                'highlights': ['Built user authentication system', 'Created responsive UI components', 'Participated in code reviews'],
                'order': 3
            }
        ]
        
        for exp_data in sample_experiences:
            experience, created = Experience.objects.get_or_create(
                company=exp_data['company'],
                role=exp_data['role'],
                defaults=exp_data
            )
            if created:
                self.stdout.write(f'✓ Created experience: {experience.role} at {experience.company}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample data!')
        )
        self.stdout.write('You can now visit the admin panel to manage your content.')
