from .models import Role, Employee

def get_next_approver(current_approver, priority):
    current_role = current_approver.role

    if priority == 'Low':
        # Approve up to the next level
        next_role = Role.objects.filter(level__lt=current_role.level).order_by('-level').first()
    elif priority == 'Medium':
        # Approve up to two levels higher
        next_role = Role.objects.filter(level__lt=current_role.level).order_by('-level')[1:2].first()
    elif priority == 'High':
        # Progressively go to the highest level, one level at a time
        higher_roles = Role.objects.filter(level__lt=current_role.level).order_by('-level')
        next_role = higher_roles.first()  # Move one step up; the next approval will move further
    elif priority == 'Urgent':
        # Skip intermediate levels and go directly to the highest level
        next_role = Role.objects.filter(level=1).first()  # Level 1 = Headteacher

    # Return the next approver if a valid role exists
    if next_role:
        return Employee.objects.filter(role=next_role).first()
    return None
