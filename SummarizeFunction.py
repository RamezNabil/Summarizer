from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config, AutoTokenizer, AutoModelWithLMHead
import torch


def Summarize(document):
    model = T5ForConditionalGeneration.from_pretrained('t5-small')
    tokenizer = T5Tokenizer.from_pretrained('t5-small')
    device = torch.device('cpu')
    preprocess_text = document.strip().replace("\n", " ")
    t5_prepared_Text = "summarize: " + preprocess_text
    tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt", max_length=5000, truncation=True).to(
        device)
    summary_ids = model.generate(tokenized_text,
                                 num_beams=2,
                                 no_repeat_ngram_size=2,
                                 min_length=10,
                                 max_length=100,
                                 early_stopping=False)

    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return output