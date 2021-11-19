import openai

"""
set up gpt-3 API connection
"""


def setup(key="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"):
    openai.api_key = key


"""
get gpt-3 to continue a prompt
"""


def get_response(prompt, engine="davinci", temp=0.7, max_tok=64, top_p=1, freq_pen=0, pres_pen=0,
                 return_whole_obj=False, echo_prompt=True):
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=max_tok,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen
    )
    if return_whole_obj is True:
        return response
    else:
        if echo_prompt is True:
            return str(prompt + response["choices"][0]["text"])
        else:
            return response["choices"][0]["text"]


"""
get gpt-3 davinci-codex to continue produce python code
"""


def codex_response(prompt, temp=0.7, max_tok=64, top_p=1, freq_pen=0, pres_pen=0,
                   return_whole_obj=False, echo_prompt=True):
    prompt = str("\"\"\"\n" + prompt + "\n\"\"\"")
    response = get_response(prompt, engine="davinci-codex", temp=temp, max_tok=max_tok,
                 top_p=top_p, freq_pen=freq_pen, pres_pen=pres_pen,
                 return_whole_obj=return_whole_obj, echo_prompt=echo_prompt)
    return response
