# import os

# from kivy.config import Config
# from kivy.lang import Builder
from libs.selector import TemplateSelector
from libs.templater import DocxTemplater

# Config.set("graphics", "window_state", "maximized")
#
# from kivy.core.window import Window
#
# Window.minimum_width, Window.minimum_height = (1200, 600)
#
# from kivymd.app import MDApp
#
# from facebook_desktop import FacebookDesktop
#
#
# class FacebookDesktopMain(MDApp):
#     def build(self):
#         self.load_all_kv_strings()
#         return FacebookDesktop()
#
#     def load_all_kv_strings(self):
#         for d, dirs, files in os.walk(self.directory):
#             for f in files:
#                 if os.path.splitext(f)[1] == ".kv":
#                     path = os.path.join(d, f)
#                     with open(path, encoding="utf-8") as kv_file:
#                         Builder.load_string(kv_file.read())
#
#     def on_start(self):
#         self.root.dispatch("on_enter", self.directory)
#

if __name__ == '__main__':
    # FacebookDesktopMain().run()
    doc = DocxTemplater('Шаблоны/Договоры/Трудовой_договор.docx')
    print(doc.undeclared_variables)
    print(doc.path)
    print(doc.absolute)
    print(doc.sub_path)
    print(doc.sub_path in doc.path)
    selector = TemplateSelector()
    print(selector.select_template())
