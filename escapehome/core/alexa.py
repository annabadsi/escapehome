from django_alexa.api import fields, intent, ResponseBuilder

HOUSES = ("gryffindor", "hufflepuff", "ravenclaw", "slytherin")


@intent(app='escapehome')
def LaunchRequest(session):
    f = open("core/alexa-resource/welcome-text.txt", "r")
    reprompt = f.readline()
    f.close()
    return ResponseBuilder.create_response(message="Willkommen im Escape Room!",
                                           reprompt=reprompt, end_session=False, launched=True)


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


class CountFlashsSlots(fields.AmazonSlots):
    counter = fields.AmazonNumber()


@intent(slots=CountFlashsSlots, app='escapehome')
def CountFlashs(session, counter):
    kwargs = {'message': f"{counter} Mal hast du gezählt."}
    if session.get('launched'):
        kwargs['reprompt'] = "Wie oft blinkt die Lampe?"
        kwargs['end_session'] = False
        kwargs['launched'] = session['launched']
    return ResponseBuilder.create_response(**kwargs)

