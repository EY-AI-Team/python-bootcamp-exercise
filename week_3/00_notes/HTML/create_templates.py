import os

def create_templates():
    templates_dir = "templates"
    os.makedirs(templates_dir, exist_ok=True)
    
    # Base template
    base_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Employee Management System{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        .navbar-brand {
            font-weight: bold;
        }
        .welcome-section {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 60px 0;
            text-align: center;
        }
        .employee-card {
            transition: transform 0.2s;
        }
        .employee-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        .table-container {
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            padding: 20px;
        }
        .department-badge {
            font-size: 0.8em;
        }
        footer {
            margin-top: 50px;
            padding: 20px 0;
            background-color: #f8f9fa;
            text-align: center;
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="{{ url_for('home') }}">
                <i class="fas fa-users"></i> Employee Management
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link {% if request.endpoint == 'home' %}active{% endif %}" href="{{ url_for('home') }}">
                            <i class="fas fa-home"></i> Home
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link {% if request.endpoint == 'get_employees' %}active{% endif %}" href="{{ url_for('get_employees') }}">
                            <i class="fas fa-users"></i> Get Employees
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Flash Messages -->
    <div class="container mt-3">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ 'danger' if category == 'error' else 'info' }} alert-dismissible fade show">
                        <i class="fas fa-{% if category == 'error' %}exclamation-triangle{% else %}info-circle{% endif %}"></i>
                        {{ message }}
                        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}
    </div>

    <!-- Main Content -->
    {% block content %}{% endblock %}

    <!-- Footer -->
    <footer class="bg-light mt-5">
        <div class="container">
            <div class="text-center py-3">
                <p class="mb-0">&copy; 2024 Employee Management System. Built with Flask & Bootstrap.</p>
            </div>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    {% block scripts %}{% endblock %}
</body>
</html>'''

    # Home template
    home_template = '''{% extends "base.html" %}

{% block title %}Home - Employee Management System{% endblock %}

{% block content %}
<!-- Welcome Section -->
<div class="welcome-section">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8 text-center">
                <h1 class="display-4 mb-4">
                    <i class="fas fa-hand-wave"></i> Welcome!
                </h1>
                <p class="lead mb-4">
                    Welcome to the Employee Management System. Your one-stop solution for managing employee information and data.
                </p>
                <a href="{{ url_for('get_employees') }}" class="btn btn-light btn-lg">
                    <i class="fas fa-users"></i> View Employees
                </a>
            </div>
        </div>
    </div>
</div>

<!-- Features Section -->
<div class="container my-5">
    <div class="row">
        <div class="col-12">
            <h2 class="text-center mb-5">System Features</h2>
        </div>
        <div class="col-md-4 mb-4">
            <div class="card h-100 text-center employee-card">
                <div class="card-body">
                    <i class="fas fa-database fa-3x text-primary mb-3"></i>
                    <h5 class="card-title">Employee Database</h5>
                    <p class="card-text">Access comprehensive employee information from our centralized database.</p>
                </div>
            </div>
        </div>
        <div class="col-md-4 mb-4">
            <div class="card h-100 text-center employee-card">
                <div class="card-body">
                    <i class="fas fa-search fa-3x text-success mb-3"></i>
                    <h5 class="card-title">Easy Search</h5>
                    <p class="card-text">Quickly find and filter employee records with our intuitive search features.</p>
                </div>
            </div>
        </div>
        <div class="col-md-4 mb-4">
            <div class="card h-100 text-center employee-card">
                <div class="card-body">
                    <i class="fas fa-chart-bar fa-3x text-info mb-3"></i>
                    <h5 class="card-title">Real-time Data</h5>
                    <p class="card-text">View up-to-date employee information fetched directly from our API.</p>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Quick Stats -->
<div class="container my-5">
    <div class="row">
        <div class="col-12">
            <div class="card bg-light">
                <div class="card-body text-center">
                    <h4 class="mb-3">Ready to Get Started?</h4>
                    <p class="mb-3">Click the button below to view all employee information</p>
                    <a href="{{ url_for('get_employees') }}" class="btn btn-primary btn-lg">
                        <i class="fas fa-arrow-right"></i> Get Employees
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}'''

    # Employees template
    employees_template = '''{% extends "base.html" %}

{% block title %}Employees - Employee Management System{% endblock %}

{% block content %}
<div class="container my-4">
    <div class="row">
        <div class="col-12">
            <div class="d-flex justify-content-between align-items-center mb-4">
                <h1><i class="fas fa-users"></i> Employee Directory</h1>
                <button onclick="location.reload()" class="btn btn-outline-primary">
                    <i class="fas fa-sync-alt"></i> Refresh Data
                </button>
            </div>

            {% if employees %}
                <!-- Employee Count -->
                <div class="alert alert-info">
                    <i class="fas fa-info-circle"></i> 
                    Displaying <strong>{{ employees|length }}</strong> employees
                </div>

                <!-- Employee Table -->
                <div class="table-container">
                    <div class="table-responsive">
                        <table class="table table-hover">
                            <thead class="table-dark">
                                <tr>
                                    <th><i class="fas fa-hashtag"></i> ID</th>
                                    <th><i class="fas fa-user"></i> Name</th>
                                    <th><i class="fas fa-envelope"></i> Email</th>
                                    <th><i class="fas fa-phone"></i> Phone</th>
                                    <th><i class="fas fa-building"></i> Department</th>
                                    <th><i class="fas fa-briefcase"></i> Position</th>
                                    <th><i class="fas fa-map-marker-alt"></i> Address</th>
                                    <th><i class="fas fa-industry"></i> Company</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for employee in employees %}
                                <tr>
                                    <td><span class="badge bg-secondary">{{ employee.id }}</span></td>
                                    <td>
                                        <strong>{{ employee.name }}</strong>
                                    </td>
                                    <td>
                                        <a href="mailto:{{ employee.email }}" class="text-decoration-none">
                                            {{ employee.email }}
                                        </a>
                                    </td>
                                    <td>
                                        <a href="tel:{{ employee.phone }}" class="text-decoration-none">
                                            {{ employee.phone }}
                                        </a>
                                    </td>
                                    <td>
                                        <span class="badge bg-primary department-badge">
                                            {{ employee.department }}
                                        </span>
                                    </td>
                                    <td>{{ employee.position }}</td>
                                    <td>
                                        <small class="text-muted">{{ employee.address }}</small>
                                    </td>
                                    <td>
                                        <small>{{ employee.company }}</small>
                                    </td>
                                </tr>
                                {% endfor %}
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Department Summary -->
                <div class="row mt-4">
                    <div class="col-12">
                        <h4>Department Summary</h4>
                        <div class="row">
                            {% set departments = {} %}
                            {% for employee in employees %}
                                {% set _ = departments.update({employee.department: departments.get(employee.department, 0) + 1}) %}
                            {% endfor %}
                            
                            {% for dept, count in departments.items() %}
                            <div class="col-md-2 mb-2">
                                <div class="card text-center">
                                    <div class="card-body p-2">
                                        <h6 class="card-title mb-1">{{ dept }}</h6>
                                        <span class="badge bg-primary">{{ count }} employees</span>
                                    </div>
                                </div>
                            </div>
                            {% endfor %}
                        </div>
                    </div>
                </div>

            {% else %}
                <!-- No Data -->
                <div class="text-center my-5">
                    <i class="fas fa-users-slash fa-5x text-muted mb-3"></i>
                    <h3 class="text-muted">No Employee Data Available</h3>
                    <p class="text-muted">Unable to fetch employee information from the API.</p>
                    <button onclick="location.reload()" class="btn btn-primary">
                        <i class="fas fa-retry"></i> Try Again
                    </button>
                </div>
            {% endif %}
        </div>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script>
// Add some interactivity
document.addEventListener('DOMContentLoaded', function() {
    // Highlight rows on hover
    const rows = document.querySelectorAll('tbody tr');
    rows.forEach(row => {
        row.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#f8f9fa';
        });
        row.addEventListener('mouseleave', function() {
            this.style.backgroundColor = '';
        });
    });
    
    // Auto-refresh every 5 minutes
    setTimeout(() => {
        console.log('Auto-refreshing employee data...');
        location.reload();
    }, 300000); // 5 minutes
});
</script>
{% endblock %}'''

    # Error template
    error_template = '''{% extends "base.html" %}

{% block title %}Error {{ error_code }} - Employee Management System{% endblock %}

{% block content %}
<div class="container my-5">
    <div class="row justify-content-center">
        <div class="col-md-6 text-center">
            <i class="fas fa-exclamation-triangle fa-5x text-warning mb-4"></i>
            <h1 class="display-4">Error {{ error_code }}</h1>
            <p class="lead">{{ error_message }}</p>
            <a href="{{ url_for('home') }}" class="btn btn-primary">
                <i class="fas fa-home"></i> Go Home
            </a>
        </div>
    </div>
</div>
{% endblock %}'''

    # Save all templates
    templates = {
        'base.html': base_template,
        'home.html': home_template,
        'employees.html': employees_template,
        'error.html': error_template
    }
    
    for filename, content in templates.items():
        with open(f"{templates_dir}/{filename}", 'w', encoding='utf-8') as f:
            f.write(content)
    
create_templates()
    
