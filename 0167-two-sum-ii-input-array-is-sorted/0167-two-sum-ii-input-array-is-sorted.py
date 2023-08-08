class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        for i in range(len(numbers)-1):
            
            if( numbers[i] + numbers[i+1] == target):
                return [i+1, i+2]
            else:
                if (target - numbers[i]) in numbers:
                    return [i+1,numbers.index(target-numbers[i])+1]
                
                    
                  
        
        
                
            # if numbers[j] == (target - numbers[i]) :

            #     res.append(i+1)
            #     res.append(numbers.index(target-numbers[i])+1)
            #     return res
            # else:
            #     i+=1

                 


