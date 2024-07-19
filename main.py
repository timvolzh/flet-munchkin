# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import flet as ft
from flet import (
    Container,
    Icon,
    Page,
    Text,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    colors,
    icons,
    margin,
)


def main(page: ft.Page):

    lvl_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    stuff_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    sum_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def level():
        page.title = "Flet counter example"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

        def minus_click(e):
            lvl_number.value = str(int(lvl_number.value) - 1)
            sum_number.value = str(int(sum_number.value) - 1)
            page.update()

        def plus_click(e):
            lvl_number.value = str(int(lvl_number.value) + 1)
            sum_number.value = str(int(sum_number.value) + 1)
            page.update()

        row = (
            ft.Row(
                [
                    ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                    lvl_number,
                    ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )
        return row

    def stuff():
        page.title = "Flet counter example"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

        def minus_click(e):
            stuff_number.value = str(int(stuff_number.value) - 1)
            sum_number.value = str(int(sum_number.value) - 1)
            page.update()

        def plus_click(e):
            stuff_number.value = str(int(stuff_number.value) + 1)
            sum_number.value = str(int(sum_number.value) + 1)
            page.update()

        row = (
            ft.Row(
                [
                    ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                    stuff_number,
                    ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )
        return row

    page.add(ft.Row([ft.Text("Сила")], alignment=ft.MainAxisAlignment.CENTER))
    page.add(ft.Row([sum_number], alignment=ft.MainAxisAlignment.CENTER))
    page.add(ft.Row([ft.Text("Уровень")], alignment=ft.MainAxisAlignment.CENTER))
    page.add(level())
    page.add(ft.Row([ft.Text("Шмотки")], alignment=ft.MainAxisAlignment.CENTER))
    page.add(stuff())


if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER)

