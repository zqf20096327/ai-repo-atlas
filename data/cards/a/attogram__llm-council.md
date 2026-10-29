# attogram/llm-council

⭐ 24 · Shell · MIT · 推送 2026-07-06 · [GitHub](https://github.com/attogram/llm-council) · 个人维护

**单文件 Bash 脚本：让本地 Ollama 上的多个模型互相群聊**

面向 Ollama 用户的群聊脚本：通过单个 Bash 脚本（要求 Bash ≥3.2）启动聊天室，把本地全部或指定模型拉入轮转对话——每轮随机排序各模型依次发言，超时（默认 30 秒）截断回复，用户可选择是否插入发言。支持命令行设置话题、指定模型、调整超时、时间戳与折行等参数；聊天记录与规则写入 ./logs 目录。属 Attogram Project 系列工具之一，无编译安装，直接运行脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单个 Bash 脚本实现，无编译依赖，要求 Bash ≥3.2
- 多模型轮转群聊机制：随机排序、逐个发言、超时截断
- 可选用户参与发言或纯旁观模式（-nouser）
- 日志落盘到 ./logs（rules.txt 与 messages.txt）

## 适用场景

- 观察多个本地模型围绕同一话题的对话与观点差异
- 对比不同小模型在自由聊天中的表现
- 以话题文件或管道输入发起多模型讨论

## 场景标签

`聊天机器人` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: Start a chat room between all, or some, of your models running on Ollama.
> L63: - Run the council with all available Ollama models,

## 星数曲线

```mermaid
xychart-beta
    title "attogram/llm-council 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `31f7fe5eef63` · [字段定义](../../DATASET.md)*
