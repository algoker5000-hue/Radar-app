from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.camera import Camera
from kivy.clock import Clock

class CardRadarApp(App):
    def build(self):
        # تنظيم الواجهة بشكل عمودي
        self.layout = BoxLayout(orientation='vertical')
        
        # تشغيل كاميرا الجوال
        self.camera = Camera(play=True, resolution=(640, 480))
        self.layout.add_widget(self.camera)
        
        # نص توضيحي يظهر أسفل الكاميرا
        self.label = Label(
            text="رادار الكروت يعمل الآن... وجه الكاميرا نحو الكرت",
            size_hint_y=0.2,
            font_size='20sp'
        )
        self.layout.add_widget(self.label)
        
        return self.layout

if __name__ == '__main__':
    CardRadarApp().run()
