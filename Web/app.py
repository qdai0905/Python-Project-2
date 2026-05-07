import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import base64


# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="Instagram User Analysis",
    page_icon="📸",
    layout="wide"
)

# ===================== LOAD DATA =====================
df = pd.read_excel("Dataset.xlsx")

# ===================== SESSION STATE =====================
if "clicked" not in st.session_state:
    st.session_state.clicked = False

# ===================== INTRO BACKGROUND =====================


def get_base64(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_intro_bg():

    img = get_base64("background.jpg")

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{img}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ===================== DASHBOARD BACKGROUND =====================
def set_dashboard_bg():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(to right, #ffffff, #ffffff);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# ===================== INTRO PAGE =====================
def show_intro():
    set_intro_bg()

    st.markdown(
        "<h1 style='text-align:left;font-size:70px;'>INSTAGRAM USERS ANALYSIS</h1>",
        unsafe_allow_html=True
    )

    st.divider()

    col1, col2 = st.columns([1, 1])

    with col1:
        st.title("Introduction")
        st.write("""
                 Ever wonder who else is doomscrolling at 2 AM? This report breaks down the numbers behind our Instagram obsessions. Please enter your name here!""")
        name = st.text_input(
            "Enter your name",
            label_visibility="collapsed"
        )

        if name:
            st.markdown(f"""
            <div style="font-size:20px">
            <b>Hello <i>{name}</i></b> 👋<br><br>
            Welcome to the Instagram User Analysis Dashboard! This platform helps you explore 
how people use Instagram, including their engagement patterns, daily activity, 
content preferences, and lifestyle factors. 

Here, you will discover valuable insights about user behavior and how different 
factors such as age, income, and habits influence interactions on social media.
            </div>
            """, unsafe_allow_html=True)

        if st.button("Click here to get started"):
            st.session_state.clicked = True
            st.rerun()


# ===================== INTRO LOGIC =====================
if not st.session_state.clicked:
    show_intro()
    st.stop()

# ===================== DASHBOARD BG =====================
set_dashboard_bg()

# ===================== SIDEBAR =====================
st.sidebar.title("📊 Instagram Dashboard")

selected_gender = st.sidebar.multiselect(
    "Gender",
    df["Gender"].unique(),
    default=df["Gender"].unique()
)

age_range = st.sidebar.slider(
    "Age Range",
    int(df["age"].min()),
    int(df["age"].max()),
    (int(df["age"].min()), int(df["age"].max()))
)

selected_income = st.sidebar.multiselect(
    "Income Level",
    df["income_level"].unique(),
    default=df["income_level"].unique()
)

# ===================== FILTER DATA =====================
filtered_df = df[
    (df["Gender"].isin(selected_gender)) &
    (df["age"].between(age_range[0], age_range[1])) &
    (df["income_level"].isin(selected_income))
]

# ===================== NAVIGATION =====================
menu = st.sidebar.radio(
    "Navigation",
    ["About our Dataset","About Instagram","Overview", "User Behavior", "Engagement Analysis", "Content Insights", "Health & Lifestyle"]
)

# ===================== DATA OVERVIEW =====================
if menu == "About our Dataset":
    st.title("📊 Data Overview")
    st.markdown('<hr style="border: none; border-top: 3px solid black;">', unsafe_allow_html=True)
# ================= AUTHOR SECTION =================
    st.header("👤 Dataset Author")
    col1, col2 = st.columns([1, 2])

    with col1:
     st.image(r"C:\Users\daidi\OneDrive\Pictures\Screenshots\Screenshot 2026-05-06 194655.png", width=200)  

    with col2:
     st.subheader("Author Information")
     st.write("""
    - **Name:** Rocky  
    - **Role:** Student at IIT Guwahati  
    - **Native place:** Delhi, Delhi, India    
    """)
    st.write("""
    This dataset was created to study Instagram user behavior, engagement patterns,
    and the relationship between social media usage and lifestyle factors.
    """)
    # ---------------- WHY ----------------
    st.header("1. Purpose of the Analysis")
    st.write("""
    The reason why this dataset is chosen is that it offers a complex perspective on the use of social media incorporating demographic information with more specific behavioral indicators. However, in contrast to simpler data, it is capable of productive subgroup analysis, e.g., comparing the lifestyle of urban and rural users or monitoring the changes in the level of engagement in accordance with age. This information allows a profound study of the effect of lifestyle and the environment on digital consumption, which is why it is a great source to study the factors that influence user retention and activity on social networks of the modern generation.
    """)

    # ---------------- WHAT ----------------
    st.header("2. What We Investigate")
    st.write("""
    The main aim of such analysis is to explain the complicated connection between the offline life of a user and online conduct. By having data that traces both the major demographic levels and feature-based interactions, we will strive to go beyond the merely usage-related statistics and delve into the psychological and social trend. Through the analysis of the navigation of various types of users on the platform, it will be possible to define the factors that have the strongest impact on the formation of digital habits and the sense of well-being.
             The analysis focuses on:
    - User engagement patterns
    - Time spent on Instagram
    - Differences across demographic groups (age, gender, income)
    - Relationships between lifestyle factors (diet, stress)
    """)

    # ---------------- HOW ----------------
    st.header("3. How We Investigate")
    st.write("""
    First, we together choose our favorite topic. Then, we will find the dataset online, if the dataset is too little or the usability is low, we will try to choose another one. After we have a suitable dataset, we will investigate the data to see which categories we should use to draw plots. By asking questions related to this topic, we can find the appropriate items. Before drawing the plot, we have to learn and read the book to know how to draw plots on R Studio, which is the most important stage in this project. After completing the initial analysis, we will also clean the dataset by removing missing or inconsistent values to ensure accuracy. Then, we will choose suitable visualization types such as bar charts, line charts, or scatter plots depending on the data characteristics. We will also customize the plots by adjusting colors, labels, and themes to make them clearer and more visually appealing. Lastly, we will draw the plots of those categories and write a description of the trend. 
             To conclude, we use data visualization and aggregation techniques to explore patterns:
    - Grouping and comparing categories
    - Visualizing distributions (histograms, box plots)
    - Exploring relationships (scatter plots, heatmaps)
    """)

    # ---------------- VARIABLES ----------------
    st.header("4. Description of Variables")

    variable_info = pd.DataFrame({
        "Variable": [
            "age", "Gender", "income_level", "employment_status",
            "daily_active_minutes_instagram", "user_engagement_score",
            "posts_created_per_week", "content_type_preference",
            "diet_quality", "perceived_stress_score"
        ],
         "Type": [
        "Numeric", "Categorical", "Categorical", "Categorical",
        "Numeric", "Numeric", "Numeric", "Categorical",
        "Categorical", "Numeric"
        ],
        "Description": [
            "Age of the user",
            "Gender of the user",
            "Income category of the user",
            "Employment status",
            "Average daily time spent on Instagram (minutes)",
            "Overall engagement score",
            "Number of posts created per week",
            "Preferred content type",
            "Self-reported diet quality",
            "Perceived stress level"
        ],
        "Unit / Values": [
        "Years",
        "Male, Female, Other",
        "Low, Medium, High",
        "Student, Employed, Unemployed",
        "Minutes",
        "Score (0–100)",
        "Posts/week",
        "Reels, Feed, Stories, etc.",
        "Poor, Average, Good",
        "Score (e.g., 1–10)"
        ],
        "Role": [
        "Demographic",
        "Demographic",
        "Demographic",
        "Demographic",
        "Behavior",
        "Target variable",
        "Behavior",
        "Preference",
        "Lifestyle",
        "Outcome variable"
        ]
    })

    st.dataframe(variable_info, width='stretch')

    # ---------------- DATA TABLE ----------------
    st.header("5. Dataset Preview")

    st.write("Original Dataset:")
    st.dataframe(df.head(201), width='stretch')

    # Optional: show dataset shape
    st.write(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

# ===================== OVERVIEW =====================
if menu == "Overview":
    st.title("📸 Overview")
    st.markdown('<hr style="border: none; border-top: 3px solid black;">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Analyzed Users", len(filtered_df))
    col2.metric("Avg Engagement", round(filtered_df["user_engagement_score"].mean(), 2))
    col3.metric("Avg Daily Time", round(filtered_df["daily_active_minutes_instagram"].mean(), 1))

    st.subheader("Age Distribution")

    fig = px.histogram(filtered_df, x="age", nbins=20, text_auto=True)
    fig.update_traces(
        marker_line_color="white",
        marker_line_width=2,
        textposition="outside"
    )

    st.plotly_chart(fig, width="stretch")
    st.markdown(
    "<p style='font-size:12px;'><b>Age Distribution Analysis of All Users</b></p>",
    unsafe_allow_html=True
)
    st.markdown(
       """
       <div style='text-align: justify;'>
       The histogram illustrates the age distribution of a user group, ranging from approximately 12 to 67 years old. Overall, the data shows a fluctuating pattern with the highest concentration of users in the middle-aged and young-adult.

In detail, the most significant peak is seen in the 32–37 age group, which has 24 users. This is closely followed by the 40–45 and 52–57 age group, both having around 23 users. Moreover, there is a notable drop in the 27–32 age range, where the number of users falls to only 10, the lowest point in the first half of the graph. As users get older, the figures generally decline, with the 57–62 category recording only 11 users before a slight rise to 13 in the final bracket.

Overall, the distribution indicates that most users are concentrated between their early 30s and mid-50s, while younger and older age groups are slightly less represented. This suggests that the platform or dataset tends to attract a larger proportion of middle-aged users compared with teenagers or seniors.
        <div/>
        """,
        unsafe_allow_html=True)

    st.subheader("Gender Distribution")
    fig = px.pie(filtered_df, names="Gender")
    st.plotly_chart(fig, width="stretch")
    st.markdown(
    "<p style='font-size:12px;'><b>Gender Distribution Analysis of All Users</b></p>",
    unsafe_allow_html=True
)
    st.markdown(
       """
       <div style='text-align: justify;'>
       The provided pie chart illustrates the gender composition of a particular population, categorized into four distinct groups. 

Overall, it is clear that the distribution is heavily dominated by individuals identifying as female or male, which together constitute the vast majority of the data. 

Females represent the largest segment at 47%, followed closely by males at 45%, indicating a relatively balanced distribution between the two primary groups with a marginal difference of only 2%. In contrast, the remaining categories account for a significantly smaller portion of the total; those identifying as non-binary make up 4.5%, while the smallest group consists of individuals who preferred not to disclose their gender, at 3.5%. 

Combined, these minority groups represent less than one-tenth of the overall gender distribution.
        <div/>
        """,
        unsafe_allow_html=True)


# ===================== USER BEHAVIOR =====================
elif menu == "User Behavior":
    st.title("👤 User Behavior")
    st.markdown('<hr style="border: none; border-top: 3px solid black;">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Daily Usage")
        fig = px.box(filtered_df, y="daily_active_minutes_instagram")
        st.plotly_chart(fig, width="stretch")

    with col2:
        st.subheader("Session Length")
        fig = px.box(filtered_df, y="average_session_length_minutes")
        st.plotly_chart(fig, width="stretch")
    st.markdown(
    "<p style='font-size:12px;'><b>Daily Usage & Session Length Analysis of All Users</b></p>",
    unsafe_allow_html=True
)
    st.markdown(
       """
       <div style='text-align: justify;'>
       The box plots compare two aspects of Instagram user engagement: total daily active minutes and average session length in minutes. 

Overall, it is evident that while the total time spent on the platform per day is substantial, individual sessions are comparatively brief. Regarding daily usage, the median sits at approximately 190 minutes, with a significant range extending from nearly zero to a peak of roughly 480 minutes. 

In contrast, session lengths are more concentrated; the median session lasts about 21 minutes, with the majority of users spending between 13 and 27 minutes per visit. Interestingly, the maximum session length of approximately 41 minutes is significantly lower than the upper reaches of daily usage, suggesting that high daily totals are likely the result of multiple frequent visits throughout the day rather than a single prolonged period of use.
        <div/>
        """,
        unsafe_allow_html=True)

    st.subheader("Urban vs Rural Usage")
    # Dropdown menu
    area_option = st.selectbox(
    "Choose Area Type",
    ["All", "Urban", "Rural", "Suburban"],
    key="scatter_content")

# Filter data based on dropdown
    if area_option != "All":
     area_df = filtered_df[
        filtered_df["urban_rural"].str.lower() == area_option.lower()
    ]
    else:
     area_df = filtered_df
    fig = px.bar(
        area_df.groupby("urban_rural")["daily_active_minutes_instagram"].mean().reset_index(),
        x="urban_rural",
        y="daily_active_minutes_instagram",
        color="urban_rural"
    )
    st.plotly_chart(fig, width='stretch')
    st.markdown(
    "<p style='font-size:12px;'><b>Daily Instagram Usage Analysis by Residential Area of All Users</b></p>",
    unsafe_allow_html=True
)
    st.markdown(
       """
       <div style='text-align: justify;'>
       The bar chart examines the relationship between residential environment and the average amount of time spent daily on Instagram. 

Overall, it is striking that usage remains relatively uniform across all three categories, despite a very slight downward trend from rural to urban settings. Rural users exhibit the highest level of engagement, recording approximately 193 minutes of activity per day. This is followed closely by suburban residents, who spend roughly 189 minutes on the app. 

Urban users account for the lowest daily usage, though at approximately 184 minutes, the figure remains substantial. Ultimately, the data reveals a negligible disparity of only about 9 minutes between rural and urban demographics, indicating that geographical location has a limited impact on the duration of Instagram usage.
        <div/>
        """,
             unsafe_allow_html=True)

# ===================== ENGAGEMENT =====================
elif menu == "Engagement Analysis":
    st.title("🔥 Engagement")
    st.markdown('<hr style="border: none; border-top: 3px solid black;">', unsafe_allow_html=True)

    st.subheader("Followers vs Engagement Score")
    # Dropdown menu
    engage_option = st.selectbox(
    "Choose Content Type",
    ["All", "Mixed", "Photos", "Reels","Videos","Stories","Live"],
    key="bar_content")

# Filter data based on dropdown
    if engage_option != "All":
     engage_df = filtered_df[
        filtered_df["content_type_preference"].str.lower() == engage_option.lower()
    ]
    else:
     engage_df = filtered_df
    fig = px.scatter(
        engage_df,
        x="Followers count",
        y="user_engagement_score",
        color="content_type_preference",
        size="posts_created_per_week"
    )
    st.plotly_chart(fig, width="stretch")
    st.markdown(
    "<p style='font-size:12px;'><b>Followers vs Engagement Score Analysis of All Users</b></p>",
    unsafe_allow_html=True
)
    st.markdown(
       """
       <div style='text-align: justify;'>
       The scatter chart illustrates the relationship between follower counts and user engagement scores on a social media platform, categorized by content preference. Overall, there is a clear concentration of users with fewer than 4,000 followers, and while engagement scores vary widely for this group, they generally decrease as follower counts increase.

Most users are clustered at the lower end of the follower scale (0 to 2,000), where engagement scores range significantly from nearly 0 to 10. Specifically, users who prefer "Live" and "Photos" content occasionally achieve the highest engagement scores, peaking at approximately 11.5 and 9.5 respectively within the 2k-4k follower range.

In contrast, users with larger followings, exceeding 8,000, tend to exhibit much lower and more stable engagement scores, rarely surpassing 2.0. Additionally, the size of the bubbles, representing the volume of content, appears larger among users with high engagement but fewer followers. Ultimately, the data suggests that having a massive follower base does not guarantee high engagement, as the most interactive accounts are often those with smaller, more niche audiences.
        <div/>
        """,
        unsafe_allow_html=True)

    st.subheader("Posts per Week vs Engagement Score")
    # Dropdown menu
    engage_option1 = st.selectbox(
    "Choose Content Type",
    ["All", "Mixed", "Photos", "Reels","Videos","Stories","Live"])

# Filter data based on dropdown
    if engage_option1 != "All":
     engage_df = filtered_df[
        filtered_df["content_type_preference"].str.lower() == engage_option1.lower()
    ]
    else:
     engage_df = filtered_df
    fig = px.bar(
        engage_df,
        x="posts_created_per_week",
        y="user_engagement_score",
        color="content_type_preference"
    )
    st.plotly_chart(fig, width='stretch')
    st.markdown(
    "<p style='font-size:12px;'><b>User Engagement by Posting Frequency Analysis of All Users</b></p>",
    unsafe_allow_html=True
)
    st.markdown(
       """
       <div style='text-align: justify;'>
       The stacked bar chart compares total user engagement scores based on the number of posts created per week, segmented by preferred content types. Overall, engagement peaks at a moderate posting frequency of two to three times per week and steadily declines as the number of weekly posts increases beyond that point.

The highest total engagement is recorded at 2 posts per week, reaching a cumulative score of nearly 70. At this level, "Photos" and "Mixed" content contribute the largest portions to the total. This is followed closely by the 3-post-per-week category, which sees a slightly lower total of approximately 55, though it maintains a diverse mix of content types including "Reels" and "Stories."

As posting frequency rises further, engagement levels drop significantly. By the time users reach 10 or more posts per week, total engagement scores fall below 20 and continue to diminish toward negligible levels at 16 posts. Notably, "Live" content (indicated in green) maintains a consistent presence across low-to-mid posting frequencies but almost disappears in the high-frequency brackets. In summary, a "less is more" trend is evident, where posting more than three times weekly correlates with a sharp reduction in total engagement.
        <div/>
        """,
        unsafe_allow_html=True)


# ===================== CONTENT =====================
elif menu == "Content Insights":
    st.title("🎥 Content")
    st.markdown('<hr style="border: none; border-top: 3px solid black;">', unsafe_allow_html=True)

    st.subheader("Content Type Preference")
     # Dropdown menu
    engage_option2 = st.selectbox(
    "Choose Content Type",
    ["All", "Mixed", "Photos", "Reels","Videos","Stories","Live"],
    key="pie_content")

# Filter data based on dropdown
    if engage_option2 != "All":
     engage_df = filtered_df[
        filtered_df["content_type_preference"].str.lower() == engage_option2.lower()
    ]
    else:
     engage_df = filtered_df
    fig = px.pie(engage_df, names="content_type_preference")
    st.plotly_chart(fig, width="stretch")
    st.markdown(
    "<p style='font-size:12px;'><b>Content Types Preference Analysis of All Users</b></p>",
    unsafe_allow_html=True
)
    st.markdown(
       """
       <div style='text-align: justify;'>
       The pie chart indicates the distribution of content type preferences on Instagram, which are live, mixed, photos, reels, stories and videos. In general, all of the content types seem to account for an equivalent percentage of the whole chart.

Looking at the figures in detail, it can be seen that live content accounts for 19.5%, which represents the highest category. This shows that live and real-time experiences are attracted by reported users. Photos and reels follow closely at 18.5% and 18% respectively, suggesting that visual, image-based content remains highly popular and continues to play an important role in user engagement. 

Moreover, reels and mixed content are not preferred, only 14% of the reported users tend to watch these types of content. Finally, videos hold the smallest proportion at 14%, however the difference compared to others is not large. This could be affected by the time the videos are mostly lengthy and the users may become bored soon.

To conclude, the chart highlights many user interests and suggests that content creators may focus on varied content types rather than focusing on a single format because audience preferences are spread evenly across multiple content types.
        <div/>
        """,
        unsafe_allow_html=True)

    st.subheader("Feature Usage (Feed, Explore, Reels, Messages)")
     # Dropdown menu
    engage_option3 = st.selectbox(
    "Choose Content Type",
    ["All", "Feed", "Explore", "Reels","Messages"],
    key="box_content")
    

# Filter data based on dropdown
    if engage_option3 != "All":
     engage_df = filtered_df[
        filtered_df["content_type_preference"].str.lower() == engage_option3.lower()
    ]
    else:
     engage_df = filtered_df
    features = ["Feed", "Explore", "Reels", "Messages"]
    # Convert dataframe to long format
    df_melt = filtered_df[features].melt(
    var_name="Feature",
    value_name="Usage")

# Filter selected feature
    if engage_option3 != "All":
     df_melt = df_melt[
        df_melt["Feature"] == engage_option3]
    fig = px.box(df_melt, x="Feature", y="Usage", color="Feature")
    st.plotly_chart(fig, width="stretch")
    st.markdown(
    "<p style='font-size:12px;'><b>Feature Usage Analysis of All Users</b></p>",
    unsafe_allow_html=True
)
    st.markdown(
       """
       <div style='text-align: justify;'>
       The following report summarizes Instagram user engagement across several metrics, including demographics, usage patterns, and feature preferences.

Overall, the platform exhibits a balanced gender distribution and high daily engagement. While the Feed remains the most utilized feature, total usage time remains incredibly stable across different residential environments.

Demographically, the user base is nearly equal, with females and males accounting for 47% and 45% of the population, respectively. In terms of behavior, the median user spends roughly 190 minutes daily on the app, though individual sessions are relatively brief at just 21 minutes, indicating frequent, short-term visits. Notably, this engagement varies little by location; rural residents spend only 9 minutes more on the app daily than their urban counterparts.

Regarding specific app components, the Feed is the dominant feature, with a median usage of nearly 100 minutes. This is followed by Reels (~60 minutes), while the Explore and Messaging features see significantly lower engagement, with medians of 35 and 30 minutes, respectively. In summary, Instagram users demonstrate consistent, high-frequency habits centered primarily around main-feed content.
        </div>
        """,
        unsafe_allow_html=True)

# ===================== HEALTH =====================
elif menu == "Health & Lifestyle":
    st.title("🥗 Health & Lifestyle")
    st.markdown('<hr style="border: none; border-top: 3px solid black;">', unsafe_allow_html=True)

    st.subheader("Diet Quality by Gender")
    
    counts = filtered_df.groupby(['Gender', 'diet_quality']).size().reset_index(name='count')
# Convert to proportion
    counts['prop'] = counts['count'] / counts.groupby('Gender')['count'].transform('sum')
# Plot (100% stacked bar)
    fig = px.bar(
    counts,
    x="Gender",
    y="prop",
    color="diet_quality",
    barmode="relative",   
    text=counts['prop'].apply(lambda x: f"{x*100:.1f}%"))
 # Styling to match dashboard
    fig.update_layout(
    title_text="",
    xaxis_title="Gender",
    yaxis_title="Proportion",
    yaxis=dict(tickformat=".0%"),
    font=dict(size=14))
# Clean look (no gridlines)
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    
    st.plotly_chart(fig, width='stretch')
    st.markdown(
    "<p style='font-size:12px;'><b>Diet Quality Analysis of All Users</b></p>",
    unsafe_allow_html=True
)
    st.markdown(
       """
       <div style='text-align: justify;'>
       The mosaic plot depicts the relationship between users' dietary quality and their gender. Generally, the average diet quality category constitutes the largest proportion across most gender groups, indicating that a significant number of users report a moderate level of dietary quality, as opposed to diets that are either extremely healthy or unhealthy.

Regarding female users, the highest proportion is found in the average diet quality category, at 37.2%, succeeded by good diet quality at 20.2%. Conversely, the poor and very poor categories represent smaller proportions, specifically 17% and 12.8%, respectively. A comparable trend is evident among male users, where the average diet quality accounts for 37.8%. 

For non-binary users, the distribution is more evenly spread across the categories, with poor, excellent, and average diet quality each representing approximately 33.3%, which suggests a more uniform distribution of dietary habits within this group. In contrast, individuals who prefer not to say their gender show a strong concentration in the average category at 57.1%, the highest proportion among all groups, followed by excellent and poor.

To conclude, the chart indicates that average diet quality is the most common across all gender groups, while other categories such as very poor or excellent diets appear less frequently.
        </div>
        """,
        unsafe_allow_html=True)

    st.subheader("Stress by Employment & Income")
    # Prepare data
    heatmap_data = filtered_df.groupby(
    ['employment_status', 'income_level'])['perceived_stress_score'].mean().reset_index()

    pivot_table = heatmap_data.pivot(
    index='employment_status',
    columns='income_level',
    values='perceived_stress_score')

# Check if data exists
    if pivot_table.empty:
     st.warning("No data available for selected filters")
    else:
     fig = px.imshow(
        pivot_table,
        text_auto=".1f",
        aspect="auto",
        color_continuous_scale=[
            "#FDEDEC", "#F5B7B1", "#EC7063", "#C0392B"
        ])

     fig.update_layout(
        title_x=0.5,
        xaxis_title="Income Level",
        yaxis_title="Employment Status",
        font=dict(size=14)
    )
     fig.update_layout(title="")
     fig.update_xaxes(showgrid=False)
     fig.update_yaxes(showgrid=False)
     st.plotly_chart(fig, width='stretch')
     st.markdown(
    "<p style='font-size:12px;'><b>Perceived Stress Analysis of All Users</b></p>",
    unsafe_allow_html=True
)
    st.markdown(
       """
       <div style='text-align: justify;'>
       The heatmap compares average stress levels across different employment statuses and income levels. Overall, unemployed individuals and students in the high-income category experience the highest stress, while retired people with high income report the lowest levels.

Specifically, the highest stress score of 36 is recorded by unemployed users with high income, followed by students in the same bracket at 32. In sharp contrast, retired individuals with high income show a minimal stress score of only 5, which is the lowest in the entire table. For other groups, stress levels remain relatively moderate. For instance, full-time employees' scores fluctuate between 13.4 and 23.9. Generally, the middle and lower middle income columns show more consistent scores, mostly ranging from 14 to 25 across most job types.

In addition, freelancers tend to experience relatively high stress levels in the upper-middle income group, reaching a value of 26. Meanwhile, part-time workers show moderate stress levels, generally ranging from around 10 to 20 depending on income level.

Overall, the heatmap suggests that stress levels vary not only by income but also significantly by employment status, with unemployed individuals and students showing greater stress fluctuations compared to other groups.
        </div>
        """,
        unsafe_allow_html=True)
# ===================== ABOUT INSTAGRAM =====================
elif menu == "About Instagram":

    st.title("📸 About Instagram")
    st.markdown('<hr style="border: none; border-top: 3px solid black;">', unsafe_allow_html=True)

    # ================= INTRO =================
    col1, col2 = st.columns([1.3, 1])

    with col1:
        st.markdown(
            """
            <div style='text-align: justify; font-size:16px; line-height:1.8;'>

            <b>Instagram</b> is one of the world's most popular social media platforms,
            allowing users to share photos, videos, stories, reels, and live streams.
            The platform was launched in 2010 and later acquired by Meta Platforms.

            Instagram has transformed digital communication by encouraging visual content,
            influencer culture, online businesses, and social interaction across the globe.
            Today, millions of users spend hours daily browsing feeds, interacting with creators,
            and consuming entertainment content.

            The platform offers several major features such as Feed posts, Stories, Reels,
            Explore pages, and direct messaging. Each feature serves different user behaviors
            and engagement patterns.

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg",
            width=250
        )

    st.divider()

    # ================= HISTORY =================
    st.header("📖 Brief History")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1611162616305-c69b3fa7fbe0?q=80&w=1200&auto=format&fit=crop",
            width='stretch'
        )

    with col2:
        st.markdown(
            """
            <div style='text-align: justify; font-size:16px; line-height:1.8;'>

            Instagram was created by Kevin Systrom and Mike Krieger.
            Initially designed as a simple photo-sharing application,
            the platform quickly became one of the fastest-growing apps worldwide.

            Over time, Instagram expanded its ecosystem by introducing:

            • Stories (2016)
            • Reels (2020)
            • Shopping features
            • Creator tools
            • AI-based recommendations
            """,
            unsafe_allow_html=True)
    st.divider()

    # ================= FEATURES =================
    st.header("⭐ Main Instagram Features")
   
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image(
            "https://cdn-icons-png.flaticon.com/512/1828/1828859.png",
            width=70
        )
        st.markdown("### Feed")
        st.caption("Main scrolling content area")

    with col2:
        st.image(
            "https://cdn-icons-png.flaticon.com/512/1828/1828884.png",
            width=70
        )
        st.markdown("### Reels")
        st.caption("Short-form entertainment videos")

    with col3:
        st.image(
            "https://cdn-icons-png.flaticon.com/512/747/747376.png",
            width=70
        )
        st.markdown("### Stories")
        st.caption("24-hour temporary content")

    with col4:
        st.image(
            "https://cdn-icons-png.flaticon.com/512/1380/1380338.png",
            width=70
        )
        st.markdown("### Messages")
        st.caption("Private communication feature")

    st.divider()
    # ================= GLOSSARY =================
    st.header("📚 Instagram Glossary")

    glossary_df = pd.DataFrame({
        "Term": [
            "Feed",
            "Reels",
            "Stories",
            "Explore",
            "DM",
            "Engagement",
            "Influencer",
            "Algorithm"
        ],

        "Meaning": [
            "Main homepage content stream",
            "Short vertical videos",
            "Temporary posts lasting 24 hours",
            "Content discovery section",
            "Direct Messages between users",
            "User interaction level (likes, comments, shares)",
            "A creator with a strong online audience",
            "System that recommends content to users"
        ]
    })

    st.dataframe(glossary_df, width='stretch')

    st.divider()

    # ================= FACTS =================
    st.header("📊 Interesting Facts")

    st.markdown(
        """
        <div style='font-size:16px; line-height:2;'>

        • Instagram has more than 2 billion monthly active users worldwide.<br>
        • Reels is currently one of the platform's fastest-growing features.<br>
        • The majority of Instagram users are under 35 years old.<br>
        • Businesses widely use Instagram for digital marketing and branding.<br>
        • Visual content generally receives higher engagement than plain text.

        </div>
        """,
        unsafe_allow_html=True
    )