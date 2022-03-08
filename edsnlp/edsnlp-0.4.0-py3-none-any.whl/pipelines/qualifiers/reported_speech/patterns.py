from typing import List

verbs: List[str] = [
    # 'admettre', > False positive: "admis à l'hopital"
    "affirmer",
    "ajouter",
    "assurer",
    "confirmer",
    "demander",
    "dire",
    "déclarer",
    "décrire",
    "décrire",
    "démontrer",
    "expliquer",
    "faire remarquer",
    "indiquer",
    "informer",
    "insinuer",
    "insister",
    "jurer",
    "nier",
    "nier",
    "noter",
    "objecter",
    "observer",
    "parler",
    "promettre",
    "préciser",
    "prétendre",
    "prévenir",
    "raconter",
    "rappeler",
    "rapporter",
    "reconnaître",
    "réfuter",
    "répliquer",
    "répondre",
    "répéter",
    "révéler",
    "se plaindre",
    "souhaiter",
    "souligner",
    "supplier",
    "verbaliser",
    "vouloir",
    "vouloir",
]

following: List[str] = [r"d'après le patient", r"d'après la patiente"]

preceding: List[str] = [
    r"pas de critique de",
    r"crainte de",
    r"menace de",
    r"insiste sur le fait que",
    r"d'après le patient",
    r"d'après la patiente",
    r"peur de",
]
quotation: str = r"(\".+\")|(\«.+\»)"
