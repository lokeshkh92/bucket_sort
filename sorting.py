class Sort:
    # Define insertion sort
    def insertionSort(self,bucket):
        for i in range (1, len (bucket)):
            var = bucket[i]
            j = i - 1
            while (j >= 0 and var < bucket[j]):
                bucket[j + 1] = bucket[j]
                j = j - 1
            bucket[j + 1] = var

    # Define bucket sort
    def bucketSort(self,sortList):
        #Find max Value and sorting number of list
        max_Value = max(sortList)
        sort_number = max_Value/len(sortList)

        #Create an empty list to append the sorted elements
        List1 = []
        for x in range(len(sortList)):
            List1.append([])

        # Put list elements into different buckets based on the number size
        for i in range(len(sortList)):
            bucketKey = int(sortList[i]/len(sortList))
            if bucketKey >= len(sortList):
                while bucketKey >= len(sortList):
                    bucketKey = bucketKey - 1
                List1[bucketKey].append(sortList[i])
            else:
                List1[bucketKey].append(sortList[i])

        # Sort elements within the buckets using Insertion Sort
        for z in range(len(sortList)):
            self.insertionSort(List1[z])

        # Concatenate buckets with sorted elements into a single list
        final_List = []
        for x in range(len (sortList)):
            final_List = final_List + List1[x]
        return final_List


def main():
    S = Sort()
    #list_to_be_sorted = [1.20,0.22,0.43,0.36,0.39,0.27]
    list_to_be_sorted = input("Enter list to be sorted: ")
    print("input List: {} ".format(list_to_be_sorted))
    print("Sorted List: {} ".format(S.bucketSort(list_to_be_sorted)))
    print("Testing is Fun")

if __name__ == "__main__":
    main()
