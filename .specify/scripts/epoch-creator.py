#!/usr/bin/env python3
"""
Epoch Creator Skill
Automates the creation of development epochs with proper governance controls
"""

import json
import sys
import os
import argparse
from datetime import datetime
from pathlib import Path

class EpochCreator:
    """Creates and manages development epochs with governance controls"""

    def __init__(self):
        self.epochs_dir = Path(".specify/epochs")
        self.epochs_dir.mkdir(exist_ok=True)

    def create_epoch(
        self,
        epoch_name: str,
        epoch_goal: str,
        allowed_actions: list,
        forbidden_actions: list,
        exit_conditions: list,
        constitution_version: str = "1.0.0",
        human_approval_required: bool = True,
        allowed_file_patterns: list = None,
        forbidden_file_patterns: list = None
    ) -> str:
        """
        Create a new epoch configuration

        Args:
            epoch_name: Name of the epoch
            epoch_goal: Goal of the epoch
            allowed_actions: Actions permitted in this epoch
            forbidden_actions: Actions prohibited in this epoch
            exit_conditions: Conditions to exit this epoch
            constitution_version: Version of constitution to comply with
            human_approval_required: Whether human approval is needed
            allowed_file_patterns: File patterns allowed in this epoch
            forbidden_file_patterns: File patterns forbidden in this epoch

        Returns:
            Path to created epoch file
        """
        if allowed_file_patterns is None:
            allowed_file_patterns = [f"{epoch_name.lower().split('_')[0]}/"]
        if forbidden_file_patterns is None:
            forbidden_file_patterns = []

        epoch_config = {
            "epoch_name": epoch_name,
            "epoch_phase": epoch_name.lower().replace(" ", "_").replace("-", "_"),
            "epoch_goal": epoch_goal,
            "allowed_actions": allowed_actions,
            "forbidden_actions": forbidden_actions,
            "exit_conditions": exit_conditions,
            "constitution_version": constitution_version,
            "human_approval_required": human_approval_required,
            "allowed_file_patterns": allowed_file_patterns,
            "forbidden_file_patterns": forbidden_file_patterns,
            "created_date": datetime.now().isoformat(),
            "primitive_isolation_rules": {
                "no_external_deps": True,
                "test_alone": True,
                "immutable_after_acceptance": True
            },
            "validation_criteria": [
                f"Epoch goal '{epoch_goal}' achieved",
                "All allowed actions completed within boundaries",
                "No forbidden actions performed",
                "Exit conditions met"
            ]
        }

        # Create filename from epoch name
        filename = f"epoch-{len(list(self.epochs_dir.glob('epoch-*.json'))) + 1}-{epoch_name.lower().replace(' ', '-').replace('_', '-')}.json"
        filepath = self.epochs_dir / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(epoch_config, f, indent=2)

        print(f"✅ Epoch created: {filepath}")
        print(f"Epoch Name: {epoch_name}")
        print(f"Goal: {epoch_goal}")
        print(f"Allowed Actions: {allowed_actions}")
        print(f"Forbidden Actions: {forbidden_actions}")
        print(f"Exit Conditions: {exit_conditions}")

        return str(filepath)

    def list_epochs(self) -> list:
        """List all available epochs"""
        epoch_files = list(self.epochs_dir.glob("epoch-*.json"))
        epochs = []
        for file in epoch_files:
            with open(file, 'r', encoding='utf-8') as f:
                epoch_data = json.load(f)
                epochs.append({
                    "filename": file.name,
                    "name": epoch_data["epoch_name"],
                    "goal": epoch_data["epoch_goal"],
                    "created": epoch_data.get("created_date", "unknown")
                })
        return epochs

    def activate_epoch(self, epoch_file: str) -> bool:
        """Activate an epoch by updating the current-epoch.json file"""
        epoch_path = Path(epoch_file)
        if not epoch_path.exists():
            print(f"❌ Epoch file not found: {epoch_file}")
            return False

        # Load the epoch configuration
        with open(epoch_path, 'r', encoding='utf-8') as f:
            epoch_config = json.load(f)

        # Update the current epoch file
        current_epoch_file = Path(".specify/current-epoch.json")
        current_config = {
            "current_epoch": epoch_config["epoch_name"],
            "current_epoch_file": str(epoch_path),
            "epoch_start_date": datetime.now().isoformat(),
            "governance_level": 4,
            "last_validation_check": datetime.now().isoformat(),
            "constitution_version": epoch_config.get("constitution_version", "1.0.0")
        }

        with open(current_epoch_file, 'w', encoding='utf-8') as f:
            json.dump(current_config, f, indent=2)

        print(f"✅ Epoch activated: {epoch_config['epoch_name']}")
        print(f"File: {epoch_path}")
        return True


def main():
    parser = argparse.ArgumentParser(description="Epoch Creator Skill - Automates epoch creation with governance controls")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Create epoch command
    create_parser = subparsers.add_parser("create", help="Create a new epoch")
    create_parser.add_argument("--name", required=True, help="Name of the epoch")
    create_parser.add_argument("--goal", required=True, help="Goal of the epoch")
    create_parser.add_argument("--allowed-actions", required=True, help="Comma-separated allowed actions")
    create_parser.add_argument("--forbidden-actions", required=True, help="Comma-separated forbidden actions")
    create_parser.add_argument("--exit-conditions", required=True, help="Comma-separated exit conditions")
    create_parser.add_argument("--constitution-version", default="1.0.0", help="Constitution version to comply with")
    create_parser.add_argument("--human-approval", action="store_true", default=True, help="Require human approval")
    create_parser.add_argument("--allowed-patterns", help="Comma-separated allowed file patterns")
    create_parser.add_argument("--forbidden-patterns", help="Comma-separated forbidden file patterns")

    # List epochs command
    list_parser = subparsers.add_parser("list", help="List all available epochs")

    # Activate epoch command
    activate_parser = subparsers.add_parser("activate", help="Activate an epoch")
    activate_parser.add_argument("--file", required=True, help="Path to epoch file to activate")

    args = parser.parse_args()

    creator = EpochCreator()

    if args.command == "create":
        allowed_actions = [a.strip() for a in args.allowed_actions.split(",")]
        forbidden_actions = [f.strip() for f in args.forbidden_actions.split(",")]
        exit_conditions = [e.strip() for e in args.exit_conditions.split(",")]
        allowed_patterns = [p.strip() for p in args.allowed_patterns.split(",")] if args.allowed_patterns else None
        forbidden_patterns = [p.strip() for p in args.forbidden_patterns.split(",")] if args.forbidden_patterns else None

        creator.create_epoch(
            epoch_name=args.name,
            epoch_goal=args.goal,
            allowed_actions=allowed_actions,
            forbidden_actions=forbidden_actions,
            exit_conditions=exit_conditions,
            constitution_version=args.constitution_version,
            human_approval_required=args.human_approval,
            allowed_file_patterns=allowed_patterns,
            forbidden_file_patterns=forbidden_patterns
        )

    elif args.command == "list":
        epochs = creator.list_epochs()
        print("Available Epochs:")
        for epoch in epochs:
            print(f"  {epoch['filename']}: {epoch['name']} - {epoch['goal']} ({epoch['created']})")

    elif args.command == "activate":
        creator.activate_epoch(args.file)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()