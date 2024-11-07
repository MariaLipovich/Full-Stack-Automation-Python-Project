import allure
from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations


class Verifications:
    @staticmethod
    @allure.step('Verify equals')
    def verify_equals(actual: str, expected: str):
        assert actual == expected, f'The verify equals failed: {actual} is not equals to {expected}'

    @staticmethod
    @allure.step('Verify an element is display')
    def verify_element_is_displayed(elem: WebElement):
        assert elem.is_displayed(), f"Verify the element is displayed failed, {elem.text} isn`t displayed"

    @staticmethod
    @allure.step('Verify elements using smart assertions')
    # This is second option for verify main page upper menu
    def smart_assert_elements(elements):
        for index in range(len(elements)):
            soft_assert(elements[index].is_displayed())
        verify_expectations()

    @staticmethod
    @allure.step('Soft verification of elements using raise AssertionError')
    # This is first option for verify main page upper menu
    def soft_displayed(elements):
        failed_elements = []
        for index in range(len(elements)):
            if elements[index].is_displayed() == False:
                failed_elements.insert(len(failed_elements), elements[index].text)
        if len(failed_elements) > 0:
            for elem in failed_elements:
                print(f"Soft displayed failed. Elements which have failed are: {str(elem)}")
            raise AssertionError("Soft Displayed Failed")

    @staticmethod
    @allure.step('Verify number of the elements')
    def verify_count_elements(expected_count, actual_count):
        assert len(
            actual_count) == expected_count, f"Count of elements is: {str(len(actual_count))}, but must be: {str(expected_count)}"

    @staticmethod
    @allure.step('Verify number of the elements')
    def verify_count_elements_with_smart_assertions(expected_count, actual_count):
        soft_assert(len(
            actual_count) == expected_count, f"Count of elements is: {str(len(actual_count))}, but must be: {str(expected_count)}")
        verify_expectations()

    @staticmethod
    @allure.step('Verify an element with smart assertions')
    def verify_element_with_smart_assertion(element: WebElement):
        soft_assert(element.is_displayed(), f"Verify the element is displayed failed, {element.text} isn`t displayed")
        verify_expectations()

    @staticmethod
    @allure.step('Verify an element within another element')
    def verify_element_in_another_element(element1, element2):
        soft_assert(element1 in element2)
        verify_expectations()
