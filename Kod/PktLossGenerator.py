# Program that takes packetloss time and packetloss length as inputs and generates a packetloss file (.txt) as output.
# A packetloss file is a file that contains the frame number and the timestamp of the frame.
class PaketlossGenerator:
    def __init__(self, numberOfFrames = 275, startingMS = 520):
        self.numberOfFrames = numberOfFrames
        self.startingMS = startingMS

    def generate_packetloss_file(self, PktLossTime, PktLossLength):
        #Init arrays
        timestamps = []
        frameArray = []
        
        #Calculate index of Pktloss and the number of lost frames
        pktLossStartIndex  = int((PktLossTime - self.startingMS) / 20 )
        numberOfFrameslost = int(PktLossLength/20)
        
        # Create array of timestamps
        for i in range(0, (self.numberOfFrames - numberOfFrameslost)):
            if i == 0:
                MS = self.startingMS
            else:
                MS = timestamps[i-1] + 20
            
            if i == pktLossStartIndex:
                MS+=PktLossLength
            timestamps.append(MS)    
            
        #Create array of packets
        packetnumber = 0
        for i in range(0,(self.numberOfFrames - numberOfFrameslost)):
            packetnumber += 1
            if i ==pktLossStartIndex:
                packetnumber += numberOfFrameslost
            frameArray.append(packetnumber)


        #DEBUGGING#
        '''
        print("Framearray: ")    
        print(len(frameArray))
        print(frameArray)
        print("Timestamps: ")
        print(len(timestamps))
        print(timestamps)      
        print("Number of frames: ",self.numberOfFrames)
        '''    
        
        # Create PktLossFile.txt
        with open(f"./pktlossfiles/pktlossfile_{PktLossLength}msLossAt{PktLossTime}.txt", "w") as f:
            for i in range(self.numberOfFrames-numberOfFrameslost):
                f.write(f"{frameArray[i]}, {timestamps[i]}\n")

                
'''
def main():    
    PLgenerator = PaketlossGenerator()
    PLgenerator.generate_packetloss_file(520, 1000)

if __name__ == "__main__":
    main()
   '''