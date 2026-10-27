"""Offline checks for the skill package and its commit-message validator."""
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / 'skills/ajimu-conventions/scripts/check_commit_message.py'


def check(message):
    return subprocess.run([sys.executable, str(CHECK), '--message', message], capture_output=True, text=True)


class PackageTests(unittest.TestCase):
    def test_repository_is_a_valid_skill_plugin(self):
        result = subprocess.run([sys.executable, str(ROOT / 'tools/validate_skill.py'), str(ROOT)],
                                capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stdout)


class CommitMessageTests(unittest.TestCase):
    def test_neutral_imperative_messages_pass(self):
        for message in ('Preserve verified work across session restarts',
                        'Add data models and payment providers\n\nDocument the new schema and its tests.'):
            with self.subTest(message=message):
                self.assertEqual(0, check(message).returncode)

    def test_authorship_and_tool_references_are_rejected(self):
        for message in ('Add export\n\nCo-Authored-By: Someone <someone@example.invalid>',
                        'Add export\n\nGenerated with an assistant', 'Use ChatGPT output for parser',
                        'Fix login.'):
            with self.subTest(message=message):
                self.assertEqual(1, check(message).returncode)

    def test_style_problems_are_warnings(self):
        result = check('Added caching for reports')
        self.assertEqual(0, result.returncode)
        self.assertIn('imperative', result.stdout)

    def test_git_comment_lines_are_ignored(self):
        self.assertEqual(0, check('Keep drafts during polling\n# Please enter the commit message').returncode)


if __name__ == '__main__':
    unittest.main()
