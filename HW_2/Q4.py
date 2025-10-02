import re

def extract_professor_names_from_file(filename):
    """
    Extract professor titles and names from an HTML file.
    Returns a list of tuples: (title, name)
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Pattern to capture title and name (handles hyphens and multiple words)
        pattern = r'(Prof\.?|Professor)\s+([A-Z][a-z]+(?:-[a-z]+)?(?:\s+[A-Z][a-z]+(?:-[a-z]+)?)+)'
        
        matches = re.findall(pattern, html_content)
        
        cleaned = []
        for title, name in matches:
            cleaned_name = re.sub(r'\s+', ' ', name.strip())
            cleaned.append((title, cleaned_name))
        
        return cleaned
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def q4():
    filename = 'dept_hist.html'
    professors = extract_professor_names_from_file(filename)
    if professors:
        print("Professor titles and names found:")
        for i, (title, prof) in enumerate(professors, 1):
            print(f"{i}. {title} {prof}")
    else:
        print("No professor names found or error reading file.")

q4()