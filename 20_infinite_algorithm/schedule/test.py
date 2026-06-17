"""
Chaque fonction de test représente une journée différente.
Lancer avec : pytest test.py -v
"""
from main import find_free_slots


def test_jour1_chevauchements_simples():
    """Deux activités qui se chevauchent + une isolée → trois plages libres."""
    activities = [(9, 11), (10, 13), (15, 17)]
    assert find_free_slots(activities, 8, 18) == [(8, 9), (13, 15), (17, 18)]


def test_jour2_aucune_activite():
    """Pas d'activité : toute la journée est libre."""
    activities = []
    assert find_free_slots(activities, 8, 18) == [(8, 18)]


def test_jour3_journee_entierement_occupee():
    """Deux activités adjacentes couvrent toute la journée : aucune plage libre."""
    activities = [(8, 12), (12, 18)]
    assert find_free_slots(activities, 8, 18) == []


def test_jour4_activites_non_triees():
    """Même journée que le jour 1 mais activités dans le désordre."""
    activities = [(15, 17), (9, 11), (10, 13)]
    assert find_free_slots(activities, 8, 18) == [(8, 9), (13, 15), (17, 18)]


def test_jour5_une_seule_activite_au_milieu():
    """Une seule activité centrale → plage libre le matin et l'après-midi."""
    activities = [(10, 14)]
    assert find_free_slots(activities, 8, 18) == [(8, 10), (14, 18)]


def test_jour6_activites_strictement_adjacentes():
    """Activités qui se touchent sans se chevaucher : pas de créneau entre elles."""
    activities = [(8, 10), (10, 14), (14, 17)]
    assert find_free_slots(activities, 8, 18) == [(17, 18)]


def test_jour7_chevauchements_imbriques():
    """Une activité longue englobe entièrement d'autres + une dernière qui prolonge."""
    activities = [(9, 17), (10, 12), (11, 15), (16, 18)]
    assert find_free_slots(activities, 8, 18) == [(8, 9)]


def test_jour8_une_activite_couvre_tout():
    """Une seule activité qui couvre toute la journée."""
    activities = [(8, 18)]
    assert find_free_slots(activities, 8, 18) == []


def test_jour9_activites_depassant_les_bornes():
    """Activités qui commencent avant ou finissent après la journée : doivent être rognées."""
    activities = [(6, 10), (16, 20)]
    assert find_free_slots(activities, 8, 18) == [(10, 16)]


def test_jour10_activites_en_debut_et_fin():
    """Activités occupant seulement le début et la fin : long créneau au milieu."""
    activities = [(8, 9), (17, 18)]
    assert find_free_slots(activities, 8, 18) == [(9, 17)]


def test_jour11_activite_entierement_hors_bornes():
    """Activité complètement en dehors de la journée : ignorée."""
    activities = [(20, 23), (10, 12)]
    assert find_free_slots(activities, 8, 18) == [(8, 10), (12, 18)]


def test_jour12_beaucoup_dactivites():
    """Journée chargée avec de nombreux chevauchements et quelques créneaux libres."""
    activities = [
        (9, 10), (9, 11), (11, 13), (12, 14),
        (15, 16), (15, 17), (17, 18)
    ]
    assert find_free_slots(activities, 8, 18) == [(8, 9), (14, 15)]
