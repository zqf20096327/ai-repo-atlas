# borhen68/picoagents

⭐ 21 · Python · MIT · 推送 2026-03-02 · [GitHub](https://github.com/borhen68/picoagents) · 个人维护

**超轻量个人 AI 助手框架：熵路由工具调用+沙箱+双层记忆**

面向个人的 AI agent 框架：以 Shannon 熵与 TF-IDF 本地计算门控工具执行，支持最多 3 次连续工具调用、向量记忆与 MEMORY.md/HISTORY.md 双层记忆、工作区沙箱（正则拦截破坏性 shell 命令、限制文件越界）。可接入多家 LLM 提供商（OpenRouter/Anthropic/OpenAI/DeepSeek/Groq/Gemini 及任意 OpenAI 兼容端点含 vllm），原生支持 MCP 协议接入外部工具并对外暴露 stdio MCP server。提供 Telegram/Discord/Slack/WhatsApp/Email 网关、cron 与心跳任务、Docker 与 systemd 部署，安装方式为 git clone 后 pip install -e .，仅 2 个依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Shannon 熵 + TF-IDF 本地门控工具执行，高不确定性时请求澄清
- 双层记忆：向量召回 + MEMORY.md/HISTORY.md 持久文件
- 零信任工作区沙箱：默认 restrict_to_workspace，拦截破坏性命令
- 原生 MCP 双向支持：接入外部工具服务器，也可作为 stdio MCP server 暴露工具

## 适用场景

- 搭建接入 Telegram/Slack/Discord 等聊天平台的个人 AI 助手
- 在本地沙箱内运行带工具调用与记忆的自动化 agent
- 通过 cron/heartbeat 定时执行任务并回传结果到聊天渠道

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L8: **picoagent** is an ultra-lightweight personal AI assistant focused on mathematical tool-routing and safety.
> L43: **Mathematically Routed**: Uses Shannon Entropy to gate tool execution. If uncertainty is high, the agent asks for 

## 星数曲线

```mermaid
xychart-beta
    title "borhen68/picoagents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `3feb8f9edc12` · [字段定义](../../DATASET.md)*
