import allure


@allure.epic("ACS")
@allure.feature("API")
class TestPipelineCount:

    @allure.title("Verify ACS provides an API endpoint to get count of \"Has Issue\" pipeline runs")
    def test_gid_210419_get_has_issue_pipeline_run_count(self):
        """
        Description:
            Verify ACS provides an API endpoint to get count of "Has Issue" pipeline runs
        Prerequisites:
            ...
        Test Data:
            ...
        Steps:
            1) ...
                ER: ...
                Notes: ...
            2) ...
            3) ...
            4) ...
            5) ...
            6) ...
        Projects: ...
        """

        # ... preparing

        with allure.step("Send a POST request"):
            # Step 1
            # artifact_obj = ...
            # artifact_obj.create_artifacts(test_context)

            # response = request_helper.get(...)

            #testcase_logger.debug(response.json())

            response_json = "{\"key\": \"value\"}"
            allure.attach(response_json, name="response", attachment_type=allure.attachment_type.JSON)

            #request_helper.check_response_code(response, HTTPStatus.OK)

        with allure.step("Get the initial pipeline runs count"):
            # ...
            response_json = "{\"key\": \"value\"}"
            allure.attach(response_json, name="response", attachment_type=allure.attachment_type.JSON)

        with allure.step("Start the pipeline run"):
            # ...
            response_json = "{\"key\": \"value\"}"
            allure.attach(response_json, name="response", attachment_type=allure.attachment_type.JSON)

        with allure.step("Check 'in_progress' increased by 1"):
            # ...
            response_json = "{\"key\": \"value\"}"
            allure.attach(response_json, name="response", attachment_type=allure.attachment_type.JSON)

        with allure.step("Abort the pipeline run"):
            # ...
            response_json = "{\"key\": \"value\"}"
            allure.attach(response_json, name="response", attachment_type=allure.attachment_type.JSON)

        with allure.step("Check 'has_issues' increased by 1"):
            # ...
            response_json = "{\"key\": \"value\"}"
            allure.attach(response_json, name="response", attachment_type=allure.attachment_type.JSON)

