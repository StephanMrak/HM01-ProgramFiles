from threading import Thread
import multiprocessing
import time
import pygame
import os
import hmsysteme

width = 1000
height = 650

def start_game(gamefile):
    mod_game=(__import__(gamefile))
    print(mod_game)
    p = multiprocessing.Process(target=mod_game.main)
    print(p)
    p.start()
    time.sleep(1)
    return p
    
def close_game(asd):
    for i in range(0,len(asd)):
        if asd[i].is_alive():           
            hmsysteme.close_pygame()
            time.sleep(0.5)
            asd[i].terminate()
            print(asd[i])
  

def mobile_com(threadname,path2,qgn,q1,q2,q3,q4,q5,size,gamefiles,hwqueue):
    import time
    import io
    import os
    import PIL.Image
    import pickle
    asdf=[]


    #import remi.gui as gui
    import remi.gui as gui
    from remi import start, App
    
    path=hmsysteme.get_path()

    playernames=[]

    container_players_added = gui.VBox(width=width, height=height,
                                       style={'padding-left': '0px', 'font-size': '15px', 'align': 'left'})
    container_players_added.style["background"] = "#404040"
    container_players_added.style["color"] = "white"


    class PILImageViewverWidget(gui.Image):
        def __init__(self, pil_image=None, **kwargs):
            super(PILImageViewverWidget, self).__init__(os.path.join(path,"screencapture.jpg"), **kwargs)
            #super(PILImageViewverWidget, self).__init__(r"C:\Users\49176\Dropbox\HM01", **kwargs)
            #super(PILImageViewverWidget, self).__init__("/home/stan/Dropbox/HM01/screen_capture.png", **kwargs)
            
            self._buf = None

        def load(self, file_path_name):
            pil_image = PIL.Image.open(file_path_name)
            self._buf = io.BytesIO()
            pil_image.save(self._buf, format='JPEG')
            self.refresh()

        def refresh(self):
            i = int(time.time() * 1e6)
            self.attributes['src'] = "/%s/get_image_data?update_index=%d" % (id(self), i)

        def get_image_data(self, update_index):
            if self._buf is None:
                return None
            self._buf.seek(0)
            headers = {'Content-type': 'image/jpg'}
            return [self._buf.read(), headers]
    
        
    
    class MyApp(App):
        def __init__(self, *args):
            super(MyApp, self).__init__(*args)
            
        def idle(self):
            time.sleep(0.1)   
            #hmsysteme.put_playernames(playernames)
            if hmsysteme.screenshot_refresh()== True:
                self.image_widget.load(file_path_name=os.path.join(path,"screencapture.jpg"))
                q1.put("ok")
            
           
        def main(self):
            bt=[]
            functions=[]
            global width
            global height
            tb = gui.TabBox(width=width ,style={'color': 'white', 'background-color': '#404040','font-size':'20px'})


            #container = gui.VBox(width=500, height=650)
            container = gui.VBox(width=width, height=height,style={'padding-left': '0px', 'font-size': '15px', 'align': 'left'})
            container.style["background"]="#404040"
            container2 = gui.VBox(width=width, height=height,style={'padding-left': '0px', 'font-size': '15px', 'align': 'left'})
            container2.style["background"] = "#404040"
            container3 = gui.VBox(width=width, height=height,style={'padding-left': '0px', 'font-size': '15px', 'align': 'left'})
            container3.style["background"] = "#404040"
            container4 = gui.VBox(width=width, height=height,style={'padding-left': '0px', 'font-size': '15px', 'align': 'left'})
            container4.style["background"] = "#404040"


            
            self.lbl = gui.Label('no game running yet', width='50%', height='8%',style={'font-size': '30px', 'text-align': 'left'})#str(q.get()))
            self.lbl.style["color"]="white"
            self.lbl_foto = gui.Label('-')
            self.lbl_count = gui.Label('-')
            
            for i in range (len(gamefiles)):
                bt.append(gui.Button('Start %s' %(str(gamefiles[i])),width='30%', height='10%' ,margin='5px',style={'font-size': '20px', 'text-align': 'center'}))
                bt[i].style["background"] = "#606060"
                bt[i].style["box-shadow"] = "none"
                
            b1 = gui.Button('Close all',width='40%', height='5%' ,margin='5px',style={'font-size': '20px', 'text-align': 'center'})
            b1.style["background"] = "#606060"
            b1.style["box-shadow"] = "none"
            b2 = gui.Button('Stop Server',width='40%', height='5%' ,margin='5px',style={'font-size': '20px', 'text-align': 'center'})
            b2.style["background"] = "#606060"
            b2.style["box-shadow"] = "none"
            b3 = gui.Button('System Shutdown',width='40%', height='5%' ,margin='5px',style={'font-size': '20px', 'text-align': 'center'})
            b3.style["background"] = "#606060"
            b3.style["box-shadow"] = "none"
            b4 = gui.Button('System reset',width='40%', height='5%' ,margin='5px',style={'font-size': '20px', 'text-align': 'center'})
            b4.style["background"] = "#606060"
            b4.style["box-shadow"] = "none"

            #self.image_widget = PILImageViewverWidget(width=width, height=height)
            self.image_widget = PILImageViewverWidget(width=width)
            self.image_widget.load(file_path_name=os.path.join(path2,"logo.jpg"))
            
            for i in range(len(gamefiles)):
                def f(widget,i=i):
                    close_game(asdf)
                    asdf.append(start_game(gamefiles[i]))
                    self.lbl.set_text(gamefiles[i]+" now runnning")
                    #print(asdf)
                functions.append(f)       
            
            # setting the listener for the onclick event of the button
            for i in range (len(gamefiles)):
                bt[i].onclick.do(functions[i])

            b1.onclick.do(self.on_button_pressed1)
            b2.onclick.do(self.on_button_pressed2)
            b3.onclick.do(self.on_button_pressed3)
            b4.onclick.do(self.on_button_pressed4)
            

            # appending a widget to another, the first argument is a string key
            container.append(self.lbl)

            
            for i in range (len(gamefiles)):
                container3.append(bt[i])
            container.append(self.image_widget)
            container.append(self.lbl_foto)
            container.append(self.lbl_count)   
            container4.append(b1)
            container4.append(b2)
            container4.append(b3)
            container4.append(b4)
            self.lbl2 = gui.Label('input player name: ', width='50%', height='8%',style={'font-size': '30px', 'text-align': 'left'})
            self.lbl2.style["color"]="white"
            container2.append(self.lbl2)

            self.txt=gui.TextInput( width='50%', height='8%',style={'font-size': '30px', 'text-align': 'left'})
            self.txt.style["background"]="#606060"
            self.txt.style["color"] = "white"
            self.txt.onchange.do(self.on_text_area_change)
            container2.append(self.txt)

            container2.append(container_players_added)

            tb.append(container,'Home')
            tb.append(container2,'Players')
            tb.append(container3, 'Games')
            tb.append(container4, 'Settings')
            # returning the root widget
            return tb
            
        def on_button_pressed1(self, widget):
            close_game(asdf)
            self.lbl.set_text("no game running yet")
            print("all closed")    
            
        def on_button_pressed2(self, widget):           
            self.server.server_starter_instance._alive=False
            self.server.server_starter_instance._sserver.shutdown()
            print("server stopped")
            
        def on_button_pressed3(self, widget):
            self.dialog = gui.GenericDialog(width=350,title='Shutdown', message='Do you really want to shutdown the system')
            self.dialog.confirm_dialog.do(self.sd_func)
            self.dialog.show(self)
            
        def on_button_pressed4(self, widget):           
            self.reset_func(self)

        def sd_func(self, widget):		
            import os
            print("system shutdown")
            os.system("sudo poweroff")
            
        def reset_func(self, widget):		
            print("system reset")
            hwqueue.put("off")
       

                
        def on_text_area_change(self, widget, newValue):           
            print(self.txt.get_text())
            container_players_added.empty()
            playernames.append([self.txt.get_text(),True])
            grid = gui.GridBox(width='50px',style={'font-size': '30px', 'align': 'left'})
            grid.style["background"] = "#404040"
            grid.style["color"] = "white"
            asd=[]
            self.checka=[]
            self.functionsc=[]
            for i in range(0, len(playernames)):
                asd.append((['value'+str(i+1), 'label'+str(i+1)]))
            grid.define_grid(asd)
            for i in range(0, len(playernames)):
                self.checka.append(gui.CheckBox(playernames[i][1]))
                def f (widget,newValue, i=i):
                    if newValue==True:
                        playernames[i][1]=True
                    else:
                        playernames[i][1]=False
                    hmsysteme.put_playernames(playernames)
                        
                self.functionsc.append(f)
                self.checka[i].onchange.do(self.functionsc[i])
                
                lbl=gui.Label(playernames[i][0],width='30%', height='8%',margin='0px',style={'font-size': '30px', 'align': 'left'})
                grid.append({'label'+str(i+1): lbl, 'value'+str(i+1): self.checka[i]})
            container_players_added.append(grid)
            self.txt.set_text("")
            hmsysteme.put_playernames(playernames)
            print(playernames)

    # starts the web server
    start(MyApp,start_browser=True)
    #start(MyApp, address='0.0.0.0', port=8081, multiple_instance=False, enable_file_cache=True, update_interval=0.1, start_browser=False)
    
