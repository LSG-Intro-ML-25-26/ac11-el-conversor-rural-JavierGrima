@namespace
class SpriteKind:
    tradear = SpriteKind.create()
    fondo = SpriteKind.create()

def on_down_pressed():
    animation.run_image_animation(nena,
        assets.animation("""
            nena-animation-down
            """),
        500,
        False)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_right_pressed():
    animation.run_image_animation(nena,
        assets.animation("""
            nena-animation-right
            """),
        500,
        False)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_left_pressed():
    animation.run_image_animation(nena,
        assets.animation("""
            nena-animation-left
            """),
        500,
        False)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_up_pressed():
    animation.run_image_animation(nena,
        assets.animation("""
            nena-animation-up
            """),
        500,
        False)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

nena: Sprite = None
nombre_productos = ["Gallina", "Patatas", "Cabra", "Huevos", "Caballo"]
valor_prodcutos = ["6", "2", "5", "3", "12"]
scene.set_background_image(assets.image("""
    mapa
    """))
nena = sprites.create(assets.image("""
    nena-front
    """), SpriteKind.player)
arbol = sprites.create(assets.image("""
    arbol
    """), SpriteKind.enemy)
arbol2 = sprites.create(assets.image("""
    arbol
    """), SpriteKind.enemy)
arbol3 = sprites.create(assets.image("""
    arbol
    """), SpriteKind.enemy)
casa = sprites.create(assets.image("""
    casa
    """), SpriteKind.enemy)
pez = sprites.create(assets.image("""
    nemo
    """), SpriteKind.enemy)
tiburon = sprites.create(assets.image("""
    tiburon
    """), SpriteKind.enemy)
tronco = sprites.create(assets.image("""
    tronco
    """), SpriteKind.enemy)
casa.set_position(27, 37)
arbol.set_position(34, 92)
arbol2.set_position(81, 65)
arbol3.set_position(135, 87)
pez.set_position(83, 16)
tiburon.set_position(127, 23)
tronco.set_position(145, 9)
controller.move_sprite(nena)
info.set_score(0)

def on_forever():
    if nena.overlaps_with(arbol):
        info.change_score_by(1)
        pause(2000)
forever(on_forever)

def on_forever2():
    if nena.overlaps_with(arbol2):
        info.change_score_by(1)
        pause(2000)
forever(on_forever2)

def on_forever3():
    if nena.overlaps_with(arbol3):
        info.change_score_by(1)
        pause(2000)
forever(on_forever3)
