from PktLossGenerator import PaketlossGenerator
import argparse

def main():
    parser = argparse.ArgumentParser(description="Generate packet loss files with the parameters 1. jitterstart, 2. jitterstop, 3. jitterlength, and 4. incrementby")
    parser.add_argument("PLstart", type = int, help = "The first packet loss time in milliseconds")
    parser.add_argument("PLstop", type = int, help="The last packet loss start time in milliseconds")
    parser.add_argument("PLlength", type = int, help = "The length of the packet loss in milliseconds")
    parser.add_argument("incrementby", type = int, help = "Value of the standard incrementation of time in milliseconds(default should be 20 ms)")
    arguments = parser.parse_args()
    
    PLgenerator = PaketlossGenerator()
    
    currentPLstart = arguments.PLstart
    while currentPLstart <= arguments.PLstop:
        print(f"Creating packetloss file with the parameters PLstart: {currentPLstart}, PLstop: {arguments.PLstop}, PL_length: {arguments.PLlength} and incrementby: {arguments.incrementby}")
        PLgenerator.generate_packetloss_file(currentPLstart, arguments.PLlength)
        currentPLstart += arguments.incrementby

if __name__ == "__main__":
    main()