Curo Housing Group faces significant challenges with inefficient property utilization. Many existing homes are under-occupied, while a substantial number of people remain on the waiting list for appropriate housing. To address this issue, we have developed a python coding solution utilizing Multiple Criteria Decision Analysis (MCDA) to optimize the allocation of housing resources. MCDA is a method that evaluates multiple conflicting criteria in decision-making, allowing us to prioritize tenants based on various factors such as family size, waiting time, and special needs (Belton and Stewart, 2002). Of course, when used in real life many more factors can be considered. This structured approach ensures that the allocation process is both efficient and fair, ultimately aiming to maximize property utilization and reduce waiting times. The example workflow for the solution is described below. 

Example Workflow 

Data Overview

Vacant Units: 

  1.  Unit 1: 3-bedroom, accessible (Units for special needs people) 

  2.  Unit 2: 2-bedroom, non-accessible 

  3.  Unit 3: 4-bedroom, accessible 

  4.  Unit 4: 3-bedroom, non-accessible  

Waiting List: 

  1.  Tenant A: 5 people, 2 years waiting, special needs 

  2.  Tenant B: 3 people, 1 year waiting 

  3.  Tenant C: 2 people, 3 years waiting, special needs 

  4.  Tenant D: 4 people, 2.5 years waiting  

Downsizing Candidates: 

  1.  Tenant X: Currently in 4-bedroom, willing to move to 2-bedroom 

  2.  Tenant Y: Currently in 3-bedroom, willing to move to 1-bedroom 

Step-by-Step Approach 

 Step 1: Data Collection 

We began by collecting data from three main sources: vacant units available for allocation, tenants on the waiting list, and current tenants willing to downsize. This data was compiled into Excel files to ensure a structured and systematic approach to analysis. 


Step 2: Define Criteria Weights 

To prioritize different factors affecting housing allocation, we established criteria weights, considering family size, waiting time, and special needs. Each criterion was assigned a specific weight reflecting its importance in the overall priority score calculation. 
 

Step 3: Apply MCDA for Downsizing 

Using the defined criteria weights, we calculated a priority score for each tenant willing to downsize. This involved evaluating each candidate based on family size, waiting time, and any special needs. The scores were then normalized to ensure fairness and sorted to identify the highest priority candidates. 


Step 4: Construct and Manage Vacancy Chains 

We identified vacancy chains by analysing the data from vacant properties, downsizing candidates, and the waiting list. This allowed us to understand the current housing stock and create sequences where one move triggers another, optimizing the utilization of available units. Next, we applied the same MCDA approach to tenants on the waiting list. Each tenant was scored based on the same criteria: family size, waiting time, and special needs. The scores were normalized and sorted to determine the allocation priority. 


Step 5: Allocate Housing 

The allocation process began by moving downsizing candidates to suitable smaller units first, as they had already expressed willingness to move. This freed up larger units, which were then allocated to tenants on the waiting list based on their priority scores. 
 

Step 6: Monitor and Adjust 

Continuous monitoring of the allocation process is essential. This includes reviewing feedback from tenants, assessing the efficiency of the allocation, and making necessary adjustments to improve the process. 
 

For example, Tenant X moved to a 2-bedroom unit, and Tenant Y moved to a 1-bedroom unit, freeing up larger units for families on the waiting list. Priority scores for downsizing candidates were calculated and normalized to identify the highest priority candidates for smaller units. By coordinating moves, we ensured multiple tenants moved in a sequence, minimizing the time units remained vacant. For instance, the vacated 4-bedroom unit from Tenant X was allocated to Tenant A, who had the highest priority on the waiting list. Tenants on the waiting list were scored and prioritized based on their needs. For example, Tenant A, with a high priority score, was allocated a newly vacated 4-bedroom unit. The remaining units were allocated based on the normalized priority scores, ensuring family size and specific needs were matched appropriately. 
