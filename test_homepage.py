from homepage import GuviAutomation
import pytest


url = "https://www.guvi.in/"
automation = GuviAutomation(url)

# test case for verifying guvi title
def test_guvi_title():
    expected_title = "GUVI | Learn to code in your native language"
    assert automation.fetch_title() == expected_title
    print("SUCCESS: GUVI TITLE VERIFIED")

# test case for verifying guvi url
def test_guvi_url():
    expected_url = "https://www.guvi.in/"
    assert automation.fetch_url() == expected_url
    print("SUCCESS: GUVI URL VERIFIED")
