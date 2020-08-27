import sys


class BatallasCriaturas:

    def __init__(self, entrenador, rivales):
        self.entrenador = entrenador
        self.rivales = rivales
        self.invicto = True
        self.victorias = 0

    def batalla_entrenadores(self):
        print(f"¡Te enfrentas contra {self.rival.nombre}!")
        print("Preparado...\nListo!\nYa!\n")
        j1 = 0
        j2 = 0
        # Ese 2 es luego 6
        while j1 < 6 and j2 < 6:
            self.batalla_criaturas(self.entrenador.bolsillo[j1], self.rival.bolsillo[j2])
            if self.entrenador.bolsillo[j1].hp == 0:
                j1 += 1
                print("Tu criatura perdió esta\n")                
            elif self.rival.bolsillo[j2].hp == 0:
                j2 += 1
                print("El rival va en su criatura número", j2)
                print("Tu criatura ganó esta\n")
            print("<"*15,">"*15)
            if j2 == 5 and self.rival.bolsillo[j2].hp == 0:
                break
        if j1 == 6: # este tambiene debe ser un 6
            self.invicto = False

    def batalla_criaturas(self, criatura1, criatura2):
        while criatura1.hp > 0 or criatura2.hp > 0:
            criatura1, criatura2 = self.atacar(criatura1, criatura2)
            if criatura2.hp  == 0:
                print(f"¡{criatura2.nombre} fue derrotado!")
                break
            print()
            criatura2, criatura1 = self.atacar(criatura2, criatura1)
            if criatura1.hp  == 0:
                print(f"¡{criatura1.nombre} fue derrotado!")
                break
            print()

    def atacar(self, criatura1, criatura2):
        print(f"{criatura1.nombre} ataca a {criatura2.nombre}", end=" ")
        print(f"con su poder de tipo {criatura1.tipo}")
        if criatura1.preferencia_combate() == "Fisico":
            dano = max(criatura1.atk*1.5 - criatura2.defense, 5)
        else:
            dano = max(criatura1.sp_atk*1.5 - criatura2.defense, 5)

        print(f"El ataque fue de {dano}")
        criatura2.recibir_ataque(dano)
        print(f"{criatura2.nombre} tiene {criatura2.hp} de vida")
        return criatura1, criatura2

    def ejecutar_simulación(self):
        try:
            print(f"Tus criaturas son\n{[x.nombre for x in self.entrenador.bolsillo]}")
        except AttributeError:
            print("Ocurrió un error, revisa que todas las clases estén completas")
            sys.exit()

        while len(self.rivales) > 0:
            self.rival = self.rivales.pop(0)
            self.batalla_entrenadores()
            if self.invicto == False:
                print(f"Has perdido valiente entrenador {self.entrenador.nombre}")
                print("¡Pero has completado la actividad!")
                print([x.nombre for x in self.entrenador.bolsillo])
                break
            else:
                print(f"¡Has ganado valiente entrenador!")
                print(f"Ahora cobrarás tu recompensa, con una criatura enemiga\n\n")
                self.victorias += 1
                self.entrenador.bolsillo + self.rival.bolsillo
                print(f"Tus criaturas ahora son\n{[x.nombre for x in self.entrenador.bolsillo]}")
                print("-"*40)
            try:
                for x in self.entrenador.bolsillo:
                        x.hp = x.hp_base
            except (AttributeError, NameError):
                print("Ocurrió un error, revisa que la property hp esté bien definida")
                sys.exit()

        estrellas = self.entrenador.bolsillo.cantidad_criaturas_estrella()
        print(f"Tu cantidad de criaturas estrella fue: {estrellas}")
        print(f"Cantidad de victorias es igual a {self.victorias}")

        if self.invicto == True:
            print("¡Ganaste todas las peleas! ¡Eres el campeon de la Liga Sinnoh!")
        print("¡Éxito programador! ¡Haz completado la actividad!")
