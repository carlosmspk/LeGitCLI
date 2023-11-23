import unittest
from legitcli.model.rules import CommitMessageTextRule
from legitcli.validator.rules import CommitMessageTextValidator
from testutils.fakes import FakeGitReadonlyClient, FakeLazyFileReader


class TestCommitMessageValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.fake_lazy_file_reader = FakeLazyFileReader("")
        self.rule = CommitMessageTextRule("", False)
        self.validator = CommitMessageTextValidator(
            self.rule,
            FakeGitReadonlyClient(),
            self.fake_lazy_file_reader,
        )

    def test_basic_regex_validated(self):
        self.validator._rule.message_regex = "message"
        self.fake_lazy_file_reader.returned_string = "message"

        result = self.validator.validate_commit()

        self.assertEqual(result.failed, False)
        self.assertEqual(result.fail_reason, None)

    def test_basic_bad_regex_invalidated(self):
        self.validator._rule.message_regex = "message"
        self.fake_lazy_file_reader.returned_string = "not message"

        result = self.validator.validate_commit()

        self.assertEqual(result.failed, True)
        self.assertIsInstance(result.fail_reason, str)

    def test_union_regex_validated(self):
        self.validator._rule.message_regex = "this|that"
        self.fake_lazy_file_reader.returned_string = "this"

        result = self.validator.validate_commit()

        self.assertEqual(result.failed, False)
        self.assertEqual(result.fail_reason, None)

        self.fake_lazy_file_reader.returned_string = "that"

        result = self.validator.validate_commit()

        self.assertEqual(result.failed, False)
        self.assertEqual(result.fail_reason, None)

        self.fake_lazy_file_reader.returned_string = "those"

        result = self.validator.validate_commit()

        self.assertEqual(result.failed, True)
        self.assertIsInstance(result.fail_reason, str)

    def test_empty_regex_always_validated(self):
        self.validator._rule.message_regex = ""
        self.fake_lazy_file_reader.returned_string = "anything"

        result = self.validator.validate_commit()

        self.assertEqual(result.failed, False)
        self.assertEqual(result.fail_reason, None)

        self.fake_lazy_file_reader.returned_string = ""

        result = self.validator.validate_commit()

        self.assertEqual(result.failed, False)
        self.assertEqual(result.fail_reason, None)

    def test_ignore_newlines_validated(self):
        self.validator._rule.message_regex = "a b"
        self.validator._rule.ignore_newlines = True
        self.fake_lazy_file_reader.returned_string = "a\nb"

        result = self.validator.validate_commit()

        self.assertEqual(result.failed, False)
        self.assertEqual(result.fail_reason, None)

    def test_consecutive_ignore_newlines_validated(self):
        self.validator._rule.message_regex = "a b"
        self.validator._rule.ignore_newlines = True
        self.fake_lazy_file_reader.returned_string = "a\n\n\n\n\nb"

        result = self.validator.validate_commit()

        self.assertEqual(result.failed, False)
        self.assertEqual(result.fail_reason, None)

    def test_consecutive_no_ignore_newlines_invalidated(self):
        self.validator._rule.message_regex = "a b"
        self.fake_lazy_file_reader.returned_string = "a\n\n\n\n\nb"

        result = self.validator.validate_commit()

        self.assertEqual(result.failed, True)
        self.assertIsInstance(result.fail_reason, str)

    def test_consecutive_ignore_newlines_with_interim_value_validated(self):
        self.validator._rule.message_regex = "a b c"
        self.validator._rule.ignore_newlines = True
        self.fake_lazy_file_reader.returned_string = "a\n\nb\n\n\nc"

        result = self.validator.validate_commit()

        self.assertEqual(result.failed, False)
        self.assertEqual(result.fail_reason, None)


if __name__ == "__main__":
    unittest.main()
