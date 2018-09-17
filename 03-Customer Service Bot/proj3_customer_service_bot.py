#CUSTOMER SERVICE BOT (JUPYTER NOTEBOOKS)
#PROJECT #3
#CODE ACADEMY 
#PROGRAMMING WITH PYTHON 
#Dean Jones, Jul.29, 2018

#----------------
#IMPORTS 
import datetime


#FUNCTION: MAIN FUNCTION
# This is a main function for (user support) this will guide the (user) decisions to find a solution
def cs_service_bot():
    #welcome message
    #print('''
    #Hello! Welcome to the DNS Cable Company\'s Service Portal. Are you a new or existing customer?
    #\t[1] New Customer
    #\t[2] Existing Customer
    #''')
    #user input
    input_welcome = input('''
**********************************************************
Hello! Welcome to the DNS Cable Company\'s Service Portal. 
        Are you a new or existing customer?
        Please select an option: 
            [1] New Customer
            [2] Existing Customer

        Your selection: '''
    )
    #input_welcome = input('Please enter the NUMBER (1-New, 2-Existing) corresponding to your choice: ')
    if (input_welcome == '1'):
        #run customer() function
        new_customer()
    elif (input_welcome == '2'):
        #run existing_customer() function
        existing_customer()
    else:
        print('Sorry, we didn\'t understand your selection.')
        #restart main function
        cs_service_bot()

#--------

#FUNCTION: CUSTOMER
def new_customer():
    print('\t\tYou are a NEW CUSTOMER, welcome!')
    #user input
    input_new = input('''
    ---------------------
    NEW CUSTOMER (OPTIONS)
        Please select an option: 
            [1] Sign up for service
            [2] Schedule a home visit
            [3] Speak to a sales representative

        Your selection: '''
    )
    if (input_new == '1'):
        sign_up()               #run
    elif (input_new == '2'):
        home_visit()            #home visit
    elif (input_new == '3'):
        live_rep()              #run
    else:
        #problem, try again
        print('PROBLEM: --------------------------------------------------------')
        print('Something went wrong while selecting an option. Please try again.')
        new_customer()

#FUNCTION: NEW CUSTOMER (SIGN-UP)
def sign_up():
    print(str_choice('NEW CUSTOMER: SIGN-UP'))
    #user input
    input_new_signup = input('''
    Great choice, friend! We're excited to have you join the DNS family! 
    Please select the package you are interested in signing up for.
    --------------------------------------------------------------------
    SIGN-UP (OPTIONS)
            [1] Bundle Deal (Internet + Cable)
            [2] Internet
            [3] Cable

        Your selection: '''
    )
    if (input_new_signup == '1'):               #Bundle Deal (Internet + Cable)
        print('''
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            You've selected the Bundle Package! 
            Please schedule a home visit and our technician will come and set up your new service.
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            '''
        )         
        home_visit("new install")               #home visit    
    elif (input_new_signup == '2'):             #Internet
        print('''
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            You've selected the Internet Only Package! 
            Please schedule a home visit and our technician will come and set up your new service.
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            '''
        )   
        home_visit("new install")               #home visit  
    elif (input_new_signup == '3'):             #Cable
        print('''
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            You've selected the Cable Only Package! 
            Please schedule a home visit and our technician will come and set up your new service.
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            '''
        )      
        home_visit("new install")               #home visit  
    else: 
        print('There was a problem with your selection, please try again.')
        sign_up()                               #re-run SIGN-UP

#FUNCTION: NEW CUSTOMER (HOME VISIT)
def home_visit(purpose='None'):
    # ARGUMENTS  
    # purpose='None'                home_visit()                (same as NO ARGUMENT)
    # purpose='support'             home_visit("support")
    # purpose='new install'         home_visit("new install")
    
    # 3 options
    #   new_customer()              home_visit()                
    #   did_that_help()             home_visit("support")       (internet or tv support)
    #   sign_up()                   home_visit("new install")
    
    #if (purpose == 'None'):
    #   3 options 
    #else:
    #   date 
    #   

    if (purpose == 'None'):
        home_visit_three_options()  #run THREE(3) OPTIONS 
    else:
        #user input
        print('''
        Please enter a date below when you are available for a technician to 
        come to your home and service you for your problem or new installation.
        -----------------------------------------------------------------------'''
        )

        #get date (for home visit)
        visit_date = home_visit_get_date()   

        print('\t-----------------------------------------------------------------------')
        print('')
        print('\t***********************************************************************')
        print('\tWonderful. A technician will visit you on: ', str(visit_date))
        print('\tPlease be available between the hours of 1:00 am and 11:00 pm.')
        print('')
        print('\tHave a wonderful, super, awesome day.')
        print('\t***********************************************************************')
        print('')

        return visit_date

#FUNCTION: HOME VISIT (GET DATE)
def home_visit_get_date():
        year = int(input('\t\tPlease enter a year: '))
        #year: 2018
        month = int(input('\t\tPlease enter a month: '))
        #month: 07
        day = int(input('\t\tPlease enter a day: '))
        #day: 30

        print('')
        #validate date
        try:
            home_visit_date = datetime.date(year, month, day)
            return home_visit_date
        except ValueError:
            print('\t\tPROBLEM -------------------------------------------')
            print('\t\tThe date you entered was invalid, please try again.')
            home_visit_get_date()      #try again
        

#FUNCTION: HOME VISIT (THREE OPTIONS)
def home_visit_three_options():
    print(str_choice('HOME VISIT'))
    #user input
    input_home_visit = input('''
    What is the purpose of your home visit?
    --------------------------------------------------------------------
    HOME VISIT (OPTIONS)
            [1] New service installation.
            [2] Existing service repair.
            [3] Location scouting for unserviced region.

        Your selection: '''
    )
    if (input_home_visit == '1'):               #New service installation.
        print('''
            +++++++++++++++++++++++++++++++
            call home_visit("new install")
            +++++++++++++++++++++++++++++++
            '''
        )         
        home_visit("new install")               #home visit (NEW INSTALL) 
    elif (input_home_visit == '2'):             #Existing service repair.
        print('''
            +++++++++++++++++++++++++++++++
            call home_visit("support")
            +++++++++++++++++++++++++++++++
            '''
        )         
        home_visit("support")                   #home visit (SUPPORT)
    elif (input_home_visit == '3'):             #Location scouting for unserviced region.
        print('''
            +++++++++++++++++++++++++++++++
            call home_visit("scout")
            +++++++++++++++++++++++++++++++
            '''
        )         
        home_visit("scout")                     #home visit (SCOUT)   
    else: 
        print('There was a problem with your selection, please try again.')
        home_visit_three_options()              #re-run THREE OPTIONS
#--------

#FUNCTION: EXISTING CUSTOMER
def existing_customer():
    print('\t\tYou selected EXISTING CUSTOMER...')
    #user input
    input_ex = input('''
    -----------------------------------
    EXISTING CUSTOMER (SUPPORT OPTIONS)
        What kind of support do you need?: 
            [1] TV
            [2] Internet
            [3] Speak to a sales representative

        Your selection: '''
    )
    #input_ex = input('Please enter the NUMBER (1-TV, 2-Internet, 3-Speak to Someone) corresponding to your choice: ')
    if (input_ex == '1'):
        television_support()    #run television_support() function
    elif (input_ex == '2'):
        internet_support()      #run internet_support() function
    elif (input_ex == '3'):       
        live_rep()              #run live_rep() function (for someone to speak to...)
    else:
        #problem, try again
        print('PROBLEM: ---------------------------------------------------------------')
        print('Something went wrong while selecting a support option. Please try again.')
        existing_customer()

#FUNCTION: SUPPORT (TV)
def television_support():
    print(str_choice('TV SUPPORT'))
    #user input
    input_tv_support = input('''
    -----------------------------------
    TV SUPPORT (OPTIONS)
            [1] I can't access certain channels.
            [2] My picture is blurry.
            [3] I keep losing service.
            [4] Other problem.

        Your selection: '''
    )
    if (input_tv_support == '1'):       #I can't access certain channels.
        print('''
            ********************************************************************************
            Please check the channel lists at DefinitelyNotSinister.com.
            If the channel you cannot access is there, please contact a live representative.
            ********************************************************************************
            '''
        )
        did_that_help()              
    elif (input_tv_support == '2'):     #My picture is blurry.
        print('''
            ****************************************************
            Try adjusting the antenna above your television set.
            ****************************************************
            '''
        )
        did_that_help()    
    elif (input_tv_support == '3'):     #I keep losing service.
        print('''
            ******************************************************************************
            Is it raining outside? If so, wait until it is not raining and then try again.
            ******************************************************************************
            '''
        )
        did_that_help()         
    elif (input_tv_support == '4'):     #Other problem.
        print('''
            *****************************************************************
            We will connect you to a live service representative immediately.
            *****************************************************************
            '''
        )
        live_rep()                      #run LIVE REP

#FUNCTION: DID THAT HELP?
def did_that_help():
    is_resolved = input('''
    Did this resolve your problem?: (Y/N) ''')

    yes = {'yes', 'y', 'ye', ''}        #blank is hitting ENTER (yes)
    no = {'no', 'n'}
    is_resolved = is_resolved.lower()   #to lowercase

    if is_resolved in yes:
        print('''
            **********
            Thank you.
            **********
            '''
        )
    elif is_resolved in no:
        not_resolved()                  #run NOT_RESOLVED()
    else:
        #problem, try again
        print('PROBLEM: --------------------------------------------------------')
        print('Something went wrong while selecting an option. Please try again.')
        did_that_help()

#FUNCTION: NOT_RESOLVED
def not_resolved():
    #if not resolved...
    input_not_resolved = input('''
    ---------------------
    Would you like to schedule a home visit, or speak to someone? (OPTIONS)
        Please select an option: 
            [1] Schedule a home visit
            [2] Speak to a sales representative

        Your selection: '''
    )
    if (input_not_resolved == '1'):
        home_visit("support")           #home visit          
    elif (input_not_resolved == '2'):
        live_rep()             
    else:
        #problem, try again
        print('PROBLEM: --------------------------------------------------------')
        print('Something went wrong while selecting an option. Please try again.')
        not_resolved()

#FUNCTION: SUPPORT (INTERNET)
def internet_support():
    print(str_choice('INTERNET SUPPORT'))
    #user input
    input_internet_support = input('''
    -----------------------------------
    INTERNET SUPPORT (OPTIONS)
            [1] I can't connect to the internet.
            [2] My connection is very slow.
            [3] I can't access certain sites.
            [4] Other problem.

        Your selection: '''
    )
    if (input_internet_support == '1'):       #I can't connect to the internet.
        print('''
            ***********************************************************************************
            Unplug your router, then plug it back in, then give it a good whack, like the Fonz.
            ***********************************************************************************
            '''
        )
        did_that_help()              
    elif (input_internet_support == '2'):     #My connection is very slow.
        print('''
            *********************************************************************************************
            Make sure that all cell phones and other peoples computers are not connected to the internet, 
            so that you can have all the bandwidth.
            *********************************************************************************************
            '''
        )
        did_that_help()    
    elif (input_internet_support == '3'):     #I can't access certain sites.
        print('''
            ****************************************************************************
            Move to a different region or install a VPN. Some areas block certain sites.
            ****************************************************************************
            '''
        )
        did_that_help()         
    elif (input_internet_support == '4'):       #Other problem.
        live_rep()                              #run LIVE REP

#FUNCTION: SUPPORT (CUSTOMER REPRESENTATIVE)
def live_rep():
    print(str_choice('LIVE REPRESENTATIVE SUPPORT'))
    print('''
            *******************************************************************************
            We will connect you to a live service representative immediately.

            Please hold while we connect you with a live (sales or support) representative. 
            The wait time will be between two minutes and six hours. 
            We thank you for your patience, but not really...
            *******************************************************************************
            '''
    )

#--------
#FUNCTION: PRINT HELP 
def str_choice(option):
    return '\t\tYou selected: {}'.format(option)


#****************
#RUN MAIN PROGRAM
cs_service_bot()
#****************

