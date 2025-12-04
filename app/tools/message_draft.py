"""
Generates customer-facing message drafts using an LLM.
"""


class MessageDraftTool:
    """Produces customer-ready drafts from job and tone memory."""

    def draft(self, job, customer, tone_profile, intent):
        raise NotImplementedError
