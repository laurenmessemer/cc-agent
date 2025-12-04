"""
Entry point for Customer Communication Agent.

Starts API/CLI.
Coordinates bootstrapping of database, scheduler, and orchestrator.
"""

from app.cli import run_cli
from app.config import settings

if __name__ == '__main__':
    run_cli()