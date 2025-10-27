"""
    Цей розділ хранить всі країни з даними
"""




austria = {
    "countrie": "Austria",
    "names":
        ["Manfred","Martin","Tobias","Jonathan","Thomas","Neris","Lois","Faren","Mikele","Lena"],
    "currency":"EUR",
    "phone_code":"+43",

    # робота
    "profession":{
            "Software Engineer":{"salary":{"min": 2800,"max":9000 }},
            "Mechanical Engineer": {"salary":{"min": 3200,"max":8000 }},
            "Teacher":{"salary":{"min": 3000,"max": 6000 }},
            "Doctor":{"salary":{"min": 6000,"max": 12000 }},
            "Farmer":{"salary":{"min": 3000,"max": 7500 }},
            "Data Analyst":{"salary":{"min": 2000,"max": 9500 }},
            "Electrician":{"salary":{"min": 3000,"max": 7000 }},
            "Nurse":{"salary":{"min": 2200,"max": 4800 }},
            "Sales Manager":{"salary":{"min": 2500,"max": 5500 }},
            "Graphic Designer":{"salary":{"min": 2000,"max": 5000 }}
    },

    "tax_rate": 0.25,  # Податкова ставка
    "cost_of_living": 1.2,  # Індекс вартості життя (1.0 = середній рівень)
    "inflation_rate": 0.02,

    # Спеціалізаця країни
    "specialization":{
        "sector": "industry",
        "factor": 1.0,
        "description": "Strong industrial and manufacturing base"
    }
}

usa = {
    "countrie": "United States of America",
    "names":
        ["Liana","Jose","Tobias","Jonathan","Thomas","Jovanni","Lois","Rosemary","Korbin","Lena"],
    "currency":"USD",
    "phone_code":"+1",

    # робота
    "profession":{
            "Software Engineer":{"salary":{"min": 2800,"max":9000 }},
            "Mechanical Engineer": {"salary":{"min": 3200,"max":8000 }},
            "Teacher":{"salary":{"min": 3000,"max": 6000 }},
            "Doctor":{"salary":{"min": 6000,"max": 12000 }},
            "Farmer":{"salary":{"min": 3000,"max": 7500 }},
            "Data Analyst":{"salary":{"min": 2000,"max": 9500 }},
            "Electrician":{"salary":{"min": 3000,"max": 7000 }},
            "Nurse":{"salary":{"min": 2200,"max": 7500 }},
            "Sales Manager":{"salary":{"min": 3000,"max": 5500 }},
            "Graphic Designer":{"salary":{"min": 3000,"max": 5000 }}
    },

    "tax_rate": 0.25,  # Податкова ставка
    "cost_of_living": 1.35,  # Індекс вартості життя (1.0 = середній рівень)
    "inflation_rate": 0.03,

    # Спеціалізаця країни
    "specialization": {
        "sector": "technology",  # Основний сектор (it, industry, agriculture, services, finance, etc.)
        "factor": 1.15,  # Коефіцієнт сили цього сектора
        "description": "Global leader in technology, innovation, and services"
    },
}

# === 1. Canada ===
canada = {
    "countrie": "Canada",
    "names": ["Oliver", "Emma", "Liam", "Sophia", "Noah", "Charlotte", "Ethan", "Isabella", "Lucas", "Amelia"],
    "currency": "CAD",
    "phone_code": "+1",
    "profession": {
        "Software Engineer": {"salary": {"min": 3500, "max": 9500}},
        "Mechanical Engineer": {"salary": {"min": 3200, "max": 8500}},
        "Teacher": {"salary": {"min": 2800, "max": 6000}},
        "Doctor": {"salary": {"min": 6000, "max": 14000}},
        "Farmer": {"salary": {"min": 2500, "max": 6000}},
        "Data Analyst": {"salary": {"min": 3000, "max": 9000}},
        "Electrician": {"salary": {"min": 2700, "max": 7000}},
        "Nurse": {"salary": {"min": 3200, "max": 8000}},
        "Sales Manager": {"salary": {"min": 2800, "max": 7000}},
        "Graphic Designer": {"salary": {"min": 2500, "max": 6000}}
    },
    "tax_rate": 0.28,
    "cost_of_living": 1.3,
    "inflation_rate": 0.025,
    "specialization": {
        "sector": "services",
        "factor": 1.0,
        "description": "Diverse service-based economy with strong technology and natural resources"
    }
}

# === 2. Germany ===
germany = {
    "countrie": "Germany",
    "names": ["Hans", "Lukas", "Sophie", "Anna", "Felix", "Lena", "Karl", "Mia", "Johann", "Lea"],
    "currency": "EUR",
    "phone_code": "+49",
    "profession": {
        "Software Engineer": {"salary": {"min": 3200, "max": 8500}},
        "Mechanical Engineer": {"salary": {"min": 3500, "max": 9500}},
        "Teacher": {"salary": {"min": 2800, "max": 6200}},
        "Doctor": {"salary": {"min": 5000, "max": 12000}},
        "Farmer": {"salary": {"min": 2000, "max": 5000}},
        "Data Analyst": {"salary": {"min": 3000, "max": 9000}},
        "Electrician": {"salary": {"min": 2600, "max": 6500}},
        "Nurse": {"salary": {"min": 2500, "max": 6000}},
        "Sales Manager": {"salary": {"min": 3000, "max": 7000}},
        "Graphic Designer": {"salary": {"min": 2500, "max": 5500}}
    },
    "tax_rate": 0.27,
    "cost_of_living": 1.25,
    "inflation_rate": 0.018,
    "specialization": {
        "sector": "industry",
        "factor": 1.1,
        "description": "Leading European industrial and automotive economy"
    }
}

# === 3. Japan ===
japan = {
    "countrie": "Japan",
    "names": ["Haruto", "Yuki", "Sakura", "Hana", "Ren", "Aoi", "Kaito", "Mei", "Riku", "Yuna"],
    "currency": "JPY",
    "phone_code": "+81",
    "profession": {
        "Software Engineer": {"salary": {"min": 3000, "max": 9000}},
        "Mechanical Engineer": {"salary": {"min": 3200, "max": 9500}},
        "Teacher": {"salary": {"min": 2500, "max": 5500}},
        "Doctor": {"salary": {"min": 5500, "max": 11000}},
        "Farmer": {"salary": {"min": 1800, "max": 4500}},
        "Data Analyst": {"salary": {"min": 2600, "max": 8500}},
        "Electrician": {"salary": {"min": 2200, "max": 6000}},
        "Nurse": {"salary": {"min": 2400, "max": 7000}},
        "Sales Manager": {"salary": {"min": 2800, "max": 6500}},
        "Graphic Designer": {"salary": {"min": 2300, "max": 6000}}
    },
    "tax_rate": 0.23,
    "cost_of_living": 1.4,
    "inflation_rate": 0.01,
    "specialization": {
        "sector": "technology",
        "factor": 1.2,
        "description": "Advanced technology and electronics industry"
    }
}

# === 4. United Kingdom ===
uk = {
    "countrie": "United Kingdom",
    "names": ["Oliver", "George", "Harry", "Jack", "Amelia", "Isla", "Emily", "Ava", "Freddie", "Sophie"],
    "currency": "GBP",
    "phone_code": "+44",
    "profession": {
        "Software Engineer": {"salary": {"min": 3500, "max": 9500}},
        "Mechanical Engineer": {"salary": {"min": 3300, "max": 8800}},
        "Teacher": {"salary": {"min": 2800, "max": 5500}},
        "Doctor": {"salary": {"min": 5500, "max": 11000}},
        "Farmer": {"salary": {"min": 2500, "max": 5200}},
        "Data Analyst": {"salary": {"min": 3000, "max": 8500}},
        "Electrician": {"salary": {"min": 2500, "max": 6200}},
        "Nurse": {"salary": {"min": 2700, "max": 6500}},
        "Sales Manager": {"salary": {"min": 3200, "max": 7000}},
        "Graphic Designer": {"salary": {"min": 2500, "max": 5800}}
    },
    "tax_rate": 0.26,
    "cost_of_living": 1.4,
    "inflation_rate": 0.02,
    "specialization": {
        "sector": "finance",
        "factor": 1.1,
        "description": "Strong financial and banking sector"
    }
}

# === 5. France ===
france = {
    "countrie": "France",
    "names": ["Lucas", "Hugo", "Léa", "Emma", "Louis", "Chloé", "Gabriel", "Jules", "Camille", "Sarah"],
    "currency": "EUR",
    "phone_code": "+33",
    "profession": {
        "Software Engineer": {"salary": {"min": 3000, "max": 8500}},
        "Mechanical Engineer": {"salary": {"min": 2800, "max": 8000}},
        "Teacher": {"salary": {"min": 2500, "max": 5000}},
        "Doctor": {"salary": {"min": 5000, "max": 11000}},
        "Farmer": {"salary": {"min": 1800, "max": 4800}},
        "Data Analyst": {"salary": {"min": 2700, "max": 8000}},
        "Electrician": {"salary": {"min": 2300, "max": 6200}},
        "Nurse": {"salary": {"min": 2400, "max": 6000}},
        "Sales Manager": {"salary": {"min": 2800, "max": 7000}},
        "Graphic Designer": {"salary": {"min": 2300, "max": 5500}}
    },
    "tax_rate": 0.28,
    "cost_of_living": 1.3,
    "inflation_rate": 0.018,
    "specialization": {
        "sector": "tourism",
        "factor": 1.0,
        "description": "Tourism, luxury goods and manufacturing economy"
    }
}

# === 6. India ===
india = {
    "countrie": "India",
    "names": ["Aarav", "Vivaan", "Aditya", "Diya", "Ananya", "Ishaan", "Riya", "Aryan", "Sneha", "Priya"],
    "currency": "INR",
    "phone_code": "+91",
    "profession": {
        "Software Engineer": {"salary": {"min": 800, "max": 4000}},
        "Mechanical Engineer": {"salary": {"min": 700, "max": 3500}},
        "Teacher": {"salary": {"min": 600, "max": 2000}},
        "Doctor": {"salary": {"min": 1200, "max": 6000}},
        "Farmer": {"salary": {"min": 400, "max": 1200}},
        "Data Analyst": {"salary": {"min": 700, "max": 3000}},
        "Electrician": {"salary": {"min": 500, "max": 2000}},
        "Nurse": {"salary": {"min": 600, "max": 2500}},
        "Sales Manager": {"salary": {"min": 700, "max": 3000}},
        "Graphic Designer": {"salary": {"min": 500, "max": 2500}}
    },
    "tax_rate": 0.18,
    "cost_of_living": 0.5,
    "inflation_rate": 0.05,
    "specialization": {
        "sector": "it",
        "factor": 1.1,
        "description": "Global IT and service outsourcing hub"
    }
}

# === 7. China ===
china = {
    "countrie": "China",
    "names": ["Wei", "Li", "Chen", "Ying", "Hua", "Jing", "Tao", "Lian", "Mei", "Bo"],
    "currency": "CNY",
    "phone_code": "+86",
    "profession": {
        "Software Engineer": {"salary": {"min": 2000, "max": 6000}},
        "Mechanical Engineer": {"salary": {"min": 1800, "max": 5500}},
        "Teacher": {"salary": {"min": 1500, "max": 3500}},
        "Doctor": {"salary": {"min": 2500, "max": 8000}},
        "Farmer": {"salary": {"min": 800, "max": 2000}},
        "Data Analyst": {"salary": {"min": 1800, "max": 6000}},
        "Electrician": {"salary": {"min": 1500, "max": 4000}},
        "Nurse": {"salary": {"min": 1600, "max": 4500}},
        "Sales Manager": {"salary": {"min": 2000, "max": 5500}},
        "Graphic Designer": {"salary": {"min": 1500, "max": 4500}}
    },
    "tax_rate": 0.2,
    "cost_of_living": 0.8,
    "inflation_rate": 0.03,
    "specialization": {
        "sector": "manufacturing",
        "factor": 1.2,
        "description": "World manufacturing and export powerhouse"
    }
}

# === 8. Brazil ===
brazil = {
    "countrie": "Brazil",
    "names": ["Gabriel", "Lucas", "Matheus", "Rafael", "Ana", "Julia", "Larissa", "Pedro", "Mariana", "João"],
    "currency": "BRL",
    "phone_code": "+55",
    "profession": {
        "Software Engineer": {"salary": {"min": 1500, "max": 6000}},
        "Mechanical Engineer": {"salary": {"min": 1300, "max": 5500}},
        "Teacher": {"salary": {"min": 1000, "max": 3500}},
        "Doctor": {"salary": {"min": 2500, "max": 9000}},
        "Farmer": {"salary": {"min": 800, "max": 2500}},
        "Data Analyst": {"salary": {"min": 1200, "max": 5000}},
        "Electrician": {"salary": {"min": 900, "max": 3000}},
        "Nurse": {"salary": {"min": 1000, "max": 4000}},
        "Sales Manager": {"salary": {"min": 1300, "max": 4500}},
        "Graphic Designer": {"salary": {"min": 1000, "max": 4000}}
    },
    "tax_rate": 0.22,
    "cost_of_living": 0.9,
    "inflation_rate": 0.04,
    "specialization": {
        "sector": "agriculture",
        "factor": 1.0,
        "description": "Agricultural and industrially developing economy"
    }
}

# === 9. Australia ===
australia = {
    "countrie": "Australia",
    "names": ["Liam", "Olivia", "Noah", "Ava", "Jack", "Isla", "Ethan", "Mia", "Harper", "William"],
    "currency": "AUD",
    "phone_code": "+61",
    "profession": {
        "Software Engineer": {"salary": {"min": 4000, "max": 10000}},
        "Mechanical Engineer": {"salary": {"min": 3500, "max": 9000}},
        "Teacher": {"salary": {"min": 3000, "max": 6000}},
        "Doctor": {"salary": {"min": 6000, "max": 13000}},
        "Farmer": {"salary": {"min": 2500, "max": 5500}},
        "Data Analyst": {"salary": {"min": 3200, "max": 9000}},
        "Electrician": {"salary": {"min": 2800, "max": 7000}},
        "Nurse": {"salary": {"min": 3200, "max": 7500}},
        "Sales Manager": {"salary": {"min": 3000, "max": 7000}},
        "Graphic Designer": {"salary": {"min": 2800, "max": 6000}}
    },
    "tax_rate": 0.26,
    "cost_of_living": 1.3,
    "inflation_rate": 0.025,
    "specialization": {
        "sector": "services",
        "factor": 1.0,
        "description": "Service-driven economy with strong mining and education sectors"
    }
}

# === 10. South Korea ===
south_korea = {
    "countrie": "South Korea",
    "names": ["Min-Jun", "Seo-Yeon", "Ji-Hoon", "Ha-Yun", "Ji-Woo", "Ye-Joon", "Soo-Bin", "Hyeon", "Yu-Jin", "Seo-Jin"],
    "currency": "KRW",
    "phone_code": "+82",
    "profession": {
        "Software Engineer": {"salary": {"min": 2800, "max": 8000}},
        "Mechanical Engineer": {"salary": {"min": 2500, "max": 7500}},
        "Teacher": {"salary": {"min": 2300, "max": 5000}},
        "Doctor": {"salary": {"min": 4000, "max": 10000}},
        "Farmer": {"salary": {"min": 1500, "max": 4000}},
        "Data Analyst": {"salary": {"min": 2600, "max": 7000}},
        "Electrician": {"salary": {"min": 2000, "max": 5000}},
        "Nurse": {"salary": {"min": 2200, "max": 5500}},
        "Sales Manager": {"salary": {"min": 2500, "max": 6500}},
        "Graphic Designer": {"salary": {"min": 2200, "max": 5500}}
    },
    "tax_rate": 0.23,
    "cost_of_living": 1.1,
    "inflation_rate": 0.02,
    "specialization": {
        "sector": "technology",
        "factor": 1.2,
        "description": "High-tech economy with strong electronics and automotive industries"
    }
}

