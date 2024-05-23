import streamlit as st 
import pandas as pd 
import streamlit.components.v1 as components
import openpyxl
import psycopg2

#Base de datos
conn = psycopg2.connect(
                        host="dpg-cokdc7gl5elc73c3klp0-a.oregon-postgres.render.com",
                        database="bajacaltec_ciencia",
                        user="bajacaltec_ciencia_user",
                        password="QnVGnpcQGxEr7q9W3YDiPS4ABxSTkAVn"
                    )


st.sidebar.caption('By Baja Caltec')

Desactivar=False
#from streamlit_lottie import st_lottie
contra = st.sidebar.text_input('Contraseña', type='password')
falcho=False
ingresar=st.sidebar.toggle('Ingresar',disabled=Desactivar)

usuarios = ('2089', '234')
#key=st.sidebar.text_input('Poner API key gemini')

if ingresar ==True and contra in usuarios:
    st.subheader('Metodología de la investigación I')
    tab1,tab2,tab3=st.tabs(['Presentación','Encuesta','Historia'])
    with tab1:
        st.subheader('Docentes')
        col1,col2=st.columns(2)
        with col1:
            st.image('Imagenes/Foto alonso.PNG',width=100)
            st.markdown('')
            st.caption('Dr. Fernando A. Núñez Moreno')
            st.caption('Cirujano General, MSc y doctorando por la universidad de Oldenburg')
        
        with col2:
            st.image('data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxISEhUSEhIVFRUXFRcVFRUVFRUVFRUWFRUWFhcXFRUYHSggGBolGxUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OGhAQGysfHR8tLS0tLi0tLS0vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKy0tLS0tK//AABEIAMIBAwMBIgACEQEDEQH/xAAcAAAABwEBAAAAAAAAAAAAAAAAAQIDBAUGBwj/xAA8EAABAwIEAwYDBgUEAwEAAAABAAIRAyEEBRIxQVFhBhMicYGRMqGxB0JSwdHwFCNikuEzgrLxFVOiQ//EABkBAAMBAQEAAAAAAAAAAAAAAAABAgMEBf/EACcRAQEAAgEEAgIBBQEAAAAAAAABAhEDBBIhMRNBIlFhMlJx4fEU/9oADAMBAAIRAxEAPwDTI4Vdh81a5lWqB4GbHi6BJt7Kmw/ax+rxU26f6SZH6rDto2h53lxo1ppgwfG0gHwmdrdUxiMzruaWPcS07ggcOsLe0nhzQ4GQRI8ilEA8E+/9wdrC4TPq1NoY1zYFhIn5pDc1qCt3406+NrG0XC3RoMO7W+wSHZfSO9Jn9oT7p+i7axuZ50+uwMe1ogyCJVbC3WYZLRdTdoptDtJ0kCLjZYgBXjZ9FYS1xBBFiLhdBy7E97Sa/mL+fFc+IWr7HVpY9n4XA/3f9KeSeDx9r0hJTpCSQstLNwihOwihGgQAgQl6UIRoG9KIhOAIi1MGoRQnC1EWpA3CKE5CSQgEJJCchEQjQNwhCVCNIEgJ5osmwE8zZBUQCh49tx5KeAouYD4fX8lUJXOCbIT5CbIVA1CCWggIHZ/M2U2vp1QdDr2E7iCCOSbzLE0BS7qjLhr1y4fD0B3KtT2Sbwqn1aP1T+C7L0mGXuL+QiB681e8fafKV2faRh6YPKfQkx8lYFKARQsquKZ/aSgCQQ+QYI0xf1Kfy3Om136GMfYSSYgfNOZhlFGsZe2/4m2PrzT+X4FlFulgjiTxPmVX46G6j5/mPc07Hxus38z6LChdExmBp1m6XtnkeI8isbm+VOoPg3afhdz6Hqqws9JyVxatb2RpMFNxDgXk+IcWgbf9rKwncLiHUnB7DBHz6Hoqym4UunQy1JITOW41tamHjyI5HiFJIWK9m4QASoRwg9kwgGrKZ325w1M6KdQvN5LBIng0O4CdyOAssxiO3bg0upOqNqTaXFzBB++2oXTLY+GL+6qY0tuolqItWAwf2jF0l4awBoJAbqJMgWJc2eKvso7c4OvY1O6dyqeEHydt6SlqwbX5akkJ2xuPQpJCR7MoiE4QkkIBCIhLISSEAkokuEUIAoTzBZNwnqYsloqMBRMwG3qpoUfMBYeaqErCE24J5wTZCYNwglQjQFy/MKYqClq8Z4C8Wm54bKSs3gsl0Vm1TiGOh2o3uZnr1WkHNKzQEUUpRREJGEI2hGAjAQQwouaYIVqZYd92nkRspLyQJAk8piVAw+e0C4tcSwgwQ8RB5TsnNhhyznvsUUKVjiO8eW7anRHKSo5XRELDIsy7l9/gdZ3T+pbcQRI2Oy5s4LW9kcW51Msd9yIPQzb0WfJj9nKvNKxP2kdoBRYMO0nU8TU0mCGcG6uGq/oDzW4qPDQSdgCT6XXG8BqzHGmtVEMEPLBMf0NvvxPos/XmtcZ3WSKzA9nsRWHefCD8IduR5cAnafY+qfiIaB6+y6k3CtASKuHHJc95s69DHpuORyfHdnCzZ/vZUtVhbZ23MbLp+b0wbFo9QsnnuHDWbbrTj5rvVZ83T463PDR/Zh2meXDA1bgNJouO4DRPdnnaSPIro7gvOeExTqVRlRhhzHBzT1Bm/RejGO1NaeYBt1ErbOargIKTCcISYUHsghJIThCSQgiEIS4RQgBCdpiybTtPZAKAUfHDw+qkpnGjweycCrcE2QnSE2UwbhBKQQGawGDdVeKbeO/QDcldEpUw0Bo2AAHom8Hl9OkIY0DmeJ8ypJCeWWyk0QglFABQYIwjAQhMImZGuADRDT+IHc+Vwsbm1Vz6pL2aHWDh1A3+i2WdYl1Ki57PiECeUmJWGqvLiXOMkmSTzWvHPtNJCn5FTpOqhtYSHCBcjxWifooSs+z2XNrVDqdAaAYG7v8AFleXomnp5NQbtSb63+qlsYAIAAHICEuqQBJ2FyqPMe0VNghnjd7NHmsNWqWGa1GtpP1OiWuA8yCLDiucdj8M6mxwDC5+q9wBYC08f8qdjsc+s7U908hwHkFY4QaqLG6i0tnbTqAJJ8MjY2ueoRnjrHy04blcvxSnZlUpgl9CQBJ0vBIAFzBA4KuHaB1aRSphkcahuZEghtrRxR0sFrfpaXP3DpdrhvHU4bWtHVV2a4YmtJ4WcLbDaDtInY2WHiT+XbjhyWezeYuq6dVSo2d4EAf8fzWZzKq58tf8MCCBcHn1C2D8JLNHdPc2IgU2XG/xyB81UYnA920yIPLeBtHVEuj+PKzywRwrnPFMCXOIa3qXHSPmV6Ow9HQxrTctaGzzgALg2BaRiO9a3UadQVGtJgEsIdJ57LvGBxPe0qdWI1sa6OUgGPTZb3LbhywuM39DckJ1ybKSCURSoRJgUIiEqEUJAAE5SSE5SSBaZxY8B/fFPgJvEjwnyTCoKQQnCkFMEQgjIQQFrXznDsEmo09G+I/JR8tzpteqWNaQ0NJk7yCBt6rE6VoOxlP+Y88mR7kfotLhJEytVCMJUIELNSofn9JtR1N+ppaYmJB9lZYXE06glj2u8j+Sqs27PNrEvadLzv8Ahd5jgqN+R4mmZa0mOLD+yq1KndbPGUA+m9p4tI+S54FMqZniWyx1R4tBBsfmoQWmE0VpQVjkWCfUq+B4bohxPGJ4BVgKfwOLdTqNc3mPUTcJ5eg6IUw/CsO7GnzAKfKJYLRW5bRH/wCTP7QqnHMpBjjUa0hpJ8QEC5vfZaEBUOZ4Vrg8HnPsZhRna6elsmVV1FzjTa7WabZ1EDS0QRZt9uBWWx2BpNeXfxZl3xN12jly9d1scJhqjXF7u7cbaNbC5tMAkmGzBJtfooub4mo5vxM4y0Uqek6jJEaZ5cVnPTt3bf8AavyzGhvhZsbQNp5+qqs1rlxMqVleGZROtxMTq08BHIcL8FTZzjhcA3JU/arnqeUfL6I1kgSYn8vour5Ewtw1IH8APvf81k+wuQU61I1qmqS8tADoDmtAkH1nbkt2WgQAIAsAOA5LbHGy7cHNyzLGYw25JISnJKtzCKSUookAlBGUIQACcpJCXS3SBxIrjwu8iloVBY+RTKqUpJSkRQZsoIyEaAypWx7KYTRS1nd5n/aLD8/dZjLcEa1RrBxuTyaNyugNphoAFgBAHQLXkv0mDQQRrJQIwUSCAJ7A6zmg+YBUTEZNh370wDzb4fopoKOUbDO1uygJllQgciJ+cp7AdmWMcHPcXxcCIEjnzV4CjBT7qWoNCEExiMSG8p+SeOFyuoLlJ7SIWUz2uQ4uG33hy5HyRNxfeOe2q515bYkQObeRVbnlWpSdTqA6mGW38tj53XTj00uN3/xn82WOcuK2weYNe2dQB4yqzOcfTYLuHNVOeYVjKNTE06hpwATSNxqJDYYRcAk9YWHx4rEg1A6HfCS4OB8iPpuuXPpssfbu4+rmXpaZvnhqGGWaFUCoSUj+GI3QqsIaYUSSelZZZX27p2TFP+Dod0dTe7F9pcbvkcDqJVo5cs7HZ4/CNFIgFrvEWk7AQARym9+i31DtHhn/AH9J5OaR89vmtcuOxx72sCEkhLY8OEtII5ggj5IEKDNEIilkJBQBFBGggCS6W6SlUt0A+ECgjCEqJEUZ3RFCiYQRok9BO7P5Z3LJd8bt+g5K0cgiSt2AQhBGEAEUIyEEAAjAQCMIAKPjKxaBBAJcGybxJ3hSFW5gC7w83Bo9TErXi4+6/wARGeXamVspxQMBzXX3DtJI8iCAUx/41msU6rq1NzvhksLXdGuAiehUqtUp1AKWKcaVWn8NSdOofia7a8BRKodUph1erUdS16aWhg7x5ExUMSeB/e+9pSRHrdn6WtzWPeXtuabtLXOHNjog/u4UHO8qf3BLTrZu10Q5hH3Xt4HgrBmGZIa+k8vBID9NX+a0CQW6njS6OEFO5IzD1HBppEy0mXUywEg3IJcee3REysOyVzOs490+lBexwhzOIBN7nluIv7Kip0SxrmVdTmmQJJ0yDDXj8O266J2kyptCt4JAIDh0BJESd4j6KpflwBlsAE+IR4JPEN5HotZ+TOzXpkKFJuxk8ibe/JTaWEHdvrugMpg6ZEh1SDpEfevwU/G5MWvbOltNzg0ltgJMTBuo1QHFvADS3DsGmnTvcfid/Ufkub/z9ue/p03qLlhr7QMlovcXVXTdtyea0jKVgUt9AMYWgaQGmw6CVIwdKWCeI6LeYsNlUSWmQSOMgkfRWNPOqtOJOscnfruq8US30vwuEK12SBIEGf35ouEs8l3NphsQ2o0OaQefMHkeRSyFiaGLdRc6q28AOI/EOI9YK1+Axja1MVG7HcHdp4g9VycnH2tJdnUEZRLNQJTN0lG3dASEYRIwhCjqC58z9UhOYn4neZTKFhKNJJQRsNGilBGEAEYRBBAKlEgUAgDhGklAFACq6Aq7FSBI4EOHUtMqbVO3uoOOcWtJiY9V6PTYScVt+3Jy5b5JP0vcdiX1GB1KkytTe3YkBzSZHG3/AEomBzIUaYoVpp1GtgFzS5puYcNO49RsoNKph6csbiazXT4nt/0yeMADbr81JwtKlSDqjKzKlRw/1KrxYLGt4i4zMmw4/wAUXOAMNayo2+mLQQBefdVnZagX1gCXaacvs6Ijb3MTG6fxuYsZTdRpv7ypULjUeBA8VnEehiyz2LzqpQpnRUfrLjIDjpaJMAx0TmNp2tB2nxpqP7loaQDdxLRDjMjUTEbeqfyXJsO8FrqpqPa0ay1w0iZgN/FF77LHte6o0lxlxEz1N+KVh3+Gff8ANXMbpNpHa5+gFjXyGvkO/EGuke8JmiwNIMC43H76KRmWG1mnq5EO9LXUbCslrRxAI89J/wAKqmJ1XYgfhKLLyCwWTlMgtkGZafomsF8MQmD+LoAtkbprDMmkZPA+yks2/wClHqu0MffyTJXVarnBrG7vA1Hk1tz9f3KtOzuYOp1C2B3bnNb1H3Q71JVFlNeRvtqL3bANDjDQTzgT0HVLJDmWaW0wZLyY1kceZHRZ5Y908ql1XSnBEqns7m4rs0kOD2C5cI1DbUPlPmrZcNmrprLsEYRIBI0pBBAJyIUeOtUd5/kFHlSszH8w+Q+iiFJZJKCBQQGmlGElKCACNEggAlBJRoAykhGid0RAbebnyUWu8CwKlEDQXEXgk+gVNVxIi5A9V7OE7cZHnX8srSMwZ4JEAjjaFnatXVaYPATHsVc1MW0yNVvl9Vnsyoi8c5BF4PTl5LLN0YIuXYsmsGk30PE87tA89/krCvgyWuA4bWAMj3WVZV0d5zAOnpqM/UFanLc6o1WatQYYu18AjyJ38ws5V2HMugtuSjq04EXjzVdSxZ1Dun0ywOOvxNIg3gXsVZYrFUo+ME7eG/0CcoMYpx7owdiz2JAN/QJo0H94wtdpaHy4fja4bH1Qe41G1I2DLG4mL+yVr1NBH4foi+S9HMJU0l7J2JjyNxHun63hFjG3tZQsSIe14jxC9uX+ISTj9I01LDZrgCQRyIGxCDW9BgAvznhxUHOTDTw8zwTNfHA0nNbUDXEWcGutyOyrMyzmkWhpqy6ACQx1zz2RchIRkrQ5mmJHeCRw+ImOuxPstLiwIG08Oiz/AGWxFItIBLnSTAB4m3rC0jZO7Y6E39U8fRX2YwuINCo14uBOsfingFqMrzFlduptiDBadxy9FnMRhA65/RMYKqcPUD2gkbObO4/VY8vHvyrHJtkEzhsQ2o0PaZB/cHkU4uTTVLlBIabJQVIVGbf6n+0KFKm50PEPL81XpaVPQ56oIoQS0bTI0QQlLQGEYKJGEAaNEjVgEcI1ie1P2h0cMXU6LRWqCZMxTaRuC4fEeg90tbDXYwxSef6TA6ws/hKU3c0ewV/i67RhzUeYGgHjuQIAAuSTYAXJWdbmDoltMgm/jif7RP1Xp8nJhxyd1cnFx557mM2dxIIOwAjiQPVQK7abrPc3jt++iM1KziS5wM/0x+ah4rAucZ28rLky6vj/AG7Mej5P0xeakd85oMghoHv+il4XBstqA8r3Uuv2Zf3heHjyj80KmW1xs0O9lM58LfZ5dPyT6Sstw9JnwtaONtypmKxMW+l1WYPBVp8VKP30R1MrxR+FgA6kRHkFp82EnuM5w536p6pjmtBBm7SInjEfmnsC+abeQNz0I69YUJvZyvudIPmfpCt8PgHtZpgF0b8JGyU6jj/ar0/J/bUHEHVTEXIP0B/QKNSxMtIABPK8q1wuRFrqjtfxv1Ry22Vtl+VMp3a0Sd3G591ln1WE9eWuPSZ334UeByOrUu/wN5feI/JFmORYWodLmubB3Y4/nIK14ZYyeCzZxEuPhmD6wuTPmzyu9uzj4MMZrQsu7LYdjP5VepxnxAE+ZaAVKFNzTDrhv3lGxOHFRhNJ5Y/mN5/qB3WUZ2lr4V7qVZof1m5B+R+S04uXk+rtny8PFrzNNfXx7AYJvty+qafjmciTy2B8yqhuaYPF036i8OLYbpa4PaRNmu2PDpZRMBitFFjal3AXduSRtc7laZ9Tnr+WePTce/4/yv8AJs1fSrBpA7t7g1wn4ZsHelp6LbrlJxYe2Ra5C3PZHMzWolrzL6Z0k8S0jwk9dx6LPHO5Xynl4pj5xaVuwRhJp7BKBWjlVWdfE09Cq1WmdD4T5/ksZ2u7QfwrA1kGo8HTOzQPvH8h+iFRfyguLV8ZUe4uc9xcTJJcboJ6N6QQKTKVKSQCOUmUYSMsJQSAlhMmG+0ztC6iwYak7S6oJe4WIZtpB4T9PNcgrmx8itl9pNQnG1J4aQPQALHVFpJ4OO8srd9H4KYDGjm5rdL3ecy0eR5oqlILPdhM1FXDRPiY6HjjLvESfMlxWiD1y8tuWd27+GY48c0IUggaAKj4jEwmDj4WfZGkzqcMIEBhh0VVVzM81Gdm5HFTcIuclaJtBqcbSb0WVOdHmjGc9UdsPvas02ou6Z5rH187aN3/ADTFPtR/62l0cRt7myc49+kXl17bsYdvJG6mAsTQ7ZkPIqt0jzlSsZ2vpxvPldX8VnuM/mlWmd4zS0tYJJ4rO0y9viN28W/eHUcwqfNu1jnQGBrL21CSSYueQG6Nucl1IFr21H6jFNsl5a2AHOEcTNhNh1TvFlrYx58d6qbjsa0A1WuAgb8+hCx1Voq1DVqusefGOHorGhlFSvW016zKGsOqQfE63xN0W0vFjDiDfzVVmlJlOqWsLnU58BqQCW2+KLTKvDiuM2zz5pldLalidQ04emTaJ+Fo9ShSwumHVn6uTQbDzPFNYbHPc3SzS0DjP5BN1atJt3PNR0bGzfYbqLFyxIrYoDhA+q2X2bS5tepwLmNHm0En/kFy/F4wvd0XSfs7zCcL3YsWPdqjjq8Qcfp/tWmOOnPyZ78Oh0tkqVUU6ro3PuhqVuY7nVRultxvzHJcq7ZZfXrYkvpsLmBjWggjhJMSZ3K6DnPwDzVJKe1RzQ5bW/8AU/8AtKC6XKCNm6AhIVJqRpFpc6xzHuEO9b+Ie4VPKEoGlx37fxBKGJZ+JU0pQcgaYL7RsuecQ6s1ssdHiHPS31F5WDfTK7pi6LajS1wkFYfN+y8GWCQqmQ9Kv7PXvZVqujwFgDueoOlsf/XutpUzE8AVU5Dgu7Y5sQdV/wC0H8yrECFjlfyrs45+EUmY5liNXhaI8/8ACrKuY4r8I+a02IpSozsNPBG4clZs4/E8QPcpqri6x4D5rQ1MH0Ud2B6KfB6rNvr1+EI6VZ/3w4+To+UfmtD/AOP6I25f0TmWvorhb9qdlSgdwWn+oE/O6YrteB4ahLTydIV9UywHgo//AIPlbyWs5oxy4araTSdJ/pg9YCW+nAVthcjeCATb9VIxOQ2V/NETirK1WwQSBtAJE8UwXvaZa4t4S06T7hXGPyx7RzGyi0cC6CTxEfNX880U4rtT1iXm5Lidy52qeW6n1qjBT7t3iIFiOBTNfBFpKZbT91Hybng7x+fJ+k+bOJA4WH6JLsvBuHSpVCraHBDu2nZY7raSVCZhLrY9gWFlR44Fl/MER9SqbCYeStj2dwfdgui5+iNozkkaWi6yXqUei6yXqVueo+bn+X6hURKus0P8sqinqkeMKQSf4imPvt/uCCx+XL9OudPj/dGpKARoLdygjQQQASkEEAZTFYIIKacVbh/Mf6f8QmX7oIKeT+p1cP8ARCXJARoKWgHZNwggppjATjAggkZTgiYEEEEkhKqIkE4mqXM9iqsbIIJ30Ih1BuqWtuggrwRmlM2SG7oIISvMnFz6LZYfZEgmzzS6ScRIK2FMZl8BWdrHwnyP0QQQqMRWu4zzQQQTaP/Z',width=200)
            st.caption('Dr. Edgar Santos Marcial')
            st.caption('Neurocirujano, Dr. Med, MSc, SNI III  ')
        st.markdown('_____')
        with st.expander('Ejes del curso'):
            sol1,sol2,sol3=st.columns(3)
            with sol1:
                st.info('Teoría')
                st.write('Temario institucional')
                st.write('Teoría del desarollo de un anteproyecto')
            with sol2:
                st.info('Pensamiento crítico')
                st.write('Características del pensamiento crítico')
                st.write('Barreras del pensamiento crítico')
                st.write('Conceptos de lógica básica')
                st.write('Fallas lógicas')
                st.write('Razonamiento inductivo')
                st.write('Ciencia y pseudociencia')
            with sol3:
                st.info('Anteproyecto')
                st.write('Elaboración de un anteproyecto de investigación')
        with st.expander('Temario'):
            df_tem={'Tema':['Historía de la ciencia']}
            df_temario=pd.read_excel('xlsx/Temario.xlsx')
            st.dataframe(df_temario,hide_index=True)
        with st.expander('Calificación'):
            df_calif=pd.read_excel('xlsx/Calificación df.xlsx',sheet_name='Sheet1')
            st.dataframe(df_calif,hide_index=True,width=600)
            df_crit=pd.read_excel('xlsx/Calificación df.xlsx',sheet_name='Sheet2')
            st.dataframe(df_crit,hide_index=True)
        
    with tab2:
        with st.form('Datos anónimos'):

            col1,col2=st.columns(2)

            with col1:
                    st.title('Encuesta')
                    edad=st.number_input('Edad',step=1)
                    género=st.radio('Género',['Femenino','Masculino'])
                    aborto=st.selectbox('¿Estás a favor o en contra del aborto?',['A favor','En contra'])
                    pena=st.selectbox('¿Estarías a favor de la pena de muerte en México en el caso de narcotraficantes?',['Si','No'])
                    qx1=st.selectbox('¿Qué consideras que es lo más importante para evitar infecciones en el quirófano',['Lavado de manos','Botas qurúrgicas','Mantener técnica esteril','Lavado de instrumental'])
                    qx2=st.selectbox('¿Estas de acuerdo con la siguiente oración?:El uso de cepillos quirúrgicos es necesario para un correcto lavado quirúrgico de manos',['Si','No'])
            with col2:
                    prob=st.selectbox('¿Crees que es más peligroso lanzarse de un paracaidas qué estar hospitalizado?',['Si','No'])
                    saber1=st.selectbox('¿Sabes por que el cielo es de color azul?',['Si','No','No sé'])
                    saber2=st.radio('Sabes por que suceden las mareas y su relación con la luna?',['Si','No'])
                    st.text_input('Si tu, respuesta es afirmativa, explica ¿por que?')
                    protocolo=st.selectbox('Si, tuvieras la oportunidad de hacer un proyecto de investigación, en cual de las siguientes áreas te gustaría realizarlo?',['Neurocirugía','Cirugía general','Urología','Manejo de la sala quirúrgica'])
                    bot_enviar=st.form_submit_button('Enviar')
                    # Conectarse a la base de datos Postgres
                    

                    # Crear un cursor para ejecutar sentencias SQL
                    cursor = conn.cursor()

                    # Insertar datos en la tabla
                    if bot_enviar:
                        creat='''CREATE TABLE IF NOT EXISTS encuestas (
                        id SERIAL PRIMARY KEY,
                        edad INTEGER NOT NULL,
                        genero VARCHAR(255) NOT NULL,
                        aborto VARCHAR(255) NOT NULL,
                        pena_muerte VARCHAR(255) NOT NULL,
                        qx1 VARCHAR(255) NOT NULL,
                        qx2 VARCHAR(255) NOT NULL,
                        paracaidas VARCHAR(255) NOT NULL,
                        saber1 VARCHAR(255) NOT NULL,
                        saber2 VARCHAR(255) NOT NULL,
                        saber2_explicacion TEXT,
                        protocolo VARCHAR(255) NOT NULL
                            )
                            '''
                        cursor.execute(creat)
                        cursor.execute("""
                            INSERT INTO encuestas (
                                edad, genero, aborto, pena_muerte, qx1, qx2, paracaidas, saber1, saber2, protocolo
                            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """, (
                            edad,
                            género,
                            aborto,
                            pena,
                            qx1,
                            qx2,
                            prob,
                            saber1,
                            saber2,
                            protocolo
                        ))

                        # Guardar los cambios en la base de datos
                        conn.commit()

                        # Mostrar un mensaje de confirmación
                        st.success("¡Datos enviados correctamente!")

                    # Cerrar la conexión a la base de datos
                    conn.close()
                        
    with tab3:
        st.title('Historia del método científico')        
        components.iframe('https://docs.google.com/presentation/d/e/2PACX-1vSe3Fg2NFEl6VES9qmoS4vnmgEp7GTjCYrSH22k9m1afpOcgF2hWv6LKe25I8vQYZq6aRQP3xkQMnSP/embed?start=false&loop=false&delayms=3000',height=500)
        