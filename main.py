import flet as ft


def main(page: ft.Page):
    #mudar a cor do beackground
    page.bgcolor = "#fdfcdc"

    product_imagens = ft.Container(
        content=ft.Column(
            #imagem principal
            controls=[
                ft.Image(
                    # src='https://imgs.ponto.com.br/1555947067/1xg.jpg',
                    src='https://www.olhonocarro.com.br/img/carro_hero.webp',
                ),
                #imagens de escolha que ficam em baixo
                ft.Row(
                    controls=[
                        ft.Container(
                            image_src='https://unidas-livre-cms-pictures-prd.s3.sa-east-1.amazonaws.com/LVR_Pag_VW_T_Cross_Comfortline_200_TSI_AT_2024_e6bf0281a3.png',
                            width=100,
                            height=100,
                        )

                    ]
                )
            ]
        )
    )

    product_details = ft.Container()

    layoutprincipal = ft.Container(
        width=900,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color="#00afb9"),
       #radiciona responsividade para aplicação
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=(
                product_imagens,
                product_details
            )

        )

    )


    page.add(layoutprincipal)


if __name__ == '__main__':
    ft.app(target=main)
