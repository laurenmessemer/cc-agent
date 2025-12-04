"""
Database repository layer.

Responsible for all persistence and retrieval of agent memory.
"""


class MemoryRepository:
    """Abstraction over database access for agent memory."""

    def get_customer(self, customer_id):
        raise NotImplementedError

    def save_message(self, message):
        raise NotImplementedError

    def save_tone_profile(self, profile):
        raise NotImplementedError

    def save_risk_event(self, risk_event):
        raise NotImplementedError

    def save_follow_up(self, reminder):
        raise NotImplementedError

    def get_job_history(self, job_id):
        raise NotImplementedError
