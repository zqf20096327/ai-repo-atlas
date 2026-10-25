# gatsby-sec/llm-sec-range

⭐ 36 · Python · MIT · 推送 2026-06-20 · [GitHub](https://github.com/gatsby-sec/llm-sec-range) · 组织维护 · 中文 README

**本地大模型攻防渗透测试靶场：提示注入CTF/OWASP/脆弱Agent**

单体 Flask Web 系统的大模型安全训练平台，整合 AIGoat、ai-prompt-ctf 等靶场玩法，提供四大模块：8 关提示注入 CTF、OWASP LLM Top 10 labs（2025 版）、带 SQL 注入/路径穿越/越权转账/命令执行漏洞的 ReAct 银行客服 Agent 靶场、以及外部靶场仓库聚合清单。目标模型可切换：DeepSeek 直连（需 API Key）、OpenRouter 中转多款小模型、本地 Ollama 离线。每轮对话附带 Prompt Inspector 展示完整 messages 与原始返回。提供脚本、Docker Compose、手动三种部署方式；Agent 危险操作可选 Docker 沙箱隔离。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Gandalf 式 8 关提示注入 CTF，防御逐级加固
- OWASP LLM Top 10（2025 版）每类风险一个可上手 lab
- 脆弱 ReAct Agent：SQL 注入/路径穿越/越权转账/命令执行四个夺旗目标
- Prompt Inspector 逐轮展示实际发送的完整 messages 与模型原始返回
- 目标模型可切换：DeepSeek 直连 / OpenRouter 中转 / 本地 Ollama 离线

## 适用场景

- 安全工程师学习提示注入与 LLM 攻击面
- AI 安全教学与 CTF 出题
- 团队 LLM 应用安全意识培训
- 对比不同模型对同一攻击的鲁棒性差异

## 场景标签

`网络安全` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L13: `LLM SecRange` 是一个**单体 Flask Web 系统**，把社区里优秀的大模型攻防靶场（AIGoat、damn-vulnerable-llm-agent、ai-prompt-ctf 等）的核心玩法，重新整合成一个
> L25: - **🖥️ 本地部署**：DeepSeek-R1 8B（Ollama，完全离线、数据不出本机）
> L62: ### 2. OWASP LLM Top 10 靶场（2025 版）

## 星数曲线

```mermaid
xychart-beta
    title "gatsby-sec/llm-sec-range 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 34 --> 37
    line [36, 35, 36]
```

2026-10-18 36 → 2026-10-25 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e04dc33b692c` · [字段定义](../../DATASET.md)*
