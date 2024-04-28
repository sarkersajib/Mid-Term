class Star_Cinema:
    __hall_list = []

    def __init__(self)->None:
        pass

    def entry_hall(self,obj):
        self.__hall_list.append(obj)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self._show_list = []
        self.seats = {}

        self.entry_hall(self)

    def entry_show(self,id,movie_name,time):
        Bio = (id,movie_name,time)
        self._show_list.append(Bio)

      
        
        
        list =[]
        for _ in range(self.rows):
            list.append([])
        for row in list:
            for _ in range(self.cols):
                row.append(0)
    
     
        self.seats[id] =list

        
    def book_seats(self,seat_id,seat_list):
        if seat_id in self.seats:
            seat = self.seats[seat_id]
           
            i,j = seat_list
            if 0 <= i <self.rows and 0 <= j < self.cols:
            

                if seat[i][j] == 0:
                    seat[i][j] = 1
                    print("booked successfully !")
                else:
                    print("Already booked !")
        else:
            print("Not Found !")
    
    def view_show_list(self):
        for show in self._show_list:
            print(f"ID: {show[0]},Movie: {show[1]},Time: {show[2]}")

    def view_available_seats(self,id):
        if id in self.seats:
            sets = self.seats[id]
            for i in range(self.rows):
                for j in range(self.cols):

                    if sets[i][j] == 0:

                        print("seat is available !")
                        print(f"Row {i}, Col {j}")
                    else:
                        print("NOT Available")
        else:
            print("Invalid ID !")


hall1 = Hall(5,6,1)
hall1.entry_show(101,"Tiger","11:00 AM")
hall1.entry_show(102,"Salaar","4:00 PM")
run = True
while run:
   

    print("Option: \n")
    print("1 : View All Show Today")
    print("2 : View Available Seats")
    print("3 : Book Ticket")
    print("4 : Exit")

    ch = int(input("\nEnter Option : "))

    if ch==1:
        hall1.view_show_list()
    elif ch==2:
        id = int(input("Enter ID: "))
        hall1.view_available_seats(id)
    elif ch==3:
        seat_id = int(input("Enter seat id: "))
        rows = int(input("Enter row: "))
        cols = int(input("Enter col: "))
        hall1.book_seats(seat_id,(rows,cols))
    elif ch==4:
        print("Exit Done")
        break
    else:
        print("Invalid Option")

        







