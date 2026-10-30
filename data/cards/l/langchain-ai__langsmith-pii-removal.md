# langchain-ai/langsmith-pii-removal

⭐ 15 · Jupyter Notebook · 推送 2026-04-21 · [GitHub](https://github.com/langchain-ai/langsmith-pii-removal) · 组织维护

**LangSmith 追踪中脱敏 PII 的示例演示仓库**

由 LangChain 团队维护的演示仓库，展示多种防止敏感信息与个人身份信息（PII）进入 LangSmith 追踪日志的方法：环境变量整体隐藏输入输出、LangSmith 客户端匿名化器（regex 掩码 email/IP/电话/信用卡/SSN/日期）、LangGraph 工作流集成，以及 LangChain PIIMiddleware 的 redact/mask/hash/block 四种策略。多数方法可在不使用 LangChain 的情况下直接配合 OpenAI SDK 运行。需要 Python 3.11+ 与 OpenAI API key，LangSmith API key 可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LangSmith create_anonymizer 自动掩码 email/IP/电话/信用卡/SSN/日期
- 无需 LangChain 即可配合标准 OpenAI SDK 使用
- LangChain PIIMiddleware 支持 redact/mask/hash/block 四种策略
- 提供非 LangChain notebook 与 LangGraph/LangChain 三个示例工程

## 适用场景

- 让 LangSmith 追踪日志不落敏感用户数据
- 在已有 LangChain/LangGraph agent 中加入 PII 检测与处理
- 比较多种 PII 脱敏方案选择适合自己的接入方式

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: A comprehensive demonstration of how to prevent logging of sensitive data and personally identifiable information (P
> L66: ### 2. LangSmith Client with Anonymizer (Recommended)
> L167: |**LangSmith Anonymizer**|✅ **Recommended for most cases** - Works with any OpenAI client, no LangChain needed|`op

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/langsmith-pii-removal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `6645511f58d6` · [字段定义](../../DATASET.md)*
