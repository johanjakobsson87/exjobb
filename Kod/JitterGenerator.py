# Program that takes JitterStart and JitterLength as inputs and generates a jitterfile (.txt) as output.







class JitterFileGenerator:
    def __init__(self, numberOfFrames = 275, startingMS = 520):
        self.numberOfFrames = numberOfFrames
        self.startingMS = startingMS

    def generate_jitter_file(self, JitterStart, JitterLength):
        timestamps = []
        
        # Create array of timestamps
        for i in range(0, self.numberOfFrames):
            MS = self.startingMS + 20*i    
            timestamps.append(MS)
        
        # Get start and end index of jitter
        jitterStartIndex = int((JitterStart - self.startingMS) / 20 )
        print("Jitter start index: ", jitterStartIndex)
        jitterEndIndex =  int(((JitterStart + JitterLength)- self.startingMS) / 20)
        print("Jitter end index: ", jitterEndIndex)

        # Add jitter between the startindex and the endindex of the jitter. All following timestamps increments by 20
        for i in range(jitterStartIndex, jitterEndIndex):
            if i < self.numberOfFrames:
                timestamps[i] = JitterStart + JitterLength                
        for i in range(jitterEndIndex+1, self.numberOfFrames):
            timestamps[i] = timestamps[i-1] + 20

        # Create JitterFile.txt
        with open(f"./jitterfiles/jitterfile_Burstjitter_{JitterLength}msDelayAt{JitterStart}.txt", "w") as f:
            for i in range(self.numberOfFrames):
                f.write(f"{i+1}, {timestamps[i]}\n")
                


def main():
    
    
    JFgenerator = JitterFileGenerator()
    JFgenerator.generate_jitter_file(1540, 1500)


if __name__ == "__main__":
    main()