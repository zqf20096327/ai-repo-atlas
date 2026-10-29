# mthamil107/prompt-shield

⭐ 18 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/mthamil107/prompt-shield) · [官网](https://mthamil107.github.io/prompt-shield/) · 个人维护

**面向 LLM 应用的提示注入防火墙：35 个输入检测器+9 个输出扫描器**

Python 库，为 LLM 应用提供提示注入防护：35 个输入检测器（10 语言、7 种编码混淆、Smith-Waterman 序列对齐、多轮话题漂移等）、9 个输出扫描器（毒性、PII、幻觉/接地、schema 校验等），辅以 DeBERTa 语义分类器、NFKC+同形字规范化管线、滑窗限流与 Prometheus 指标。提供 OpenAI/Anthropic 包装器、LangChain/LlamaIndex/CrewAI/Haystack 等框架集成、Docker REST API、GitHub Action 与 MCP 服务器；v0.7.0 增加 ToolResultGuard 扫描工具返回内容，检测器默认 flag 不拦截。附 ed25519 签名的联邦威胁情报源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 35 个输入检测器覆盖 10 语言、7 种编码混淆方案
- 9 个输出扫描器（PII/毒性/幻觉接地/schema 校验等）
- ToolResultGuard 扫描工具返回内容中的注入（默认 flag 模式）
- 提供 9 个数据集 10,700+ 样本评测与对比基准

## 适用场景

- 在 LLM 应用入口拦截提示注入与越狱攻击
- 扫描 agent 工具返回内容中的间接注入
- CI 中用 GitHub Action 扫描 PR 的注入与 PII
- 通过 MCP 服务器为 Claude Desktop/Cursor 提供防护

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L29: The most comprehensive open-source prompt injection firewall for LLM applications. Combines **35 input detectors** 
> L182: |**OpenAI / Anthropic**|Drop-in client wrappers (block or monitor mode)|
> L207: ## Tool-Result Injection Defense (v0.7.0)

## 星数曲线

```mermaid
xychart-beta
    title "mthamil107/prompt-shield 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-29 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `73da87d60137` · [字段定义](../../DATASET.md)*
