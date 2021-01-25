# mkdocs-same-dir

**[Plugin][] for [MkDocs][] to allow placing *mkdocs.yml* in the same directory as documentation**

[![PyPI](https://img.shields.io/pypi/v/mkdocs-same-dir)](https://pypi.org/project/mkdocs-same-dir/)
[![GitHub](https://img.shields.io/github/license/oprypin/mkdocs-same-dir)](https://github.com/oprypin/mkdocs-same-dir/blob/master/LICENSE.md)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/oprypin/mkdocs-same-dir/CI)](https://github.com/oprypin/mkdocs-same-dir/actions?query=event%3Apush+branch%3Amaster)

```shell
pip install mkdocs-same-dir
```

[mkdocs]: https://www.mkdocs.org/
[plugin]: https://www.mkdocs.org/user-guide/plugins/

## Usage

Activate the plugin in **mkdocs.yml**, along with actually changing `docs_dir`  
(normally, MkDocs *absolutely wouldn't* let you set it to `.`):

```yaml
site_name: mkdocs-same-dir
docs_dir: .
site_dir: ../site

plugins:
  - search
  - same-dir
```

and now you can move this **mkdocs.yml** into your **docs** directory, or move your docs alongside **mkdocs.yml**.

[**See example layout**](https://github.com/oprypin/mkdocs-same-dir/tree/master/example)
