def recommendation_badge(

    recommendation

):

    badges = {

        "Priority Entry":
            ("⭐", "green"),

        "Strong Candidate":
            ("🟢", "blue"),

        "Monitor":
            ("🟡", "orange"),

        "Avoid":
            ("🔴", "red")

    }


    return badges.get(

        recommendation,

        ("⚪", "gray")

    )