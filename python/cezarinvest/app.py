"""
Application permettant de calculer un intérêt composé
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class ceZarInvest(toga.App):

    def startup(self):
                
        # Créer la boîte de saisie et le bouton "Calculer"
        principal_label = toga.Label('Capital initial : ', 
                                  style=Pack(padding=20, font_size=15))
        self.principal_input = toga.TextInput(style=Pack(flex=1))
        
        month_label = toga.Label('Investissement Mensuel : ', 
                                  style=Pack(padding=20, font_size=15))
        self.month_input = toga.TextInput(style=Pack(flex=1))
        
        rate_label = toga.Label('Taux d\'intérêt : ', 
                                  style=Pack(padding=20, font_size=15))
        self.rate_input = toga.TextInput(style=Pack(flex=1))

        time_label = toga.Label('Période de temps (en années) : ', 
                                  style=Pack(padding=20, font_size=15))
        self.time_input = toga.TextInput(style=Pack(flex=1))
        
        submit_button = toga.Button('Calculer', on_press=self.calculate_interest)

        # Créer la boîte de texte pour afficher le résultat
        self.result_label = toga.Label('', style=Pack(padding=20, font_size=15))

        # Créer la mise en page de l'application
        box = toga.Box(children=[principal_label, # Label pour le capital initial
                                 self.principal_input, # L'input utilisateur pour le capital initial
                                 month_label, # Label pour le montant investi mensuel
                                 self.month_input, # L'input utilisateur pour le montant investi mensuel
                                 rate_label, # Label pour le taux d'intérêt
                                 self.rate_input, # L'input utilisateur pour le taux d'intérêt
                                 time_label, # Label pour la période de temps
                                 self.time_input, # L'input utilisateur pour la période de temps
                                 submit_button, # Bouton pour lancer le calcul
                                 self.result_label], # Réponse
                       style=Pack(direction=COLUMN))

        # Ajouter la mise en page à la fenêtre principale
        self.main_window = toga.MainWindow(title=self.name)
        self.main_window.content = box
        self.main_window.show()

    async def calculate_interest(self, widget):
        principal_input = self.principal_input.value
        capital_base = principal_input
        month_input = self.month_input.value
        rate_input = self.rate_input.value
        time_input = self.time_input.value

        # Vérifier si les saisies sont des nombres
        try:
            principal_input = float(principal_input)
            month_input = float(month_input)
            rate_input = float(rate_input)
            time_input = float(time_input)
        except ValueError:
            self.result_label.text = 'La saisie doit être un nombre'
            return

        # Calculer l'intérêt composé mensuel
        rate_period = rate_input / 100 / 12 # Taux d'intérêt par période
        total_periods = time_input * 12 # Nombre total de périodes d'investissement
        total_interest = 0

        for i in range(int(total_periods)):
            # Calculer les intérêts mensuels
            monthly_interest = (principal_input + month_input * i) * rate_period
            total_interest += monthly_interest

            # Ajouter les intérêts au capital
            principal_input += month_input + monthly_interest

        # Arrondir les résultats à deux décimales
        capital_final = round(principal_input, 2)
        total_interest = round(total_interest, 2)

        # Afficher le résultat
        self.result_label.text = f"""   
        Votre placement initial de {capital_base} €, plus un montant de {month_input} € \n
        versé une fois par mois, à un taux d’intérêt annualisé de {rate_input} % \n
        vaudra {capital_final} € dans 5 ans """

# Pour chaque période mensuelle, on calcule d'abord les intérêts mensuels en multipliant 
# le capital actuel (capital initial + investissement mensuel * nombre de mois déjà investis) par le taux d'intérêt mensuel. 
# On ajoute ensuite les intérêts obtenus au capital actuel pour obtenir le nouveau capital.

# On répète ce processus pour chaque mois de la période d'investissement, en ajoutant les intérêts obtenus à chaque étape 
# pour obtenir le montant total des intérêts gagnés.

# À la fin de la période, on obtient le capital final qui est le résultat de l'investissement initial, des investissements 
# mensuels et des intérêts gagnés tout au long de la période.





def main():
    return ceZarInvest()
