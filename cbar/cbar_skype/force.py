import math
import table
# import matplotlib.pyplot as plt

class MomentA:
    plane1 = []
    plane2 = []


class MomentB:
    plane1 = []
    plane2 = []


class Shear:
    plane1 = []
    plane2 = []


class Axial:
    force = []


class CBar:
    """Get a list contain header, subheader and table data to
    Create Cbar object
    """

    def __init__(self, table):
        self.table = table
        self.element_id = self.table.get("element_id")
        self.header = self.table.get("header")
        self.sub_header = self.table.get("sub_header") 
        self.body = self.table.get("body") 
        self.el_type = self.table.get("el_type") 
        self.time = []
        self.moment_a = MomentA()
        self.moment_b = MomentB()
        self.shear = Shear()
        self.axial = Axial()
        self.torque = []
        self.total_shear = []
        # call force method to create forces columns for Cbar
        self._forces()
        self._total_shear()

    def row(self, index=0):
        """get a row index and return the row as list if it exsist"""
        try:
            return self.body[index]
        except IndexError:
            print("Index out of range")
            return []

    def _forces(self):
        """Create forces object for each force of a CBar."""
        for row in self.body:
            self.time.append(row[0])
            self.moment_a.plane1.append(row[1])
            self.moment_a.plane2.append(row[2])
            self.moment_b.plane1.append(row[3])
            self.moment_b.plane2.append(row[4])
            self.shear.plane1.append(row[5])
            self.shear.plane2.append(row[6])
            self.axial.force.append(row[7])
            self.torque.append(row[8])
        return None

    def add_column(self, column):
        """Add new column to the body of the table."""
        for row, item in zip(self.body, column):
            row.append(item)

    def _total_shear(self):
       
        shear_plane1 = self.shear.plane1
        shear_plane2 = self.shear.plane2
        for plane1, plane2 in zip(shear_plane1, shear_plane2):
            self.total_shear.append(math.sqrt(plane1**2 + plane2**2))
        # add total_shear as a new column to the body of the table.
        
        if "Total Shear" not in self.header:
            self.header.append("Total Shear")
            self.add_column(self.total_shear)

    def __getitem__(self, index):
        return self.body[index]

    def __len__(self) -> int:
        return len(self.body)

    def __str__(self) -> str:
        return f"CBar<{self.element_id}>"

    def __repr__(self) -> str:
        return f"CBar<{self.element_id}>"


class CBush():
   
      # TIME           FORCE-X       FORCE-Y       FORCE-Z      MOMENT-X      MOMENT-Y      MOMENT-Z

    def __init__(self, table):
        self.table = table
        self.element_id = self.table.get("element_id")
        self.header = self.table.get("header")
        self.body = self.table.get("body") 
        self.el_type = self.table.get("el_type") 
        self.time = []
        self.moment_x = []
        self.moment_y = []
        self.moment_z = []
        self.force_x = []
        self.force_y = []
        self.force_z = []
        self.total_shear = []
        # call force method to create forces columns for Cbar
        self._forces()
        self._total_shear()        
        
    def row(self, index=0):
        """get a row index and return the row as list if it exsist"""
        try:
            return self.body[index]
        except IndexError:
            print("Index out of range")
            return []

    def _forces(self):
        """Create forces object for each force of a CBar."""
        for row in self.body:
            self.time.append(row[1])
            self.force_x.append(row[2])
            self.force_y.append(row[3])
            self.force_z.append(row[4])

            self.moment_x.append(row[5])
            self.moment_y.append(row[6])
            self.moment_z.append(row[7])


        return None

    def add_column(self, column):
        """Add new column to the body of the table."""
        for row, item in zip(self.body, column):
            row.append(item)

    def _total_shear(self):
        
        shear_plane1 = self.force_y
        shear_plane2 = self.force_z
        for plane1, plane2 in zip(shear_plane1, shear_plane2):
            self.total_shear.append(math.sqrt(plane1**2 + plane2**2))
        # add total_shear as a new column to the body of the table.
        if "Total Shear" not in self.header:
            self.header.append("Total Shear")
            self.add_column(self.total_shear)

    def __getitem__(self, index):
        return self.body[index]

    def __len__(self) -> int:
        return len(self.body)

    def __str__(self) -> str:
        return f"CBush<{self.element_id}>"

    def __repr__(self) -> str:
        return f"CBush<{self.element_id}>"


if __name__ == "__main__":
    # in windows path isn't seperate witn `/` it's required to be handled 
    tables = table.read_pickle("/nobackup/vol01/a420192/GSO/CNA_7139_MV2_Hood/cvm_bolt/it12/test_it/PPVT736_CNA_7139_it12_U_sol112t_008.f06.pickle")
    #tables = table.read_pickle("/nobackup/vol01/a420192/GSO/CNA_7139_MV2_Hood/cvm_bolt/it2/test/xaa.pickle")
    table0 = tables[0]
    c1 = CBar(table0)
    print(c1)
    print(c1.header)
    # y = c1.force_y
    # x = c1.time
    # plt.figure()
    # plt.plot(x, y, marker='o', linestyle='-', color='b', label='Data')

    # # Add labels and title
    # plt.xlabel('Time')
    # plt.ylabel('total shear')
    # plt.title('Simple Line Plot')
    
    # # Add a legend
    # plt.legend()
    
    # # Show the plot
    # plt.show()
