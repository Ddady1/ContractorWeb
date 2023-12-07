from nicegui import ui


with ui.column().classes("w-full items-center"):
    with ui.tabs().classes("w-full items-center") as configs:
        a_tab = ui.tab("A")
        b_tab = ui.tab("B")
        c_tab = ui.tab("C")
with ui.column().classes("w-full items-center"):
    with ui.tab_panels(configs, value=a_tab).classes("column items-center justify-center"):
        with ui.tab_panel(a_tab):
            ui.card().style("min-height: 600px").style("min-width: 700px")
            #ui.button('Next', on_click=ui.tab_panels(configs, value=b_tab).classes("column items-center justify-center"))
        with ui.tab_panel(b_tab):
            ui.card().style("min-height: 500px").style("min-width: 500px")
        with ui.tab_panel(c_tab):
            ui.card().style("min-height: 700px").style("min-width: 600px")

ui.run(dark=True)