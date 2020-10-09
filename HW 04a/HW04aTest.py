import unittest, json
from unittest.mock import Mock, patch
import time
import HW04a
# from HW04a import GitHub

class testGitHub(unittest.TestCase):
    time.sleep(1)
    @patch('HW04a.GitHub')
    def test1pass(self, mockGitHubFunc):
        mockGitHubFunc.return_value = ["Repo: csp Number of commits: 2", "Repo: hellogitworld Number of commits: 30",
        "Repo: helloworld Number of commits: 6", "Repo: Mocks Number of commits: 10", "Repo: Project1 Number of commits: 2", 
        "Repo: richkempinski.github.io Number of commits: 9", "Repo: threads-of-life Number of commits: 1", "Repo: try_nbdev Number of commits: 2", 
        "Repo: try_nbdev2 Number of commits: 5"]
        self.assertEqual(HW04a.GitHub('richkempinski'), ["Repo: csp Number of commits: 2", "Repo: hellogitworld Number of commits: 30",
        "Repo: helloworld Number of commits: 6", "Repo: Mocks Number of commits: 10", "Repo: Project1 Number of commits: 2", 
        "Repo: richkempinski.github.io Number of commits: 9", "Repo: threads-of-life Number of commits: 1", "Repo: try_nbdev Number of commits: 2", 
        "Repo: try_nbdev2 Number of commits: 5"])
        # self.assertEqual(GitHub('richkempinski'), ["Repo: csp Number of commits: 2", "Repo: hellogitworld Number of commits: 30",
        # "Repo: helloworld Number of commits: 6", "Repo: Mocks Number of commits: 10", "Repo: Project1 Number of commits: 2", 
        # "Repo: richkempinski.github.io Number of commits: 9", "Repo: threads-of-life Number of commits: 1", "Repo: try_nbdev Number of commits: 2", 
        # "Repo: try_nbdev2 Number of commits: 5"])

    time.sleep(1)
    @patch('HW04a.GitHub')
    def test2pass(self, mockGitHubFunc):
        mockGitHubFunc.return_value = ["Repo: Homework4 Number of commits: 30", "Repo: SSW345 Number of commits: 3", 
        "Repo: test-Homework4 Number of commits: 2"]
        self.assertEqual(HW04a.GitHub('olivepowers'), ["Repo: Homework4 Number of commits: 30", "Repo: SSW345 Number of commits: 3", 
        "Repo: test-Homework4 Number of commits: 2"])
        # self.assertEqual(GitHub('olivepowers'), ["Repo: Homework4 Number of commits: 30", "Repo: SSW345 Number of commits: 3", 
        # "Repo: test-Homework4 Number of commits: 2"])

    time.sleep(1)
    @patch('HW04a.GitHub')
    def test3fail(self, mockGitHubFunc):
        mockGitHubFunc.return_value = "This account is not valid"
        self.assertEqual(HW04a.GitHub('abcdeefghijklmnopqrstuvwxyz'), "This account is not valid")

    time.sleep(1)
    @patch('HW04a.GitHub')
    def test4fail(self, mockGitHubFunc):
        mockGitHubFunc.return_value = "This account is not valid"
        self.assertEqual(HW04a.GitHub(19283894389), "This account is not valid")



if __name__ == "__main__":
    unittest.main()