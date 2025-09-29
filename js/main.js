// Main JavaScript file for the academic website

class AcademicWebsite {
    constructor() {
        this.initializeEventListeners();
        this.loadData();
        this.initializeScrollAnimations();
    }

    initializeEventListeners() {
        // Mobile menu toggle
        const hamburger = document.querySelector('.hamburger');
        const navMenu = document.querySelector('.nav-menu');

        hamburger?.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });

        // Close mobile menu when clicking on links
        document.querySelectorAll('.nav-menu a').forEach(link => {
            link.addEventListener('click', () => {
                hamburger?.classList.remove('active');
                navMenu?.classList.remove('active');
            });
        });

        // Smooth scrolling for navigation links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Header background on scroll
        window.addEventListener('scroll', this.handleScroll.bind(this));
    }

    handleScroll() {
        const header = document.querySelector('.header');
        if (window.scrollY > 100) {
            header.style.background = 'rgba(255, 255, 255, 0.95)';
            header.style.backdropFilter = 'blur(10px)';
        } else {
            header.style.background = '#fff';
            header.style.backdropFilter = 'none';
        }
    }

    async loadData() {
        try {
            await Promise.all([
                this.loadResearch(),
                this.loadPublications(),
                this.loadEvents(),
                this.loadRepositories()
            ]);
        } catch (error) {
            console.error('Error loading data:', error);
        }
    }

    async loadResearch() {
        try {
            const response = await fetch('data/research.json');
            if (!response.ok) throw new Error('Research data not found');
            const research = await response.json();
            this.renderResearch(research);
        } catch (error) {
            console.log('Loading sample research data...');
            this.renderResearch(this.getSampleResearchData());
        }
    }

    async loadPublications() {
        try {
            const response = await fetch('data/publications.json');
            if (!response.ok) throw new Error('Publications data not found');
            const publications = await response.json();
            this.renderPublications(publications);
        } catch (error) {
            console.log('Loading sample publications data...');
            this.renderPublications(this.getSamplePublicationsData());
        }
    }

    async loadEvents() {
        try {
            const response = await fetch('data/events.json');
            if (!response.ok) throw new Error('Events data not found');
            const events = await response.json();
            this.renderEvents(events);
        } catch (error) {
            console.log('Loading sample events data...');
            this.renderEvents(this.getSampleEventsData());
        }
    }

    async loadRepositories() {
        try {
            const response = await fetch('data/repositories.json');
            if (!response.ok) throw new Error('Repositories data not found');
            const repositories = await response.json();
            this.renderRepositories(repositories);
        } catch (error) {
            console.log('Loading sample repositories data...');
            this.renderRepositories(this.getSampleRepositoriesData());
        }
    }

    renderResearch(research) {
        const container = document.getElementById('research-container');
        if (!container) return;

        container.innerHTML = research.map(item => `
            <div class="research-item fade-in-up">
                <h3>${item.title}</h3>
                <p>${item.description}</p>
                <div class="research-tags">
                    ${item.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
                </div>
            </div>
        `).join('');

        this.animateElements(container);
    }

    renderPublications(publications) {
        const container = document.getElementById('publications-container');
        if (!container) return;

        container.innerHTML = publications.map(pub => `
            <div class="publication-item fade-in-up">
                <h3 class="publication-title">${pub.title}</h3>
                <p class="publication-authors">${pub.authors}</p>
                <p class="publication-venue">${pub.venue}</p>
                <p class="publication-year">${pub.year}</p>
                <div class="publication-links">
                    ${pub.links.map(link => `
                        <a href="${link.url}" target="_blank">
                            <i class="${link.icon}"></i> ${link.text}
                        </a>
                    `).join('')}
                </div>
            </div>
        `).join('');

        this.animateElements(container);
    }

    renderEvents(events) {
        const container = document.getElementById('events-container');
        if (!container) return;

        container.innerHTML = events.map(event => `
            <div class="event-item fade-in-up">
                <div class="event-date">${event.date}</div>
                <h3 class="event-title">${event.title}</h3>
                <p class="event-location">${event.location}</p>
                <p class="event-description">${event.description}</p>
            </div>
        `).join('');

        this.animateElements(container);
    }

    renderRepositories(repositories) {
        const container = document.getElementById('repositories-container');
        if (!container) return;

        container.innerHTML = repositories.map(repo => `
            <div class="repository-item fade-in-up">
                <div class="repo-header">
                    <i class="fab fa-github"></i>
                    <a href="${repo.url}" target="_blank" class="repo-name">${repo.name}</a>
                </div>
                <p class="repo-description">${repo.description}</p>
                <div class="repo-stats">
                    <span class="repo-language">${repo.language}</span>
                    <span><i class="fas fa-star"></i> ${repo.stars}</span>
                    <span><i class="fas fa-code-branch"></i> ${repo.forks}</span>
                </div>
            </div>
        `).join('');

        this.animateElements(container);
    }

    initializeScrollAnimations() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        // Observe all animated elements
        document.querySelectorAll('.fade-in-up').forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(el);
        });
    }

    animateElements(container) {
        const elements = container.querySelectorAll('.fade-in-up');
        elements.forEach((el, index) => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            
            setTimeout(() => {
                el.style.opacity = '1';
                el.style.transform = 'translateY(0)';
            }, index * 100);
        });
    }

    // Sample data methods
    getSampleResearchData() {
        return [
            {
                title: "Inteligência Artificial em Educação",
                description: "Pesquisa sobre aplicação de técnicas de IA para personalização do ensino e melhoria do processo de aprendizagem.",
                tags: ["IA", "Educação", "Machine Learning"]
            },
            {
                title: "Análise de Dados Educacionais",
                description: "Desenvolvimento de metodologias para análise de grandes volumes de dados educacionais visando insights pedagógicos.",
                tags: ["Big Data", "Analytics", "Educação"]
            },
            {
                title: "Sistemas Adaptativos de Aprendizagem",
                description: "Criação de plataformas educacionais que se adaptam ao ritmo e estilo de aprendizagem de cada estudante.",
                tags: ["Sistemas Adaptativos", "E-learning", "Personalização"]
            }
        ];
    }

    getSamplePublicationsData() {
        return [
            {
                title: "Machine Learning Applications in Educational Data Mining",
                authors: "Nome do Docente, Co-autor A, Co-autor B",
                venue: "Journal of Educational Technology & Society",
                year: "2024",
                links: [
                    { text: "PDF", url: "#", icon: "fas fa-file-pdf" },
                    { text: "DOI", url: "#", icon: "fas fa-external-link-alt" }
                ]
            },
            {
                title: "Adaptive Learning Systems: A Comprehensive Review",
                authors: "Nome do Docente, Co-autor C",
                venue: "International Conference on Educational Technology",
                year: "2023",
                links: [
                    { text: "PDF", url: "#", icon: "fas fa-file-pdf" },
                    { text: "Slides", url: "#", icon: "fas fa-presentation" }
                ]
            },
            {
                title: "Data-Driven Approaches to Personalized Education",
                authors: "Co-autor D, Nome do Docente, Co-autor E",
                venue: "Computers & Education",
                year: "2023",
                links: [
                    { text: "PDF", url: "#", icon: "fas fa-file-pdf" },
                    { text: "Code", url: "#", icon: "fab fa-github" }
                ]
            }
        ];
    }

    getSampleEventsData() {
        return [
            {
                date: "Dezembro 2024",
                title: "Palestra: IA na Educação do Futuro",
                location: "Conferência Nacional de Educação, São Paulo",
                description: "Apresentação sobre as tendências e desafios da aplicação de inteligência artificial em ambientes educacionais."
            },
            {
                date: "Outubro 2024",
                title: "Workshop: Análise de Dados Educacionais",
                location: "Universidade Federal, Rio de Janeiro",
                description: "Facilitação de workshop prático sobre técnicas de mineração de dados educacionais para professores e pesquisadores."
            },
            {
                date: "Agosto 2024",
                title: "Participação em Mesa Redonda",
                location: "Simpósio Brasileiro de Informática na Educação",
                description: "Discussão sobre ética e privacidade no uso de dados de estudantes em sistemas educacionais inteligentes."
            }
        ];
    }

    getSampleRepositoriesData() {
        return [
            {
                name: "educational-data-mining",
                description: "Conjunto de ferramentas e algoritmos para mineração de dados educacionais, incluindo análise de padrões de aprendizagem.",
                url: "https://github.com/username/educational-data-mining",
                language: "Python",
                stars: "45",
                forks: "12"
            },
            {
                name: "adaptive-learning-platform",
                description: "Plataforma web para ensino adaptativo com recomendação personalizada de conteúdo baseada em IA.",
                url: "https://github.com/username/adaptive-learning-platform",
                language: "JavaScript",
                stars: "32",
                forks: "8"
            },
            {
                name: "ml-education-toolkit",
                description: "Biblioteca de machine learning especificamente projetada para aplicações educacionais e análise de desempenho.",
                url: "https://github.com/username/ml-education-toolkit",
                language: "Python",
                stars: "67",
                forks: "15"
            }
        ];
    }
}

// Initialize the website when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new AcademicWebsite();
});

// Add loading state for GitHub repositories
async function loadGitHubRepositories(username) {
    try {
        const response = await fetch(`https://api.github.com/users/${username}/repos?sort=updated&per_page=10`);
        if (!response.ok) throw new Error('GitHub API error');
        
        const repos = await response.json();
        const publicRepos = repos.filter(repo => !repo.private && !repo.fork);
        
        return publicRepos.map(repo => ({
            name: repo.name,
            description: repo.description || 'Sem descrição disponível',
            url: repo.html_url,
            language: repo.language || 'N/A',
            stars: repo.stargazers_count,
            forks: repo.forks_count
        }));
    } catch (error) {
        console.error('Error loading GitHub repositories:', error);
        return [];
    }
}

// Export for potential external use
window.AcademicWebsite = AcademicWebsite;