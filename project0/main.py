import argparse
import project0

def main(url):
    data = project0.fetchIncidents(url)
    incidents = project0.extractIncidents(data)

    project0.createDB()

    project0.populatedb(incidents)

    project0.status()


if __name__== '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("--incidents",type=str,required=True,help="The incidents url")

    args=parser.parse_args()
    if args.incidents:
        main(args.incidents)


