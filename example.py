from MoveToBeacon1D import MoveToBeacon1D

if __name__ == '__main__':
    environment = MoveToBeacon1D()
    state,reward,_,_ = environment.step(-1)

    print(state,reward)

