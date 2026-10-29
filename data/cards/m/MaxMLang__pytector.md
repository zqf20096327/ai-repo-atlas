# MaxMLang/pytector

⭐ 45 · Python · Apache-2.0 · 推送 2026-08-10 · [GitHub](https://github.com/MaxMLang/pytector) · [官网](https://pytector.readthedocs.io/en/latest/) · 个人维护

**LLM 提示注入检测与输入净化 Python 库**

面向 LLM 应用的提示注入防护 Python 包：基于 transformers 的本地检测模型（DeBERTa/DistilBERT/ONNX/GGUF），也可接入 Groq 托管的 safeguard 模型做内容安全判定。提供六策略输入净化、PII 检测（27 类实体）、毒性分类、正则扫描、金丝雀令牌、关键词阻断，以及框架无关的 ToolOutputGuard/WebPageScanner 用于间接注入防护，并支持 LangChain LCEL 护栏 Runnable 组合进链。README 明确声明不提供 100% 防护，建议与其他安全层叠加使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 transformers 模型与 Groq API 双通道注入检测
- ToolOutputGuard/WebPageScanner 屏蔽工具与网页返回内容中的间接注入
- 六策略输入净化管线（编码检测/unicode 归一化/正则/模糊匹配等）
- LangChain LCEL 护栏 Runnable（PytectorGuard/PytectorToolGuard）

## 适用场景

- LLM 应用上线前阻断提示注入攻击
- Agent 系统中筛查网页/工具返回的间接注入内容
- 对用户输入做净化与 PII 检测后再交给模型

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L38: - **LangChain Guardrail Runnable**: Adds `PytectorGuard` for LCEL pipelines (`guard | prompt | llm`) so unsafe prom
> L39: - **Tool & Web Output Screening**: Adds `ToolOutputGuard`, a framework-agnostic guard for *indirect* prompt injecti
> L86: **Important**: Always combine multiple security layers appropriate for your use case and risk profile.

## 星数曲线

```mermaid
xychart-beta
    title "MaxMLang/pytector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-29 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cb40cc6e29aa` · [字段定义](../../DATASET.md)*
