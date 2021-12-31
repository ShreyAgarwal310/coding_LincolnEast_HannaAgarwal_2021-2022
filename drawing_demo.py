import tkinter as tk


class ExampleApp(tk.Tk):

    def __init__(self):

        tk.Tk.__init__(self)

        self.previous_x = self.previous_y = 0

        self.x = self.y = 0

        self.points_recorded = []

        self.canvas = tk.Canvas(

            self, width=400, height=400, bg="black", cursor="cross")

        self.canvas.pack(side="top", fill="both", expand=True)

        self.button_print = tk.Button(

            self, text="Display points", command=self.print_points)

        self.button_print.pack(side="top", fill="both", expand=True)

        self.button_clear = tk.Button(

            self, text="Clear", command=self.clear_all)

        self.button_clear.pack(side="top", fill="both", expand=True)

        self.canvas.bind("<Motion>", self.tell_me_where_you_are)

        self.canvas.bind("<B1-Motion>", self.draw_from_where_you_are)

    def clear_all(self):
        global closed_points
        self.canvas.delete("all")
        self.points_recorded[:] = closed_points
        self.canvas.create_line(self.points_recorded, fill="yellow")

    def print_points(self):

        if self.points_recorded:
            self.points_recorded.pop()
            self.points_recorded.pop()

        self.canvas.create_line(self.points_recorded, fill="yellow")
        print(self.points_recorded)

        self.points_recorded[:] = []

    def tell_me_where_you_are(self, event):
        self.previous_x = event.x

        self.previous_y = event.y

    def draw_from_where_you_are(self, event):
        global closed_points
        if self.points_recorded:
            self.points_recorded.pop()
            self.points_recorded.pop()

        if ([self.previous_x, self.previous_y] in self.points_recorded):
            closed_index_initial = self.points_recorded.index(
                [self.previous_x, self.previous_y])
            closed_points = self.points_recorded[closed_index_initial + 1:]
            print(
                f"closed: {self.previous_x}, {self.previous_y}, {closed_index_initial}")
            closed_points.append([self.previous_x, self.previous_y])

            # print(closed_points)
            # closed_index_final = closed_points.index(
            #     [self.previous_x, self.previous_y])
            # closed_points = closed_points[:closed_index_final]
            # print(closed_points)

        self.x = event.x

        self.y = event.y

        self.canvas.create_line(self.previous_x, self.previous_y,

                                self.x, self.y, fill="yellow")

        self.points_recorded.append([self.previous_x, self.previous_y])

        # self.points_recorded.append(self.previous_y)
        self.points_recorded.append(self.x)
        self.points_recorded.append(self.x)
        self.previous_x = self.x

        self.previous_y = self.y


if __name__ == "__main__":

    app = ExampleApp()

    app.mainloop()
