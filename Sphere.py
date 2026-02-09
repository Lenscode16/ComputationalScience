import matplotlib.pyplot as plt  # For making the graph
import pandas as pd              # For organizing data
from mpmath import mp, mpf       # For high-precision math (100+ decimals)

# --- STEP 1: SETTINGS ---
# We need 200 decimal places of accuracy because normal Python only does 15.
mp.dps = 200

# The list of precisions your teacher asked for
precisions_list = [20, 40, 60, 100]
radius = 5

# Get the "Perfect" Pi to compare against
true_pi = +mp.pi

# --- STEP 2: THE FORMULAS ---

# Formula 1: Volume of a Sphere (V = 4/3 * pi * r^3)
def get_sphere_volume(pi_value, r):
    return (mpf(4) / mpf(3)) * pi_value * (r ** 3)

# Formula 2: Truncate (Chopping off decimals)
def truncate(number, decimals):
    factor = mpf(10) ** decimals
    return mp.floor(number * factor) / factor

# Formula 3: Round (Rounding to nearest)
def round_num(number, decimals):
    factor = mpf(10) ** decimals
    return mp.nint(number * factor) / factor

# Calculate the "Perfect Volume" to see how far off we are later
perfect_volume = get_sphere_volume(true_pi, radius)

# --- STEP 3: RUN THE EXPERIMENT ---
results = []

print("-" * 100) # Print a divider line
print(f"{'DPS':<5} | {'Type':<8} | {'Error Amount (Difference from Perfect)'}")
print("-" * 100)

for p in precisions_list:
    # A. Create the two imperfect Pis
    pi_chop = truncate(true_pi, p)
    pi_rnd  = round_num(true_pi, p)
    
    # B. Calculate the Volume with these imperfect Pis
    vol_chop = get_sphere_volume(pi_chop, radius)
    vol_rnd  = get_sphere_volume(pi_rnd, radius)
    
    # C. Find the Error (Positive difference)
    error_chop = abs(perfect_volume - vol_chop)
    error_rnd  = abs(perfect_volume - vol_rnd)
    
    # D. Save data for the graph later
    results.append({" decimals": p, "error": error_chop, "type": "Truncation"})
    results.append({" decimals": p, "error": error_rnd,  "type": "Rounding"})
    
    # E. Print the table row (Matches your screenshot)
    # We turn the number into a string so we can see the long "0.00000..."
    print(f"{p:<5} | Trunc    | {str(error_chop)[:60]}...") 
    print(f"{p:<5} | Round    | {str(error_rnd)[:60]}...")

# --- STEP 4: DRAW THE GRAPH ---
# Convert our data into a format helpful for plotting
df = pd.DataFrame(results)

# Separate the data into two lines
line1 = df[df["type"] == "Truncation"]
line2 = df[df["type"] == "Rounding"]

plt.figure(figsize=(10, 6))

# Plot the Red Dashed Line (Truncation)
plt.plot(line1[" decimals"], line1["error"], 
         color='orange', linestyle='--', marker='o', label='Truncation (Chopping)')

# Plot the Blue Solid Line (Rounding)
plt.plot(line2[" decimals"], line2["error"], 
         color='black', linestyle='-', marker='s', label='Rounding')

# Make the Y-axis "Logarithmic" so we can see tiny errors
plt.yscale('log') 

# Add labels and title
plt.title("Error in Sphere Volume: Truncating vs. Rounding Pi")
plt.xlabel("Decimal Places Used")
plt.ylabel("Size of Error (Log Scale)")
plt.grid(True, alpha=0.3)
plt.legend()

# Save and Show
plt.savefig("lab_result_graph.png")
print("\nGraph saved as 'lab_result_graph.png'")
plt.show()