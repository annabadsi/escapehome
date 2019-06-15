from django_alexa.api import fields, intent, ResponseBuilder

HOUSES = ("gryffindor", "hufflepuff", "ravenclaw", "slytherin")


@intent(app='escapehome')
def LaunchRequest(session):
    return ResponseBuilder.create_response(message="Willkommen im Escape Room!",
                                           reprompt="Finde den Code heraus, welcher die Box öffnet.",
                                           end_session=False,
                                           launched=True)


class PointsForHouseSlots(fields.AmazonSlots):
    house = fields.AmazonCustom(label="HOUSE_LIST", choices=HOUSES)
    points = fields.AmazonNumber()


@intent(slots=PointsForHouseSlots, app='escapehome')
def PointsForHouse(session, house, points):
    kwargs = {'message': f"{points} Punkte wurden dem Haus {house} hinzugefügt."}
    if session.get('launched'):
        kwargs['reprompt'] = "Welchem Haus möchtest du Punkte hinzufügen?"
        kwargs['end_session'] = False
        kwargs['launched'] = session['launched']
    return ResponseBuilder.create_response(**kwargs)
