# mkdocs-same-dir

**[Plugin][] for [MkDocs][] to allow placing *mkdocs.yml* in the same directory as documentation**

[![PyPI](https://img.shields.io/pypi/v/mkdocs-same-dir)](https://pypi.org/project/mkdocs-same-dir/)
[![License](https://img.shields.io/github/license/oprypin/mkdocs-same-dir)](https://github.com/oprypin/mkdocs-same-dir/blob/master/LICENSE.md)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/oprypin/mkdocs-same-dir/ci.yml.svg)](https://github.com/oprypin/mkdocs-same-dir/actions?query=event%3Apush+branch%3Amaster)

```shell
pip install mkdocs-same-dir
```

[mkdocs]: https://www.mkdocs.org/
[plugin]: https://www.mkdocs.org/user-guide/plugins/

## Usage

Activate the plugin in **mkdocs.yml**, along with actually changing `docs_dir`  
(normally, MkDocs *absolutely wouldn't* let you set it to `.`):

```yaml
site_name: foo
docs_dir: .
site_dir: ../site

plugins:
  - search
  - same-dir
```

and now you can move this **mkdocs.yml** into your **docs** directory, or move your docs alongside **mkdocs.yml**.

[**See example layout**](https://github.com/oprypin/mkdocs-same-dir/tree/master/example)

### Important notes

Another necessary effect of this plugin is that files *directly at the root* of the **docs** dir will no longer be picked up, unless they are Markdown files.

And note that the [implementation](https://github.com/oprypin/mkdocs-same-dir/blob/master/mkdocs_same_dir/plugin.py) of this plugin is a huge hack that monkeypatches MkDocs' internals. But I pledge to keep up with MkDocs updates and keep it working as long as that's still possible.
