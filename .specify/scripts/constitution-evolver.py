#!/usr/bin/env python3
"""
Constitution Evolver
Manages controlled evolution of the constitution with proper validation
"""

import json
import sys
import os
import re
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

class ConstitutionEvolver:
    """Manages controlled evolution of the constitution with proper validation"""

    def __init__(self):
        self.constitution_path = ".specify/memory/constitution.md"
        self.history_dir = ".specify/memory/history"
        self.history_dir.mkdir(exist_ok=True)
        self.amendments_dir = ".specify/amendments"
        self.amendments_dir.mkdir(exist_ok=True)

    def load_constitution(self) -> str:
        """Load the current constitution"""
        with open(self.constitution_path, 'r', encoding='utf-8') as f:
            return f.read()

    def save_constitution(self, content: str):
        """Save the constitution with proper validation"""
        # Validate constitution structure before saving
        if not self.validate_constitution_structure(content):
            raise ValueError("Constitution structure validation failed")

        with open(self.constitution_path, 'w', encoding='utf-8') as f:
            f.write(content)

    def validate_constitution_structure(self, content: str) -> bool:
        """Validate that the constitution has required sections"""
        required_sections = [
            "Core Principles",
            "Technical Standards",
            "Development Workflow",
            "Governance"
        ]

        for section in required_sections:
            if f"## {section}" not in content and f"### {section}" not in content:
                print(f"Missing required section: {section}")
                return False

        return True

    def create_amendment(self, title: str, description: str, changes: List[Dict[str, Any]],
                        epoch_name: str = None) -> str:
        """Create a new constitution amendment"""
        amendment_id = f"AMD-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

        amendment = {
            "id": amendment_id,
            "title": title,
            "description": description,
            "created_date": datetime.now().isoformat(),
            "changes": changes,
            "epoch_name": epoch_name,
            "status": "proposed",
            "applied_version": None
        }

        amendment_file = self.amendments_dir / f"{amendment_id}.json"
        with open(amendment_file, 'w', encoding='utf-8') as f:
            json.dump(amendment, f, indent=2)

        print(f"Created amendment: {amendment_id}")
        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"File: {amendment_file}")

        return str(amendment_file)

    def apply_amendment(self, amendment_file: str) -> bool:
        """Apply an amendment to the constitution"""
        with open(amendment_file, 'r', encoding='utf-8') as f:
            amendment = json.load(f)

        if amendment["status"] != "proposed":
            print(f"Amendment {amendment['id']} is not in proposed status")
            return False

        # Load current constitution
        current_constitution = self.load_constitution()

        # Apply changes
        updated_constitution = self._apply_changes(current_constitution, amendment["changes"])

        # Validate updated constitution
        if not self.validate_constitution_structure(updated_constitution):
            print(f"Amendment {amendment['id']} would create invalid constitution")
            return False

        # Backup current constitution
        backup_path = self._backup_constitution()

        # Update constitution file
        self.save_constitution(updated_constitution)

        # Update amendment status
        amendment["status"] = "applied"
        amendment["applied_version"] = self._get_current_version(updated_constitution)
        amendment["applied_date"] = datetime.now().isoformat()

        # Save updated amendment
        with open(amendment_file, 'w', encoding='utf-8') as f:
            json.dump(amendment, f, indent=2)

        print(f"Applied amendment: {amendment['id']}")
        print(f"Backup saved to: {backup_path}")

        return True

    def _apply_changes(self, constitution: str, changes: List[Dict[str, Any]]) -> str:
        """Apply changes to the constitution text"""
        updated_constitution = constitution

        for change in changes:
            change_type = change["type"]
            if change_type == "replace_section":
                section_name = change["section"]
                new_content = change["content"]

                # Find and replace the section
                pattern = rf"(##\s+{re.escape(section_name)}.*?)(?=##\s+\w|\Z)"
                updated_constitution = re.sub(
                    pattern,
                    f"## {section_name}\n\n{new_content}",
                    updated_constitution,
                    flags=re.DOTALL
                )
            elif change_type == "append_to_section":
                section_name = change["section"]
                content_to_add = change["content"]

                pattern = rf"(##\s+{re.escape(section_name)}.*?)(?=##\s+\w|\Z)"
                updated_constitution = re.sub(
                    pattern,
                    lambda m: m.group(0).rstrip() + f"\n\n{content_to_add}",
                    updated_constitution,
                    flags=re.DOTALL
                )
            elif change_type == "add_section":
                section_name = change["section"]
                content = change["content"]
                new_section = f"\n## {section_name}\n\n{content}\n"
                updated_constitution = updated_constitution.rstrip() + new_section

        return updated_constitution

    def _backup_constitution(self) -> str:
        """Create a backup of the current constitution"""
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        backup_path = self.history_dir / f"constitution-backup-{timestamp}.md"

        current_content = self.load_constitution()
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(current_content)

        return str(backup_path)

    def _get_current_version(self, constitution: str = None) -> str:
        """Extract the current version from the constitution"""
        if constitution is None:
            constitution = self.load_constitution()

        version_match = re.search(r'\*\*Version\*\*:\s*([^\n\r|]+)', constitution)
        if version_match:
            return version_match.group(1).strip()

        return "unknown"

    def increment_version(self, current_version: str, version_type: str = "patch") -> str:
        """Increment the version number"""
        if current_version == "unknown":
            return "1.0.0"

        try:
            major, minor, patch = map(int, current_version.split('.'))
        except ValueError:
            # If version is not in X.Y.Z format, default to 1.0.0
            return "1.0.0"

        if version_type == "major":
            major += 1
            minor = 0
            patch = 0
        elif version_type == "minor":
            minor += 1
            patch = 0
        else:  # patch
            patch += 1

        return f"{major}.{minor}.{patch}"

    def update_version_in_constitution(self, new_version: str):
        """Update the version in the constitution file"""
        content = self.load_constitution()

        # Replace the version line
        updated_content = re.sub(
            r'(\*\*Version\*\*:\s*)([^\n\r|]+)',
            f'**Version**: {new_version}',
            content
        )

        # If version line doesn't exist, add it to the end
        if updated_content == content:
            updated_content = content.rstrip() + f"\n\n**Version**: {new_version} | **Ratified**: {datetime.now().strftime('%Y-%m-%d')} | **Last Amended**: {datetime.now().strftime('%Y-%m-%d')}\n"

        self.save_constitution(updated_content)

    def propose_constitution_change(self, title: str, description: str, changes: List[Dict[str, Any]],
                                  version_type: str = "patch", epoch_name: str = None) -> str:
        """Propose a constitution change with version update"""
        # Get current version and increment it
        current_version = self._get_current_version()
        new_version = self.increment_version(current_version, version_type)

        # Add version update to changes
        version_change = {
            "type": "update_version",
            "new_version": new_version
        }

        changes.append(version_change)

        # Create amendment
        amendment_file = self.create_amendment(title, description, changes, epoch_name)

        print(f"Proposed constitution change: {title}")
        print(f"New version will be: {new_version}")
        print(f"Amendment file: {amendment_file}")

        return amendment_file

    def list_amendments(self) -> List[Dict[str, Any]]:
        """List all amendments"""
        amendments = []
        for file_path in self.amendments_dir.glob("*.json"):
            with open(file_path, 'r', encoding='utf-8') as f:
                amendment = json.load(f)
                amendments.append(amendment)

        return sorted(amendments, key=lambda x: x['created_date'], reverse=True)

    def validate_for_epoch(self, epoch_config: Dict[str, Any]) -> List[str]:
        """Validate that the current constitution is compatible with the epoch"""
        violations = []

        # Load current constitution
        constitution = self.load_constitution()

        # Check if constitution allows the epoch's requirements
        allowed_actions = epoch_config.get("allowed_actions", [])
        forbidden_actions = epoch_config.get("forbidden_actions", [])

        # Basic validation - in a real system, this would be more sophisticated
        if "write" in forbidden_actions and "write" in constitution.lower():
            violations.append("Constitution permits writes but epoch forbids them")

        return violations


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Constitution Evolver - Manages controlled evolution of the constitution")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Propose change command
    propose_parser = subparsers.add_parser("propose", help="Propose a constitution change")
    propose_parser.add_argument("--title", required=True, help="Title of the amendment")
    propose_parser.add_argument("--description", required=True, help="Description of the amendment")
    propose_parser.add_argument("--epoch", help="Epoch this amendment applies to")
    propose_parser.add_argument("--version-type", choices=["major", "minor", "patch"], default="patch",
                               help="Type of version increment")

    # Add arguments for different types of changes
    change_group = propose_parser.add_mutually_exclusive_group(required=True)
    change_group.add_argument("--replace-section", nargs=2, metavar=("SECTION", "CONTENT"),
                             help="Replace an entire section")
    change_group.add_argument("--append-to-section", nargs=2, metavar=("SECTION", "CONTENT"),
                             help="Append content to a section")
    change_group.add_argument("--add-section", nargs=2, metavar=("SECTION", "CONTENT"),
                             help="Add a new section")

    # Apply amendment command
    apply_parser = subparsers.add_parser("apply", help="Apply a proposed amendment")
    apply_parser.add_argument("--amendment-file", required=True, help="Path to amendment file")

    # List amendments command
    subparsers.add_parser("list", help="List all amendments")

    # Validate for epoch command
    validate_parser = subparsers.add_parser("validate-epoch", help="Validate constitution for epoch")
    validate_parser.add_argument("--epoch-config", required=True, help="Path to epoch config file")

    args = parser.parse_args()

    evolver = ConstitutionEvolver()

    if args.command == "propose":
        changes = []

        if args.replace_section:
            changes.append({
                "type": "replace_section",
                "section": args.replace_section[0],
                "content": args.replace_section[1]
            })
        elif args.append_to_section:
            changes.append({
                "type": "append_to_section",
                "section": args.append_to_section[0],
                "content": args.append_to_section[1]
            })
        elif args.add_section:
            changes.append({
                "type": "add_section",
                "section": args.add_section[0],
                "content": args.add_section[1]
            })

        evolver.propose_constitution_change(
            title=args.title,
            description=args.description,
            changes=changes,
            version_type=args.version_type,
            epoch_name=args.epoch
        )

    elif args.command == "apply":
        success = evolver.apply_amendment(args.amendment_file)
        if not success:
            print("Failed to apply amendment")
            sys.exit(1)

    elif args.command == "list":
        amendments = evolver.list_amendments()
        print("Constitution Amendments:")
        for amendment in amendments:
            print(f"  {amendment['id']}: {amendment['title']} - {amendment['status']} ({amendment['created_date']})")

    elif args.command == "validate-epoch":
        with open(args.epoch_config, 'r') as f:
            epoch_config = json.load(f)

        violations = evolver.validate_for_epoch(epoch_config)
        if violations:
            print("Constitution-epoch compatibility violations:")
            for violation in violations:
                print(f"  - {violation}")
            sys.exit(1)
        else:
            print("Constitution is compatible with epoch configuration")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()