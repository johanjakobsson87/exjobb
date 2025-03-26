from JitterGenerator import JitterFileGenerator
import argparse
'''
jitterlength = 250  # (ms)
jitterstart = 640   # (ms)
jitterstop = 780    # (ms)
incrementBy = 20    # (ms)
'''


    

def main():
    parser = argparse.ArgumentParser(description="Generate jitter files with the parameters 1. jitterstart, 2. jitterstop, 3. jitterlength, and 4. incrementby")
    parser.add_argument("jitterstart", type = int, help = "The first jitter start time in milliseconds")
    parser.add_argument("jitterstop", type = int, help="The last jitter start time in milliseconds")
    parser.add_argument("jitterlength", type = int, help = "The length of the jitter in milliseconds")
    parser.add_argument("incrementby", type = int, help = "Value of the standard incrementation of time in milliseconds(default should be 20 ms)")

    arguments = parser.parse_args()
    
    
    JFgenerator = JitterFileGenerator()
    
    currentJitterStart = arguments.jitterstart
    while currentJitterStart <= arguments.jitterstop:
        print(f"Creating jitterfile with the parameters jitterstart: {currentJitterStart}, jitterstop: {currentJitterStart+arguments.jitterlength}, jitterlength: {arguments.jitterlength} and incrementby: {arguments.incrementby}")
        JFgenerator.generate_jitter_file(currentJitterStart, arguments.jitterlength)
        currentJitterStart += arguments.incrementby


if __name__ == "__main__":
    main()