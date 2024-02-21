import math
import table

x = 0
if x: 
 print('hello')

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
        self.sub_header.append("Total Shear")
        shear_plane1 = self.shear.plane1
        shear_plane2 = self.shear.plane2
        for plane1, plane2 in zip(shear_plane1, shear_plane2):
            self.total_shear.append(math.sqrt(plane1**2 + plane2**2))
        # add total_shear as a new column to the body of the table.
        self.add_column(self.total_shear)

    def __getitem__(self, index):
        return self.body[index]

    def __len__(self):
        return len(self.body)

    def __str__(self) -> str:
        return f"CBar<{self.element_id}>"

    def __repr__(self) -> str:
        return f"CBar<{self.element_id}>"


if __name__ == "__main__":
    table = table.all_tables("fileaa")
    c1 = CBar(table[-1])
    print(c1)
