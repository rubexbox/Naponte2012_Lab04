# COT 4930  Python Programming
# name: Nicolas Aponte
# id  : Z23216341
# lab : 04
dict = { }

def make_dict( ) :
    #Opens the text file fl_cities.txt
    #fl_cities.txt contains a list of cities in Florida with their zipcodes
    ifile = open( "fl_cities.txt", "r" )

    #reads fl_cities.txt and creates a dictionary using the zipcode as the keys
    for line in ifile :
        line = line.rstrip( )
        ( e, f ) = line.split( ":" )
        #test condition-prints cities and zipcodes
        print( "\t'%-8s'\t'%-8s'" % ( e, f ) )
        dict[ f] = e

    ifile.close( )

def test_dict( ):
    ifile = open( "fl_maint.txt", "r" )
    #fl_maint.txt contains a list of commands
    #this program will read the file and, if the commands are valid, execute them
    for word in ifile :
        word = word.rstrip( )
        (g,h)=word.split("-")
        #(f)inds a city in the dictionary
        #if the city exists in dictionary, print city and zip code
        #otherwise, display an error message
        if (g=="f"):
            print( "%-10s %-10s" %( h, dict.get( h, "city unknown." ) ) )
        #(p)rints dictionary with cities in alphabetical order
        elif (g=="p"):
            keys =  list( dict.keys( ) )
            keys.sort( )
            for zipcode in keys :
                print( "\t'%-8s'\t'%-8s'" % ( zipcode, dict[ zipcode ] ) )
        #(c)hanges zipcode of city, if that city exists in the dictionary
        elif(g=="c"):
            (i,j)=h.split(":")
            if (dict.get(j, "city unknown")=="city unknown"):
                print ("city unknown")
            else:
                dict[j]=i
                print ("zipcode changed.")
        else:
            print("Unrecognized command")
        print()
    ifile.close( )


make_dict( )
print( )
test_dict( )
