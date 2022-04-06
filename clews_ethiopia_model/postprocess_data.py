import os.path
import sys


COLMAP = {
    "AccumulatedNewCapacity": ["REGION", "TECHNOLOGY", "YEAR"],
    "AnnualEmissions": ["REGION", "EMISSION", "YEAR"],
    "AnnualFixedOperatingCost": ["REGION", "TECHNOLOGY", "YEAR"],
    "AnnualTechnologyEmission": ["REGION", "TECHNOLOGY", "EMISSION", "YEAR"],
    "AnnualTechnologyEmissionByMode": ["REGION", "TECHNOLOGY", "EMISSION", "MODE_OF_OPERATION", "YEAR"],
    "AnnualVariableOperatingCost": ["REGION", "TECHNOLOGY", "YEAR"],
    "CapitalInvestment": ["REGION", "TECHNOLOGY", "YEAR"],
    "Demand": ["REGION", "TIMESLICE", "COMMODITY", "YEAR"],
    "DiscountedSalvageValue": ["REGION", "TECHNOLOGY", "YEAR"],
    "DiscountedTechnologyEmissionsPenalty": ["REGION", "TECHNOLOGY", "YEAR"],
    "NewCapacity": ["REGION", "TECHNOLOGY", "YEAR"],
    "NewStorageCapacity": ["REGION", "STORAGE", "YEAR"],
    "NumberOfNewTechnologyUnits": ["REGION", "TECHNOLOGY", "YEAR"],
    "ProductionByTechnologyAnnual": ["REGION", "TECHNOLOGY", "COMMODITY", "YEAR"],
    "RateOfActivity": ["REGION", "TIMESLICE", "TECHNOLOGY", "MODE_OF_OPERATION", "YEAR"],
    "RateOfTotalActivity": ["REGION", "TECHNOLOGY", "TIMESLICE", "YEAR"],
    "SalvageValue": ["REGION", "TECHNOLOGY", "YEAR"],
    "SalvageValueStorage": ["REGION", "STORAGE", "YEAR"],
    "TechnologyActivityChangeByMode": ["REGION", "TECHNOLOGY", "MODE_OF_OPERATION", "YEAR"],
    "TechnologyActivityChangeByModeCostTotal": ["REGION", "TECHNOLOGY", "MODE_OF_OPERATION", "YEAR"],
    "TotalAnnualTechnologyActivityByMode": ["REGION", "TECHNOLOGY", "MODE_OF_OPERATION", "YEAR"],
    "TotalCapacityAnnual": ["REGION", "TECHNOLOGY", "YEAR"],
    "TotalTechnologyAnnualActivity": ["REGION", "TECHNOLOGY", "YEAR"],
    "TotalTechnologyModelPeriodActivity": ["REGION", "TECHNOLOGY"],
    "Trade": ["REGION", "REGION", "TIMESLICE", "COMMODITY", "YEAR"],
}


def main(results_infile, output_dir):
    curr_file = None
    with open(results_infile, "r") as infile:
        for in_line in infile:
            if in_line.startswith("**"):
                continue
            records = in_line.split()
            output_line = f"{records[1].replace('(', ',').replace(')', ',')}{records[2]}"
            table_name, *data = output_line.split(',')
            filename = os.path.join(output_dir, f"{table_name}.csv")
            if not data:
                continue

            if curr_file is None or curr_file.name != filename:
                if hasattr(curr_file, "close"):
                    curr_file.close()
                curr_file = open(filename, "w")
                try:
                    columns = COLMAP[table_name]
                    curr_file.write(",".join(columns) + ",VALUE\n")
                except KeyError:
                    print(f"Unknown columns for table '{table_name}'")

            curr_file.write(",".join(data) + "\n")

    if hasattr(curr_file, "close"):
        curr_file.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        msg = "Usage: python {} <input_file> <output_dir>"
        print(msg.format(sys.argv[0]))
        sys.exit(1)
    else:
        results_infile = sys.argv[1]
        output_dir = sys.argv[2]
        if not os.path.isdir(output_dir):
            msg = "Usage: python {} <input_file> <output_dir>\n    output_dir must be a directory"
            print(msg.format(sys.argv[0]))
            sys.exit(1)

        main(results_infile, output_dir)
