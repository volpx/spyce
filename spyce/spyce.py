
# Library to do ngspice simulations
import subprocess
class Circuit(object):
    """docstring for Circuit."""
    def __init__(self, filename, title='Circuit'):
        #super(Circuit, self).__init__()
        self.title=title
        self.comp_index=0
        self.filename=filename
        self.file=open(filename,'w')
        self.file.write('*'+title+'\n')

    def __del__(self,):
        try:
            self.file.close()
        except:
            pass

    ############ PLACE COMPONENTS ############
    def r(self,*args,**kwargs):
        if len(args)>=3:
            p=(args[0],args[1])
            value=args[2]
            if len(args)==4:
                name=args[3]
            else:
                name=str(self.comp_index)
        self._place_component(p=p,name=name,value=value,type='r')
    def c(self,*args,**kwargs):
        if len(args)>=3:
            p=(args[0],args[1])
            value=args[2]
            if len(args)==4:
                name=args[3]
            else:
                name=str(self.comp_index+1)
        self._place_component(p=p,name=name,value=value,type='c')
    def l(self,*args,**kwargs):
        if len(args)>=3:
            p=(args[0],args[1])
            value=args[2]
            if len(args)==4:
                name=args[3]
            else:
                name=str(self.comp_index+1)
        self._place_component(p=p,name=name,value=value,type='l')
    def m(self,*args,**kwargs):
        # drain, gate, source, body, model, name
        if len(args)>=5:
            p=(args[0],args[1],args[2],args[3])
            model=args[4]
            if len(args)==6:
                name=args[5]
            else:
                name=str(self.comp_index+1)
        self._place_component(p=p,name=name,value=value,type='m')
    def x(self,p,subckt,name=None):
        name=name if name is not None else str(self.comp_index+1)
        self._place_component(p=p,name=name,value=subckt,type='x')
    def source(self,p1,p2,descr,type='v',name=None):
        name=name if name is not None else str(self.comp_index+1)
        self._place_component(p=(p1,p2),name=name,value=descr,type=type)

    def _place_component(self,p,name,value,type):
        self.comp_index+=1
        self.file.write('{type}{name} {p} {value}\n'.format(
                    type=type,
                    p=' '.join(map(str,p)),
                    name=name,
                    value=value))

    ############ SIMULAT  ############
    def sim_trans(self,step, stop, start=0):
        self.file.write('.tran {} {} {}\n'.format(step,stop,start))

    ############ CONTROL  ############
    def begin_control(self):
        self.file.write('.control\n')
    def run_control(self):
        self.file.write('run\n')
    def save(self,outfilename,*vectors,numdgt=4):
        self.file.write('set wr_singlescale\n')
        self.file.write('set wr_vecnames\n')
        self.file.write('option numdgt={}\n'.format(str(numdgt)))
        self.file.write('wrdata {out} {vecs}\n'.format(
        out=outfilename, vecs=' '.join(map('v({})'.format,vectors)),
        ))
    def end_control(self):
        self.file.write('.endc\n')

    ############ SUPPORTS ############
    def end(self):
        self.file.write('.end\n')
    def include(self,filename):
        self.file.write('.include {}\n'.format(filename))
    def comment(self,comment):
        self.file.write('*'+comment+'\n')
    def raw_write(self,text):
        self.file.write(text+'\n')
    def raw_write1(self,text):
        self.file.write(text)

    ########### TERMINAL ###########
    def run(self):
        try:
            self.file.close()
        except:
            pass
        return subprocess.run('ngspice -b {}'.format(self.filename),shell=True)
