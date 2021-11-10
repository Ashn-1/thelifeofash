
import logging
import argparse
import datetime
import os
import re


def create_daily():
    current_day = 0
    day_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}-day-(\d+)")
    for entry in os.listdir("_posts/daily"):
        match = day_pattern.search(entry)
        if match:
            match = int(match[1])
            if current_day < match:
                current_day = match

    now = datetime.datetime.now()
    draft_path = f"_posts/daily/{now.strftime('%Y-%m-%d')}-day-{current_day + 1}.md"
    draft_content = f"""---
layout: post-daily
title: 'Day {current_day + 1}: *'
author: Ash
categories: daily
tags: [default, personal]
worktime: 0
date: {now.strftime('%Y-%m-%d %H:%M %z')}
---
    """

    with open(draft_path, "w") as file:
        file.write(draft_content)


if __name__ == "__main__":
    logging.basicConfig(format="[%(asctime)s] [%(levelname)8s] --- %(message)s", level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("category", help="Specifies the category for which the post is created")
    args = parser.parse_args()

    if args.category == "daily":
        create_daily()
