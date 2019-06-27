#!/usr/bin/python
class DictExample(object):
    def __init__(
        self, repo_namespace: str, repo_name: str, tag_name: str, https_url: str
    ):
        self.repo_namespace = repo_namespace
        self.repo_name = repo_name
        self.tag_name = tag_name
        self.https_url = https_url

    def get_dict(self) -> dict:
        result = self.__dict__
        return result


if __name__ == '__main__':
    de = DictExample(repo_namespace="rpms", repo_name="foobar",
                     tag_name="release",
                     https_url="src.fp.org")
    print(de.get_dict())
