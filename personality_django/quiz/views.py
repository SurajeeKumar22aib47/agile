# quiz/views.py

import logging
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuizForm
from .models import PersonalityType,Question,TopicScore
from django.http import  HttpResponse

from django.shortcuts import render, get_object_or_404
from .models import PersonalityType
logger = logging.getLogger(__name__)
def home(request):
    return render(request,'home.html')
from django.shortcuts import render, redirect
from .forms import QuizForm



def index(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            answers = list(form.cleaned_data.values())
            personality_code = calculate_points(answers)
            request.session['personality_code'] = personality_code
            return redirect('careerquiz')  # Redirect to career quiz
    else:
        form = QuizForm()
    
    return render(request, 'index.html', {'form': form})


def result(request):
    personality_code = request.session.get('personality_code')
    logger.debug(f"Retrieved personality code from session: {personality_code}")  # Log the retrieved personality code
    try:
        personality_type = get_object_or_404(PersonalityType, code=personality_code)
        return render(request, 'result.html', {'personality_type': personality_type})
    except PersonalityType.DoesNotExist:
        logger.error(f"PersonalityType with code '{personality_code}' does not exist.")  # Log the error
        return render(request, 'error.html', {'error_message': 'Personality type not found'})

def calculate_points(answers):
    e = i = s = n = t = f = j = p = 0
    for idx, answer in enumerate(answers):
        if (idx % 7 == 0):
            if answer == '1':
                e += 1
            elif answer == '2':
                i += 1
        elif (idx % 7 in [1, 2]):
            if answer == '1':
                s += 1
            elif answer == '2':
                n += 1
        elif (idx % 7 in [3, 4]):
            if answer == '1':
                t += 1
            elif answer == '2':
                f += 1
        elif (idx % 7 in [5, 6]):
            if answer == '1':
                j += 1
            elif answer == '2':
                p += 1

    personality = ''
    personality += 'E' if e > i else 'I'
    personality += 'S' if s > n else 'N'
    personality += 'T' if t > f else 'F'
    personality += 'J' if j > p else 'P'

    return personality

marketingManagerQuestions = [
    {
        "question": "What is the primary role of a Marketing Manager?",
        "options": [
            "Developing and implementing marketing strategies",
            "Recruiting and managing employees",
            "Selling products or services",
            "Handling customer inquiries and complaints"
        ],
        "answer": "Developing and implementing marketing strategies"
    },
    {
        "question": "Which of the following is a key responsibility of a Marketing Manager?",
        "options": [
            "Conducting market research",
            "Managing payroll and benefits",
            "Analyzing financial data",
            "Writing press releases"
        ],
        "answer": "Conducting market research"
    },
    {
        "question": "What is the purpose of managing advertising campaigns?",
        "options": [
            "To increase brand awareness and drive sales",
            "To recruit new employees",
            "To handle employee relations",
            "To provide customer service"
        ],
        "answer": "To increase brand awareness and drive sales"
    },
    {
        "question": "Which of the following tools is commonly used in digital marketing?",
        "options": [
            "Google Analytics",
            "Microsoft Excel",
            "Adobe Photoshop",
            "AutoCAD"
        ],
        "answer": "Google Analytics"
    },
    {
        "question": "What is the significance of SEO in marketing?",
        "options": [
            "To improve website visibility in search engine results",
            "To manage employee payroll",
            "To analyze financial trends",
            "To handle public relations"
        ],
        "answer": "To improve website visibility in search engine results"
    },
    {
        "question": "Which of the following is a common marketing strategy?",
        "options": [
            "Content marketing",
            "Employee training",
            "Customer complaint resolution",
            "Financial auditing"
        ],
        "answer": "Content marketing"
    },
    {
        "question": "What is the role of social media in marketing?",
        "options": [
            "To engage with customers and promote products",
            "To conduct employee evaluations",
            "To analyze market trends",
            "To manage company finances"
        ],
        "answer": "To engage with customers and promote products"
    },
    {
        "question": "Which metric is commonly used to measure the success of a marketing campaign?",
        "options": [
            "Return on Investment (ROI)",
            "Employee turnover rate",
            "Customer satisfaction score",
            "Gross profit margin"
        ],
        "answer": "Return on Investment (ROI)"
    },
    {
        "question": "What is the primary goal of brand management?",
        "options": [
            "To create a strong, positive perception of the company",
            "To recruit talented employees",
            "To manage employee benefits",
            "To provide customer support"
        ],
        "answer": "To create a strong, positive perception of the company"
    },
    {
        "question": "Which of the following best describes 'target market'?",
        "options": [
            "A specific group of potential customers for a product",
            "A database of all company employees",
            "A list of financial assets",
            "A collection of customer complaints"
        ],
        "answer": "A specific group of potential customers for a product"
    }
]
hrManagerQuestions = [
    {
        "question": "What is the primary role of a Human Resources (HR) Manager?",
        "options": [
            "Recruiting and managing employees",
            "Developing marketing strategies",
            "Selling products or services",
            "Handling customer inquiries and complaints"
        ],
        "answer": "Recruiting and managing employees"
    },
    {
        "question": "Which of the following is a key responsibility of an HR Manager?",
        "options": [
            "Handling employee relations",
            "Managing advertising campaigns",
            "Analyzing financial data",
            "Writing press releases"
        ],
        "answer": "Handling employee relations"
    },
    {
        "question": "What is the purpose of conducting employee evaluations?",
        "options": [
            "To assess performance and provide feedback",
            "To increase brand awareness",
            "To handle customer service",
            "To analyze market trends"
        ],
        "answer": "To assess performance and provide feedback"
    },
    {
        "question": "Which tool is commonly used in HR management?",
        "options": [
            "Human Resource Information System (HRIS)",
            "Google Analytics",
            "Adobe Photoshop",
            "AutoCAD"
        ],
        "answer": "Human Resource Information System (HRIS)"
    },
    {
        "question": "What is the significance of payroll management?",
        "options": [
            "To ensure employees are paid accurately and on time",
            "To manage marketing campaigns",
            "To analyze financial trends",
            "To handle public relations"
        ],
        "answer": "To ensure employees are paid accurately and on time"
    },
    {
        "question": "Which of the following is a common HR function?",
        "options": [
            "Talent acquisition",
            "Customer complaint resolution",
            "Financial auditing",
            "Content marketing"
        ],
        "answer": "Talent acquisition"
    },
    {
        "question": "What is the role of employee training and development?",
        "options": [
            "To improve employee skills and performance",
            "To conduct market research",
            "To analyze company finances",
            "To manage social media"
        ],
        "answer": "To improve employee skills and performance"
    },
    {
        "question": "Which metric is commonly used to measure HR effectiveness?",
        "options": [
            "Employee turnover rate",
            "Return on Investment (ROI)",
            "Customer satisfaction score",
            "Gross profit margin"
        ],
        "answer": "Employee turnover rate"
    },
    {
        "question": "What is the primary goal of employee relations?",
        "options": [
            "To maintain a positive work environment",
            "To recruit new employees",
            "To manage employee benefits",
            "To provide customer support"
        ],
        "answer": "To maintain a positive work environment"
    },
    {
        "question": "Which of the following best describes 'onboarding'?",
        "options": [
            "The process of integrating new employees into the company",
            "A marketing strategy",
            "A financial planning tool",
            "A customer feedback method"
        ],
        "answer": "The process of integrating new employees into the company"
    }
]
financialAnalystQuestions = [
    {
        "question": "What is the primary role of a Financial Analyst?",
        "options": [
            "Analyzing financial data and trends",
            "Developing marketing strategies",
            "Recruiting and managing employees",
            "Handling customer inquiries and complaints"
        ],
        "answer": "Analyzing financial data and trends"
    },
    {
        "question": "Which of the following is a key responsibility of a Financial Analyst?",
        "options": [
            "Making recommendations for investments",
            "Managing advertising campaigns",
            "Writing press releases",
            "Selling products or services"
        ],
        "answer": "Making recommendations for investments"
    },
    {
        "question": "What is the purpose of financial modeling?",
        "options": [
            "To forecast future financial performance",
            "To increase brand awareness",
            "To handle customer service",
            "To analyze market trends"
        ],
        "answer": "To forecast future financial performance"
    },
    {
        "question": "Which tool is commonly used in financial analysis?",
        "options": [
            "Microsoft Excel",
            "Google Analytics",
            "Adobe Photoshop",
            "AutoCAD"
        ],
        "answer": "Microsoft Excel"
    },
    {
        "question": "What is the significance of financial statements?",
        "options": [
            "To provide a summary of financial performance and position",
            "To manage marketing campaigns",
            "To handle employee relations",
            "To write press releases"
        ],
        "answer": "To provide a summary of financial performance and position"
    },
    {
        "question": "Which of the following is a common financial metric?",
        "options": [
            "Earnings per share (EPS)",
            "Customer complaint resolution",
            "Content marketing",
            "Employee turnover rate"
        ],
        "answer": "Earnings per share (EPS)"
    },
    {
        "question": "What is the role of risk assessment in financial analysis?",
        "options": [
            "To evaluate the potential risks of an investment",
            "To conduct market research",
            "To analyze company finances",
            "To manage social media"
        ],
        "answer": "To evaluate the potential risks of an investment"
    },
    {
        "question": "Which metric is commonly used to measure financial performance?",
        "options": [
            "Return on Investment (ROI)",
            "Employee turnover rate",
            "Customer satisfaction score",
            "Gross profit margin"
        ],
        "answer": "Return on Investment (ROI)"
    },
    {
        "question": "What is the primary goal of financial planning?",
        "options": [
            "To ensure long-term financial stability and growth",
            "To recruit new employees",
            "To manage employee benefits",
            "To provide customer support"
        ],
        "answer": "To ensure long-term financial stability and growth"
    },
    {
        "question": "Which of the following best describes 'asset management'?",
        "options": [
            "The process of managing a client's investments and assets",
            "A marketing strategy",
            "A financial planning tool",
            "A customer feedback method"
        ],
        "answer": "The process of managing a client's investments and assets"
    }
]
prSpecialistQuestions = [
    {
        "question": "What is the primary role of a Public Relations (PR) Specialist?",
        "options": [
            "Managing the public image of an organization or individual",
            "Developing marketing strategies",
            "Recruiting and managing employees",
            "Handling customer inquiries and complaints"
        ],
        "answer": "Managing the public image of an organization or individual"
    },
    {
        "question": "Which of the following is a key responsibility of a PR Specialist?",
        "options": [
            "Writing press releases",
            "Managing advertising campaigns",
            "Analyzing financial data",
            "Selling products or services"
        ],
        "answer": "Writing press releases"
    },
    {
        "question": "What is the purpose of handling media relations?",
        "options": [
            "To ensure positive coverage of the organization or individual",
            "To increase brand awareness",
            "To handle customer service",
            "To analyze market trends"
        ],
        "answer": "To ensure positive coverage of the organization or individual"
    },
    {
        "question": "Which tool is commonly used in public relations?",
        "options": [
            "Media monitoring software",
            "Google Analytics",
            "Adobe Photoshop",
            "AutoCAD"
        ],
        "answer": "Media monitoring software"
    },
    {
        "question": "What is the significance of crisis management in PR?",
        "options": [
            "To protect and restore the public image during a negative event",
            "To manage marketing campaigns",
            "To analyze financial trends",
            "To handle employee relations"
        ],
        "answer": "To protect and restore the public image during a negative event"
    },
    {
        "question": "Which of the following is a common PR tactic?",
        "options": [
            "Event planning",
            "Customer complaint resolution",
            "Financial auditing",
            "Content marketing"
        ],
        "answer": "Event planning"
    },
    {
        "question": "What is the role of social media in public relations?",
        "options": [
            "To engage with the public and manage the organization's image",
            "To conduct market research",
            "To analyze company finances",
            "To manage employee benefits"
        ],
        "answer": "To engage with the public and manage the organization's image"
    },
    {
        "question": "Which metric is commonly used to measure PR effectiveness?",
        "options": [
            "Media impressions",
            "Return on Investment (ROI)",
            "Customer satisfaction score",
            "Gross profit margin"
        ],
        "answer": "Media impressions"
    },
    {
        "question": "What is the primary goal of brand storytelling?",
        "options": [
            "To create a compelling narrative that resonates with the audience",
            "To recruit new employees",
            "To manage employee benefits",
            "To provide customer support"
        ],
        "answer": "To create a compelling narrative that resonates with the audience"
    },
    {
        "question": "Which of the following best describes 'press conference'?",
        "options": [
            "An event where an organization communicates with the media",
            "A marketing strategy",
            "A financial planning tool",
            "A customer feedback method"
        ],
        "answer": "An event where an organization communicates with the media"
    }
]
iasOfficerQuestions = [
    {
        "question": "What is the primary role of an IAS officer?",
        "options": [
            "To implement government policies and manage administrative functions",
            "To enforce law and order",
            "To manage public health services",
            "To teach in government schools"
        ],
        "answer": "To implement government policies and manage administrative functions"
    },
    {
        "question": "Which examination must be cleared to become an IAS officer?",
        "options": [
            "UPSC Civil Services Examination",
            "SSC Combined Graduate Level Examination",
            "IBPS PO Examination",
            "CTET Examination"
        ],
        "answer": "UPSC Civil Services Examination"
    },
    {
        "question": "What is the full form of UPSC?",
        "options": [
            "Union Public Service Commission",
            "United Professional Service Commission",
            "Unified Public Service Commission",
            "Universal Public Service Commission"
        ],
        "answer": "Union Public Service Commission"
    },
    {
        "question": "Which of the following is a key responsibility of an IAS officer?",
        "options": [
            "Overseeing district administration",
            "Conducting criminal investigations",
            "Managing railway operations",
            "Providing healthcare services"
        ],
        "answer": "Overseeing district administration"
    },
    {
        "question": "What is the tenure of an IAS officer's training at the Lal Bahadur Shastri National Academy of Administration (LBSNAA)?",
        "options": [
            "Two years",
            "One year",
            "Six months",
            "Three years"
        ],
        "answer": "Two years"
    },
    {
        "question": "Which of the following is a power granted to IAS officers?",
        "options": [
            "To sign agreements on behalf of the government",
            "To manage and administer public funds",
            "To enact laws",
            "To conduct judicial trials"
        ],
        "answer": "To manage and administer public funds"
    },
    {
        "question": "What is the role of an IAS officer in disaster management?",
        "options": [
            "To coordinate relief and rehabilitation efforts",
            "To provide medical care",
            "To enforce criminal laws",
            "To teach disaster preparedness"
        ],
        "answer": "To coordinate relief and rehabilitation efforts"
    },
    {
        "question": "Which of the following sectors can an IAS officer be assigned to?",
        "options": [
            "Health, Education, Agriculture, and Home Affairs",
            "Only Health and Education",
            "Only Agriculture and Home Affairs",
            "Only Health and Agriculture"
        ],
        "answer": "Health, Education, Agriculture, and Home Affairs"
    },
    {
        "question": "What is the role of an IAS officer in policy formulation?",
        "options": [
            "To provide inputs and implement policies at the ground level",
            "To conduct surveys",
            "To manage media relations",
            "To conduct research in laboratories"
        ],
        "answer": "To provide inputs and implement policies at the ground level"
    },
    {
        "question": "What is the cadre system in the IAS?",
        "options": [
            "A system that assigns IAS officers to different states or regions",
            "A system for promotion based on years of service",
            "A system for training new recruits",
            "A system for evaluating performance"
        ],
        "answer": "A system that assigns IAS officers to different states or regions"
    }
]
ipsOfficerQuestions = [
    {
        "question": "What is the primary role of an IPS officer?",
        "options": [
            "To maintain law and order and oversee police operations",
            "To implement government policies",
            "To manage public health services",
            "To teach in government schools"
        ],
        "answer": "To maintain law and order and oversee police operations"
    },
    {
        "question": "Which examination must be cleared to become an IPS officer?",
        "options": [
            "UPSC Civil Services Examination",
            "SSC Combined Graduate Level Examination",
            "IBPS PO Examination",
            "CTET Examination"
        ],
        "answer": "UPSC Civil Services Examination"
    },
    {
        "question": "What is the full form of IPS?",
        "options": [
            "Indian Police Service",
            "Indian Public Service",
            "Indian Protective Service",
            "Indian People Service"
        ],
        "answer": "Indian Police Service"
    },
    {
        "question": "Which of the following is a key responsibility of an IPS officer?",
        "options": [
            "Preventing and investigating crimes",
            "Overseeing district administration",
            "Managing railway operations",
            "Providing healthcare services"
        ],
        "answer": "Preventing and investigating crimes"
    },
    {
        "question": "What is the training period for IPS officers at the Sardar Vallabhbhai Patel National Police Academy (SVPNPA)?",
        "options": [
            "Two years",
            "One year",
            "Six months",
            "Three years"
        ],
        "answer": "Two years"
    },
    {
        "question": "Which of the following powers is granted to IPS officers?",
        "options": [
            "To maintain public order",
            "To sign international agreements",
            "To enact laws",
            "To conduct judicial trials"
        ],
        "answer": "To maintain public order"
    },
    {
        "question": "What is the role of an IPS officer in counter-terrorism?",
        "options": [
            "To lead and coordinate anti-terrorism operations",
            "To provide medical care",
            "To enforce civil laws",
            "To teach counter-terrorism tactics"
        ],
        "answer": "To lead and coordinate anti-terrorism operations"
    },
    {
        "question": "Which of the following units can an IPS officer be assigned to?",
        "options": [
            "Crime Branch, Anti-Terrorism Squad, and Traffic Police",
            "Only Crime Branch",
            "Only Anti-Terrorism Squad",
            "Only Traffic Police"
        ],
        "answer": "Crime Branch, Anti-Terrorism Squad, and Traffic Police"
    },
    {
        "question": "What is the role of an IPS officer in community policing?",
        "options": [
            "To engage with the community to prevent crime and enhance security",
            "To conduct surveys",
            "To manage media relations",
            "To conduct research in laboratories"
        ],
        "answer": "To engage with the community to prevent crime and enhance security"
    },
    {
        "question": "What is the significance of the cadre system in the IPS?",
        "options": [
            "It assigns IPS officers to different states or regions",
            "It is a promotion system based on years of service",
            "It is a training system for new recruits",
            "It is a performance evaluation system"
        ],
        "answer": "It assigns IPS officers to different states or regions"
    }
]
ifsOfficerQuestions = [
    {
        "question": "What is the primary role of an IFS officer?",
        "options": [
            "To manage diplomatic relations and represent India abroad",
            "To enforce law and order",
            "To implement government policies",
            "To manage public health services"
        ],
        "answer": "To manage diplomatic relations and represent India abroad"
    },
    {
        "question": "Which examination must be cleared to become an IFS officer?",
        "options": [
            "UPSC Civil Services Examination",
            "SSC Combined Graduate Level Examination",
            "IBPS PO Examination",
            "CTET Examination"
        ],
        "answer": "UPSC Civil Services Examination"
    },
    {
        "question": "What is the full form of IFS?",
        "options": [
            "Indian Foreign Service",
            "Indian Forest Service",
            "Indian Financial Service",
            "Indian Federal Service"
        ],
        "answer": "Indian Foreign Service"
    },
    {
        "question": "Which of the following is a key responsibility of an IFS officer?",
        "options": [
            "Handling international negotiations and consular services",
            "Preventing and investigating crimes",
            "Managing railway operations",
            "Providing healthcare services"
        ],
        "answer": "Handling international negotiations and consular services"
    },
    {
        "question": "Where do IFS officers undergo training?",
        "options": [
            "Foreign Service Institute (FSI), New Delhi",
            "Lal Bahadur Shastri National Academy of Administration (LBSNAA)",
            "Sardar Vallabhbhai Patel National Police Academy (SVPNPA)",
            "National Academy of Direct Taxes (NADT)"
        ],
        "answer": "Foreign Service Institute (FSI), New Delhi"
    },
    {
        "question": "Which of the following powers is granted to IFS officers?",
        "options": [
            "To represent India in foreign countries",
            "To sign international agreements",
            "To enact laws",
            "To conduct judicial trials"
        ],
        "answer": "To represent India in foreign countries"
    },
    {
        "question": "What is the role of an IFS officer in economic diplomacy?",
        "options": [
            "To promote Indian trade and investment abroad",
            "To provide medical care",
            "To enforce civil laws",
            "To teach international trade"
        ],
        "answer": "To promote Indian trade and investment abroad"
    },
    {
        "question": "Which of the following sectors can an IFS officer be assigned to?",
        "options": [
            "Political, Economic, and Consular affairs",
            "Only Political affairs",
            "Only Economic affairs",
            "Only Consular affairs"
        ],
        "answer": "Political, Economic, and Consular affairs"
    },
    {
        "question": "What is the role of an IFS officer in consular services?",
        "options": [
            "To assist Indian citizens abroad and issue visas",
            "To conduct surveys",
            "To manage media relations",
            "To conduct research in laboratories"
        ],
        "answer": "To assist Indian citizens abroad and issue visas"
    },
    {
        "question": "What is the importance of language skills for an IFS officer?",
        "options": [
            "It helps in effective communication with foreign nationals",
            "It enhances physical fitness",
            "It increases technical knowledge",
            "It regulates emotions"
        ],
        "answer": "It helps in effective communication with foreign nationals"
    }
]
salesManagerQuestions = [
    {
        "question": "What is the primary role of a Sales Executive/Manager?",
        "options": [
            "Selling products or services",
            "Developing marketing strategies",
            "Recruiting and managing employees",
            "Handling customer inquiries and complaints"
        ],
        "answer": "Selling products or services"
    },
    {
        "question": "Which of the following is a key responsibility of a Sales Executive/Manager?",
        "options": [
            "Building and maintaining client relationships",
            "Managing advertising campaigns",
            "Analyzing financial data",
            "Writing press releases"
        ],
        "answer": "Building and maintaining client relationships"
    },
    {
        "question": "What is the purpose of a sales pitch?",
        "options": [
            "To persuade potential customers to purchase a product or service",
            "To increase brand awareness",
            "To handle customer service",
            "To analyze market trends"
        ],
        "answer": "To persuade potential customers to purchase a product or service"
    },
    {
        "question": "Which tool is commonly used in sales management?",
        "options": [
            "Customer Relationship Management (CRM) software",
            "Google Analytics",
            "Adobe Photoshop",
            "AutoCAD"
        ],
        "answer": "Customer Relationship Management (CRM) software"
    },
    {
        "question": "What is the significance of sales forecasting?",
        "options": [
            "To predict future sales and set targets",
            "To manage marketing campaigns",
            "To analyze financial trends",
            "To handle public relations"
        ],
        "answer": "To predict future sales and set targets"
    },
    {
        "question": "Which of the following is a common sales technique?",
        "options": [
            "Upselling",
            "Customer complaint resolution",
            "Financial auditing",
            "Content marketing"
        ],
        "answer": "Upselling"
    },
    {
        "question": "What is the role of customer feedback in sales?",
        "options": [
            "To improve products and services based on customer input",
            "To conduct market research",
            "To analyze company finances",
            "To manage social media"
        ],
        "answer": "To improve products and services based on customer input"
    },
    {
        "question": "Which metric is commonly used to measure sales performance?",
        "options": [
            "Sales revenue",
            "Return on Investment (ROI)",
            "Customer satisfaction score",
            "Gross profit margin"
        ],
        "answer": "Sales revenue"
    },
    {
        "question": "What is the primary goal of lead generation?",
        "options": [
            "To identify potential customers",
            "To recruit new employees",
            "To manage employee benefits",
            "To provide customer support"
        ],
        "answer": "To identify potential customers"
    },
    {
        "question": "Which of the following best describes 'cold calling'?",
        "options": [
            "Contacting potential customers who have not expressed interest",
            "A marketing strategy",
            "A financial planning tool",
            "A customer feedback method"
        ],
        "answer": "Contacting potential customers who have not expressed interest"
    }
]
contentWriterQuestions = [
    {
        "question": "What is the primary role of a Content Writer/Editor?",
        "options": [
            "Creating and editing written content for various platforms",
            "Developing marketing strategies",
            "Recruiting and managing employees",
            "Handling customer inquiries and complaints"
        ],
        "answer": "Creating and editing written content for various platforms"
    },
    {
        "question": "Which of the following is a key responsibility of a Content Writer/Editor?",
        "options": [
            "Ensuring content aligns with brand and audience expectations",
            "Managing advertising campaigns",
            "Writing press releases",
            "Selling products or services"
        ],
        "answer": "Ensuring content aligns with brand and audience expectations"
    },
    {
        "question": "What is the purpose of content proofreading?",
        "options": [
            "To identify and correct errors in the text",
            "To increase brand awareness",
            "To handle customer service",
            "To analyze market trends"
        ],
        "answer": "To identify and correct errors in the text"
    },
    {
        "question": "Which tool is commonly used in content writing?",
        "options": [
            "Grammarly",
            "Google Analytics",
            "Adobe Photoshop",
            "AutoCAD"
        ],
        "answer": "Grammarly"
    },
    {
        "question": "What is the significance of SEO in content writing?",
        "options": [
            "To improve content visibility in search engine results",
            "To manage marketing campaigns",
            "To handle employee relations",
            "To write press releases"
        ],
        "answer": "To improve content visibility in search engine results"
    },
    {
        "question": "Which of the following is a common content format?",
        "options": [
            "Blog posts",
            "Customer complaint resolution",
            "Content marketing",
            "Employee turnover rate"
        ],
        "answer": "Blog posts"
    },
    {
        "question": "What is the role of keyword research in content writing?",
        "options": [
            "To identify relevant keywords to target in the content",
            "To conduct market research",
            "To analyze company finances",
            "To manage social media"
        ],
        "answer": "To identify relevant keywords to target in the content"
    },
    {
        "question": "Which metric is commonly used to measure content performance?",
        "options": [
            "Page views",
            "Return on Investment (ROI)",
            "Customer satisfaction score",
            "Gross profit margin"
        ],
        "answer": "Page views"
    },
    {
        "question": "What is the primary goal of content marketing?",
        "options": [
            "To attract and engage the target audience through valuable content",
            "To recruit new employees",
            "To manage employee benefits",
            "To provide customer support"
        ],
        "answer": "To attract and engage the target audience through valuable content"
    }
]
communicationQuestions = [
    {
        "question": "What is the primary goal of effective communication?",
        "options": [
            "To clearly convey information and ideas",
            "To enhance physical fitness",
            "To improve technical skills",
            "To regulate emotions"
        ],
        "answer": "To clearly convey information and ideas"
    },
    {
        "question": "Which of the following is a key component of effective communication?",
        "options": [
            "Active listening",
            "Physical strength",
            "Technical proficiency",
            "Emotional regulation"
        ],
        "answer": "Active listening"
    },
    {
        "question": "What is the first step in the communication process?",
        "options": [
            "Encoding the message",
            "Sending the message",
            "Receiving the message",
            "Providing feedback"
        ],
        "answer": "Encoding the message"
    },
    {
        "question": "Which of the following best describes 'feedback' in communication?",
        "options": [
            "The response from the receiver",
            "The physical act of speaking",
            "The technical detail of the message",
            "The regulation of emotions"
        ],
        "answer": "The response from the receiver"
    },
    {
        "question": "Why is nonverbal communication important?",
        "options": [
            "It conveys additional information through body language and facial expressions",
            "It improves physical fitness",
            "It increases technical knowledge",
            "It enhances emotional intelligence"
        ],
        "answer": "It conveys additional information through body language and facial expressions"
    },
    {
        "question": "What role does clarity play in effective communication?",
        "options": [
            "It ensures the message is understood correctly",
            "It improves physical endurance",
            "It enhances technical skills",
            "It regulates emotions"
        ],
        "answer": "It ensures the message is understood correctly"
    },
    {
        "question": "Which of the following strategies can improve communication skills?",
        "options": [
            "Practicing public speaking",
            "Learning new physical exercises",
            "Improving technical proficiency",
            "Increasing emotional awareness"
        ],
        "answer": "Practicing public speaking"
    },
    {
        "question": "How can effective communication improve workplace relationships?",
        "options": [
            "By reducing misunderstandings and fostering collaboration",
            "By increasing physical strength",
            "By enhancing technical skills",
            "By improving emotional regulation"
        ],
        "answer": "By reducing misunderstandings and fostering collaboration"
    },
    {
        "question": "What is the importance of considering the audience in communication?",
        "options": [
            "It helps tailor the message to the audience's needs and understanding",
            "It enhances physical fitness",
            "It increases technical knowledge",
            "It regulates emotions"
        ],
        "answer": "It helps tailor the message to the audience's needs and understanding"
    },
    {
        "question": "Which of the following is an example of a communication barrier?",
        "options": [
            "Language differences",
            "Learning new physical activities",
            "Practicing technical skills",
            "Regulating emotions"
        ],
        "answer": "Language differences"
    }
]

emotionalIntelligenceQuestions = [
    {
        "question": "What is emotional intelligence?",
        "options": [
            "The ability to reason logically",
            "The ability to recognize and manage emotions",
            "The ability to solve complex problems",
            "The ability to understand technical concepts"
        ],
        "answer": "The ability to recognize and manage emotions"
    },
    {
        "question": "Which of the following is a component of emotional intelligence?",
        "options": [
            "Self-awareness",
            "Mathematical skills",
            "Technical proficiency",
            "Physical strength"
        ],
        "answer": "Self-awareness"
    },
    {
        "question": "Empathy is a key aspect of which skill?",
        "options": [
            "Logical reasoning",
            "Emotional intelligence",
            "Technical writing",
            "Public speaking"
        ],
        "answer": "Emotional intelligence"
    },
    {
        "question": "How can emotional intelligence benefit workplace relationships?",
        "options": [
            "By improving technical skills",
            "By reducing conflict and increasing collaboration",
            "By enhancing physical fitness",
            "By speeding up task completion"
        ],
        "answer": "By reducing conflict and increasing collaboration"
    },
    {
        "question": "Which of the following best describes self-regulation in the context of emotional intelligence?",
        "options": [
            "Controlling one's own emotions",
            "Regulating team activities",
            "Managing project timelines",
            "Balancing work and personal life"
        ],
        "answer": "Controlling one's own emotions"
    },
    {
        "question": "What role does motivation play in emotional intelligence?",
        "options": [
            "It drives individuals to achieve their goals",
            "It increases logical reasoning abilities",
            "It improves physical endurance",
            "It enhances technical skills"
        ],
        "answer": "It drives individuals to achieve their goals"
    },
    {
        "question": "Which skill is essential for understanding others' emotions?",
        "options": [
            "Empathy",
            "Technical proficiency",
            "Logical reasoning",
            "Physical strength"
        ],
        "answer": "Empathy"
    },
    {
        "question": "What is the importance of social skills in emotional intelligence?",
        "options": [
            "They improve interpersonal interactions and build relationships",
            "They enhance technical abilities",
            "They increase physical endurance",
            "They improve logical reasoning"
        ],
        "answer": "They improve interpersonal interactions and build relationships"
    },
    {
        "question": "Which of the following strategies can help develop emotional intelligence?",
        "options": [
            "Practicing self-awareness",
            "Learning new technical skills",
            "Increasing physical activity",
            "Enhancing logical reasoning"
        ],
        "answer": "Practicing self-awareness"
    },
    {
        "question": "How does emotional intelligence impact leadership?",
        "options": [
            "It helps leaders manage their own emotions and understand others'",
            "It increases physical strength",
            "It enhances technical skills",
            "It improves logical reasoning"
        ],
        "answer": "It helps leaders manage their own emotions and understand others'"
    }
]
criticalThinkingQuestions = [
    {
        "question": "What is the primary goal of critical thinking?",
        "options": [
            "To solve problems and make decisions based on logical reasoning",
            "To enhance physical fitness",
            "To improve technical skills",
            "To increase emotional intelligence"
        ],
        "answer": "To solve problems and make decisions based on logical reasoning"
    },
    {
        "question": "Which of the following is a key component of critical thinking?",
        "options": [
            "Analyzing facts",
            "Physical strength",
            "Technical proficiency",
            "Emotional regulation"
        ],
        "answer": "Analyzing facts"
    },
    {
        "question": "What is the first step in the critical thinking process?",
        "options": [
            "Identifying the problem",
            "Implementing a solution",
            "Evaluating the outcome",
            "Communicating the decision"
        ],
        "answer": "Identifying the problem"
    },
    {
        "question": "Which of the following best describes 'evaluation' in critical thinking?",
        "options": [
            "Assessing the credibility and relevance of information",
            "Enhancing physical endurance",
            "Improving technical skills",
            "Regulating emotions"
        ],
        "answer": "Assessing the credibility and relevance of information"
    },
    {
        "question": "Why is open-mindedness important in critical thinking?",
        "options": [
            "It allows consideration of multiple perspectives",
            "It improves physical fitness",
            "It increases technical knowledge",
            "It enhances emotional intelligence"
        ],
        "answer": "It allows consideration of multiple perspectives"
    },
    {
        "question": "What role does logical reasoning play in critical thinking?",
        "options": [
            "It helps draw sound conclusions based on evidence",
            "It improves physical endurance",
            "It enhances technical skills",
            "It regulates emotions"
        ],
        "answer": "It helps draw sound conclusions based on evidence"
    },
    {
        "question": "Which of the following strategies can enhance critical thinking skills?",
        "options": [
            "Practicing reflective thinking",
            "Learning new physical exercises",
            "Improving technical proficiency",
            "Increasing emotional awareness"
        ],
        "answer": "Practicing reflective thinking"
    },
    {
        "question": "How can critical thinking improve decision-making?",
        "options": [
            "By evaluating options and anticipating potential outcomes",
            "By increasing physical strength",
            "By enhancing technical skills",
            "By improving emotional regulation"
        ],
        "answer": "By evaluating options and anticipating potential outcomes"
    },
    {
        "question": "What is the importance of questioning assumptions in critical thinking?",
        "options": [
            "It challenges biases and improves understanding",
            "It enhances physical fitness",
            "It increases technical knowledge",
            "It regulates emotions"
        ],
        "answer": "It challenges biases and improves understanding"
    },
    {
        "question": "Which of the following is an example of a critical thinking exercise?",
        "options": [
            "Analyzing case studies",
            "Learning new physical activities",
            "Practicing technical skills",
            "Regulating emotions"
        ],
        "answer": "Analyzing case studies"
    }
]
codingTheoryQuestions = [
    {
      "question": "What is the time complexity of the following Python code: for i in range(n): ...?",
      "options": [
        "O(1)",
        "O(log n)",
        "O(n)",
        "O(n^2)"
      ],
      "answer": "O(n)"
    },
    {
      "question": "Which data structure is most suitable for implementing a stack in Python?",
      "options": [
        "List",
        "Tuple",
        "Dictionary",
        "Set"
      ],
      "answer": "List"
    },
    {
      "question": "What is the purpose of the break statement in a Python loop?",
      "options": [
        "To skip to the next iteration",
        "To exit the loop immediately",
        "To restart the loop from the beginning",
        "To print an error message"
      ],
      "answer": "To exit the loop immediately"
    },
    {
      "question": "Which of the following Python functions finds the maximum value in a list of integers?",
      "options": [
        "max_val = arr[0], num > max_val, num, max_val",
        "max_val = arr[-1], num < max_val, num, max_val",
        "max_val = arr[0], num < max_val, num, max_val",
        "max_val = arr[-1], num > max_val, num, max_val"
      ],
      "answer": "max_val = arr[0], num > max_val, num, max_val"
    },
    {
      "question": "What is the difference between pass and continue statements in a Python loop?",
      "options": [
        "pass skips to the next iteration, while continue exits the loop",
        "pass does nothing, while continue skips to the next iteration",
        "pass exits the loop, while continue does nothing",
        "pass and continue are interchangeable"
      ],
      "answer": "pass does nothing, while continue skips to the next iteration"
    },
    {
      "question": "Which of the following is NOT a characteristic of a recursive function in Python?",
      "options": [
        "It calls itself",
        "It has a base case",
        "It uses a loop",
        "It has a fixed number of iterations"
      ],
      "answer": "It uses a loop"
    },
    {
      "question": "What is the purpose of the return statement in a Python function?",
      "options": [
        "To print a message",
        "To exit the function and return a value",
        "To skip to the next line of code",
        "To restart the function from the beginning"
      ],
      "answer": "To exit the function and return a value"
    },
    {
      "question": "Which of the following Python functions reverses a string?",
      "options": [
        "reversed_s = \"\", i = 0, i < len(s), s[i]",
        "reversed_s = \"\", i = len(s) - 1, i >= 0, s[i]",
        "reversed_s = \"\", i = len(s), i > 0, s[i - 1]",
        "reversed_s = \"\", i = len(s) - 1, i >= 0, s[i - 1]"
      ],
      "answer": "reversed_s = \"\", i = len(s) - 1, i >= 0, s[i - 1]"
    },
    {
      "question": "What is the time complexity of the following Python code: for i in range(n): for j in range(n): ...?",
      "options": [
        "O(1)",
        "O(log n)",
        "O(n)",
        "O(n^2)"
      ],
      "answer": "O(n^2)"
    },
    {
      "question": "Which of the following is a trade-off between time and space complexity in Python?",
      "options": [
        "Using a list comprehension instead of a for loop",
        "Using a generator instead of a list",
        "Using a dictionary instead of a list",
        "All of the above"
      ],
      "answer": "All of the above"
    }
  ]

networkWizardryQuestions = [
    {
      "question": "What is the primary function of a router in a computer network?",
      "options": [
        "To connect multiple networks",
        "To transmit data between devices",
        "To provide security for network traffic",
        "To manage network bandwidth"
      ],
      "answer": "To connect multiple networks"
    },
    {
      "question": "Which of the following is NOT a layer in the OSI model?",
      "options": [
        "Physical",
        "Data Link",
        "Network",
        "Application",
        "Session"
      ],
      "answer": "Session"
    },
    {
      "question": "Which of the following protocols is used for secure web browsing?",
      "options": [
        "HTTP",
        "HTTPS",
        "FTP",
        "SMTP"
      ],
      "answer": "HTTPS"
    },
    {
      "question": "Which of the following is NOT a type of network topology?",
      "options": [
        "Star",
        "Ring",
        "Mesh",
        "Tree",
        "Square"
      ],
      "answer": "Square"
    },
    {
      "question": "Which of the following is used to assign IP addresses to devices on a network?",
      "options": [
        "DHCP",
        "DNS",
        "FTP",
        "SMTP"
      ],
      "answer": "DHCP"
    },
    {
      "question": "Which of the following is used to convert domain names to IP addresses?",
      "options": [
        "DHCP",
        "DNS",
        "FTP",
        "SMTP"
      ],
      "answer": "DNS"
    },
    {
      "question": "Which of the following is used to transfer files between devices on a network?",
      "options": [
        "FTP",
        "HTTP",
        "HTTPS",
        "SMTP"
      ],
      "answer": "FTP"
    },
    {
      "question": "Which of the following is used to send emails over a network?",
      "options": [
        "FTP",
        "HTTP",
        "HTTPS",
        "SMTP"
      ],
      "answer": "SMTP"
    },
    {
      "question": "Which of the following is used to manage network traffic and prioritize data packets?",
      "options": [
        "QoS",
        "DHCP",
        "DNS",
        "SMTP"
      ],
      "answer": "QoS"
    },
    {
      "question": "Which of the following is used to provide wireless connectivity to devices on a network?",
      "options": [
        "Access Point",
        "Router",
        "Switch",
        "Hub"
      ],
      "answer": "Access Point"
    }
  ]
  
databaseDynamicsQuestions = [
    {
      "question": "Which of the following is NOT a type of database?",
      "options": [
        "Relational",
        "Object-oriented",
        "NoSQL",
        "All of the above"
      ],
      "answer": "All of the above"
    },
    {
      "question": "Which of the following is used to define the structure of a database table?",
      "options": [
        "Schema",
        "Index",
        "View",
        "Query"
      ],
      "answer": "Schema"
    },
    {
      "question": "Which of the following is used to retrieve data from a database?",
      "options": [
        "Schema",
        "Index",
        "View",
        "Query"
      ],
      "answer": "Query"
    },
    {
      "question": "Which of the following is used to improve database performance?",
      "options": [
        "Schema",
        "Index",
        "View",
        "Query"
      ],
      "answer": "Index"
    },
    {
      "question": "Which of the following is used to provide a simplified view of a database table?",
      "options": [
        "Schema",
        "Index",
        "View",
        "Query"
      ],
      "answer": "View"
    },
    {
      "question": "Which of the following is used to store large amounts of unstructured data?",
      "options": [
        "Relational database",
        "Object-oriented database",
        "NoSQL database",
        "All of the above"
      ],
      "answer": "NoSQL database"
    },
    {
      "question": "Which of the following is used to ensure data consistency and integrity in a database?",
      "options": [
        "raints",
        "Triggers",
        "Stored procedures",
        "All of the above"
      ],
      "answer": "All of the above"
    },
    {
      "question": "Which of the following is used to manage database transactions?",
      "options": [
        "raints",
        "Triggers",
        "Stored procedures",
        "Transactions"
      ],
      "answer": "Transactions"
    },
    {
      "question": "Which of the following is used to execute a set of SQL statements repeatedly?",
      "options": [
        "raints",
        "Triggers",
        "Stored procedures",
        "Views"
      ],
      "answer": "Stored procedures"
    },
    {
      "question": "Which of the following is used to map database objects to programming language objects?",
      "options": [
        "Object-relational mapping (ORM)",
        "Object-oriented database",
        "Relational database",
        "NoSQL database"
      ],
      "answer": "Object-relational mapping (ORM)"
    }
  ]
  
artificialIntelligenceQuestions = [
    {
      "question": "Which of the following is NOT a type of machine learning algorithm?",
      "options": [
        "Supervised",
        "Unsupervised",
        "Reinforcement",
        "Human-in-the-loop"
      ],
      "answer": "Human-in-the-loop"
    },
    {
      "question": "Which type of machine learning algorithm is used for clustering data?",
      "options": [
        "Decision Tree",
        "Random Forest",
        "K-Means"
      ],
      "answer": "K-Means"
    },
    {
      "question": "What is the term for the process of selecting the most relevant features in a dataset?",
      "options": [
        "Feature engineering",
        "Feature extraction",
        "Feature selection"
      ],
      "answer": "Feature selection"
    },
    {
      "question": "Which evaluation metric is used to measure the performance of a classification model?",
      "options": [
        "Mean Squared Error",
        "R-Squared",
        "F1 Score"
      ],
      "answer": "F1 Score"
    },
    {
      "question": "Which of the following is used to improve the interpretability of a machine learning model?",
      "options": [
        "Feature engineering",
        "Model selection",
        "Hyperparameter tuning",
        "Explainability techniques"
      ],
      "answer": "Explainability techniques"
    },
    {
      "question": "Which of the following is used to handle missing values in a dataset?",
      "options": [
        "Imputation",
        "Interpolation",
        "Extrapolation",
        "All of the above"
      ],
      "answer": "Imputation"
    },
    {
      "question": "Which of the following is used to reduce the dimensionality of a dataset?",
      "options": [
        "Feature selection",
        "Feature extraction",
        "Dimensionality reduction",
        "All of the above"
      ],
      "answer": "All of the above"
    },
    {
      "question": "Which of the following is used to cluster similar data points together?",
      "options": [
        "K-means clustering",
        "Hierarchical clustering",
        "Density-based clustering",
        "All of the above"
      ],
      "answer": "All of the above"
    },
    {
      "question": "Which of the following is used to classify data points into predefined categories?",
      "options": [
        "Regression",
        "Classification",
        "Clustering",
        "All of the above"
      ],
      "answer": "Classification"
    },
    {
      "question": "Which of the following is used to predict continuous values?",
      "options": [
        "Regression",
        "Classification",
        "Clustering",
        "All of the above"
      ],
      "answer": "Regression"
    }
  ]
  
userExperienceQuestions = [
    {
      "question": "Which of the following is NOT a principle of user-centered design?",
      "options": [
        "Empathy",
        "User research",
        "Usability testing",
        "Aesthetics"
      ],
      "answer": "Aesthetics"
    },
    {
      "question": "Which of the following is used to create a visual representation of a user interface?",
      "options": [
        "Wireframe",
        "Prototype",
        "Mockup",
        "All of the above"
      ],
      "answer": "All of the above"
    },
    {
      "question": "Which of the following is used to test the usability of a user interface?",
      "options": [
        "Usability testing",
        "A/B testing",
        "User research",
        "All of the above"
      ],
      "answer": "Usability testing"
    },
    {
      "question": "Which of the following is used to understand user behavior and preferences?",
      "options": [
        "User research",
        "Usability testing",
        "A/B testing",
        "All of the above"
      ],
      "answer": "User research"
    },
    {
      "question": "Which of the following is used to create a functional and interactive user interface?",
      "options": [
        "Prototype",
        "Mockup",
        "Wireframe",
        "All of the above"
      ],
      "answer": "Prototype"
    },
    {
      "question": "Which of the following is used to evaluate the accessibility of a user interface?",
      "options": [
        "Accessibility testing",
        "Usability testing",
        "User research",
        "All of the above"
      ],
      "answer": "Accessibility testing"
    },
    {
      "question": "Which of the following is used to create a user interface that is easy to use and navigate?",
      "options": [
        "Information architecture",
        "Interaction design",
        "Visual design",
        "All of the above"
      ],
      "answer": "All of the above"
    },
    {
      "question": "Which of the following is used to understand the user's goals and tasks?",
      "options": [
        "User research",
        "Usability testing",
        "Task analysis",
        "All of the above"
      ],
      "answer": "Task analysis"
    },
    {
      "question": "Which UX design tool is used to visualize the structure and organization of a website or application?",
      "options": [
        "Wireframe",
        "Prototype",
        "Sitemap"
      ],
      "answer": "Sitemap"
    },
    {
      "question": "What is the term for the process of creating a simple, low-fidelity representation of a product or interface?",
      "options": [
        "Prototyping",
        "Wireframing",
        "Storyboarding"
      ],
      "answer": "Wireframing"
    }
  ]
  
cyberSecurityQuestions = [
    {
      "question": "Which of the following is NOT a type of cyber attack?",
      "options": [
        "Phishing",
        "Ransomware",
        "SQL injection",
        "Social engineering"
      ],
      "answer": "Social engineering"
    },
    {
      "question": "Which type of malware is designed to encrypt files and demand payment in exchange for the decryption key?",
      "options": [
        "Virus",
        "Worm",
        "Ransomware"
      ],
      "answer": "Ransomware"
    },
    {
      "question": "What is the term for a fake Wi-Fi network set up to trick users into connecting to it?",
      "options": [
        "Evil Twin",
        "Rogue Access Point",
        "Man-in-the-Middle"
      ],
      "answer": "Evil Twin"
    },
    {
      "question": "Which security protocol is used to secure online communications between a web browser and a web server?",
      "options": [
        "SSL",
        "TLS",
        "HTTPS"
      ],
      "answer": "TLS"
    },
    {
      "question": "What is the term for a security vulnerability that is unknown to the vendor or the public?",
      "options": [
        "Zero-day exploit",
        "Known vulnerability",
        "Patchable vulnerability"
      ],
      "answer": "Zero-day exploit"
    },
    {
      "question": "Which of the following is used to protect against malware and viruses?",
      "options": [
        "Antivirus software",
        "Firewall",
        "Encryption",
        "All of the above"
      ],
      "answer": "Antivirus software"
    },
    {
      "question": "Which of the following is used to authenticate users and prevent unauthorized access?",
      "options": [
        "Authentication",
        "Authorization",
        "Accounting",
        "All of the above"
      ],
      "answer": "Authentication"
    },
    {
      "question": "Which of the following is used to ensure the confidentiality, integrity, and availability of data?",
      "options": [
        "CIA triad",
        "AAA framework",
        "NIST cybersecurity framework",
        "All of the above"
      ],
      "answer": "CIA triad"
    },
    {
      "question": "Which of the following is used to respond to a cyber attack?",
      "options": [
        "Incident response",
        "Disaster recovery",
        "Business continuity planning",
        "All of the above"
      ],
      "answer": "Incident response"
    },
    {
      "question": "Which of the following is used to prevent insider threats?",
      "options": [
        "Access control",
        "Data masking",
        "Encryption",
        "All of the above"
      ],
      "answer": "Access control"
    }
  ]
  
gameDevelopmentQuestions = [
    {
      "question": "Which of the following is NOT a type of game engine?",
      "options": [
        "Unity",
        "Unreal Engine",
        "Godot",
        "Photoshop"
      ],
      "answer": "Photoshop"
    },
    {
      "question": "Which 3D modeling software is known for its free and open-source nature?",
      "options": [
        "Blender",
        "Maya",
        "3ds Max"
      ],
      "answer": "Blender"
    },
    {
      "question": "Which programming language is commonly used for game development on the Unity platform?",
      "options": [
        "C#",
        "Java",
        "Python"
      ],
      "answer": "C#"
    },
    {
      "question": "What is the primary function of a level editor in game development?",
      "options": [
        "To create 3D models",
        "To design game levels and environments",
        "To program game logic"
      ],
      "answer": "To design game levels and environments"
    },
    {
      "question": "Which audio editing software is commonly used for adding sound effects and music to games?",
      "options": [
        "Audacity",
        "Adobe Audition",
        "FMOD"
      ],
      "answer": "Adobe Audition"
    },
    {
      "question": "Which game engine is known for its ease of use and cross-platform support?",
      "options": [
        "Unity",
        "Unreal Engine",
        "Godot"
      ],
      "answer": "Unity"
    },
    {
      "question": "What is the primary goal of game optimization?",
      "options": [
        "To improve game graphics",
        "To increase game difficulty",
        "To reduce game loading times"
      ],
      "answer": "To reduce game loading times"
    },
    {
      "question": "Which tool is used to identify and fix errors in game code?",
      "options": [
        "Debugger",
        "Compiler",
        "Profiler"
      ],
      "answer": "Debugger"
    },
    {
      "question": "Which AI technique is used to create realistic character movements in games?",
      "options": [
        "Behavior trees",
        "State machines",
        "Inverse kinematics"
      ],
      "answer": "Inverse kinematics"
    },
    {
      "question": "Which digital distribution platform is commonly used to sell and distribute PC games?",
      "options": [
        "Steam",
        "GOG",
        "Epic Games Store"
      ],
      "answer": "Steam"
    }
  ]



def careerquiz(request):
    if request.method == 'POST':
        # Define dictionaries to hold answers and scores
        technical_answers = {
            'coding_theory': [],
            'network': [],
            'database': [],
            'ai': [],
            'ui': [],
            'cybersecurity': [],
            'gamedevelopment': [],
        }
        non_technical_answers = {
            'content_writer': [],
            'financial_analyst': [],
            'pr_specialist': [],
            'sales_manager': [],
            'hr_manager': [],
            'marketing_manager': [],
            'ifs_officer': [],
            'ips_officer': [],
            'ias_officer': [],
            'communication': [],
            'critical_thinking': [],
            'emotional_intelligence': [],
        }

        # Define question dictionaries
        technical_questions = {
            'coding_theory': codingTheoryQuestions,
            'network': networkWizardryQuestions,
            'database': databaseDynamicsQuestions,
            'ai': artificialIntelligenceQuestions,
            'ui': userExperienceQuestions,
            'cybersecurity': cyberSecurityQuestions,
            'gamedevelopment': gameDevelopmentQuestions,
        }
        non_technical_questions = {
            'content_writer': contentWriterQuestions,
            'financial_analyst': financialAnalystQuestions,
            'pr_specialist': prSpecialistQuestions,
            'sales_manager': salesManagerQuestions,
            'hr_manager': hrManagerQuestions,
            'marketing_manager': marketingManagerQuestions,
            'ifs_officer': ifsOfficerQuestions,
            'ips_officer': ipsOfficerQuestions,
            'ias_officer': iasOfficerQuestions,
            'communication': communicationQuestions,
            'critical_thinking': criticalThinkingQuestions,
            'emotional_intelligence': emotionalIntelligenceQuestions,
        }

        # Collect answers for technical questions
        for category, question_list in technical_questions.items():
            for i in range(len(question_list)):
                answer = request.POST.get(f'{category}_questions_{i}')
                technical_answers[category].append(answer)

        # Collect answers for non-technical questions
        for category, question_list in non_technical_questions.items():
            for i in range(len(question_list)):
                answer = request.POST.get(f'{category}_questions_{i}')
                non_technical_answers[category].append(answer)

        # Calculate scores for technical questions
        technical_scores = {}
        for category, question_list in technical_questions.items():
            technical_scores[category] = sum(1 for i, answer in enumerate(technical_answers[category]) if answer == question_list[i]['answer'])

        # Calculate scores for non-technical questions
        non_technical_scores = {}
        for category, question_list in non_technical_questions.items():
            non_technical_scores[category] = sum(1 for i, answer in enumerate(non_technical_answers[category]) if answer == question_list[i]['answer'])

        # Retrieve personality code from session
        personality_code = request.session.get('personality_code')
        try:
            personality_type = get_object_or_404(PersonalityType, code=personality_code)
        except PersonalityType.DoesNotExist:
            return render(request, 'error.html', {'error_message': 'Personality type not found'})

        # Combine results and determine highest scoring category for both types
        combined_scores = {**technical_scores, **non_technical_scores}
        highest_score_category = max(combined_scores, key=combined_scores.get)
        highest_score = combined_scores[highest_score_category]

        # Suggest courses and jobs based on the highest score category
        suggested_courses = get_suggested_courses(highest_score_category, highest_score)
        suggested_jobs = get_suggested_jobs(highest_score_category, highest_score)
        job_info = get_job_information(suggested_jobs[0])  # Assuming the first job in the list

        # Combine results and render combined results page
        combined_results = {
            'personality_type': personality_type,
            'technical_scores': technical_scores,
            'non_technical_scores': non_technical_scores,
            'highest_score_category': highest_score_category,
            'suggested_jobs': suggested_jobs,
            'job_info': job_info,
            'suggested_courses': suggested_courses,
        }
        return render(request, 'combined_results.html', combined_results)

    else:
        # Render career quiz page with questions
        questions = {
            'coding_theory_questions': codingTheoryQuestions,
            'network_questions': networkWizardryQuestions,
            'database_questions': databaseDynamicsQuestions,
            'ai_questions': artificialIntelligenceQuestions,
            'ui_questions': userExperienceQuestions,
            'cybersecurity_questions': cyberSecurityQuestions,
            'gamedevelopment_questions': gameDevelopmentQuestions,
            'content_writer_questions': contentWriterQuestions,
            'financial_analyst_questions': financialAnalystQuestions,
            'pr_specialist_questions': prSpecialistQuestions,
            'sales_manager_questions': salesManagerQuestions,
            'hr_manager_questions': hrManagerQuestions,
            'marketing_manager_questions': marketingManagerQuestions,
            'ifs_officer_questions': ifsOfficerQuestions,
            'ips_officer_questions': ipsOfficerQuestions,
            'ias_officer_questions': iasOfficerQuestions,
            'communication_questions': communicationQuestions,
            'critical_thinking_questions': criticalThinkingQuestions,
            'emotional_intelligence_questions': emotionalIntelligenceQuestions,
        }
        return render(request, 'careerquiz.html', {'questions': questions})

def get_suggested_courses(category, score):
    suggested_courses = []  # Initialize the list of suggested courses

    if category == 'network':
        if score >= 7:
            suggested_courses.extend([
                {"name": "Advanced Network Engineering", "description": "Advanced topics in network engineering and optimization.", "url": "https://example.com/advanced-network-engineering"},
                {"name": "Telecommunications Systems", "description": "Study of telecommunications systems and technologies.", "url": "https://example.com/telecommunications-systems"},
            ])
        elif score >= 5:
            suggested_courses.extend([
                {"name": "Network Security", "description": "Principles and practices of network security.", "url": "https://example.com/network-security"},
                {"name": "Wireless Networks", "description": "Study of wireless communication networks.", "url": "https://example.com/wireless-networks"},
            ])
        elif score >= 3:
            suggested_courses.extend([
                {"name": "Computer Networking Basics", "description": "Fundamentals of computer networking.", "url": "https://example.com/computer-networking-basics"},
                {"name": "Cloud Computing Fundamentals", "description": "Introduction to cloud computing technologies.", "url": "https://example.com/cloud-computing-fundamentals"},
            ])
        elif score >= 1:
            suggested_courses.extend([
                {"name": "Introduction to Network Engineering", "description": "Introduction to basic network engineering concepts.", "url": "https://example.com/intro-to-network-engineering"},
                {"name": "Network Administration", "description": "Practical skills in network administration.", "url": "https://example.com/network-administration"},
            ])

    elif category == 'database':
        if score >= 7:
            suggested_courses.extend([
                {"name": "Advanced Database Management", "description": "Advanced topics in database management and optimization.", "url": "https://example.com/advanced-database-management"},
                {"name": "Big Data Analytics", "description": "Analysis of large datasets and analytics techniques.", "url": "https://example.com/big-data-analytics"},
            ])
        elif score >= 5:
            suggested_courses.extend([
                {"name": "Data Science for Databases", "description": "Data science techniques applied to database management.", "url": "https://example.com/data-science-for-databases"},
                {"name": "Business Intelligence", "description": "Use of data for business insights and decision-making.", "url": "https://example.com/business-intelligence"},
            ])
        elif score >= 3:
            suggested_courses.extend([
                {"name": "Introduction to Database Systems", "description": "Basic concepts and principles of database systems.", "url": "https://example.com/intro-to-database-systems"},
                {"name": "SQL Fundamentals", "description": "Fundamental skills in SQL programming.", "url": "https://example.com/sql-fundamentals"},
            ])
        elif score >= 1:
            suggested_courses.extend([
                {"name": "Database Design Basics", "description": "Fundamentals of database design principles.", "url": "https://example.com/database-design-basics"},
                {"name": "Data Management Fundamentals", "description": "Fundamental principles of data management.", "url": "https://example.com/data-management-fundamentals"},
            ])

    elif category == 'ai':
        if score >= 7:
            suggested_courses.extend([
                {"name": "Advanced Algorithms", "description": "Learn advanced algorithms and data structures.", "url": "https://example.com/advanced-algorithms"},
                {"name": "Programming Languages Theory", "description": "Explore theoretical foundations of programming languages.", "url": "https://example.com/programming-languages-theory"},
            ])
        elif score >= 5:
            suggested_courses.extend([
                {"name": "Data Structures", "description": "Study fundamental data structures and their implementation.", "url": "https://example.com/data-structures"},
                {"name": "Algorithm Design", "description": "Learn how to design efficient algorithms.", "url": "https://example.com/algorithm-design"},
            ])
        elif score >= 3:
            suggested_courses.extend([
                {"name": "Introduction to Algorithms", "description": "Introduction to basic algorithms and problem-solving techniques.", "url": "https://example.com/intro-to-algorithms"},
                {"name": "Programming Fundamentals", "description": "Fundamental principles of programming.", "url": "https://example.com/programming-fundamentals"},
            ])
        elif score >= 1:
            suggested_courses.extend([
                {"name": "Introduction to Programming", "description": "Introduction to programming concepts and basics.", "url": "https://example.com/intro-to-programming"},
                {"name": "Python Crash Course", "description": "A quick crash course on Python programming language.", "url": "https://example.com/python-crash-course"},
            ])

    elif category == 'ui':
        if score >= 7:
            suggested_courses.extend([
                {"name": "Advanced Interaction Design", "description": "Advanced principles of interaction design.", "url": "https://example.com/advanced-interaction-design"},
                {"name": "User Research Methods", "description": "Methods for conducting user research.", "url": "https://example.com/user-research-methods"},
            ])
        elif score >= 5:
            suggested_courses.extend([
                {"name": "UX/UI Design Principles", "description": "Fundamental principles of UX/UI design.", "url": "https://example.com/ux-ui-design-principles"},
                {"name": "Visual Design for Digital Media", "description": "Visual design techniques for digital media.", "url": "https://example.com/visual-design-digital-media"},
            ])
        elif score >= 3:
            suggested_courses.extend([
                {"name": "Introduction to Human-Computer Interaction", "description": "Basic concepts of human-computer interaction.", "url": "https://example.com/intro-to-human-computer-interaction"},
                {"name": "Design Thinking", "description": "Learn design thinking methodologies.", "url": "https://example.com/design-thinking"},
            ])
        elif score >= 1:
            suggested_courses.extend([
                {"name": "User Interface Design Fundamentals", "description": "Fundamentals of user interface design.", "url": "https://example.com/ui-design-fundamentals"},
                {"name": "Web Design Principles", "description": "Principles of effective web design.", "url": "https://example.com/web-design-principles"},
            ])

    elif category == 'cybersecurity':
        if score >= 7:
            suggested_courses.extend([
                {"name": "Advanced Cyber Security Management", "description": "Advanced topics in cyber security management.", "url": "https://example.com/advanced-cyber-security-management"},
                {"name": "Digital Forensics and Incident Response", "description": "Techniques for digital forensics and incident response.", "url": "https://example.com/digital-forensics-incident-response"},
            ])
        elif score >= 5:
            suggested_courses.extend([
                {"name": "Network Defense and Countermeasures", "description": "Defense strategies and countermeasures for networks.", "url": "https://example.com/network-defense-countermeasures"},
                {"name": "Ethical Hacking", "description": "Learn ethical hacking techniques.", "url": "https://example.com/ethical-hacking"},
            ])
        elif score >= 3:
            suggested_courses.extend([
                {"name": "Introduction to Cyber Security", "description": "Basic concepts and principles of cyber security.", "url": "https://example.com/intro-to-cyber-security"},
                {"name": "Cyber Security Essentials", "description": "Essential skills and techniques in cyber security.", "url": "https://example.com/cyber-security-essentials"},
            ])
        elif score >= 1:
            suggested_courses.extend([
                {"name": "Information Security Fundamentals", "description": "Fundamentals of information security.", "url": "https://example.com/info-security-fundamentals"},
                {"name": "Cyber Security Awareness", "description": "Awareness training in cyber security practices.", "url": "https://example.com/cyber-security-awareness"},
            ])

    elif category == 'gamedevelopment':
        if score >= 7:
            suggested_courses.extend([
                {"name": "Advanced Game Design", "description": "Advanced techniques in game design and development.", "url": "https://example.com/advanced-game-design"},
                {"name": "Virtual Reality Development", "description": "Development of virtual reality applications.", "url": "https://example.com/virtual-reality-development"},
            ])
        elif score >= 5:
            suggested_courses.extend([
                {"name": "Game Programming", "description": "Programming techniques for game development.", "url": "https://example.com/game-programming"},
                {"name": "Mobile Game Development", "description": "Development of games for mobile platforms.", "url": "https://example.com/mobile-game-development"},
            ])
        elif score >= 3:
            suggested_courses.extend([
                {"name": "Introduction to Game Development", "description": "Basic concepts and principles of game development.", "url": "https://example.com/intro-to-game-development"},
                {"name": "Unity Game Development", "description": "Development using the Unity game engine.", "url": "https://example.com/unity-game-development"},
            ])
        elif score >= 1:
            suggested_courses.extend([
                {"name": "Game Design Fundamentals", "description": "Fundamentals of game design.", "url": "https://example.com/game-design-fundamentals"},
                {"name": "Introduction to Unity", "description": "Introduction to the Unity game engine.", "url": "https://example.com/intro-to-unity"},
            ])

    elif category == 'sales_manager':
        if score >= 7:
            suggested_courses.extend([
                {"name": "Advanced Game Design", "description": "Advanced techniques in game design and development.", "url": "https://example.com/advanced-game-design"},
                {"name": "Virtual Reality Development", "description": "Development of virtual reality applications.", "url": "https://example.com/virtual-reality-development"},
            ])
        elif score >= 5:
            suggested_courses.extend([
                {"name": "Game Programming", "description": "Programming techniques for game development.", "url": "https://example.com/game-programming"},
                {"name": "Mobile Game Development", "description": "Development of games for mobile platforms.", "url": "https://example.com/mobile-game-development"},
            ])
        elif score >= 3:
            suggested_courses.extend([
                {"name": "Introduction to Game Development", "description": "Basic concepts and principles of game development.", "url": "https://example.com/intro-to-game-development"},
                {"name": "Unity Game Development", "description": "Development using the Unity game engine.", "url": "https://example.com/unity-game-development"},
            ])
        elif score >= 1:
            suggested_courses.extend([
                {"name": "Game Design Fundamentals", "description": "Fundamentals of game design.", "url": "https://example.com/game-design-fundamentals"},
                {"name": "Introduction to Unity", "description": "Introduction to the Unity game engine.", "url": "https://example.com/intro-to-unity"},
            ])

    elif category == 'hr_manager':
        if score >= 7:
            suggested_courses.extend([
                {"name": "Advanced Game Design", "description": "Advanced techniques in game design and development.", "url": "https://example.com/advanced-game-design"},
                {"name": "Virtual Reality Development", "description": "Development of virtual reality applications.", "url": "https://example.com/virtual-reality-development"},
            ])
        elif score >= 5:
            suggested_courses.extend([
                {"name": "Game Programming", "description": "Programming techniques for game development.", "url": "https://example.com/game-programming"},
                {"name": "Mobile Game Development", "description": "Development of games for mobile platforms.", "url": "https://example.com/mobile-game-development"},
            ])
        elif score >= 3:
            suggested_courses.extend([
                {"name": "Introduction to Game Development", "description": "Basic concepts and principles of game development.", "url": "https://example.com/intro-to-game-development"},
                {"name": "Unity Game Development", "description": "Development using the Unity game engine.", "url": "https://example.com/unity-game-development"},
            ])
        elif score >= 1:
            suggested_courses.extend([
                {"name": "Game Design Fundamentals", "description": "Fundamentals of game design.", "url": "https://example.com/game-design-fundamentals"},
                {"name": "Introduction to Unity", "description": "Introduction to the Unity game engine.", "url": "https://example.com/intro-to-unity"},
            ])

        

    return suggested_courses

        # Example: Suggest jobs based on the highest score category
       

def get_suggested_jobs(category, score):
    suggested_jobs = []

    if category == 'coding_theory':
        if score >= 7:
            suggested_jobs.extend(["Software Architect", "Backend Developer"])
        elif score >= 5:
            suggested_jobs.extend(["Full Stack Developer", "Software Engineer"])
        elif score >= 3:
            suggested_jobs.extend(["Frontend Developer", "Web Developer"])
        elif score >= 1:
            suggested_jobs.extend(["Junior Developer", "Entry-level Programmer"])

    elif category == 'network':
        if score >= 7:
            suggested_jobs.extend(["Network Architect", "Network Security Engineer"])
        elif score >= 5:
            suggested_jobs.extend(["Network Engineer", "Systems Administrator"])
        elif score >= 3:
            suggested_jobs.extend(["IT Support Specialist", "Network Technician"])
        elif score >= 1:
            suggested_jobs.extend(["Technical Support Analyst", "Help Desk Technician"])

    elif category == 'database':
        if score >= 7:
            suggested_jobs.extend(["Database Architect", "Data Engineer"])
        elif score >= 5:
            suggested_jobs.extend(["Database Administrator", "SQL Developer"])
        elif score >= 3:
            suggested_jobs.extend(["Database Analyst", "Data Specialist"])
        elif score >= 1:
            suggested_jobs.extend(["Database Support Specialist", "Junior Database Administrator"])

    elif category == 'ai':
        if score >= 7:
            suggested_jobs.extend(["AI Research Scientist", "Machine Learning Engineer"])
        elif score >= 5:
            suggested_jobs.extend(["Data Scientist", "AI Developer"])
        elif score >= 3:
            suggested_jobs.extend(["AI Programmer", "AI Software Engineer"])
        elif score >= 1:
            suggested_jobs.extend(["AI Analyst", "AI Intern"])

    elif category == 'ui':
        if score >= 7:
            suggested_jobs.extend(["UX Architect", "UI Design Director"])
        elif score >= 5:
            suggested_jobs.extend(["UI/UX Designer", "Interaction Designer"])
        elif score >= 3:
            suggested_jobs.extend(["Visual Designer", "User Researcher"])
        elif score >= 1:
            suggested_jobs.extend(["UI Developer", "UX/UI Intern"])

    elif category == 'cybersecurity':
        if score >= 7:
            suggested_jobs.extend(["Cybersecurity Architect", "Chief Information Security Officer"])
        elif score >= 5:
            suggested_jobs.extend(["Security Engineer", "Cybersecurity Analyst"])
        elif score >= 3:
            suggested_jobs.extend(["Information Security Specialist", "Network Security Consultant"])
        elif score >= 1:
            suggested_jobs.extend(["Security Administrator", "Security Operations Center (SOC) Analyst"])

    elif category == 'gamedevelopment':
        if score >= 7:
            suggested_jobs.extend(["Game Developer", "Game Designer"])
        elif score >= 5:
            suggested_jobs.extend(["Unity Developer", "Game Programmer"])
        elif score >= 3:
            suggested_jobs.extend(["Game Artist", "Game Tester"])
        elif score >= 1:
            suggested_jobs.extend(["Game Producer", "Game Development Intern"])
    
    elif category == 'sales_manager':
        if score >= 7:
            suggested_jobs.extend(["Game Developer", "Game Designer"])
        elif score >= 5:
            suggested_jobs.extend(["Unity Developer", "Game Programmer"])
        elif score >= 3:
            suggested_jobs.extend(["Game Artist", "Game Tester"])
        elif score >= 1:
            suggested_jobs.extend(["Game Producer", "Game Development Intern"])
    
    elif category == 'hr_manager':
        if score >= 7:
            suggested_jobs.extend(["Game Developer", "Game Designer"])
        elif score >= 5:
            suggested_jobs.extend(["Unity Developer", "Game Programmer"])
        elif score >= 3:
            suggested_jobs.extend(["Game Artist", "Game Tester"])
        elif score >= 1:
            suggested_jobs.extend(["Game Producer", "Game Development Intern"])

    # Retrieve job information for each suggested job
   
    job_info_list = []
    for job in suggested_jobs:
        job_info = get_job_information(job)
        job_info_list.append(job_info)

    return job_info_list


def get_job_information(job_title):
    job_info = {
        "Software Architect": {
            "description": "Software Architects design and create high-level structure of software solutions.",
            "salary": "$120,000 - $180,000 per year"
        },
        "Backend Developer": {
            "description": "Backend Developers design and develop the server-side logic, database integration, and API connectivity.",
            "salary": "$80,000 - $120,000 per year"
        },
        "Full Stack Developer": {
            "description": "Full Stack Developers design and develop the user interface, server-side logic, database integration, and API connectivity.",
            "salary": "$70,000 - $110,000 per year"
        },
        "Software Engineer": {
            "description": "Software Engineers design, develop, test, and maintain software applications.",
            "salary": "$60,000 - $100,000 per year"
        },
        "Frontend Developer": {
            "description": "Frontend Developers design and develop the user interface and user experience of software applications.",
            "salary": "$50,000 - $90,000 per year"
        },
        "Web Developer": {
            "description": "Web Developers design and develop websites and web applications.",
            "salary": "$40,000 - $80,000 per year"
        },
        "Junior Developer": {
            "description": "Junior Developers assist in designing, developing, testing, and maintaining software applications.",
            "salary": "$30,000 - $60,000 per year"
        },
        "Entry-level Programmer": {
            "description": "Entry-level Programmers assist in designing, developing, testing, and maintaining software applications.",
            "salary": "$25,000 - $50,000 per year"
        },
        "Network Architect": {
            "description": "Network Architects design and build computer networks, including local area networks (LANs), wide area networks (WANs), and the Internet.",
            "salary": "$100,000 - $150,000 per year"
        },
        "Network Security Engineer": {
            "description": "Network Security Engineers design and implement secure computer networks, including firewalls, intrusion detection systems, and encryption technologies.",
            "salary": "$90,000 - $140,000 per year"
        },
        "Network Engineer": {
            "description": "Network Engineers design, implement, and maintain computer networks, including local area networks (LANs), wide area networks (WANs), and the Internet.",
            "salary": "$70,000 - $120,000 per year"
        },
        "Systems Administrator": {
            "description": "Systems Administrators install, configure, and maintain computer systems and networks.",
            "salary": "$50,000 - $90,000 per year"
        },
        "IT Support Specialist": {
            "description": "IT Support Specialists troubleshoot and resolve technical issues with computer systems and networks.",
            "salary": "$30,000 - $60,000 per year"
        },
        "Network Technician": {
            "description": "Network Technicians install, configure, and maintain computer networks and equipment.",
            "salary": "$25,000 - $50,000 per year"
        },
        "Technical Support Analyst": {
            "description": "Technical Support Analysts troubleshoot and resolve technical issues with computer systems and networks.",
            "salary": "$20,000 - $40,000 per year"
        },
        "Help Desk Technician": {
            "description": "Help Desk Technicians troubleshoot and resolve technical issues with computer systems and networks.",
            "salary": "$15,000 - $30,000 per year"
        },
        "Database Architect": {
            "description": "Database Architects design and implement database systems, including data modeling, database design, and database performance tuning.",
            "salary": "$120,000 - $180,000 per year"
        },
        "Data Engineer": {
            "description": "Data Engineers design, build, and maintain large-scale data systems, including data pipelines, data warehousing, and data processing.",
            "salary": "$100,000 - $150,000 per year"
        },
        "Database Administrator": {
            "description": "Database Administrators design, implement, and maintain database systems, including data modeling, database design, and database performance tuning.",
            "salary": "$80,000 - $120,000 per year"
        },
        "SQL Developer": {
            "description": "SQL Developers design, develop, and maintain database systems, including data modeling, database design, and database performance tuning.",
            "salary": "$60,000 - $100,000 per year"
        },
        "Database Analyst": {
            "description": "Database Analysts analyze and interpret data to help organizations make informed business decisions.",
            "salary": "$50,000 - $90,000 per year"
        },
        "Data Specialist": {
            "description": "Data Specialists analyze and interpret data to help organizations make informed business decisions.",
            "salary": "$40,000 - $80,000 per year"
        },
        "Database Support Specialist": {
            "description": "Database Support Specialists troubleshoot and resolve technical issues with database systems.",
            "salary": "$30,000 - $60,000 per year"
        },
        "Junior Database Administrator": {
            "description": "Junior Database Administrators assist in designing, implementing, and maintaining database systems.",
            "salary": "$25,000 - $50,000 per year"
        },
        "AI Research Scientist": {
            "description": "AI Research Scientists design and develop artificial intelligence and machine learning models.",
            "salary": "$150,000 - $200,000 per year"
        },
        "Machine Learning Engineer": {
            "description": "Machine Learning Engineers design and develop artificial intelligence and machine learning models.",
            "salary": "$120,000 - $180,000 per year"
        },
        "Data Scientist": {
            "description": "Data Scientists analyze and interpret complex data to help organizations make informed business decisions.",
            "salary": "$100,000 - $150,000 per year"
        },
        "AI Developer": {
            "description": "AI Developers design and develop artificial intelligence and machine learning models.",
            "salary": "$90,000 - $140,000 per year"
        },
        "AI Programmer": {
            "description": "AI Programmers design and develop artificial intelligence and machine learning models.",
            "salary": "$80,000 - $130,000 per year"
        },
        "AI Software Engineer": {
            "description": "AI Software Engineers design and develop software applications that use artificial intelligence and machine learning models.",
            "salary": "$70,000 - $120,000 per year"
        },
        "AI Analyst": {
            "description": "AI Analysts analyze and interpret artificial intelligence and machine learning models to help organizations make informed business decisions.",
            "salary": "$60,000 - $110,000 per year"
        },
        "AI Intern": {
            "description": "AI Interns assist in designing, developing, and implementing artificial intelligence and machine learning models.",
            "salary": "$30,000 - $50,000 per year"
        },
        "UX Architect": {
            "description": "UX Architects design and develop the overall user experience and user interface for software applications.",
            "salary": "$110,000 - $160,000 per year"
        },
        "UI Design Director": {
            "description": "UI Design Directors lead and manage the user interface design team and oversee the development of user interfaces for software applications.",
            "salary": "$120,000 - $170,000 per year"
        },
        "UI/UX Designer": {
            "description": "UI/UX Designers design and develop the user interface and user experience for software applications.",
            "salary": "$80,000 - $130,000 per year"
        },
        "Interaction Designer": {
            "description": "Interaction Designers design and develop the interactions between users and software applications.",
            "salary": "$70,000 - $120,000 per year"
        },
        "Visual Designer": {
            "description": "Visual Designers design and develop the visual elements of software applications, including layout, typography, and color schemes.",
            "salary": "$60,000 - $110,000 per year"
        },
        "User Researcher": {
            "description": "User Researchers conduct research to understand user needs and behaviors and inform the design of software applications.",
            "salary": "$50,000 - $90,000 per year"
        },
        "UI Developer": {
            "description": "UI Developers design and develop the user interface for software applications.",
            "salary": "$60,000 - $100,000 per year"
        },
        "UX/UI Intern": {
            "description": "UX/UI Interns assist in designing and developing user interfaces and user experiences for software applications.",
            "salary": "$30,000 - $50,000 per year"
        },
        "Cybersecurity Architect": {
            "description": "Cybersecurity Architects design and implement secure computer networks and systems.",
            "salary": "$120,000 - $180,000 per year"
        },
        "Chief Information Security Officer": {
            "description": "Chief Information Security Officers oversee the organization's information security strategy and operations.",
            "salary": "$150,000 - $250,000 per year"
        },
        "Security Engineer": {
            "description": "Security Engineers design and implement security measures to protect computer networks and systems.",
            "salary": "$100,000 - $150,000 per year"
        },
        "Cybersecurity Analyst": {
            "description": "Cybersecurity Analysts monitor and protect computer networks and systems from cyber threats.",
            "salary": "$80,000 - $120,000 per year"
        },
        "Information Security Specialist": {
            "description": "Information Security Specialists develop and implement security policies and procedures to protect information systems.",
            "salary": "$70,000 - $110,000 per year"
        },
        "Network Security Consultant": {
            "description": "Network Security Consultants provide expert advice and recommendations on securing computer networks and systems.",
            "salary": "$90,000 - $140,000 per year"
        },
        "Security Administrator": {
            "description": "Security Administrators manage and monitor security measures for computer networks and systems.",
            "salary": "$60,000 - $100,000 per year"
        },
        "Security Operations Center (SOC) Analyst": {
            "description": "SOC Analysts monitor and respond to security incidents and threats within an organization's security operations center.",
            "salary": "$50,000 - $90,000 per year"
        },
        "Game Developer": {
            "description": "Game Developers design and develop video games for various platforms.",
            "salary": "$70,000 - $120,000 per year"
        },
        "Game Designer": {
            "description": "Game Designers create the concepts, rules, and structure for video games.",
            "salary": "$60,000 - $110,000 per year"
        },
        "Unity Developer": {
            "description": "Unity Developers design and develop video games and interactive applications using the Unity game engine.",
            "salary": "$70,000 - $120,000 per year"
        },
        "Game Programmer": {
            "description": "Game Programmers write code and develop software for video games.",
            "salary": "$60,000 - $110,000 per year"
        },
        "Game Artist": {
            "description": "Game Artists create visual assets and animations for video games.",
            "salary": "$50,000 - $90,000 per year"
        },
        "Game Tester": {
            "description": "Game Testers play and test video games to identify bugs and issues before release.",
            "salary": "$30,000 - $60,000 per year"
        },
        "Game Producer": {
            "description": "Game Producers oversee the development and production of video games from concept to release.",
            "salary": "$80,000 - $130,000 per year"
        },
        "Game Development Intern": {
            "description": "Game Development Interns assist in various aspects of video game development and gain hands-on experience.",
            "salary": "$20,000 - $40,000 per year"
        },
        "Sales Manager": {
            "description": "Sales Managers lead and manage a sales team and develop strategies to achieve sales targets.",
            "salary": "$70,000 - $120,000 per year"
        },
        "HR Manager": {
            "description": "HR Managers oversee human resources functions, including recruitment, employee relations, and compliance.",
            "salary": "$60,000 - $100,000 per year"
        }
    }

    info = job_info.get(job_title)

    return info