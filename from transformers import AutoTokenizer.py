from transformers import AutoTokenizer
from transformers import pipeline as PP
from huggingface_hub import login
import torch

login(token="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")
model = "meta-llama/Llama-2-7b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = PP(
    "text-generation",
    model=model,
    torch_dtype=torch.float32,
    device_map="auto"
)

def generate_text(prompt):
    sequences = pipeline(
    prompt,
    do_sample=True,
    top_k=50,
    top_p=0.95,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    )
    aboba=sequences[0]['generated_text']
    print(aboba)

prompt = """The increase in the credit rating of Ural Steel Joint Stock Company (hereinafter referred to as Ural Steel, the Company) is caused by an improvement in the quality assessment of liquidity in connection with the refinancing of a short—term bank loan through the issuance of a bond loan with repayment in 2025. Also, the revision of strategic plans for the implementation of a number of investment projects contributed to the improvement of the indicator "capital expenditures to revenue". An improvement in the price situation on the global pig iron market ensured the launch of blast furnace No. 3, which was previously in reserve, which will have an additional positive impact on the Company's cash flow in 2023. The Company's credit rating is determined by the average market position, business profile and level of corporate governance, as well as the average rating for the size of the business. The indicators of profitability, liquidity, debt burden, debt service and cash flow received high marks. Ural Steel is one of Russia's largest producers of commercial cast iron, bridge steel and steel for the production of large diameter pipes (LDP). At the beginning of 2022, Zagorsky Pipe Plant Joint Stock Company (ACRA rating — rating, Stable outlook; hereinafter — ZTZ) acquired 100% of the Company's authorized capital from METALLOINVEST HC JSC ( ACRA rating is a rating, the forecast is "Stable" ). Key assessment factors The average assessment of the market position is determined by the assessment of the market positions of Ural Steel for the main types of products (mostostal, strips and cast iron), weighted taking into account their share in the consolidated revenue of the Company. The average assessment of the Company's business profile is determined by: a low assessment of the degree of vertical integration, which is absent in the Company because it is not provided with its own coal and iron ore raw materials; an average assessment for the share of products with high added value, which takes into account steel for LDPE and mostostal as high-tech products; the average rating for the characterization and diversification of sales markets, since the sales markets of the main products of Ural Steel are characterized by moderate cyclicity and saturation, and the Company's product portfolio is moderately diversified. The average estimate of geographical diversification is a consequence of the presence of exports of cast iron, rolled steel and billets, the share of which forms up to 50% of the Company's consolidated revenue. On the one hand, this leads to a high assessment of the subfactor "accessibility and diversification of sales markets", and on the other hand, a very low assessment of the subfactor "concentration at one plant". The average level of corporate governance is due to the transparent structure of the business and the successful implementation of the Company's strategy of growth and expansion of the product portfolio. The Company's top management is represented by experts with extensive experience in the industry. Ural Steel applies certain elements of the risk management system (for example, hedging currency risk in certain cases), but unified documents on strategy and risk management, as well as on dividend policy have not yet been approved. The Board of Directors and key committees have not yet been formed. The business structure is simple. The Company prepares financial statements in accordance with IFRS. The high assessment of the Company's financial risk profile is due to: a high assessment for profitability (the return on FFO before interest and taxes for 2022 was 12% and the ACRE is expected to be about 18% in 2023); a high assessment for debt servicing (the ratio of FFO to net interest payments to interest payments was 24.7x according to the results of 2022 and the ACRE is projected at about 11.7x in 2023); a high assessment for the debt burden (the ratio of total debt, taking into account the guarantee on the debt of ZTZ to FFO to net interest payments is expected to be an ACRE on at the level of 2.5x (0.8x excluding sureties) according to the results of 2023); an average estimate of the size of the business (the absolute value of the annual FFO before net interest payments and taxes is less than 30 billion rubles). High assessment of the level of liquidity. In December 2022, the Company refinanced short-term bank debt at the expense of a longer-term bond loan with repayment in 2025. ACRA has improved the qualitative assessment of the Company's liquidity due to a more comfortable repayment schedule, as well as the availability of internal sources of liquidity in the form of cash and the expected positive free cash flow (FCF) by the results of 2023. High cash flow estimation. As a result of the revision of strategic plans for the implementation of a number of investment projects, the Company's capital expenditures were changed downwards, which had a positive impact on the "capital expenditures to revenue" indicator and thereby improved the overall assessment of the "cash flow" factor. Key assumptions capital expenditures in accordance with the business plan; no dividend payments in the forecast period. Factors of a possible change in the forecast or rating "Stable" the forecast assumes with a high degree of probability that the rating will remain unchanged for 12-18 months. A positive rating action can lead to: reduction of the ratio of total debt, taking into account the guarantee on the ZTZ debt to FFO, to net interest payments below 1.0x, combined with an improvement in the qualitative assessment of the debt burden to high and an increase in the absolute value of FFO to net interest payments and taxes above 30 billion rubles per year. Negative rating action may result in: an increase in the ratio of total debt, taking into account the guarantee on the ZTZ debt to FFO, to net interest payments above 2.0x; a decrease in the profitability of FFO before interest and taxes below 15%; a decrease in the profitability of FCF below 5%, including due to the payment of dividends. Rating components Assessment of own creditworthiness (USC): a. Adjustments: None. Issue ratings Justification of the credit rating. The issue is the senior unsecured debt of Ural Steel. Due to the lack of structural and contractual subordination of the issue, ACRA evaluates these bonds as equal in order of execution to other existing and future unsecured and unsubordinated obligations of the Company. In accordance with the ACRA methodology, the Agency used a detailed approach to determine the issue rating. According to ACRA calculations, the level of compensation for senior unsecured debt belongs to category I, and therefore the credit rating of the issue is equated to the credit rating of the Company —rating. Non-documentary interest-bearing non—convertible exchange—traded bonds of Ural Steel Joint Stock Company with centralized accounting of rights, placed by open subscription, series BO—001P-01 (RU000A105Q63), maturity date - 12/25/2025, issue volume - 10 billion rubles, -rating. Regulatory Disclosure The credit ratings of Ural Steel Joint Stock Company and the bond issue of Ural Steel Joint Stock Company (RU000A105Q63) were assigned on a national scale for the Russian Federation based on the Methodology for Assigning credit ratings to non-financial Companies on a national Scale for the Russian Federation and the Basic Concepts used by the Analytical Credit Rating Agency in rating activities. When assigning a credit rating to the specified bond issue , the Methodology for Assigning credit Ratings to Financial Instruments according to the National Scale for the Russian Federation was also used . For the first time, the credit rating of Ural Steel Joint Stock Company was published by ACRA on 12/14/2022, the credit rating of the bond issue (RU000A105Q63) — on 12/29/2022. The next revision of the credit rating and forecast for the credit rating of Ural Steel Joint Stock Company, as well as the credit rating of the bond issue of Ural Steel Joint Stock Company (RU000A105Q63) is expected within one year from the date of publication of this press release. Credit ratings were assigned based on data provided by Ural Steel Joint Stock Company, information from open sources, as well as ACRA databases. Credit ratings were assigned based on the statements of Ural Steel Joint Stock Company under IFRS and RAS. Credit ratings are requested, Ural Steel Joint Stock Company participated in the process of assigning credit ratings. When assigning credit ratings, information was used, the quality and reliability of which, in the opinion of ACRA, are appropriate and sufficient for the application of methodologies. ACRA did not provide additional services to Ural Steel Joint Stock Company. No conflicts of interest have been identified within the credit rating assignment process."
Write out all the key sentences from the text below highlight them as bulleted list, completely  writing them in their original form without applying formatting and don't rephrase it at all."""
generate_text(prompt)
