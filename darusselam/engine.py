import os
import yaml
import re
from typing import Dict, List, Any

class ComplianceEngine:
    def __init__(self, pillars_path: str):
        with open(pillars_path, 'r', encoding='utf-8') as f:
            self.pillars = yaml.safe_load(f)['pillars']
        
    def scan_directory(self, root_dir: str) -> Dict[str, Any]:
        results = {
            "summary": {
                "total_files_scanned": 0,
                "violations_found": 0,
                "status": "Incomplete"
            },
            "violations": []
        }
        
        for root, dirs, files in os.walk(root_dir):
            # Skip hidden and ignored folders
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', 'venv', '__pycache__']]
            
            for file in files:
                if file.endswith(('.py', '.js', '.html', '.css', '.yaml', '.json')):
                    file_path = os.path.join(root, file)
                    results["summary"]["total_files_scanned"] += 1
                    file_violations = self.scan_file(file_path)
                    if file_violations:
                        results["violations"].extend(file_violations)
                        results["summary"]["violations_found"] += len(file_violations)

        results["summary"]["status"] = "PASSED (Compliant)" if results["summary"]["violations_found"] == 0 else "FAILED (Non-compliant)"
        return results

    def scan_file(self, file_path: str) -> List[Dict[str, Any]]:
        violations = []
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            for p_key, p_data in self.pillars.items():
                # Check heuristics
                heuristics = p_data.get('heuristics', {})
                
                # Check patterns
                for pattern in heuristics.get('patterns', []):
                    if re.search(pattern, content, re.IGNORECASE):
                        violations.append({
                            "pillar": p_data['name'],
                            "file": os.path.relpath(file_path),
                            "marker": pattern,
                            "type": "Pattern Match"
                        })
                
                # Check specific libraries for JS/Python
                if file_path.endswith(('package.json', 'requirements.txt')):
                    for lib in heuristics.get('non_compliant_libs', []):
                        if lib in content:
                            violations.append({
                                "pillar": p_data['name'],
                                "file": os.path.relpath(file_path),
                                "marker": lib,
                                "type": "Forbidden Dependency"
                            })
        except Exception as e:
            pass # Skip unreadable files
            
        return violations
