import pandas as pd

# Step 1: Read Data from Excel Files
vacant_units_df = pd.read_excel('data/vacant_units.xlsx')
waiting_list_df = pd.read_excel('data/waiting_list.xlsx')
downsizing_candidates_df = pd.read_excel('data/downsizing_candidates.xlsx')

# Step 2: Define Criteria Weights
weights = {
    'Family_Size': 0.3,
    'Waiting_Time_In_Months': 0.4,
    'Special_Needs': 0.3
}

# Step 3: Define Function to Calculate Priority Score
def calculate_priority_score(row, weights):
    score = 0
    score += row.get('Family_Size', 0) * weights['Family_Size']
    score += row.get('Waiting_Time_In_Months', 0) * weights['Waiting_Time_In_Months']
    score += row.get('Special_Needs', 0) * weights['Special_Needs']
    return score

# Step 4: Apply MCDA for Downsizing
# 4.1 Apply the scoring function to downsizing candidates
downsizing_candidates_df['Priority Score'] = downsizing_candidates_df.apply(
    lambda row: calculate_priority_score(row, weights), axis=1)

# 4.2 Normalize scores
downsizing_candidates_df['Normalized Score'] = downsizing_candidates_df['Priority Score'] / downsizing_candidates_df[
    'Priority Score'].sum()

# 4.3 Sort by normalized score
downsizing_candidates_df = downsizing_candidates_df.sort_values(by='Normalized Score', ascending=False)

# Step 5: Apply MCDA for Waiting List
# 5.1 Apply the scoring function to waiting list
waiting_list_df['Priority Score'] = waiting_list_df.apply(
    lambda row: calculate_priority_score(row, weights), axis=1)

# 5.2 Normalize scores
waiting_list_df['Normalized Score'] = waiting_list_df['Priority Score'] / waiting_list_df['Priority Score'].sum()

# 5.3 Sort by normalized score
waiting_list_df = waiting_list_df.sort_values(by='Normalized Score', ascending=False)


# Step 6: Allocate Housing
# Function to allocate units
def allocate_units(vacant_units_df, waiting_list_df, downsizing_candidates_df):
    allocation = []

    # Move downsizing candidates first
    for candidate in downsizing_candidates_df.itertuples(index=False, name='Candidate'):
        for unit in vacant_units_df.itertuples(index=False, name='Unit'):
            if hasattr(candidate, 'Desired_Bedrooms'):
                if unit.Bedrooms == candidate.Desired_Bedrooms:
                    allocation.append((candidate.Tenant_ID, unit.Unit_ID))
                    vacant_units_df = vacant_units_df.drop(
                        vacant_units_df[vacant_units_df['Unit_ID'] == unit.Unit_ID].index)
                    break
            else:
                print(f"Error: 'Candidate' object has no attribute 'Desired_Bedrooms'")
                return []

    # Allocate remaining units based on priority
    for tenant in waiting_list_df.itertuples(index=False, name='Tenant'):
        for unit in vacant_units_df.itertuples(index=False, name='Unit'):
            if unit.Bedrooms >= tenant.Family_Size:
                allocation.append((tenant.Tenant_ID, unit.Unit_ID))
                vacant_units_df = vacant_units_df.drop(
                    vacant_units_df[vacant_units_df['Unit_ID'] == unit.Unit_ID].index)
                break

    return allocation

# Perform allocation
allocation_result = allocate_units(vacant_units_df, waiting_list_df, downsizing_candidates_df)

# Step 7: Display and Save Allocation Result
# Display allocation result
allocation_df = pd.DataFrame(allocation_result, columns=['Tenant_ID', 'Allocated_Unit_ID'])
print(allocation_df)

# Save the result to an Excel file
allocation_df.to_excel('data/allocation_result.xlsx', index=False)