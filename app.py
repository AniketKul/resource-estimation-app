from flask import Flask, render_template
from scripts import story1 as s1, story2 as s2
import pandas as pd

app = Flask(__name__)

# Assign hardware filename to `file`
file_hardware = 'hardware.xlsx'

# Load spreadsheet
xl_hardware = pd.ExcelFile(file_hardware)


# Load a sheet into a DataFrame by name: df_hardware
df = xl_hardware.parse('Page 1')
print(df)

df_hardware = df[df["Group"] != "Marketing"]

#print(df_hardware["Group"].unique())

#print(df_hardware)

# Assign prices filename to `file`
file_prices = 'prices.xlsx'
#Load Spreadsheet
xl_prices = pd.ExcelFile(file_prices)

# print(xl1.sheet_names)

# Load a sheet into a DataFrame by name: df_prices
df_prices = xl_prices.parse('Sheet1')

# Assign hardware filename to `file`
file_hardware = 'hardware.xlsx'

@app.route('/')
def todo():
    # Render default page templat
    listOfDept = s1.listOfAllDepartments(df_hardware)
    return render_template('listOfAllDepartments.html', items=listOfDept)


@app.route('/listOfAppsByDept', methods=['GET'])
def listOfAppsByDept():
    listOfApps = s1.listOfAllAppByDepartments(df_hardware)
    return render_template('listOfAppsByDept.html', items=listOfApps)


@app.route('/cpuMemByDept', methods=['GET'])
def cpuMemByDept():
    cpuMemByD = s1.noOfCPUMemByDep(df_hardware)
    return render_template('cpuMemByDept.html', items=cpuMemByD)


@app.route('/cpuMemByApp', methods=['GET'])
def cpuMemByApp():
    cpuMemByA = s1.noOfCPUMemByApp(df_hardware)
    return render_template('cpuMemByApp.html', items=cpuMemByA)


@app.route('/cpuMemByDC', methods=['GET'])
def cpuMemByDC():
    cpuMemBydc = s1.noOfCPUMemByDataCenters(df_hardware)
    return render_template('cpuMemByDC.html', items=cpuMemBydc)


@app.route('/cost', methods=['GET'])
def cost():
    costByDept = s2.Estimate(df_hardware, df_prices)
    return render_template('cost.html', items=costByDept)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)