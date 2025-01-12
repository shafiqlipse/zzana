

def room_name_processor(request):
    # Provide a default room name or dynamically fetch based on request
    return {
        'room_name': request.GET.get('room_name', 'default_room'),  # Example: use 'default_room' if no room_name is provided
    }