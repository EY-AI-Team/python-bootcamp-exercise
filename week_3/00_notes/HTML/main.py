
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
import os
from logging_config import setup_logging

setup_logging()


logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Configuration
API_BASE_URL = "http://localhost:8000"  # Default FastAPI server URL
REQUEST_TIMEOUT = 30


@app.route('/')
def index():
   return "Hello, This is a sample case scenario!"

@app.route('/csv-files')
def list_csv_files():
    """Display available CSV files"""
    try:
        files = api_client.get("/files/")
        return render_template('file_list.html', files=files)
    except Exception as e:
        flash(f"Error fetching files: {str(e)}", 'error')
        return render_template('file_list.html', files=[])

@app.route('/csv/<filename>')
def view_csv_data(filename):
    """View CSV data with pagination and filtering"""
    try:
        # Get query parameters
        page = request.args.get('page', 1, type=int)
        page_size = request.args.get('page_size', 20, type=int)
        filter_column = request.args.get('filter_column', '')
        filter_value = request.args.get('filter_value', '')
        filter_operator = request.args.get('filter_operator', 'equals')
        columns = request.args.get('columns', '')
        
        # Build API parameters
        params = {
            'page': page,
            'page_size': page_size
        }
        
        if filter_column and filter_value:
            params.update({
                'filter_column': filter_column,
                'filter_value': filter_value,
                'filter_operator': filter_operator
            })
        
        if columns:
            params['columns'] = columns
        
        # Fetch data from API
        data = api_client.get(f"/csv/{filename}", params)
        
        # Get file info for column names
        file_info = api_client.get(f"/info/{filename}")
        
        return render_template('csv_viewer.html', 
                             filename=filename,
                             data=data,
                             file_info=file_info,
                             current_page=page,
                             page_size=page_size,
                             filter_column=filter_column,
                             filter_value=filter_value,
                             filter_operator=filter_operator,
                             columns=columns)
        
    except Exception as e:
        flash(f"Error loading CSV data: {str(e)}", 'error')
        return redirect(url_for('list_csv_files'))

@app.route('/csv/<filename>/info')
def csv_info(filename):
    """Display CSV file information"""
    try:
        file_info = api_client.get(f"/info/{filename}")
        summary = api_client.get(f"/csv/{filename}/summary")
        return render_template('csv_info.html', 
                             filename=filename,
                             file_info=file_info,
                             summary=summary)
    except Exception as e:
        flash(f"Error loading file info: {str(e)}", 'error')
        return redirect(url_for('list_csv_files'))

@app.route('/api-test')
def api_test():
    """Test different API endpoints"""
    test_results = []
    
    # Test endpoints
    endpoints = [
        ("/", "Root endpoint"),
        ("/files/", "List files"),
    ]
    
    for endpoint, description in endpoints:
        try:
            start_time = datetime.now()
            response = api_client.get(endpoint)
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            test_results.append({
                'endpoint': endpoint,
                'description': description,
                'status': 'Success',
                'response_time': f"{duration:.3f}s",
                'data': json.dumps(response, indent=2) if response else "No data"
            })
        except Exception as e:
            test_results.append({
                'endpoint': endpoint,
                'description': description,
                'status': 'Error',
                'response_time': 'N/A',
                'data': str(e)
            })
    
    return render_template('api_test.html', test_results=test_results)

@app.route('/custom-api')
def custom_api_form():
    """Form to test custom API endpoints"""
    return render_template('custom_api.html')

@app.route('/custom-api', methods=['POST'])
def test_custom_api():
    """Test custom API endpoint"""
    try:
        api_url = request.form.get('api_url', '').strip()
        endpoint = request.form.get('endpoint', '').strip()
        
        if not api_url or not endpoint:
            flash("Please provide both API URL and endpoint", 'error')
            return redirect(url_for('custom_api_form'))
        
        # Create temporary API client
        custom_client = APIClient(api_url)
        response = custom_client.get(endpoint)
        
        return render_template('api_response.html',
                             api_url=api_url,
                             endpoint=endpoint,
                             response=json.dumps(response, indent=2, default=str),
                             success=True)
        
    except Exception as e:
        return render_template('api_response.html',
                             api_url=request.form.get('api_url', ''),
                             endpoint=request.form.get('endpoint', ''),
                             response=str(e),
                             success=False)

# AJAX endpoints for dynamic updates

@app.route('/api/search-csv/<filename>')
def search_csv_data(filename):
    """AJAX endpoint for searching CSV data"""
    try:
        search_term = request.args.get('search', '')
        column = request.args.get('column', '')
        
        if not search_term:
            return jsonify({'error': 'No search term provided'})
        
        params = {
            'filter_column': column,
            'filter_value': search_term,
            'filter_operator': 'contains',
            'page_size': 50  # Limit results for search
        }
        
        data = api_client.get(f"/csv/{filename}", params)
        
        return jsonify({
            'success': True,
            'data': data['data'],
            'total_rows': data['total_rows']
        })
        
    except Exception as e:
        return jsonify({'error': str(e)})

# Error handlers

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', 
                         error_code=404,
                         error_message="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html',
                         error_code=500,
                         error_message="Internal server error"), 500

# Template creation functions (these would normally be in separate files)

def create_templates():
    """Create HTML templates"""
    
    templates_dir = "templates"
    os.makedirs(templates_dir, exist_ok=True)
    
    # Base template
    base_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}API Data Viewer{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        .sidebar {
            background-color: #f8f9fa;
            min-height: 100vh;
            padding: 20px;
        }
        .api-status-connected { color: #28a745; }
        .api-status-error { color: #dc3545; }
        .table-container { max-height: 600px; overflow-y: auto; }
        .search-highlight { background-color: #fff3cd; }
        .pagination-container { margin-top: 20px; }
    </style>
</head>
<body>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-2 sidebar">
                <h5><i class="fas fa-database"></i> API Data Viewer</h5>
                <nav class="nav flex-column">
                    <a class="nav-link" href="{{ url_for('index') }}">
                        <i class="fas fa-home"></i> Home
                    </a>
                    <a class="nav-link" href="{{ url_for('list_csv_files') }}">
                        <i class="fas fa-file-csv"></i> CSV Files
                    </a>
                    <a class="nav-link" href="{{ url_for('api_test') }}">
                        <i class="fas fa-flask"></i> API Test
                    </a>
                    <a class="nav-link" href="{{ url_for('custom_api_form') }}">
                        <i class="fas fa-cogs"></i> Custom API
                    </a>
                </nav>
            </div>
            <div class="col-md-10">
                <div class="container mt-4">
                    {% with messages = get_flashed_messages(with_categories=true) %}
                        {% if messages %}
                            {% for category, message in messages %}
                                <div class="alert alert-{{ 'danger' if category == 'error' else 'info' }} alert-dismissible fade show">
                                    {{ message }}
                                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                                </div>
                            {% endfor %}
                        {% endif %}
                    {% endwith %}
                    
                    {% block content %}{% endblock %}
                </div>
            </div>
        </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    {% block scripts %}{% endblock %}
</body>
</html>
    '''
    
    # Index template
    index_template = '''
{% extends "base.html" %}

{% block title %}Home - API Data Viewer{% endblock %}

{% block content %}
<div class="row">
    <div class="col-12">
        <h1><i class="fas fa-home"></i> API Data Viewer</h1>
        <p class="lead">Connect to APIs and view data in a user-friendly interface</p>
        
        <div class="card mb-4">
            <div class="card-header">
                <h5><i class="fas fa-plug"></i> API Connection Status</h5>
            </div>
            <div class="card-body">
                <p><strong>API URL:</strong> {{ api_url }}</p>
                <p><strong>Status:</strong> 
                    <span class="{% if 'Error' in api_status %}api-status-error{% else %}api-status-connected{% endif %}">
                        <i class="fas fa-{% if 'Error' in api_status %}times-circle{% else %}check-circle{% endif %}"></i>
                        {{ api_status }}
                    </span>
                </p>
                {% if api_info %}
                <div class="mt-3">
                    <h6>API Information:</h6>
                    <pre class="bg-light p-3 rounded">{{ api_info | tojson(indent=2) }}</pre>
                </div>
                {% endif %}
            </div>
        </div>
        
        <div class="row">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-body text-center">
                        <i class="fas fa-file-csv fa-3x mb-3 text-primary"></i>
                        <h5>View CSV Data</h5>
                        <p>Browse and filter CSV files from the API</p>
                        <a href="{{ url_for('list_csv_files') }}" class="btn btn-primary">Browse Files</a>
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <div class="card">
                    <div class="card-body text-center">
                        <i class="fas fa-flask fa-3x mb-3 text-success"></i>
                        <h5>Test API</h5>
                        <p>Test different API endpoints and view responses</p>
                        <a href="{{ url_for('api_test') }}" class="btn btn-success">Test API</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
    '''
    
    # File list template
    file_list_template = '''
{% extends "base.html" %}

{% block title %}CSV Files - API Data Viewer{% endblock %}

{% block content %}
<div class="row">
    <div class="col-12">
        <h1><i class="fas fa-file-csv"></i> Available CSV Files</h1>
        
        {% if files %}
        <div class="row">
            {% for file in files %}
            <div class="col-md-4 mb-3">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">
                            <i class="fas fa-file-csv text-success"></i> {{ file }}
                        </h5>
                        <div class="btn-group" role="group">
                            <a href="{{ url_for('view_csv_data', filename=file) }}" class="btn btn-primary btn-sm">
                                <i class="fas fa-eye"></i> View Data
                            </a>
                            <a href="{{ url_for('csv_info', filename=file) }}" class="btn btn-info btn-sm">
                                <i class="fas fa-info-circle"></i> Info
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
        {% else %}
        <div class="alert alert-warning">
            <i class="fas fa-exclamation-triangle"></i> No CSV files found or unable to connect to API.
        </div>
        {% endif %}
    </div>
</div>
{% endblock %}
    '''
    
    # CSV viewer template
    csv_viewer_template = '''
{% extends "base.html" %}

{% block title %}{{ filename }} - CSV Viewer{% endblock %}

{% block content %}
<div class="row">
    <div class="col-12">
        <h1><i class="fas fa-table"></i> {{ filename }}</h1>
        
        <!-- Filters and Search -->
        <div class="card mb-4">
            <div class="card-header">
                <h5><i class="fas fa-filter"></i> Filters and Search</h5>
            </div>
            <div class="card-body">
                <form method="GET" class="row g-3">
                    <div class="col-md-3">
                        <label class="form-label">Filter Column:</label>
                        <select name="filter_column" class="form-select">
                            <option value="">-- Select Column --</option>
                            {% for col in file_info.column_names %}
                            <option value="{{ col }}" {% if col == filter_column %}selected{% endif %}>{{ col }}</option>
                            {% endfor %}
                        </select>
                    </div>
                    <div class="col-md-3">
                        <label class="form-label">Filter Value:</label>
                        <input type="text" name="filter_value" class="form-control" value="{{ filter_value }}">
                    </div>
                    <div class="col-md-2">
                        <label class="form-label">Operator:</label>
                        <select name="filter_operator" class="form-select">
                            <option value="equals" {% if filter_operator == 'equals' %}selected{% endif %}>Equals</option>
                            <option value="contains" {% if filter_operator == 'contains' %}selected{% endif %}>Contains</option>
                            <option value="greater" {% if filter_operator == 'greater' %}selected{% endif %}>Greater</option>
                            <option value="less" {% if filter_operator == 'less' %}selected{% endif %}>Less</option>
                        </select>
                    </div>
                    <div class="col-md-2">
                        <label class="form-label">Page Size:</label>
                        <select name="page_size" class="form-select">
                            <option value="10" {% if page_size == 10 %}selected{% endif %}>10</option>
                            <option value="20" {% if page_size == 20 %}selected{% endif %}>20</option>
                            <option value="50" {% if page_size == 50 %}selected{% endif %}>50</option>
                            <option value="100" {% if page_size == 100 %}selected{% endif %}>100</option>
                        </select>
                    </div>
                    <div class="col-md-2">
                        <label class="form-label">&nbsp;</label>
                        <button type="submit" class="btn btn-primary d-block">
                            <i class="fas fa-search"></i> Apply
                        </button>
                    </div>
                </form>
            </div>
        </div>
        
        <!-- Data Summary -->
        <div class="alert alert-info">
            <strong>Showing:</strong> {{ data.data|length }} of {{ data.total_rows }} rows
            {% if data.page %} (Page {{ data.page }} of {{ data.total_pages }}) {% endif %}
        </div>
        
        <!-- Data Table -->
        {% if data.data %}
        <div class="table-container">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        {% for col in data.data[0].keys() %}
                        <th>{{ col }}</th>
                        {% endfor %}
                    </tr>
                </thead>
                <tbody>
                    {% for row in data.data %}
                    <tr>
                        {% for value in row.values() %}
                        <td>{{ value }}</td>
                        {% endfor %}
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        
        <!-- Pagination -->
        {% if data.total_pages and data.total_pages > 1 %}
        <div class="pagination-container">
            <nav>
                <ul class="pagination justify-content-center">
                    {% if current_page > 1 %}
                    <li class="page-item">
                        <a class="page-link" href="?page=1&page_size={{ page_size }}&filter_column={{ filter_column }}&filter_value={{ filter_value }}&filter_operator={{ filter_operator }}">First</a>
                    </li>
                    <li class="page-item">
                        <a class="page-link" href="?page={{ current_page - 1 }}&page_size={{ page_size }}&filter_column={{ filter_column }}&filter_value={{ filter_value }}&filter_operator={{ filter_operator }}">Previous</a>
                    </li>
                    {% endif %}
                    
                    {% for page_num in range([1, current_page - 2]|max, [data.total_pages + 1, current_page + 3]|min) %}
                    <li class="page-item {% if page_num == current_page %}active{% endif %}">
                        <a class="page-link" href="?page={{ page_num }}&page_size={{ page_size }}&filter_column={{ filter_column }}&filter_value={{ filter_value }}&filter_operator={{ filter_operator }}">{{ page_num }}</a>
                    </li>
                    {% endfor %}
                    
                    {% if current_page < data.total_pages %}
                    <li class="page-item">
                        <a class="page-link" href="?page={{ current_page + 1 }}&page_size={{ page_size }}&filter_column={{ filter_column }}&filter_value={{ filter_value }}&filter_operator={{ filter_operator }}">Next</a>
                    </li>
                    <li class="page-item">
                        <a class="page-link" href="?page={{ data.total_pages }}&page_size={{ page_size }}&filter_column={{ filter_column }}&filter_value={{ filter_value }}&filter_operator={{ filter_operator }}">Last</a>
                    </li>
                    {% endif %}
                </ul>
            </nav>
        </div>
        {% endif %}
        
        {% else %}
        <div class="alert alert-warning">
            <i class="fas fa-exclamation-triangle"></i> No data found with current filters.
        </div>
        {% endif %}
    </div>
</div>
{% endblock %}
    '''
    
    # Save templates
    templates = {
        'base.html': base_template,
        'index.html': index_template,
        'file_list.html': file_list_template,
        'csv_viewer.html': csv_viewer_template
    }
    
    for filename, content in templates.items():
        with open(f"{templates_dir}/{filename}", 'w') as f:
            f.write(content)
    
    logger.info("HTML templates created successfully")

if __name__ == '__main__':
    # Create templates on startup
    create_templates()
    
    print("🚀 Flask API Client Application")
    print("=" * 40)
    print(f"API URL: {API_BASE_URL}")
    print("Starting Flask application...")
    print("Access the app at: http://localhost:5000")
    print("=" * 40)
    
    # Run Flask app
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        threaded=True
    )

# Requirements file (requirements.txt):
"""
Flask>=2.3.0
requests>=2.31.0
urllib3>=1.26.0
Jinja2>=3.1.0
"""

# Usage Instructions:
"""
1. Install dependencies:
   pip install Flask requests urllib3

2. Make sure your FastAPI server is running:
   uvicorn main:app --reload --host 0.0.0.0 --port 8000

3. Run the Flask application:
   python flask_app.py

4. Open your browser and go to:
   http://localhost:5000

Features:
- Home page with API connection status
- Browse available CSV files
- View CSV data with pagination and filtering
- Search and filter data dynamically
- Responsive Bootstrap UI
- Error handling and user feedback
- API testing interface

Navigation:
- Home: API status and quick links
- CSV Files: List all available files
- View Data: Interactive data table with filters
- API Test: Test different endpoints
- Custom API: Test external APIs
"""