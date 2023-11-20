import flet as ft


async def main(page: ft.Page):
    async def route_change(e: ft.RouteChangeEvent):
        print("Route change:", e.route)

    page.on_route_change = route_change

    await page.add_async(ft.Text("Hello, World!"))
    

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550)
