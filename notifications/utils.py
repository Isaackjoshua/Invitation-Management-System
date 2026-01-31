def build_ticket_sms(event, attendee, ticket):
    return event.sms_template.format(
        name=attendee.full_name,
        event=event.name,
        code=ticket.numeric_code
    )
