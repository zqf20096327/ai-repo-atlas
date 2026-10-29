# openscilab/tocount

⭐ 23 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/openscilab/tocount) · 组织维护

**轻量级 token 数估算库：多种规则与 ML 策略估计文本 token 数**

Python 库 ToCount，用规则与机器学习两类方法估算文本的 token 数，为不同估算策略提供统一接口，适用于提示词分析与 token 预算管理。内置 RULE_BASED、TIKTOKEN（R50K/CL100K/O200K）、DEEPSEEK_R1、QWEN_QWQ、LLAMA_3_1 等系列模型，各附 R²/MAE 等评估指标；训练与测试数据取自 Lmsys-chat-1m 与 WildChat 数据集。通过 PyPI 以 pip 安装，也支持源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一接口支持规则与 ML 两类估算策略
- 覆盖 Tiktoken/DeepSeek R1/Qwen QwQ/Llama 3.1 等多个模型系列的估算器
- 各模型附 R²/MAE/RMSE 等评估指标
- 训练测试数据来自 Lmsys-chat-1m 与 WildChat

## 适用场景

- 在调用 LLM 前估算提示词 token 数以做预算控制
- 对比不同 tokenizer 下的 token 消耗
- token 计费或截断策略的开发与测试

## 场景标签

 · 领域:NLP/LLM 工具

## 证据(README 行号)

> L12: ToCount is a lightweight and extensible Python library for estimating token counts from text inputs using both rule
> L96: ℹ️ The training and testing dataset is taken from Lmsys-chat-1m [1] and Wildchat [2].
> L101: >>> from tocount import estimate_text_tokens, TextEstimator

## 星数曲线

```mermaid
xychart-beta
    title "openscilab/tocount 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2046e8df1472` · [字段定义](../../DATASET.md)*
