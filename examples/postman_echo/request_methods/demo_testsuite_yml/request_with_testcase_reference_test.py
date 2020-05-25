# NOTICE: Generated By HttpRunner. DO'NOT EDIT!
# FROM: examples/postman_echo/request_methods/demo_testsuite_yml/request_with_testcase_reference.yml
from httprunner import HttpRunner, TConfig, TStep

from examples.postman_echo.request_methods.request_with_functions_test import (
    TestCaseRequestWithFunctions,
)


class TestCaseRequestWithTestcaseReference(HttpRunner):
    config = TConfig(
        **{
            "name": "request with referenced testcase",
            "variables": {"foo1": "session_bar1", "var2": "testsuite_val2"},
            "base_url": "https://postman-echo.com",
            "verify": False,
            "path": "examples/postman_echo/request_methods/demo_testsuite_yml/request_with_testcase_reference_test.py",
        }
    )

    teststeps = [
        TStep(
            **{
                "name": "request with functions",
                "variables": {"foo1": "override_bar1"},
                "testcase": TestCaseRequestWithFunctions,
            }
        ),
    ]


if __name__ == "__main__":
    TestCaseRequestWithTestcaseReference().test_start()
