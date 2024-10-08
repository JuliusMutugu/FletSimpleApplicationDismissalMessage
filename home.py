import flet as ft 

def main(page:ft.Page):
    page.theme_mode = 'light'
    page.window.bgcolor = "#FF56FF"
    # page.width_window = 100
    page.window_width = 400
    page.adaptive = True
    page.appbar = ft.AppBar(
        leading= ft.IconButton(icon=ft.icons.DASHBOARD), 
        title= ft.Text(' This is a simple app ! ', style= ft.TextAlign.CENTER), 
        bgcolor=ft.cupertino_colors.ACTIVE_BLUE,
        
        
    )
    page.navigation_bar = ft.NavigationBar(
        destinations= [
            ft.NavigationBarDestination(label= "home", icon= ft.icons.HOME), 
            ft.NavigationBarDestination(label= "market place", icon= ft.icons.EXPLORE), 
            ft.NavigationBarDestination(label= 'user', icon= ft.icons.VERIFIED_USER_SHARP)
        ],
        bgcolor=ft.colors.BLUE

    )
 

    single_message  = ft.Container(
        bgcolor= ft.colors.PURPLE, 
        padding= ft.padding.all(4), 
        height= page.height / 6 ,
        width= page.width /4 *3 , 
        content=
                ft.Row(
            [
                ft.CircleAvatar(content= ft.Text("J")),
                ft.Card(
                    color = ft.colors.WHITE,
                    adaptive= True,
                    # tooltip = ft.Text("click to view! "), 
                    content= ft.Column(
                        [

                            ft.Text("this is a message to be read"),
                            ft.Text("this is the day that the Lord has made : \n  keep the Faith alive ", style= ft.TextDecoration.NONE ),
                            
                        ]   
                    ),
                    

                    

                    
                )
            ]
        )
        
                                                                                                                                                                                                                                                                               
        
    )
       # this section will be included after clicking the dashboard icon
    side_icons = ft.ListView(
        controls= [
            ft.ExpansionPanelList(
                divider_color = ft.colors.BLACK, 
                expand=True, 
                controls= [ ft.ExpansionPanel(
                    content= single_message,
                    header = ft.IconButton(icon= ft.icons.DASHBOARD),
                    can_tap_header=True, 
                )
                ],
                
            )
        ]
    )
     # this will appear when deleting items
    container_for_delete = ft.Container(
        content= ft.ListTile(
           leading= ft.IconButton(icon= ft.icons.DELETE, icon_color= "#FFFFFF"),
           title= ft.Text("item deleted ! ", color= "#FFFFFF")
        )
     ) 
    
    
    # here the user gets to choose whether or no to delete the item selected.
    def choose_to_delete_item(e):
        print(e)



    # notification after dismissal 
    actions_for_notification = ft.ElevatedButton('yes', data = 1,  on_click= choose_to_delete_item)
    notify_to_delete = ft.AlertDialog(
        modal= True, 
        title=ft.Text("Are you sure you want to delete ? "), 
        actions=[
            actions_for_notification,
            ft.ElevatedButton(
                text= "NO",
                on_click = choose_to_delete_item,
                data = 1
                #onPressed= lambda: notify_to_delete.dismiss()
            )
        ]
    )
    def notify_delete(e):

        page.open(notify_to_delete)


    # the user will be able to dismiss this content 
    dismss_content = ft.Dismissible(
        content= single_message, 
        on_dismiss= notify_delete, 
        dismiss_direction=  ft.DismissDirection.END_TO_START,
        background= ft.Container(
            
            content= container_for_delete, 
            
            bgcolor= ft.colors.RED, 
        )
    )

    messaging_container = ft.GridView(
        # controls= single_message
    )
    page.add(dismss_content)
    

    page.update()
    page.open(notify_to_delete)

ft.app(target=main)    