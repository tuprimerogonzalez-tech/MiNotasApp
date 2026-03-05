from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window


class NotasHonor(App):
    def build(self):
        # Color de fondo oscuro estilo Honor
        Window.clearcolor = (0.05, 0.05, 0.05, 1)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

        # Título
        layout.add_widget(
            Label(
                text="MIS NOTAS",
                font_size="24sp",
                bold=True,
                color=(0.34, 0.65, 1, 1),
                size_hint_y=None,
                height=50,
            )
        )

        # Área de escritura
        self.entrada = TextInput(
            hint_text="Escribe algo aquí...",
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(0.34, 0.65, 1, 1),
            font_size="18sp",
        )
        layout.add_widget(self.entrada)

        # Botón Guardar
        btn_guardar = Button(
            text="GUARDAR NOTA",
            background_normal="",
            background_color=(0.13, 0.52, 0.92, 1),
            size_hint_y=None,
            height=60,
            bold=True,
        )
        btn_guardar.bind(on_press=self.guardar)
        layout.add_widget(btn_guardar)

        return layout

    def guardar(self, instance):
        texto = self.entrada.text
        if texto:
            with open("notas.txt", "a") as f:
                f.write(texto + "\n---\n")
            self.entrada.text = ""
            print("Nota guardada localmente")


if __name__ == "__main__":
    NotasHonor().run()
