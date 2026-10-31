# cnvipstar/codex-model-switch

⭐ 14 · Shell · MIT · 推送 2026-06-18 · [GitHub](https://github.com/cnvipstar/codex-model-switch) · 个人维护 · 中文 README

**OpenAI Codex 本地/云端模型切换脚本，免手改 config.toml**

Bash 脚本，用于在 OpenAI Codex CLI/App 的本地模型（Ollama 或任意 OpenAI 兼容端点）与原生云端模型之间切换：通过交互菜单或 local/native/status 子命令，仅重写 config.toml 顶层的 model、model_provider、oss_provider 三个键，其余配置不动；每次切换执行原子写入并生成带时间戳备份，切换前检查本地端点与模型是否就绪。面向已安装 Codex 且搭配本地推理服务的开发者，需 macOS/Linux 与 bash/python3/curl；切换后需重启 Codex 生效。

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

- 交互菜单列出本地与云端已装模型，也提供 local/native/status 子命令供脚本化调用
- 仅重写 model/model_provider/oss_provider 三个顶层键，原子写入并自动备份
- 预检本地端点与所选模型可用性
- 通过环境变量支持 LM Studio 等自定义 OpenAI 兼容端点

## 适用场景

- 让 Codex CLI/App 在本地 Ollama 模型与云端模型间一键切换
- 避免手改 config.toml 造成 model 与 provider 不匹配的 404 错误
- 自动化脚本中用子命令批量切换 Codex 模型配置

## 场景标签

 · 领域:开发者工具/LLM 配置管理

## 证据(README 行号)

> L3: > One command to toggle the **OpenAI Codex** CLI/App between a **local model** (Ollama / any OpenAI‑compatible provi
> L14: The Codex desktop App's model picker only lists the models on your **cloud** account — local Ollama models never ap
> L62: - A local provider for local mode — e.g. Ollama with at least one model pulled (`ollama pull gpt-oss:20b`)

## 星数曲线

```mermaid
xychart-beta
    title "cnvipstar/codex-model-switch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `126a91256100` · [字段定义](../../DATASET.md)*
