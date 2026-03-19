from pages.base_page import Basepage
from utilities.read_properties import AnnotationConfig

class Annotation(Basepage):
    Annotation_Page_Url = AnnotationConfig.get_annotation_url
    STT_Maithili_Page = AnnotationConfig.get_locator("STT_Maithili")
    Tokens_Button = AnnotationConfig.get_locator("Tokens_button")
    Pick_Token = AnnotationConfig.get_locator("Pick_Tokens")

    Pick_Tokens_Auto = AnnotationConfig.get_locator("Pick_Tokens_Auto")
    Pending_Task = AnnotationConfig.get_locator("Pending_Task")
    My_Task_Button = AnnotationConfig.get_locator("My_Task_button")
    Pick_Successful = AnnotationConfig.get_locator("Pick_Successful")
    Pick_Task = AnnotationConfig.get_locator("Pick_Task")
    Use_AI_Button = AnnotationConfig.get_locator("Use_AI_Button")
    transcription_success_msg_locator = AnnotationConfig.get_locator("Transcription_Generation_Successful_Message")
    Next_Task_Button = AnnotationConfig.get_locator("Next_Task")
    Submit_Task = AnnotationConfig.get_locator("Submit_Task")
    Pick_Token
    Remaining_Task= AnnotationConfig.get_locator("Remaining_Task")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_stt_maithili(self):
        self.click(self.STT_Maithili_Page)

    def click_tokens_button(self):
        self.click(self.Tokens_Button)

    def click_pick_tokens(self):
        self.click(self.Pick_Token)

    def filter_pending_task(self):
        self.click(self.Pending_Task)

    def click_my_task(self):
        self.click(self.My_Task_Button)

    def pick_successful(self):
        return self.toast_alert(self.Pick_Successful).text

    def pick_task(self):
        self.click(self.Pick_Task)

    def pick_auto_tokens(self):
        self.click(self.Pick_Tokens_Auto)
    
    def use_AI(self):
        self.click(self.Use_AI_Button)

    def get_transcription_success_message(self):
        return self.toast_alert(self.transcription_success_msg_locator).text
    
    def submit_button(self):
        self.click(self.Submit_Task)

    def click_next_task(self):
        self.click(self.Next_Task_Button)

    def get_remaining_tasks_count(self):
        text= self.find_element(self.Remaining_Task).text
        return int(text.split()[0])
    