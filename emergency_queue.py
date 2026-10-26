class Patient():
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency



class MinHeap:
    def __init__(self):
        self.data = [] #List of patient instances. Index 0 is the most urgent patient.

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            current_task = self.data[index]
            parent_task = self.data[parent_index]

            if current_task.urgency < parent_task.urgency:
                temp = self.data[index]
                self.data[index] = self.data[parent_index]
                self.data[parent_index] = temp

                index = parent_index
            else:
                break
        
    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)


    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
            smallest = left

        if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right

        if smallest != index:
            temp = self.data[index]
            self.data[index] = self.data[smallest]
            self.data[smallest] = temp

            self.heapify_down(smallest)

    def remove_min(self):
        if not self.data:
            return None

        if len(self.data) == 1:
            return self.data.pop()

        min_value = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return min_value
    
    def peek(self):
        a_patient = self.data[0]
        return a_patient


    def print_heap(self):
        print("\nCurrent Patients:")
        for patient in self.data:
            print(f"Patient Name: {patient.name}, Urgency: {patient.urgency}")

heap = MinHeap()
heap.insert(Patient("Talia", 3))
heap.insert(Patient("Steven", 1))
heap.insert(Patient("Billy", 5))
heap.print_heap()

next_up = heap.peek()
print(next_up.name, next_up.urgency)

served = heap.remove_min()
print(served.name)
heap.print_heap()

