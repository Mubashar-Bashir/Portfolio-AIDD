#!/usr/bin/env python3
"""
Primitive Validator
Validates primitives against isolation rules
"""

import ast
import json
import sys
import os
import re
from pathlib import Path
from typing import List, Dict, Set, Tuple
import subprocess

class PrimitiveValidator:
    """Validates primitives against isolation rules"""

    def __init__(self):
        self.primitive_dirs = [
            "primitives/",
            "backend/primitives/",
            "frontend/src/primitives/",
            "shared/primitives/"
        ]
        self.allowed_external_deps = [
            "typing",
            "json",
            "os",
            "sys",
            "pathlib",
            "datetime",
            "re",
            "collections",
            "itertools",
            "functools",
            "operator",
            "enum",
            "dataclasses",
            "abc",
            "copy",
            "weakref",
            "types",
            "inspect",
            "warnings",
            "logging",  # Only if it's basic logging
        ]
        self.forbidden_deps = [
            "requests",
            "urllib",
            "http",
            "socket",
            "subprocess",
            "os.environ",  # Unless properly handled
            "sys.argv",
            "builtins.open",  # Unless for local files only
        ]

    def is_primitive_file(self, file_path: str) -> bool:
        """Check if a file is part of a primitive directory"""
        path = Path(file_path)
        for primitive_dir in self.primitive_dirs:
            if str(path).startswith(primitive_dir):
                return True
        return False

    def analyze_python_imports(self, file_path: str) -> Dict[str, List[str]]:
        """Analyze Python file for imports and dependencies"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        try:
            tree = ast.parse(content)
        except SyntaxError:
            return {"imports": [], "suspicious": [f"Syntax error in {file_path}"]}

        imports = []
        suspicious_imports = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)
                    if alias.name in self.forbidden_deps:
                        suspicious_imports.append(f"Import {alias.name} is forbidden in primitives")
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module)
                    if node.module in self.forbidden_deps:
                        suspicious_imports.append(f"Import {node.module} is forbidden in primitives")

        return {"imports": imports, "suspicious": suspicious_imports}

    def analyze_js_imports(self, file_path: str) -> Dict[str, List[str]]:
        """Analyze JavaScript/TypeScript file for imports and dependencies"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        imports = []
        suspicious_imports = []

        # Match ES6 imports: import ... from '...'
        import_pattern = r"import\s+.*?\s+from\s+['\"](.*?)['\"]"
        matches = re.findall(import_pattern, content)
        imports.extend(matches)

        # Match require calls: require('...')
        require_pattern = r"require\s*\(\s*['\"](.*?)['\"]\s*\)"
        matches = re.findall(require_pattern, content)
        imports.extend(matches)

        # Check for forbidden patterns
        forbidden_patterns = [
            r"fetch\s*\(",  # Network calls
            r"XMLHttpRequest",  # Network calls
            r"window\.",  # Browser globals that might access external resources
            r"document\.",  # DOM access that might load external resources
        ]

        for pattern in forbidden_patterns:
            if re.search(pattern, content):
                suspicious_imports.append(f"Potentially forbidden pattern '{pattern}' found in {file_path}")

        return {"imports": imports, "suspicious": suspicious_imports}

    def check_external_deps(self, file_path: str) -> List[str]:
        """Check for external dependencies that violate isolation"""
        suspicious = []

        if file_path.endswith('.py'):
            analysis = self.analyze_python_imports(file_path)
            suspicious.extend(analysis["suspicious"])
        elif file_path.endswith(('.js', '.ts', '.jsx', '.tsx')):
            analysis = self.analyze_js_imports(file_path)
            suspicious.extend(analysis["suspicious"])

        return suspicious

    def validate_primitive_file(self, file_path: str) -> Dict[str, any]:
        """Validate a single primitive file"""
        results = {
            "file": file_path,
            "valid": True,
            "issues": [],
            "warnings": []
        }

        # Check if file is in correct location
        if not self.is_primitive_file(file_path):
            results["valid"] = False
            results["issues"].append(f"File {file_path} is not in a primitive directory")

        # Check external dependencies
        external_deps = self.check_external_deps(file_path)
        if external_deps:
            results["valid"] = False
            results["issues"].extend(external_deps)

        # Check for hardcoded credentials
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        credential_patterns = [
            r'password\s*[:=]\s*["\'][^"\']*["\']',
            r'secret\s*[:=]\s*["\'][^"\']*["\']',
            r'token\s*[:=]\s*["\'][^"\']*["\']',
            r'key\s*[:=]\s*["\'][^"\']*["\']',
            r'api_key\s*[:=]\s*["\'][^"\']*["\']',
        ]

        for pattern in credential_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                results["valid"] = False
                results["issues"].append(f"Potential hardcoded credential found in {file_path}")

        return results

    def validate_primitive_directory(self, dir_path: str) -> Dict[str, any]:
        """Validate all primitive files in a directory"""
        results = {
            "directory": dir_path,
            "valid": True,
            "files": [],
            "summary": {"valid_files": 0, "invalid_files": 0}
        }

        dir_path = Path(dir_path)
        if not dir_path.exists():
            results["valid"] = False
            results["issues"] = [f"Directory {dir_path} does not exist"]
            return results

        # Find all Python and JavaScript files in the primitive directory
        extensions = ['*.py', '*.js', '*.ts', '*.jsx', '*.tsx']
        files_to_check = []
        for ext in extensions:
            files_to_check.extend(dir_path.rglob(ext))

        for file_path in files_to_check:
            file_result = self.validate_primitive_file(str(file_path))
            results["files"].append(file_result)

            if file_result["valid"]:
                results["summary"]["valid_files"] += 1
            else:
                results["summary"]["invalid_files"] += 1
                results["valid"] = False

        return results

    def validate_all_primitives(self) -> Dict[str, any]:
        """Validate all primitive directories in the project"""
        results = {
            "overall_valid": True,
            "directories": [],
            "summary": {"valid_dirs": 0, "invalid_dirs": 0}
        }

        for primitive_dir in self.primitive_dirs:
            dir_path = Path(primitive_dir)
            if dir_path.exists():
                dir_result = self.validate_primitive_directory(primitive_dir)
                results["directories"].append(dir_result)

                if dir_result["valid"]:
                    results["summary"]["valid_dirs"] += 1
                else:
                    results["summary"]["invalid_dirs"] += 1
                    results["overall_valid"] = False

        return results

    def generate_report(self, results: Dict[str, any]) -> str:
        """Generate a validation report"""
        report_lines = ["Primitive Isolation Validation Report", "=" * 40]

        if "directories" in results:  # All primitives validation
            report_lines.append(f"Overall Valid: {results['overall_valid']}")
            report_lines.append(f"Valid Directories: {results['summary']['valid_dirs']}")
            report_lines.append(f"Invalid Directories: {results['summary']['invalid_dirs']}")
            report_lines.append("")

            for dir_result in results["directories"]:
                report_lines.append(f"Directory: {dir_result['directory']}")
                report_lines.append(f"  Valid: {dir_result['valid']}")
                report_lines.append(f"  Valid Files: {dir_result['summary']['valid_files']}")
                report_lines.append(f"  Invalid Files: {dir_result['summary']['invalid_files']}")

                for file_result in dir_result["files"]:
                    if not file_result["valid"]:
                        report_lines.append(f"  File Issues ({file_result['file']}):")
                        for issue in file_result["issues"]:
                            report_lines.append(f"    - {issue}")
                report_lines.append("")
        else:  # Single file validation
            report_lines.append(f"File: {results['file']}")
            report_lines.append(f"Valid: {results['valid']}")
            if results["issues"]:
                report_lines.append("Issues:")
                for issue in results["issues"]:
                    report_lines.append(f"  - {issue}")
            if results["warnings"]:
                report_lines.append("Warnings:")
                for warning in results["warnings"]:
                    report_lines.append(f"  - {warning}")

        return "\n".join(report_lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: primitive-validator.py <file_or_directory>")
        print("Examples:")
        print("  primitive-validator.py primitives/auth/")
        print("  primitive-validator.py primitives/auth/login_primitive.py")
        sys.exit(1)

    target = sys.argv[1]
    validator = PrimitiveValidator()

    if os.path.isfile(target):
        # Validate single file
        result = validator.validate_primitive_file(target)
    elif os.path.isdir(target):
        # Validate directory
        result = validator.validate_primitive_directory(target)
    else:
        print(f"Error: {target} is not a valid file or directory")
        sys.exit(1)

    report = validator.generate_report(result)
    print(report)

    # Exit with error code if validation failed
    if not result.get("valid", True) and not result.get("overall_valid", True):
        sys.exit(1)


if __name__ == "__main__":
    main()