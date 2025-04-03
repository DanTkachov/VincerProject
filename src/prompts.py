def make_prompt(convo_text):
    '''Makes a prompt. Injects the conversation text in the middle for Claude to analyze.'''
    return f"""
    You are an AI system designed to analyze conversations and predict the probability of various psychological stressors appearing in the dialog. Your task is to examine the given conversation and estimate the likelihood of each of the following stressors being present:

    1. Role Ambiguity
    2. Role Conflict
    3. Role Overload
    4. Interpersonal Conflict
    5. Perceived Lack of Control

    Here is the conversation text you need to analyze:

    <conversation>
    {convo_text}
    </conversation>

    Carefully read through the conversation and look for indicators of each stressor. Consider the context, language used, and any explicit or implicit mentions of issues related to these stressors.

    The beginning of your response will have the 5 stressors and the probability of each stressor appearing in the dialogue. The format of the first 5 lines will be as follows:
    <stressor name>:<percentage>
    [Repeat the above structure for each of the five stressors]

    Your message should ONLY have 5 lines: one for each stressor and its probability.
    End each line with a '\n' delimiter.

    Ensure that your probability estimates are based solely on the content of the given conversation. Do not make assumptions beyond what is explicitly stated or strongly implied in the text. If there is insufficient information to make a confident estimate for any stressor, you may indicate this by providing a lower probability estimate.
    """