import json
import urllib.request
import urllib.parse
import urllib.error

# these methods are exposed to Internet by wsgi.py
__all__ = ["show", "latest_status", "all_status", "torumemo"]

_text = """
                                  #############                     ######## 
                                  #############                  ############## 
                                  #############                ################## 
                                  #############              ###################### 
                                     ########               ######################## 
                                    #######                ########################## 
                                    ######                ############################ 
                                   ######                ################        ###### 
                                   #####                 ##############            #### 
                                  #####                 ##############              #### 
                                  #####                 #############               #### 
                                  ####                  #############               #### 
                                  ####                  ############                #### 
                                  ####                 #############                #### 
                                  ####                 #############                #### 
                                  ####                #############                ##### 
                                  ####                #############               ##### 
                                  #####              ##############              ###### 
                                   ####              #############              ###### 
                                   #####            ##############             ####### 
                                    #####          ##############            ######## 
                                    ######       ################          ############# 
                                     ###########################           ############# 
                                      ##########################           ############# 
                                       ########################            ############# 
                                         #################### 
                                           ################ 
                                               ######### 
                                                         
                                  ####                                                                                   #### 
                                  ####                                                                                   #### 
                                  ########################################################################################### 
                                  ########################################################################################### 
                                  ########################################################################################### 
                                  ########################################################################################### 
                                  ########################################################################################### 
                                  ########################################################################################### 
                                  ########################################################################################### 
                                  ########################################################################################### 
                                  ####                                      ##### 
                                  ####                                        ##### 
                                                                               ##### 
                                                                                ##### 
                                                                                ###### 
                                                                                 ###### 
                                                                                 ###### 
                                                                                 ####### 
                                                                                 ####### 
                                                                                ######## 
                                  ####                                         ######### 
                                  ####                                      ############ 
                                  ###################################################### 
                                  ##################################################### 
                                  ##################################################### 
                                  #################################################### 
                                  ################################################### 
                                  ################################################# 
                                  ############################################## 
                                  ########################################## 
                                  #### 
                                  #### 
                                       
                                                    ################## 
                                               ############################ 
                                             ################################ 
                                           #################################### 
                                         ######################################## 
                                       ############################################ 
                                      ############################################## 
                                     #############                      ############# 
                                    #########                                ######### 
                                    #######                                    ####### 
                                   ######                                        ###### 
                                   #####                                          ##### 
                                  #####                                            ##### 
                                  ####                                              #### 
                                  ####                                              #### 
                                  ####                                              #### 
                                  ####                                              #### 
                                  #####                                            ##### 
                                  #####                                            ##### 
                                   #####                                          ##### 
                                   ######                                        ###### 
                                    #######                                    ####### 
                                    #########                                ######### 
                                     #############                      ############# 
                                      ############################################## 
                                       ############################################ 
                                         ######################################## 
                                           #################################### 
                                             ################################ 
                                               ############################ 
                                                    ################## 
                                                                       
                                                                                    #### 
                                                                                    #### 
                                                                                 ####### 
                                                                              ########## 
                                                                          ############## 
                                                                      ################## 
                                                                  ###################### 
                                                               ######################### 
                                                           ############################# 
                                                       ################################# 
                                                   ##################################### 
                                                ################################    #### 
                                            ################################        #### 
                                        ################################ 
                                    ################################# 
                                  ############################### 
                                     ######################## 
                                        ################# 
                                            ############ 
                                                ############ 
                                                   ############# 
                                                #################### 
                                            ############################ 
                                        ############################### 
                                    ################################ 
                                  ############################## 
                                     ######################## 
                                        ################# 
                                            ############ 
                                                ############ 
                                                    ############ 
                                                       ############# 
                                                           ############# 
                                                               #############        #### 
                                                                   #############    #### 
                                                                       ################# 
                                                                           ############# 
                                                                              ########## 
                                                                                  ###### 
                                                                                    #### 
                                                                                    #### 
                                                                                    #### 
    """


def show():
    """Say show :-)"""
    return _text


def show_gui():
    try:
        from bucho.gui import BuchoFrame

        frame = BuchoFrame(_text)
        frame.run()
    except Exception:
        print("Sorry, bucho is busy.")


def latest_status():
    """Print latest bucho's tweet."""
    url = urllib.request.urlopen(
        "http://twitter.com/statuses/user_timeline/torufurukawa.json"
    )
    tof = json.loads(url.read().decode("utf-8"))
    return tof[0]["text"]


def all_status():
    """Print all bucho's tweet."""
    url = urllib.request.urlopen(
        "http://twitter.com/statuses/user_timeline/torufurukawa.json"
    )
    tof = json.loads(url.read().decode("utf-8"))
    return "\n".join(t["text"] for t in tof)


def torumemo():
    """Open torumemo with webbrowser."""
    import webbrowser

    webbrowser.open("http://oldriver.org/torumemo/")
    return "OK"
