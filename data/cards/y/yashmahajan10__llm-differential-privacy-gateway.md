# yashmahajan10/llm-differential-privacy-gateway

⭐ 28 · Python · Apache-2.0 · 推送 2026-08-02 · [GitHub](https://github.com/yashmahajan10/llm-differential-privacy-gateway) · 个人维护

**差分隐私网关：让不可信 LLM agent 安全查询敏感数据**

以 MCP 服务器形式运行的差分隐私数据查询网关：LLM 将自然语言编译为受限 AST 查询，可信的 DP 引擎在预算账本下执行并注入拉普拉斯噪声返回答案，隐私保证不依赖模型可信度。内置三类攻击演示（差分、成员推断、重识别再识别），结果在 CI 中回归测试，噪声机制与 OpenDP 交叉核对至 1e-9。支持 Claude Desktop 接入（无需 API key），另提供 Docker 本地单租户 NL 界面。HTTP/Streamlit 界面仅限本地演示，身份头可伪造。

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

- Laplace 机制 + 混合 zCDP 预算记账（(ε, δ)-DP 保证）
- 三种隐私攻击可运行演示并在 CI 中回归锁定
- 噪声机制与 OpenDP 参考实现在 35 项检查中一致至 1e-9
- 以 MCP stdio 服务器接入 Claude Desktop，agent 端不可信

## 适用场景

- 让 Claude 等 agent 查询敏感数据集而不泄露个体记录
- 验证差分隐私机制对差分/成员推断/重识别攻击的防御
- 在本地演示自然语言到 DP 查询的完整流程

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L18: - **Built for AI agents.** Runs as an MCP server for Claude Desktop. The connecting agent is untrusted by design, a
> L39: The gateway runs as an MCP stdio server for Claude Desktop. The agent becomes the untrusted query author, and it ge
> L23: The interesting part isn't that an LLM can write queries. It's that **the privacy guarantee does not depend on the 

## 星数曲线

```mermaid
xychart-beta
    title "yashmahajan10/llm-differential-privacy-gateway 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `4ce0460f612c` · [字段定义](../../DATASET.md)*
