import flet as ft

def main(page: ft.Page):
    page.title = "Contact Page"
    
    # Use a sample logo URL
    logo_url = "https://via.placeholder.com/200"
    logo = ft.Image(src=logo_url, width=200, height=200)
    
    # Create WhatsApp button with icon
    whatsapp_button = ft.ElevatedButton(
        text="Contact on WhatsApp",
        icon=ft.icons.MESSAGE,
        on_click=lambda e: page.launch_url("https://wa.me/60168687563")
    )
    
    # Create Facebook button with icon
    facebook_button = ft.ElevatedButton(
        text="Visit Facebook Profile",
        icon=ft.icons.FACEBOOK,
        on_click=lambda e: page.launch_url("https://www.facebook.com/CPLUSCARSPA")
    )
    
    # Add components to the page
    page.add(
        ft.Column(
            [
                logo,
                ft.Text("C-Plus"),
                whatsapp_button,
                facebook_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

# Run the app
ft.app(target=main)
