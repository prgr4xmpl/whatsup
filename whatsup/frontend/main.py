import flet as ft


async def main(page: ft.Page):
    async def route_change(e: ft.RouteChangeEvent):
        print("Route change:", e.route)

    async def page_resize(e):
        nw = page.window_width
        message_field.width = int(nw * 4 // 5)
        numbers_field.width = int(nw * 4 // 5)
        await page.update_async()

    page.on_route_change = route_change
    page.on_resize = page_resize
    
    message_field = ft.TextField(label="Message", width=page.window_width*4//5, multiline=True)
    numbers_field = ft.TextField(label="Numbers", width=page.window_width*4//5, multiline=True)

    send_message_button = ft.TextButton("Send message", width=120)

    message_and_numbers_container = ft.Container(content=ft.Column(
        controls=[message_field, numbers_field]))

    buttons_column = ft.Column(controls=[send_message_button], horizontal_alignment='end')
    row = ft.Row(controls=[message_and_numbers_container,
                 ft.VerticalDivider(), buttons_column], expand=True)

    await page.add_async(row)


ft.app(target=main)
