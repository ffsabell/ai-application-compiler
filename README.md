# AI Application Compiler

## Overview

AI Application Compiler is a compiler-inspired system that converts natural language application requirements into structured application specifications.

The system transforms a user prompt into:

* Intent Analysis
* Application Architecture
* Database Schema
* API Schema
* UI Schema
* Authentication Rules
* Validation Reports
* Runtime Simulation Results

The objective is to create reliable, structured, and executable application configurations from natural language input.

---

## Problem Statement

Users provide open-ended requirements such as:

> Build a CRM with login, contacts, dashboard, role-based access, payments and admin analytics.

The system converts these requirements into a complete application specification that can be validated and executed through a runtime simulation layer.

---

## System Architecture

User Prompt

↓

Compiler Engine

↓

Validation Engine

↓

Repair Engine

↓

Runtime Simulator

↓

Final Application Configuration

---

## Features

### Compiler Engine

Converts natural language requirements into:

* Intent
* Architecture
* Database Schema
* API Schema
* UI Schema
* Authentication Configuration

### Validation Engine

Checks generated output for:

* Missing sections
* Missing schemas
* Missing authentication rules
* Structural consistency

### Repair Engine

Automatically repairs incomplete outputs by generating default configurations where required.

### Runtime Simulator

Validates whether the generated application configuration is executable.

### Metrics Dashboard

Tracks:

* Latency
* Validation Errors
* Repairs Applied

---

## Technology Stack

* Python
* Streamlit
* Google Gemini API
* JSON
* Validation Engine
* Runtime Simulation

---

## Project Structure

AI-App-Compiler/

frontend.py

pipeline/

* compiler.py
* validator.py
* repair_engine.py
* runtime.py

evaluation/

* dataset.json
* run_evaluation.py

README.md

---

## Evaluation Framework

Dataset contains:

* 10 Normal Product Prompts
* 10 Edge Case Prompts

Examples:

* CRM System
* Ecommerce Platform
* Hospital Management
* Learning Management System

Edge Cases:

* Build something useful
* Create a website
* CRM without users
* Payment system without customers

---

## Metrics

The system measures:

* Request Latency
* Validation Failures
* Repairs Applied
* Runtime Success

---

## Reliability Strategy

To improve reliability:

* Structured JSON generation is enforced.
* Validation checks are performed on every output.
* Automatic repairs are applied when required.
* Runtime simulation verifies execution readiness.

---

## Cost vs Quality Tradeoff

The initial design used multiple LLM stages:

Intent Extraction

↓

Architecture Design

↓

Schema Generation

To reduce latency and API cost, the architecture was optimized into a single compiler stage while preserving validation, repair, and execution checks.

This approach improves performance while maintaining output quality.

---

## Future Improvements

* Full Application Code Generation
* Real Database Deployment
* API Generation Framework
* Multi-Agent Architecture
* Advanced Runtime Validation
* Production Deployment Pipeline
