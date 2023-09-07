import json
from typing import Any


# List of the input files to evaluate
inputs_paths = [
    "rules_engine/input1.json",
    "rules_engine/input2.json",
    "rules_engine/input3.json",
    "rules_engine/bonus/input4.json",
    "rules_engine/bonus/input5.json",
]


def extract_rule_data(file_path: str) -> dict:
    """Catches the input json file to extract the rule from it.

    Args:
        file_path (str): the path of the file to use

    Returns:
        rule (dict): the rule that has been extracted
    """
    with open(file_path, "r") as input_file:
        rule_data = json.load(input_file)

    return rule_data


def evaluate_rule(rule: Any, context: dict = None) -> Any:
    """Recurcively decomposes a rule to evaluate its result.

    Args:
        rule (Any): rule or subrule to evaluate
        context (dict, optional): context of the rule. Defaults to None.

    Raises:
        ValueError: raised if the rule / subrule isn't recongnised

    Returns:
        Any: return value. Could be any type.
    """
    if isinstance(rule, (bool, int, str)):
        return rule
    elif isinstance(rule, dict):
        if "and" in rule:
            # return true if all subrules are true
            return all(evaluate_rule(subrule, context) for subrule in rule["and"])
        elif "var" in rule:
            # eval() is used to convert a point separated path like
            # path.to.goal in json path [path][to][goal] to use it on context
            return eval("context['" + "']['".join(rule["var"][0].split(".")) + "']")
        elif "increment" in rule:
            # same as var rule with an increment
            return 1 + eval(
                "context['" + "']['".join(rule["increment"][0].split(".")) + "']"
            )
        elif "equals" in rule:
            # works if there are only two values to compare
            return evaluate_rule(rule["equals"][0], context) == evaluate_rule(
                rule["equals"][1], context
            )
        elif "lower_than" in rule:
            # works if there are only two values to compare
            return evaluate_rule(rule["lower_than"][0], context) < evaluate_rule(
                rule["lower_than"][1], context
            )
        elif "prop" in rule:
            # prop can't search for a subrule, context don't contain them
            return context[rule["prop"][0]]
        elif "filter" in rule:
            # filter rule compare each item in a list of items
            return [
                item
                for item in evaluate_rule(rule["filter"][0], context)
                if evaluate_rule(rule["filter"][1], item)
            ]
        elif "if" in rule:
            # if first rule true, function returns second statement, else third
            if evaluate_rule(rule["if"][0], context):
                return evaluate_rule(rule["if"][1], context)
            return evaluate_rule(rule["if"][2])
    else:
        raise ValueError("Invalid rule")


def main():
    """Main function, this the only function that should be called"""
    for input in inputs_paths:
        rule_data = extract_rule_data(input)
        result = evaluate_rule(
            rule_data["input"]["rule"], rule_data["input"]["context"]
        )

        print(f"Path : {input}")
        print(f"Résultat : {result}")
        # Compare the found output with the wanted output. Should be true
        print(f"Correspondance : {result == rule_data['output']}\n")


main()
