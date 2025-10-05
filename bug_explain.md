# Bug Report: SQL Conflict

**Date:** 2025-10-05

## Bug Title

SQL Conflict

## Context

Migrating from SQLite to PostgreSQL

## Symptom

Migration failed, version mismatch error

## Cause

Error entering PostgreSQL identity data

## Fix

A new DB was created and configured for PostgreSQL.

## Lesson

Always check the version difference between db edits.
