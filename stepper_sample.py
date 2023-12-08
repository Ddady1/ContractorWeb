from nicegui import ui, app

def checkdb(con):
    print(con)
    if con != 'MySQL':
        return 'set_visibility', 'disable'
    '''else:
        return'''

app.native.window_args['resizable'] = False
app.native.start_args['debug'] = True
with ui.stepper().props('horizontal').classes('w-full items-center') as stepper:
    with ui.step('Choose DB'):
        #db_radio = ui.radio(['MySQL', 'MongoDB-Soon', 'Excel-Soon'], value='MySQL').props('Inline')
        db_radio = ui.radio(['MySQL', 'MongoDB-Soon', 'Excel-Soon']).props('Inline')
        with ui.stepper_navigation():
            #print(db_radio.value)
            #g, c = str(checkdb(db_radio.value))
            #print(g)
            ui.button('Next', on_click=checkdb(db_radio.value))
        print(db_radio.value)

    with ui.step('Ingredients'):
        ui.label('Mix the ingredients')
        with ui.stepper_navigation():
            ui.button('Next', on_click=stepper.next)# example # .props('disable')
            ui.button('Back', on_click=stepper.previous).props('flat')
    with ui.step('Bake'):
        ui.label('Bake for 20 minutes')
        with ui.stepper_navigation():
            ui.button('Done', on_click=lambda: ui.notify(db_radio.value, type='positive', position='center'))
            ui.button('Back', on_click=stepper.previous).props('flat')


ui.run(native=True, window_size=(800, 600), fullscreen=False)