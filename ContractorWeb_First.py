from nicegui import ui, app


app.native.window_args['resizable'] = False
app.native.start_args['debug'] = True



with ui.card().classes('w-[740px] h-[520px]'):
    ui.label('ContractorWeb')














ui.run(native=True, window_size=(800, 600), title='ContractorWEB', fullscreen=False)