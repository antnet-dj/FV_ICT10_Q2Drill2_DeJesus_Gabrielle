from pyscript import document, display

# sets of members
grade_7 = {"Isaac Hilary", "Rose Harriette"}
grade_8 = {"Kinita Hanan", "Miyana Lee"}
grade_9 = {"Theodore Marianus", "Amber Stone"}
grade_10 = {"Ash Zackery", "Kael Xochitl"}

# combine all sets
all_members = grade_7 | grade_8 | grade_9 | grade_10

# function to add a new member
def add_member(event):
    global all_members

    # get the names from the text boxes
    first = document.querySelector("#first_name").value
    last = document.querySelector("#last_name").value
    new_member = first + " " + last     # combine the names
    all_members = all_members | {new_member}     # add the new member
    members_list = "<br>".join(sorted(all_members))     # sort the members alphabetically

    # display the results
    document.querySelector("#results").innerHTML = f""" 
    <h3>All Members</h3>
    {members_list}
    <h3>Total Members: {len(all_members)}</h3>
    """