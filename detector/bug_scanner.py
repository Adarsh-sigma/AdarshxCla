import ast
import re
import requests
from sklearn.model_selection import train_test_split
from tensorflow import keras
from typing import List, Dict, Tuple

class BugScanner:
    def __init__(self):
        self.vulnerabilities = {
            'SQL Injection': (re.compile(r"(?i)(SELECT\s+\*\s+FROM\s+\w+\s+WHERE\s+\w+\s*=\s*'"), 'HIGH'),
            'XSS': (re.compile(r"(?i)(<script>.*?</script>)"), 'HIGH'),
            'Hardcoded Credentials': (re.compile(r"(?i)(password\s*=\s*['"]\w+['"])", re.MULTILINE), 'MEDIUM')
        }
        self.model = self.load_model()

    def load_model(self):
        try:
            model = keras.models.load_model('path_to_your_model.h5')
            return model
        except Exception as e:
            print(f"Error loading model: {e}")
            return None

    def fetch_code(self, repo_owner: str, repo_name: str) -> str:
        try:
            url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/"
            response = requests.get(url)
            response.raise_for_status() 
            code = response.json()
            # Assume we get the code content in a specific format
            return '\n'.join([file['content'] for file in code if file['name'].endswith(('.py', '.js', '.java'))])
        except Exception as e:
            print(f"Error fetching code from GitHub: {e}")
            return ""

    def static_analysis(self, code: str) -> List[Tuple[str, str]]:
        findings = []
        for vuln, (pattern, severity) in self.vulnerabilities.items():
            matches = pattern.findall(code)
            for match in matches:
                findings.append((vuln, severity, match))
        return findings

    def semantic_analysis(self, code: str) -> List[Tuple[str, str]]:
        # Placeholder for using ML model to analyze the code semantics
        # Here you'd preprocess code and use `self.model` to make predictions
        return []

    def scan_code(self, code: str) -> List[Dict[str, str]]:
        findings = []
        findings.extend(self.static_analysis(code))
        findings.extend(self.semantic_analysis(code))
        return findings

    def evaluate(self, repo_owner: str, repo_name: str) -> None:
        code = self.fetch_code(repo_owner, repo_name)
        findings = self.scan_code(code)
        for finding in findings:
            print(f"Finding: {finding[0]}, Severity: {finding[1]}, Match: {finding[2]}")

# Sample usage
if __name__ == "__main__":
    scanner = BugScanner()
    scanner.evaluate("Adarsh-sigma", "AdarshxCla")
