import ROOT
import os
import sys

os.mkdir("TH1Fs")

def convert(file_in,file_out):
    f = ROOT.TFile(file_in)
    fout = ROOT.TFile("TH1Fs/"+file_out,"RECREATE")
    for key in f.GetListOfKeys():
        h1D = f.Get(key.GetName())
        h1F = ROOT.TH1F()
        h1D.Copy(h1F)
        
        fout.cd()
        h1F.Write()

for name in ["vhbb_Wen-2017.root","vhbb_Wmn-2017.root","vhbb_Zee-2017.root","vhbb_Zmm-2017.root","vhbb_Znn-2017.root"]:
    print(name)
    convert(name,name)


