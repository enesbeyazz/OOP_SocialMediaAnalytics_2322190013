Social Media Analytics Platform
Student: Enes Beyaz (2322190013)
Assignment: Assignment 9 - Social Media Analytics Platform
Course: Object Based Programming (2019G0005)

📋 Project Overview
This project implements a Social Media Analytics Platform using Object-Oriented Programming principles. The system manages social media accounts, posts, and interactions across multiple platforms (Instagram, X, Facebook) and provides analytics capabilities for engagement metrics and account performance.

🎯 Project Objectives
Apply OOP principles (Encapsulation, Inheritance, Polymorphism, Abstraction)
Implement data structures for efficient analytics computation
Develop algorithms for engagement tracking and recommendation
Create a modular, maintainable architecture
🏗️ Architecture Design (Stage 1)
Class Diagram
┌─────────────────────────────────────┐
│         SocialAccount               │
├─────────────────────────────────────┤
│ - id: int                           │
│ - username: str                     │
│ - platform: str                     │
│ - followers_count: int              │
│ - following_count: int              │
│ - posts: List[SocialPost]           │
├─────────────────────────────────────┤
│ + view_profile(): str               │
└─────────────────────────────────────┘
                 │
                 │ has many
                 ▼
┌─────────────────────────────────────┐
│           SocialPost                │
├─────────────────────────────────────┤
│ - id: int                           │
│ - content: str                      │
│ - account: SocialAccount            │
│ - timestamp: datetime               │
│ - likes: int                        │
│ - comments: int                     │
│ - shares: int                       │
│ - impressions: int                  │
│ - interactions: List[Interaction]   │
├─────────────────────────────────────┤
│ + add_like(source_account): void   │
│ + add_comment(source_account): void│
│ + add_share(source_account): void  │
│ + add_impression(): void            │
└─────────────────────────────────────┘
                 │
                 │ has many
                 ▼
┌─────────────────────────────────────┐
│          Interaction                │
├─────────────────────────────────────┤
│ - id: int                           │
│ - type: str                         │
│ - post: SocialPost                  │
│ - timestamp: datetime               │
│ - source_account: SocialAccount     │
├─────────────────────────────────────┤
│ (no public methods)                 │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│       AnalyticsEngine               │
├─────────────────────────────────────┤
│ (no attributes)                     │
├─────────────────────────────────────┤
│ + calculate_engagement_rate(): float│
│ + get_account_summary(): Dict       │
└─────────────────────────────────────┘
                 ▲
                 │ uses
                 │
┌─────────────────────────────────────┐
│  SocialMediaAnalyticsSystem         │
├─────────────────────────────────────┤
│ - accounts: List[SocialAccount]     │
│ - posts: List[SocialPost]           │
│ - analytics_engine: AnalyticsEngine │
│ - accounts_by_id: Dict[int, Account]│
│ - posts_by_id: Dict[int, Post]      │
├─────────────────────────────────────┤
│ + add_account(account): void        │
│ + add_post(post): void              │
│ + get_post_by_id(id): SocialPost    │
│ + get_account_by_id(id): Account    │
│ + get_top_posts_by_engagement(): []│
│ + get_account_summary(id): Dict     │
└─────────────────────────────────────┘
Relationships
┌──────────────────┐         ┌──────────────────┐
│ SocialAccount    │ 1     * │   SocialPost     │
│                  │◆────────│                  │
└──────────────────┘         └──────────────────┘
                                      │
                                      │ 1
                                      │
                                      │ *
                                      ▼
                             ┌──────────────────┐
                             │   Interaction    │
                             └──────────────────┘

┌──────────────────────────────┐
│ SocialMediaAnalyticsSystem   │
│                              │
│  ┌────────────────────┐      │
│  │ AnalyticsEngine    │      │
│  └────────────────────┘      │
└──────────────────────────────┘
🔧 Implementation Details
Core Classes
1. Interaction
Represents a single interaction event (like, comment, share, view)
Stores timestamp and optional source account
Immutable after creation
2. SocialAccount
Represents a user account on any platform
Manages follower/following counts
Contains list of owned posts
Key Methods:
view_profile(): Returns formatted profile information
3. SocialPost
Represents a post with content and metrics
Tracks likes, comments, shares, impressions
Maintains interaction history
Key Methods:
add_like(), add_comment(), add_share(): Update metrics and log interactions
add_impression(): Track post views
4. AnalyticsEngine
Centralized analytics computation
Calculates engagement metrics
Generates account summaries
Key Methods:
calculate_engagement_rate(): (likes + comments + shares) / followers
get_account_summary(): Aggregate statistics for an account
5. SocialMediaAnalyticsSystem
Main orchestrator/facade
Manages all accounts and posts
Provides fast lookup via hash maps
Key Methods:
add_account(), add_post(): Register new entities
get_top_posts_by_engagement(): Ranked post list
get_account_summary(): Account statistics
💡 OOP Principles Applied
✅ Encapsulation
Private data managed through public methods
Interaction metrics updated only through defined methods
Internal collections hidden behind system interface
✅ Composition
SocialAccount has many SocialPost
SocialPost has many Interaction
SocialMediaAnalyticsSystem uses AnalyticsEngine
✅ Aggregation
System aggregates accounts and posts
Weak ownership - entities can exist independently
✅ Single Responsibility Principle
Each class has one clear purpose
AnalyticsEngine separated from data management
Interaction only represents interaction events
🔍 Algorithms Implemented (Stage 2)
1. Interaction Counting
Integer counters maintained in SocialPost
O(1) increment operations
2. Engagement Rate Calculation
engagement_rate = (likes + comments + shares) / followers
3. Search by ID
Hash map lookup: O(1) average case
posts_by_id, accounts_by_id dictionaries
4. Sorting by Engagement
Uses Python's built-in sort with custom key
Time complexity: O(n log n)
📊 Data Structures
Structure	Purpose	Access Time
List[SocialPost]	Store all posts	O(n) search
Dict[int, SocialPost]	Fast post lookup	O(1) average
Dict[int, SocialAccount]	Fast account lookup	O(1) average
List[Interaction]	Interaction history	O(n) traverse
🚀 Usage Example
# Initialize system
system = SocialMediaAnalyticsSystem()

# Create account
user = SocialAccount(1, "hz.enes_official", "Instagram")
user.followers_count = 1500
system.add_account(user)

# Create post
post = SocialPost(101, "Respect to hz_enes", user)
system.add_post(post)

# Add interactions
post.add_like()
post.add_comment()
post.add_share()
post.add_impression()

# Get analytics
engagement = system.analytics_engine.calculate_engagement_rate(post)
summary = system.get_account_summary(1)

print(f"Engagement Rate: {engagement:.2%}")
print(f"Account Summary: {summary}")
📁 Project Structure
OOP_SocialMediaAnalytics_2322190013/
│
├── README.md                          # This file
├── main.py                            # Main implementation
│
├── S1_Design/                         # Stage 1: Architecture
│   └── class_diagram.pdf
│
├── S2_BasicImplementation/            # Stage 2: Basic Features
│   └── main.py
│
└── S3_AdvancedAlgorithms/             # Stage 3: Advanced Features
    └── (to be implemented)
🎯 Stage 2 Completed Features
✅ Core class implementation
✅ Account and post management
✅ Interaction logging
✅ Basic analytics (engagement rate, account summary)
✅ Fast lookup using hash maps
✅ Sorting by engagement
🔜 Stage 3 - Planned Features
Polymorphic Post Types
TextPost, ImagePost, VideoPost subclasses
Polymorphic getContentSummary() method
Advanced Algorithms
Recommendation System

Top N posts by engagement
Top N accounts by average engagement
Trending Detection

Hashtag frequency analysis
Keyword trending over time
Usage Analytics

Per-platform statistics
Content type breakdown
System-wide summaries
Additional Features
JSON data import/export
Simple UI/Dashboard
Multi-platform comparison
🛠️ Technologies Used
Language: Python 3.x
Core Libraries:
datetime - Timestamp management
typing - Type hints for clarity
📝 Design Decisions
Hash Maps for Fast Lookup: Used dictionaries for O(1) access to posts and accounts by ID
Composition over Inheritance: Preferred composition for relationships (Account has Posts)
Centralized Analytics: Separated analytics logic into dedicated engine class
Interaction Logging: Complete history maintained for future analytics capabilities
Optional Source Account: Allows tracking anonymous interactions while supporting user attribution
🧪 Testing Strategy
Unit Tests (Planned)
Account creation and profile viewing
Post creation and metric updates
Engagement rate calculation
Top posts ranking algorithm
Account summary generation
Mock Objects
Mock accounts for testing analytics
Simulated interaction patterns
📚 References
Course Materials: Introduction to OOP (cs01, cs02_01)
Assignment Description: Final Assignment Descriptions.pdf
Python Documentation: docs.python.org
👤 Student Information
Name: Enes Beyaz
Student ID: 2322190013
Program: Software Engineering (English)
Course: Object Based Programming
Lecturer: Dr. Coşkun Şahin