'''
Created on Nov 10, 2018

@author: rAiN
'''

import Tkinter as tk
import turtle


class Room:
    def __init__(self, r_id, b_id, x, y, height, width, left_nbr, down_nbr):
        
        self.r_id = r_id
        self.b_id = b_id
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.left_nbr = left_nbr
        self.down_nbr = down_nbr
        
class Block:
    def __init__(self, block_id, parent, left_child, right_child, room_id, slice_type, height, width, area ):
        self.block_id = block_id
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        self.room_id  = room_id
        self.slice_type = slice_type
        self.height = height
        self.width = width
        self.area = area


pen = None
scale = 20
origin = {"x" : -100, "y" : -300}
block_arr = []
# block_ids give according to preorder traversal of slicing tree
room_arr = []
# HARDCODED PART..........................
block_arr.append(Block(0, None, 1, 2, None, 'V', 8.0, 12.0, 96.0)) 
block_arr.append(Block(1, 0, None, None, 1, 'N', 8.0, 4.0, 32.0))
block_arr.append(Block(2, 0, 3, 4, None, 'H', 8.0, 8.0, 64.0))
block_arr.append(Block(3, 2, None, None, 2, 'N', 4.0, 8.0, 32.0))
block_arr.append(Block(4, 2, 5, 6, None, 'V', 4.0, 8.0, 32.0))
block_arr.append(Block(5, 4, None, None, 4, 'N', 4.0, 4.0, 16.0))
block_arr.append(Block(6, 4, 7, 8, None, 'H', 4.0, 4.0, 16.0))
block_arr.append(Block(7, 6, None, None, 3, 'N', 2.0, 4.0, 8.0))
block_arr.append(Block(8, 6, None, None, 5, 'N', 2.0, 4.0, 8.0))
    
room_arr.append(Room(1,1,0,0,8,4,None, None))
room_arr.append(Room(2,3,4,4,4,8,1,3))
room_arr.append(Room(3,7,4,2,2,4,1,5))
room_arr.append(Room(4,5,8,0,4,4,5,None))
room_arr.append(Room(5,8,4,0,2,4,1,None))

# block_arr.append(Block(0, None, 1, 2, None, 'H', 9.0, 14.0, 126.0)) 
# block_arr.append(Block(1, 0, 3, 4, None, 'V', 4.0, 14.0, 56.0))
# block_arr.append(Block(2, 0, 9, 10, None, 'V', 5.0, 14.0, 70.0))
# block_arr.append(Block(3, 1, None, None, 1, 'N', 4.0, 4.0, 16.0))
# block_arr.append(Block(4, 1, 5, 6, None, 'V', 4.0, 10.0, 40.0))
# block_arr.append(Block(5, 4, 7, 8, None, 'H', 4.0, 7.0, 28.0))
# block_arr.append(Block(6, 4, None, None, 3, 'N', 4.0, 3.0, 12.0))
# block_arr.append(Block(7, 5, None, None, 2, 'N', 2.0, 7.0, 14.0))
# block_arr.append(Block(8, 5, None, None, 4, 'N', 2.0, 7.0, 14.0))
# block_arr.append(Block(9, 2, 11, 12, None, 'H', 5.0, 2.0, 10.0))
# block_arr.append(Block(10, 2, 13, 14, None, 'V', 5.0, 12.0, 60.0))
# block_arr.append(Block(11, 9, None, None, 6, 'N', 2.0, 2.0, 4.0))
# block_arr.append(Block(12, 9, None, None, 7, 'N', 3.0, 2.0, 6.0))
# block_arr.append(Block(13, 10, None, None, 8, 'N', 5.0, 1.0, 5.0))
# block_arr.append(Block(14, 10, 15, 20, None, 'V', 5.0, 11.0, 55.0))
# block_arr.append(Block(15, 14, 16, 17, None, 'H', 5.0, 9.0, 45.0))
# block_arr.append(Block(16, 15, None, None, 5, 'N', 3.0, 9.0, 27.0))
# block_arr.append(Block(17, 15, 18, 19, None, 'V', 2.0, 9.0, 18.0))
# block_arr.append(Block(18, 17, None, None, 9, 'N', 2.0, 7.0, 14.0))
# block_arr.append(Block(19, 17, None, None, 11, 'N', 2.0, 2.0, 4.0))
# block_arr.append(Block(20, 14, None, None, 10, 'N', 5.0, 2.0, 10.0))
#    
# room_arr.append(Room(1,3,0,5,4,4,None,6))
# room_arr.append(Room(2,7,4,7,2,7,1,4))
# room_arr.append(Room(3,6,11,5,4,3,4,5))
# room_arr.append(Room(4,8,4,5,2,7,1,5))
# room_arr.append(Room(5,16,3,2,3,9,8,9))
# room_arr.append(Room(6,11,0,3,2,2,None,7))
# room_arr.append(Room(7,12,0,0,3,2,None,None))
# room_arr.append(Room(8,13,2,0,5,1,7,None))
# room_arr.append(Room(9,18,3,0,2,7,8,None))
# room_arr.append(Room(10,20,12,0,5,2,11,None))
# room_arr.append(Room(11,19,10,0,2,2,9,None))
# HARDCODED PART ENDS..........................
def solve(init_turtle, final_turtle):
    print("Room details before Algorithm is run")
    print_room_details(block_arr[0], init_turtle)
    change_id = int(raw_input("Enter the room id of the room you want to change: "))
    change_block = find(block_arr[0], change_id)
    if(change_block == None):
        print "Room with id ", change_id, " does not exists"
        return
    choice = int(raw_input("Enter 1 to change height, 2 to change width: "))
    w = 0
    h = 0
    if(choice == 1):
        h = float(raw_input("Enter new height: "))
        w = change_block.area / h        
    elif(choice == 2):
        w = float(raw_input("Enter new width: "))
        h = change_block.area / w

    change_block.height = h
    change_block.width = w
    update_parent(block_arr[change_block.parent], change_block)
    
    update_room(room_arr[1])
    update_room(room_arr[3])
     
#     update_room(room_arr[2])
#     update_room(room_arr[1])
#     update_room(room_arr[0])
#     update_room(room_arr[9])
    
    print("After updation")
    print_room_details(block_arr[0], final_turtle)

def find(root, r_id):
    
    if (root == None): return None
    if (root.room_id == r_id):
        return root
    if(root.slice_type == 'N'): return
    l = find(block_arr[root.left_child], r_id)
    if l:
        return l
    return find(block_arr[root.right_child], r_id)

def print_room_details(root, pentype):
    if(root == None): return
    if root.room_id:
        print "id:",root.room_id, ", height:", root.height, ", width:", root.width
        draw_room(room_arr[root.room_id - 1], pentype)
        return
    print_room_details(block_arr[root.left_child], pentype)
    print_room_details(block_arr[root.right_child], pentype)
    
def draw_room(room, pentype):
    global pen
    pen = pentype
    pen.pencolor('red')
    pen.penup()
    pen.setposition(room.x * scale + origin["x"], room.y*scale + origin["y"])
    pen.pendown()
    pen.setposition((room.x + room.width)*scale + origin["x"], (room.y)*scale + origin["y"])
    pen.setposition((room.x + room.width)*scale + origin["x"], (room.y + room.height)*scale + origin["y"])
    pen.setposition((room.x)*scale + origin["x"], (room.y + room.height)*scale + origin["y"])
    pen.setposition((room.x)*scale + origin["x"], (room.y)*scale + origin["y"])
    
def update_parent(root, child):
    if(root == None): return
    if(root.slice_type == 'V'):
        root.height = child.height
        root.width = root.area / root.height
        if(block_arr[root.left_child].block_id == child.block_id):
            update_child(block_arr[root.right_child], child.height, -1)
        else:
            update_child(block_arr[root.left_child], child.height, -1)        
    
    elif(root.slice_type == 'H'):
        root.width = child.width
        root.height = root.area / root.width
        if(block_arr[root.left_child].block_id == child.block_id):
            update_child(block_arr[root.right_child], -1, child.width)
        else:
            update_child(block_arr[root.left_child], -1, child.width)   
    else: return
    if (root.parent != None): update_parent(block_arr[root.parent], root)
    else: 
        return
    

def update_child(root, height, width):
    if(height == -1):
        root.width = width
        root.height = root.area / root.width
    elif(width == -1):
        root.height = height
        root.width = root.area / root.height
    else: print("Fatal Error")
    
    if(root.slice_type == 'V'): 
            update_child(block_arr[root.left_child], root.height, -1)
            update_child(block_arr[root.right_child], root.height, -1)
    elif(root.slice_type == 'H'):
        update_child(block_arr[root.left_child], -1, root.width)
        update_child(block_arr[root.right_child], -1, root.width)
    else: return
    
def update_room(room):
    if(room.left_nbr == None and room.down_nbr == None) :
        room.x = 0
        room.y = 0
    elif(room.left_nbr == None):
        update_room(room_arr[room.down_nbr-1])
        room.x = 0
        room.y = room_arr[room.down_nbr-1].y + room_arr[room.down_nbr-1].height
    elif(room.down_nbr == None):
        update_room(room_arr[room.left_nbr-1])
        room.x = room_arr[room.left_nbr-1].x + room_arr[room.left_nbr-1].width
        room.y = 0
    else:
        update_room(room_arr[room.left_nbr-1])
        update_room(room_arr[room.down_nbr-1])
        room.x = room_arr[room.left_nbr-1].x + room_arr[room.left_nbr-1].width
        room.y = room_arr[room.down_nbr-1].y + room_arr[room.down_nbr-1].height
    room.height = block_arr[room.b_id].height
    room.width = block_arr[room.b_id].width
    
        
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Resizing Algo')
    root.geometry(str(1000)+'x'+str(600))
    root.resizable(0, 0)
    root.grid_columnconfigure(0, weight=1, uniform=1)
    root.grid_columnconfigure(1, weight=1, uniform=1)
    root.grid_rowconfigure(0, weight=1)
    
    border_details = {'highlightbackground':'black', 'highlightcolor':'black', 'highlightthickness':1}
     
    init_canvas = tk.Canvas(root, **border_details)
    init_canvas.pack_propagate(0)
    init_canvas.grid(row=0, column = 0, sticky='nsew', padx=4, pady=4)
    init_turtle = turtle.RawTurtle(init_canvas)
    
    final_canvas = tk.Canvas(root, **border_details)
    final_canvas.pack_propagate(0)
    final_canvas.grid(row=0, column = 1, sticky='nsew', padx=4, pady=4)
    final_turtle = turtle.RawTurtle(final_canvas)
    
    solve(init_turtle, final_turtle)
    root.mainloop()