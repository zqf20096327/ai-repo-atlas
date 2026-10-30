# ali-faraz-py/SentimentSense

⭐ 26 · Python · 推送 2026-07-25 · [GitHub](https://github.com/ali-faraz-py/SentimentSense) · [官网](https://sentiment-sense-ai.streamlit.app/) · 个人维护

**面向企业反馈的 ABSA 情感分析 Streamlit 仪表盘**

基于 Python 与 Streamlit 构建的 NLP 仪表盘，采用双模型流水线：DistilBERT 做情感分析，BART-Large-MNLI 做零样本主题分类，自动识别文本中的 Food、Service、Price 等业务类别，支持处理否定等复杂语言结构，面向企业反馈处理场景。通过 git clone 与 pip install -r requirements.txt 安装，streamlit run app.py 运行；部署于 Streamlit Community Cloud。需 Python 3.12+，依赖 PyTorch 与 Hugging Face Transformers。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DistilBERT（情感）+ BART-Large-MNLI（零样本主题）双模型流水线
- 无需人工标注自动抽取 Food/Service/Price 等方面类别
- 处理否定与复杂语言结构的上下文识别
- Streamlit 交互式仪表盘并附侧栏技术文档

## 适用场景

- 分析客户评价中不同业务方面的情感倾向
- 无需标注数据快速对反馈文本做主题分类
- 企业反馈处理的实时交互式分析

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L12: * **Dual-Model Pipeline:** Combines a DistilBERT transformer for sentiment with a BART-Large model for zero-shot to
> L13: * **Aspect-Based Analysis (ABSA):** Automatically identifies specific categories (Food, Service, Price, etc.) menti

## 星数曲线

```mermaid
xychart-beta
    title "ali-faraz-py/SentimentSense 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `4193a2d27285` · [字段定义](../../DATASET.md)*
