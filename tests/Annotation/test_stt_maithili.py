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

        total_pick = 500
        picked = 0

        # Initial flow
        page.click_stt_maithili()
        page.click_tokens_button()

        # 🔁 Pick tokens first
        while picked < total_pick:
            try:
                page.click_pick_tokens()
                time.sleep(2)
                picked += 1
                self.logger.info(f"Picked token {picked}")
            except Exception as e:
                self.logger.warning(f"Stopped picking at {picked}: {e}")
                break

        self.logger.info("Token picking completed")

        # 👉 Now move forward
        page.click_my_task()
        time.sleep(2)
        page.filter_pending_task()
        time.sleep(2)
        page.pick_task()
        time.sleep(2)

        iteration = 0
        max_iterations = 500

        while True:
            time.sleep(3)
            remaining = page.get_remaining_tasks_count()
            self.logger.info(f"Remaining: {remaining}")

            if remaining == 0:
                self.logger.info("All tasks completed ✅")
                break

            if iteration >= max_iterations:
                self.logger.warning("Stopped due to max iteration limit")
                break

            iteration += 1

            # 👉 Perform task
            time.sleep(3)
            page.use_AI()
            time.sleep(3)
            page.submit_button()
            time.sleep(3)

            if page.get_remaining_tasks_count() > 0:
                page.click_next_task()