# PatchedReality/ai-cli-switchboard

⭐ 15 · Shell · Apache-2.0 · 推送 2026-07-07 · [GitHub](https://github.com/PatchedReality/ai-cli-switchboard) · 个人维护

**让 Claude Code / Codex CLI 作为前端接入任意云端或本地 LLM 的框架**

面向 Apple Silicon macOS 用户的框架：通过 LiteLLM 代理（端口 18080）、MLX 或 LM Studio，把 Claude Code 或 Codex CLI 连接到云端模型（Z.AI、Gemini、DeepSeek、OpenRouter）或本地模型，支持 20+ 模型配置。提供四类 runner（local_mlx/local_lmstudio/remote_litellm/remote_zai）、YAML 配置与元数据驱动的别名自动生成、统一的启停脚本。限制：本地 MLX 路径要求 Apple Silicon，需安装 Python 3.10+、Claude Code 与 LiteLLM。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四类 runner：本地 MLX/LM Studio 与远程 LiteLLM/Z.AI 直连
- setup.sh 一键安装依赖，别名由配置元数据自动生成
- 支持 20+ 模型配置，YAML 模板可自行扩展新模型
- 统一的服务启停管理与 .env 自动加载 API key

## 适用场景

- 在 Claude Code / Codex CLI 中使用 DeepSeek、Gemini 等非官方模型
- 在 Apple Silicon Mac 上本地跑 MLX/LM Studio 模型接入 CLI 编码工具
- 按配置文件快速切换不同模型并自动生成对应命令别名

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: A simple framework for using Claude Code or Codex CLI as the frontend to any cloud or local LLM on Apple Silicon. Co
> L131: - **Engine**: LiteLLM proxy for API model abstraction
> L182: - **Proxy**: LiteLLM on port 18080 (for remote_litellm runner type)

## 星数曲线

```mermaid
xychart-beta
    title "PatchedReality/ai-cli-switchboard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `25f39be017b6` · [字段定义](../../DATASET.md)*
