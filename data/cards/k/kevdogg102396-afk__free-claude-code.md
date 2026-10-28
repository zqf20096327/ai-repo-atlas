# kevdogg102396-afk/free-claude-code

⭐ 24 · Shell · MIT · 推送 2026-05-03 · [GitHub](https://github.com/kevdogg102396-afk/free-claude-code) · 个人维护

**免费 AI 编程 agent：用 NVIDIA 开源模型替换 Claude Code 后端**

Nemo Code 以 Claude Code CLI 为运行时依赖，通过本地 LiteLLM 代理把 Anthropic 风格请求转发到 NVIDIA NIM 托管的开源模型端点，把 Sonnet/Opus/Haiku 三个模型槽位映射到 Kimi、Qwen、MiniMax 等模型，提供一条命令安装（shell/PowerShell 脚本），支持 Docker 沙箱与本地两种运行模式，并附 Telegram 桥接实现手机访问。本地模式需 Node.js 18+ 与 Python 3.8+，需 NVIDIA API key；README 提示开源模型可能比 Claude 更易受提示注入攻击。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LiteLLM 代理将 Claude 模型槽位映射到 NVIDIA NIM 开源模型端点
- 一条命令安装，提供 Docker 沙箱与本地两种模式
- Docker 模式内置 Telegram 桥接（对话记忆、allowlist、/model 切换）
- NEMO_MODEL 环境变量可自选默认路由模型

## 适用场景

- 不付订阅费用开源模型驱动 Claude Code CLI 工作流
- 在 Docker 沙箱中运行全权限编程 agent 以降低风险
- 通过 Telegram 在手机上远程使用编码 agent

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L11: - Claude Code CLI as a runtime dependency
> L115: You -> Claude Code CLI -> LiteLLM proxy -> NVIDIA NIM -> open/free model
> L120: 3. LiteLLM maps Claude model IDs to NVIDIA NIM model IDs.

## 星数曲线

```mermaid
xychart-beta
    title "kevdogg102396-afk/free-claude-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `fa976f1e7bc9` · [字段定义](../../DATASET.md)*
