import unittest

from cms_core import build_target_path, render_markdown, slugify


class CmsCoreTests(unittest.TestCase):
  def test_slugify_normalizes_title(self):
    self.assertEqual(slugify("Hello, HAT World!"), "hello-hat-world")

  def test_render_markdown_includes_frontmatter(self):
    content = render_markdown(
      "post",
      {
        "title": "Welcome",
        "publishdate": "2026-04-08T10:30:00-05:00",
        "author": "Mark",
        "tags": "One, Two",
        "categories": "General",
        "draft": False,
        "body": "Body text",
      },
    )
    self.assertIn("title: Welcome", content)
    self.assertIn("publishdate: '2026-04-08T10:30:00-05:00'", content)
    self.assertIn("- One", content)
    self.assertTrue(content.endswith("Body text\n"))

  def test_build_target_path_uses_date_prefix(self):
    path = build_target_path(
      "/tmp/project",
      "site",
      "event",
      {
        "title": "Steering Committee Meeting",
        "publishDate": "2026-04-08T10:30:00-05:00",
        "filename_slug": "committee-meeting",
      },
    )
    self.assertEqual(str(path).endswith("site/content/event/2026-04-08_committee-meeting.md"), True)


if __name__ == "__main__":
  unittest.main()