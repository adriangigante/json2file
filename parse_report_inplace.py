import platform

def run(url, contents):

    if url.find("swellnet") != -1:
        
        str = contents.split('Surf:')
        if len(str) > 1:
            if str[1].find('Lorem ipsum') != -1:
                fullReport = "Daily surf reports are exclusive to Swellnet Pro subscribers until 9am"
            else:    
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
        else:
            fullReport = "Too early! Nothing to report yet."

    elif url.find("coastalwatch") != -1:

        str = contents.split('s rating - <strong> ');
        if len(str) > 1:

            str = str[1].split(' </');
            rating = str[0];
            #alert('Rating: ' + rating);

            str = str[1].split('Bottom">');
            report = str[1].split('<')[0].strip();
            #alert('Report: ' + report);

            str = contents.split('<strong class="val">');
            surf = str[1].split('</strong>')[0] + ' ' + str[1].split('<span class="dir">')[1].split('</span>')[0] + str[1].split('<span>')[1].split('</span>')[0];
            #alert(surf);

            str = contents.split('<strong class="val">');
            winds = str[2].split('</strong>')[0] + ' ' + str[2].split('<span class="dir">')[1].split('</span>')[0];
            #alert(winds);

            str = contents.split('<div class="floatLeft report water">');
            water = str[1].split('>')[1].split('<')[0];
            #alert(water);
                            

            fullReport = "Surf: " + surf + "<br>" + "Winds: " + winds + "<br>" + "Water: " + water + "<br>" + "Rating: " + rating + "<br>" + report
        else:
            fullReport = "Too early! Nothing to report yet." 

    return fullReport
