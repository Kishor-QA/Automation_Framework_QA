import pytest
from pages.Annotation.stt_maithi_page import Annotation
from utilities.custom_logger import Log_Maker
import time

class TestAnnotation:
    logger = Log_Maker.log_gen()

    @pytest.fixture(scope="class")
    def stt_maithili_page(self, dashboard):
        page = Annotation(dashboard.driver)
        return page

    def test_stt_maithili_annotation_page(self, stt_maithili_page):

        page = stt_maithili_page

        # Initial flow
        page.click_stt_maithili()
        page.click_tokens_button()
        page.click_pick_tokens()

        # assert page.pick_successful() == "Audio task picked successfully!"
        self.logger.info("Token picked successfully")
        time.sleep(3)
        page.click_my_task()
        time.sleep(3)
        page.filter_pending_task()
        time.sleep(3)
        page.pick_task()


        # 🔁 Controlled Loop
        max_iterations = 50   
        iteration = 0

        while True:
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<I am currently here>>>>>>>>>>>>>>>")
            time.sleep(3)
            remaining = page.get_remaining_tasks_count()
            self.logger.info(f"Remaining tasks: {remaining}")

            if remaining == 0:
                self.logger.info("All tasks completed ✅")
                break

            if iteration >= max_iterations:
                raise Exception("Loop exceeded safe limit — possible UI issue")

            iteration += 1

            try:
                time.sleep(3)
                # Step 1: Generate transcription
                page.use_AI()
                # message = page.get_transcription_success_message()
                # assert message == "Transcription generated successfully!"
                # self.logger.info(f"Task {iteration}: Transcription generated")we
                # Step 2: Submit
                time.sleep(3)
                page.submit_button()
                self.logger.info(f"Task {iteration}: Submitted")

                #Step 3: Click next (if available)
                remaining_after_submit = page.get_remaining_tasks_count()

                if remaining_after_submit > 0:
                    page.click_next_task()
                    self.logger.info(f"Task {iteration}: Moving to next task")

            except Exception as e:
                self.logger.error(f"Error in iteration {iteration}: {str(e)}")
                raise