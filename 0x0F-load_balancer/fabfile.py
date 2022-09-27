from fabric.api import *

def list_root():
    local('ls /')
