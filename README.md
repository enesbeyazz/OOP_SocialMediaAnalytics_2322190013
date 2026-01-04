## Social Media Analytics Platform

**Student:** Enes Beyaz (2322190013)  
**Assignment:** Assignment 9 – Social Media Analytics Platform  
**Course:** Object Based Programming (2019G0005)  

---

## 📋 Project Overview

This project implements a **Social Media Analytics Platform** using **Object-Oriented Programming (OOP)** principles.  
The system manages social media accounts, posts, and interactions across multiple platforms (**Instagram, X, Facebook**) and provides analytics capabilities for engagement metrics and account performance.

---

## 🎯 Project Objectives

- Apply OOP principles (Encapsulation, Inheritance, Polymorphism, Abstraction)
- Implement data structures for efficient analytics computation
- Develop algorithms for engagement tracking and recommendation
- Create a modular, maintainable architecture

---

## 🏗️ Architecture Design (Stage 1)

### Class Diagram

┌─────────────────────────────────────┐
│ SocialAccount │
├─────────────────────────────────────┤
│ - id: int │
│ - username: str │
│ - platform: str │
│ - followers_count: int │
│ - following_count: int │
│ - posts: List[SocialPost] │
├─────────────────────────────────────┤
│ + view_profile(): str │
└─────────────────────────────────────┘
│ has many
▼
┌─────────────────────────────────────┐
│ SocialPost │
├─────────────────────────────────────┤
│ - id: int │
│ - content: str │
│ - account: SocialAccount │
│ - timestamp: datetime │
│ - likes: int │
│ - comments: int │
│ - shares: int │
│ - impressions: int │
│ - interactions: List[Interaction] │
├─────────────────────────────────────┤
│ + add_like(source_account) │
│ + add_comment(source_account) │
│ + add_share(source_account) │
│ + add_impression() │
└─────────────────────────────────────┘
│ has many
▼
┌─────────────────────────────────────┐
│ Interaction │
├─────────────────────────────────────┤
│ - id: int │
│ - type: str │
│ - post: SocialPost │
│ - timestamp: datetime │
│ - source_account: SocialAccount │
├─────────────────────────────────────┤
│ (no public methods) │
└─────────────────────────────────────┘

---

## 🔧 Implementation Details

### Core Classes

**Interaction**  
Represents a single interaction event (like, comment, share, view).  
Stores timestamp and optional source account.  
Immutable after creation.

**SocialAccount**  
Represents a user account on any platform.  
Manages follower/following counts.  
Contains list of owned posts.

Key Method:
- `view_profile()`

**SocialPost**  
Represents a post with content and metrics.  
Tracks likes, comments, shares, impressions.  
Maintains interaction history.

Key Methods:
- `add_like()`
- `add_comment()`
- `add_share()`
- `add_impression()`

**AnalyticsEngine**  
Centralized analytics computation.  
Calculates engagement metrics and generates summaries.

Key Methods:
- `calculate_engagement_rate()`
- `get_account_summary()`

**SocialMediaAnalyticsSystem**  
Main orchestrator / facade.  
Manages all accounts and posts.  
Provides fast lookup via hash maps.

Key Methods:
- `add_account()`
- `add_post()`
- `get_post_by_id()`
- `get_account_by_id()`
- `get_top_posts_by_engagement()`
- `get_account_summary()`

---

## 💡 OOP Principles Applied

### ✅ Encapsulation
- Private data managed through public methods
- Interaction metrics updated only through defined methods

### ✅ Composition
- SocialAccount has many SocialPost
- SocialPost has many Interaction
- System uses AnalyticsEngine

### ✅ Aggregation
- System aggregates accounts and posts
- Weak ownership (entities can exist independently)

### ✅ Single Responsibility Principle
- Each class has one clear purpose
- Analytics logic separated from data management

---

## 🔍 Algorithms Implemented (Stage 2)

**Interaction Counting**  
- Integer counters in `SocialPost`
- O(1) increment operations

**Engagement Rate Calculation**

**Search by ID**
- Hash map lookup
- O(1) average case

**Sorting by Engagement**
- Python built-in sort
- Time complexity: O(n log n)

---

## 📊 Data Structures

| Structure | Purpose | Access Time |
|--------|--------|------------|
| List[SocialPost] | Store all posts | O(n) |
| Dict[int, SocialPost] | Fast post lookup | O(1) |
| Dict[int, SocialAccount] | Fast account lookup | O(1) |
| List[Interaction] | Interaction history | O(n) |

---

## 🚀 Usage Example

```python
system = SocialMediaAnalyticsSystem()

user = SocialAccount(1, "hz.enes_official", "Instagram")
user.followers_count = 1500
system.add_account(user)

post = SocialPost(101, "Respect to hz_enes", user)
system.add_post(post)

post.add_like()
post.add_comment()
post.add_share()
post.add_impression()

engagement = system.analytics_engine.calculate_engagement_rate(post)
summary = system.get_account_summary(1)

print(f"Engagement Rate: {engagement:.2%}")
print(f"Account Summary: {summary}")
OOP_SocialMediaAnalytics_2322190013/
│
├── README.md
├── main.py
├── S1_Design/
│   └── class_diagram.pdf
├── S2_BasicImplementation/
│   └── main.py
└── S3_AdvancedAlgorithms/
Stage 3 – Planned Features

Polymorphic Post Types (TextPost, ImagePost, VideoPost)

Recommendation System

Trending Detection

Hashtag Frequency Analysis

JSON Import / Export

Simple UI Dashboard
🛠️ Technologies Used

Python 3.x

datetime

typing
👤 Student Information

Name: Enes Beyaz
Student ID: 2322190013
Program: Software Engineering (English)
Course: Object Based Programming
Lecturer: Dr. Coşkun Şahin