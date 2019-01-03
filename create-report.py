import config

f = open("/tmp/swellnet.com-reports-australia-new-south-wales-eastern-beaches", "r")
if f.mode == 'r':
    contents = f.read()
    #print(contents)

    str = contents.split('Surf:')
    str = str[1].split('</span>')
    str = str[1].split('>')
    surf =  str[1]
    #print(surf)

    str = contents.split('Winds:')
    str = str[1].split('</span>')
    str = str[1].split('>')
    winds = str[1]
    #print(winds)
    
    str = contents.split('Weather:')
    str = str[1].split('</span>')
    str = str[1].split('>')
    weather = str[1]
    #print(weather)

    str = contents.split('Rating:')
    str = str[1].split('</span>')
    str = str[1].split('>')
    rating = str[1]
    #print(rating)

    str = contents.split('views-field views-field-body')
    str = str[1].split('<p>')
    str = str[1].split('</p>')
    report = str[0]
    #print(report)

    fullReport = "Surf: " + surf + "<br>" + "Winds: " + winds + "<br>" + "Weather: " + weather + "<br>" + "Rating: " + rating + "<br>" + report;
    #print(fullReport)

    f.close()

    f = open(config.surfcamWebroot + "/data/swellnet.com-reports-australia-new-south-wales-eastern-beaches", "w+")
    f.write(fullReport)
    f.close()
