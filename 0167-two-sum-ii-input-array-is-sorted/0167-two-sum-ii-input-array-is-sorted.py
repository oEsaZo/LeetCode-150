class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        for i in range(len(numbers)-1):
            j=i+1
            if( numbers[i] + numbers[j] == target):
                return [i+1, j+1]
            else:
                if (target - numbers[i]) in numbers:
                    return [i+1,numbers.index(target-numbers[i])+1]
                
                    
                  
        
        
                
            # if numbers[j] == (target - numbers[i]) :

            #     res.append(i+1)
            #     res.append(numbers.index(target-numbers[i])+1)
            #     return res
            # else:
            #     i+=1

                 


