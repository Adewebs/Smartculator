from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class SmartCalculator(App):
    def build(self):
        # you can change calculator logo here

        self.icon = "calculator.png"

        # here are variables for holding values and performing
        # various operations

        self.last_was_operator = None
        self.last_button = None
        self.operators = ["/", "*", "-"]

        #Here you design the total outlook of your calculator
        main_layout = BoxLayout(orientation="vertical")
        # Here is wher you design the calculator
        # output or display look
        self.solution = TextInput(background_color="black", foreground_color="white",
                                  multiline= False, halign="right", font_size=55, readonly= True)

            #I simply add the display screen to my calculator layout
        main_layout.add_widget(self.solution)
        #here is where i place array of numbers to be display on my
        #calculator screen
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"], ]
        # i have to iterated through my arrays
        #then display them like a button on the screen
        for row in buttons:
            h_layout = BoxLayout()
            for items in row:
                button = Button(
                    text= items, font_size=30, background_color="grey",
                    pos_hint={"center_x": 0.5, "center_y": 0.5}
                )
                #here i created a fuction that listen to the click of each button
                button.bind(on_press=self.on_button_press)
                #i adeded each values in the array inside an array of buttons
                h_layout.add_widget(button)
                #here i added the layout to collect the value on the main screen
            main_layout.add_widget(h_layout)
            #here the equal button screen was created
        equal_button = Button(
            text="=", font_size=30, background_color="grey",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
#then i set a function to collect equal sign and carry out the operation
        equal_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ == "__main__":
    app = SmartCalculator()
    app.run()
