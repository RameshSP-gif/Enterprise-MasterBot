def classify_query(query):
    query = query.lower()
    if any(word in query for word in ["leave", "holiday", "vacation", "policy", "payroll"]):
        return "hr"
    elif any(word in query for word in ["invoice", "salary", "reimbursement", "budget"]):
        return "finance"
    elif any(word in query for word in ["campaign", "branding", "marketing", "advertisement"]):
        return "marketing"
    else:
        return "general"