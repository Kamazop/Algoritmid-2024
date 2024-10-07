# Quicksortiga raamatute järjestamine
def quicksort(raamatud):
    if len(raamatud) <= 1: # Kui nimekirjas on 0 või 1 raamatut, on see juba sorteeritud
        return raamatud
    
    pivot = raamatud[len(raamatud) // 2]  # Valime pivotiks keskmise raamatu
    # Jaotab raamatud gruppidesse
    väiksemad = [x for x in raamatud if x < pivot]  # Raamatud, mis on pivotist madalamad
    võrdsed = [x for x in raamatud if x == pivot]   # Pivotiga võrdse kõrgusega raamatud
    suuremad = [x for x in raamatud if x > pivot]  # Raamatud, mis on pivotist kõrgemad
    
    # Rakendab rekursiivselt quicksorti väiksematele ja suurematele raamatu gruppidele
    return quicksort(väiksemad) + võrdsed + quicksort(suuremad)

raamatu_kõrgused = [15, 8, 22, 5, 17, 13, 10, 20]

# Sorteerib raamatud kõrguse järgi
sorteeritud_raamatud = quicksort(raamatu_kõrgused)

# Väljastab sorteeritud raamatute kõrgused
print("Sorteeritud raamatute kõrgused:", sorteeritud_raamatud)
