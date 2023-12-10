from nicegui import ui, app


app.native.window_args['resizable'] = False
app.native.start_args['debug'] = True
text_color = '#104E8B'
crd = ui.card().classes('w-[740px] h-[520px]')

def card_first(crd_1):

    #crd_1 = ui.card().classes('w-[740px] h-[520px]')
    with crd_1:
        ui.label('ContractorWeb').style(f'color: {text_color}; font-size: 40px; font-family: Verdana, Sans-serif')
        ui.separator()
        contract_first_info = '''ContractorWeb is a Python web application which let you organize in one place\n
            all your contracts information and will notify you when it\'s time to renew it.\n
            Please be advise that you need some pre-installation depends on the DB you\'ll choose.'''
        ui.label(contract_first_info).style(f'color: {text_color};font-size: 20px;font-family: Verdana, Sans-serif')
        ui.button('Next', on_click=lambda: (crd_1.delete()))




def card_second(crd_2):

    with crd_2:
        ui.label('Database selection').style(f'color: {text_color}; font-size: 40px; font-family: Verdana, Sans-serif')
        ui.separator()
        db_info = 'Please select your preferred Database to work with\n' \
                  'Please be advise that each DB needs it\'s pre-settings in order to work.'
        ui.label(db_info).style(f'color: {text_color};font-size: 20px;font-family: Verdana, Sans-serif')
        ui.button('Next', on_click=lambda: card_third()).props('inline')
        ui.button('Previous', on_click=lambda: card_first(crd)).props('inline')


def card_third():
    pass


card_first(crd)
card_second(crd)


ui.run(native=True, window_size=(800, 600), title='ContractorWEB', fullscreen=False)