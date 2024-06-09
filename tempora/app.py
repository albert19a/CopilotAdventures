'''
def sync_clocks(clock_times):
    grand_clock_time = 15 * 60  # Convert to minutes
    result = []

    for clock_time in clock_times:
        hours, minutes = map(int, clock_time.split(':'))
        clock_time_in_minutes = hours * 60 + minutes
        difference = clock_time_in_minutes - grand_clock_time
        result.append(difference)

    return result

# Test the function
clock_times = ["14:45", "15:05", "15:00", "14:40"]
print(sync_clocks(clock_times))  # Output: [-15, 5, 0, -20]
'''
def convert_time_to_minutes(time):
    """Convert a time in HH:MM format to minutes."""
    hours, minutes = map(int, time.split(':'))
    return hours * 60 + minutes

def sync_clocks(clock_times, grand_clock_time):
    # il tuo codice qui
#def sync_clocks(clock_times):
    """Return a list of time differences between each clock and the Grand Clock Tower."""
    # grand_clock_time_in_minutes = convert_time_to_minutes("15:00")
    grand_clock_time_in_minutes = convert_time_to_minutes(grand_clock_time)
    time_differences = []

    for clock_time in clock_times:
        clock_time_in_minutes = convert_time_to_minutes(clock_time)
        difference = clock_time_in_minutes - grand_clock_time_in_minutes
        time_differences.append(difference)

    return time_differences


# Test the function
clock_times = ["14:45", "15:05", "15:00", "14:40"]
print(sync_clocks(clock_times,"15:00"))  # Output: [-15, 5, 0, -20]

# Plot the time differences
import matplotlib.pyplot as plt

def plot_clocks(clock_times):
    # Converti i tempi dell'orologio in minuti
    clock_minutes = [int(time.split(':')[0]) * 60 + int(time.split(':')[1]) for time in clock_times]

    # Crea un grafico a barre orizzontali
    plt.barh(range(len(clock_minutes)), clock_minutes)

    # Imposta le etichette y per essere i tempi dell'orologio
    plt.yticks(range(len(clock_minutes)), clock_times)

    # Imposta l'etichetta x
    plt.xlabel('Minuti dopo la mezzanotte')

    # Mostra il grafico a schermo ATTENZIONE: non funziona su Codespaces
    plt.show()

    # Salva il grafico come un file immagine (per Codespaces)
    plt.savefig('clocks.png')

# Esempio di utilizzo della funzione
clock_times = ["14:45", "15:05", "15:00", "14:40"]
plot_clocks(clock_times)