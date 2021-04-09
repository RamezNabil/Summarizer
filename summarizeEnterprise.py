from kivy.app import App
from kivy.uix.widget import Widget                       #used to work with box layout
from kivy.properties import StringProperty, ObjectProperty               #used to pass link the elements in the .kv file to the attributes in the code
from kivy.lang import Builder                            #used to work with builder and apply any design file
from kivy.core.window import Window                      #used to change the color of the back ground
from kivy.uix.screenmanager import ScreenManager, Screen #used to apply multiple screens
from webScraping import ReadFromWebSite
from ReadDocument import ReadingFromPDF

# building different pages
running_app = App.get_running_app()

class MainPage(Screen):
    pass

myText = ""
class TextPage(Screen):

    def __init__(self, text="", type_id=None, **kwargs):
        super(TextPage, self).__init__(**kwargs)
        self.text = text
        self.type_id = type_id
    ##########################################################

    def test(self):
        print(self.text)
        #self.ids.userWrittenText.text = "Hey we are here"
        self.ids.userWrittenText.text = self.text
        self.ids.userWrittenText.text = myText
    ##########################################################
    def compression_Rate_Picked(self, value):
        self.ids.compression_Ratio_Label_ID.text = value


class FilePage(Screen):

    def selectedFile(self, filePath):
        self.ids.fileSelectedtxt.text = filePath[0]
        layout = self.manager.get_screen('textPage').layout
        print(ReadingFromPDF(filename=filePath[0],f=1,l=4))
        layout.text = ReadingFromPDF(filename=filePath[0],f=1,l=10)


class UrlPage(Screen):
    def UserUrl(self, url):
        self.ids.urltxt.text = url
        layout = self.manager.get_screen('textPage').layout
        layout.text = ReadFromWebSite(WEBSITE=url)
    
    pass

class PageManager(ScreenManager):
    pass

######################################################

# calling and building the design file (GUI)


TheApp = Builder.load_file('summarizeEnterpriseGUI.kv')

######################################################


######################################################
class SummarizeEnterprise(App):

    def Summarize(document):
        model = T5ForConditionalGeneration.from_pretrained('t5-small')
        tokenizer = T5Tokenizer.from_pretrained('t5-small')
        device = torch.device('cpu')
        preprocess_text = document.strip().replace("\n", " ")
        t5_prepared_Text = "summarize: " + preprocess_text
        tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt", max_length=5000, truncation=True).to(device)
        summary_ids = model.generate(tokenized_text,
                                    num_beams=2,
                                    no_repeat_ngram_size=2,
                                    min_length=10,
                                    max_length=100,
                                    early_stopping=False)

        output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return output

    def build(self):
        # setting the color of the background
        Window.clearcolor = (52/255.0, 73/255.0, 94/255.0, 1)
        #####################################################
        #sm = ScreenManager()
        #sm.add_widget(MainPage())
        #sm.add_widget(TextPage(FileName_or_URL="", TypeTextRecieved=0))
        #sm.add_widget(FilePage())
        #sm.add_widget(UrlPage())

        return TheApp#sm

    


if __name__ == '__main__':
    SummarizeEnterprise().run()
