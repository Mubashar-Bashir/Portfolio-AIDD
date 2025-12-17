#!/usr/bin/env python3
"""
Executable Constitution Validator
Enforces the active constitution evaluation rules before any AI action
"""

import json
import sys
import os
from typing import Dict, List, Optional, Any
from pathlib import Path

class ConstitutionValidator:
    """Validates AI actions against constitutional rules"""

    def __init__(self, constitution_path: str = ".specify/memory/constitution.md"):
        self.constitution_path = constitution_path
        self.epoch_path = ".specify/current-epoch.json"

    def load_constitution(self) -> str:
        """Load the current constitution"""
        try:
            with open(self.constitution_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            raise ValueError(f"Constitution file not found: {self.constitution_path}")

    def load_current_epoch(self) -> Dict[str, Any]:
        """Load the current epoch configuration"""
        default_epoch = {
            "epoch_name": "initial",
            "epoch_phase": "setup",
            "allowed_actions": ["read", "analyze"],
            "forbidden_actions": ["write", "modify", "implement"],
            "exit_conditions": [],
            "human_approval_required": True
        }

        if os.path.exists(self.epoch_path):
            with open(self.epoch_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Create default epoch file
            with open(self.epoch_path, 'w', encoding='utf-8') as f:
                json.dump(default_epoch, f, indent=2)
            return default_epoch

    def validate_action(self, action_type: str, target_files: List[str], context: str = "") -> Dict[str, Any]:
        """
        Validate an AI action against constitutional rules

        Args:
            action_type: Type of action (read, write, modify, etc.)
            target_files: Files the action will affect
            context: Additional context about the action

        Returns:
            Validation result with success/failure and reasons
        """
        epoch_config = self.load_current_epoch()
        constitution_text = self.load_constitution()

        result = {
            "valid": True,
            "violations": [],
            "warnings": [],
            "epoch_info": epoch_config
        }

        # Check if action is allowed in current epoch
        if action_type not in epoch_config.get("allowed_actions", []):
            result["valid"] = False
            result["violations"].append(
                f"Action '{action_type}' not allowed in current epoch '{epoch_config['epoch_name']}'. "
                f"Allowed actions: {epoch_config.get('allowed_actions', [])}"
            )

        # Check if action is forbidden in current epoch
        if action_type in epoch_config.get("forbidden_actions", []):
            result["valid"] = False
            result["violations"].append(
                f"Action '{action_type}' is forbidden in current epoch '{epoch_config['epoch_name']}'"
            )

        # Check file access against isolation rules
        violations = self._check_file_isolation(target_files, epoch_config)
        if violations:
            result["valid"] = False
            result["violations"].extend(violations)

        # Check for constitutional principle violations
        const_violations = self._check_constitutional_principles(action_type, target_files, constitution_text)
        if const_violations:
            result["valid"] = False
            result["violations"].extend(const_violations)

        # Check if human approval required
        if epoch_config.get("human_approval_required", False):
            result["requires_human_approval"] = True
            if result["valid"]:
                result["valid"] = False  # Force human review even for valid actions
                result["warnings"].append("Human approval required for this epoch")

        return result

    def _check_file_isolation(self, target_files: List[str], epoch_config: Dict[str, Any]) -> List[str]:
        """Check if file operations violate isolation rules"""
        violations = []

        # Define primitive isolation rules
        primitive_dirs = [
            "primitives/",  # Dedicated primitives directory
            "backend/primitives/",
            "frontend/src/primitives/"
        ]

        # Check for cross-boundary violations
        for file_path in target_files:
            # Check if trying to modify files outside allowed scope
            allowed_patterns = epoch_config.get("allowed_file_patterns", [])
            forbidden_patterns = epoch_config.get("forbidden_file_patterns", [])

            for forbidden_pattern in forbidden_patterns:
                if forbidden_pattern in file_path:
                    violations.append(
                        f"File '{file_path}' violates isolation - forbidden pattern: {forbidden_pattern}"
                    )

            # Add more sophisticated isolation checks here
            # For example, preventing backend changes during frontend epoch, etc.

        return violations

    def _check_constitutional_principles(self, action_type: str, target_files: List[str], constitution_text: str) -> List[str]:
        """Check for violations of constitutional principles"""
        violations = []

        # Check for security violations (hardcoded credentials)
        for file_path in target_files:
            if file_path.endswith(('.py', '.js', '.ts', '.json', '.env')):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Look for hardcoded credentials (basic check)
                    suspicious_patterns = [
                        'password', 'secret', 'token', 'key', 'credential', 'api_key'
                    ]

                    for pattern in suspicious_patterns:
                        if pattern.lower() in content.lower():
                            # Check if it's in an environment variable assignment
                            lines = content.split('\n')
                            for i, line in enumerate(lines):
                                if pattern.lower() in line.lower() and '=' in line:
                                    if 'os.environ' not in line and 'process.env' not in line:
                                        violations.append(
                                            f"Potential hardcoded credential in {file_path}:{i+1}. "
                                            f"Use environment variables instead."
                                        )
                except:
                    # File might not exist or be readable, skip check
                    pass

        return violations

    def enforce_validation(self, action_type: str, target_files: List[str], context: str = "") -> bool:
        """
        Enforce validation and either allow or block the action

        Args:
            action_type: Type of action to validate
            target_files: Files the action will affect
            context: Additional context about the action

        Returns:
            True if action is allowed, False otherwise
        """
        result = self.validate_action(action_type, target_files, context)

        if not result["valid"]:
            print("❌ CONSTITUTIONAL VIOLATION DETECTED")
            print(f"Epoch: {result['epoch_info']['epoch_name']}")
            print(f"Action: {action_type}")
            print(f"Target files: {target_files}")
            print("\nViolations:")
            for violation in result["violations"]:
                print(f"  - {violation}")

            if result.get("warnings"):
                print("\nWarnings:")
                for warning in result["warnings"]:
                    print(f"  - {warning}")

            print(f"\nAllowed actions in current epoch: {result['epoch_info'].get('allowed_actions', [])}")
            print(f"Forbidden actions in current epoch: {result['epoch_info'].get('forbidden_actions', [])}")

            return False

        if result.get("requires_human_approval"):
            print("⚠️  HUMAN APPROVAL REQUIRED")
            print(f"Epoch: {result['epoch_info']['epoch_name']}")
            print(f"Action: {action_type}")
            print("This action requires human approval to proceed.")
            return False  # Block until human approves

        print("✅ Action approved by constitutional validator")
        return True


def main():
    """Command line interface for the constitution validator"""
    if len(sys.argv) < 3:
        print("Usage: constitution-validator.py <action_type> <file1> [file2...] [context]")
        print("Example: constitution-validator.py write backend/main.py 'Adding new endpoint'")
        sys.exit(1)

    action_type = sys.argv[1]
    target_files = sys.argv[2:-1] if len(sys.argv) > 3 else sys.argv[2:3]
    context = sys.argv[-1] if len(sys.argv) > 3 else ""

    if len(sys.argv) == 3:  # No context provided
        target_files = [sys.argv[2]]
        context = ""

    validator = ConstitutionValidator()
    is_allowed = validator.enforce_validation(action_type, target_files, context)

    if is_allowed:
        print("VALIDATION PASSED - Proceeding with action")
        sys.exit(0)
    else:
        print("VALIDATION FAILED - Action blocked by constitution")
        sys.exit(1)


if __name__ == "__main__":
    main()