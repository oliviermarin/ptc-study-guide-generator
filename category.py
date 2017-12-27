# -*- coding: utf-8 -*-

from enum import Enum
from color import Color

class Category(Enum):
	AGGLOMERATION={'title': 'Agglom\xe9ration', 'color': Color(26, 188, 156)}
	INDICATION={'title': 'Indication', 'color': Color(46, 204, 113)}
	DANGER={'title': 'Danger', 'color': Color(52, 152, 219)}
	DIRECTION={'title': 'Direction', 'color': Color(155, 89, 182)}
	LOCALISATION={'title': 'Localisation', 'color': Color(241, 196, 15)}
	PANONCEAUX={'title': 'Panonceaux', 'color': Color(230, 126, 34)}
	INTERDICTION={'title': 'Interdiction', 'color': Color(231, 76, 60)}
	BALISES={'title': 'Balises', 'color': Color(236, 240, 241)}
	SYMBOLES={'title': 'Symboles', 'color': Color(189, 195, 199)}
	OBLIGATION={'title': 'Obligation', 'color': Color(149, 165, 166)}
	IDEOGRAMMES={'title': 'Id\xe9ogrammes', 'color': Color(155, 89, 182)}
	PRIORITES={'title': 'Priorit\xe9s', 'color': Color(22, 160, 133)}
	CARTOUCHES={'title': 'Cartouches', 'color': Color(39, 174, 96)}
	ZONE={'title': 'Zone', 'color': Color(41, 128, 185)}
	TRAVAUX={'title': 'Travaux', 'color': Color(192, 57, 43)}
