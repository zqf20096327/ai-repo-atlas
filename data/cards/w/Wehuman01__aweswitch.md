# Wehuman01/aweswitch

⭐ 28 · Python · MPL-2.0 · 推送 2026-09-19 · [GitHub](https://github.com/Wehuman01/aweswitch) · 个人维护 · 中文 README

**本地 CLI 启动器：切换 AI agent 的 API/模型配置档案**

Python CLI 工具，从 ~/.config/aweswitch/config.json 读取档案，提供两种模式：Launch 以隔离环境启动一次性 agent 会话（各自 API endpoint/token/model，多终端可并行不同档案）；Write 将档案写入 agent 自身配置作为持久默认（Claude settings.json、Codex config.toml、OpenCode/zcode 配置）。支持 Claude Code、Codex、OpenCode、zcode 四类档案及官方 OAuth 登录。附带 agent 技能，可通过自然语言管理档案；首次写入自动备份，v0.4 前旧配置自动迁移。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Launch 模式不触碰全局配置，多终端并行运行不同档案
- Write 模式写入 Claude/Codex/OpenCode/zcode 配置并自动备份
- 配套 agent 技能，用自然语言增删改查档案
- 检查命令对密钥做脱敏显示

## 适用场景

- 在多个 API 供应商与模型之间快速切换 coding agent 配置
- 不同终端并行运行不同档案的 agent 会话
- 让 agent 代为管理档案配置与默认模型

## 场景标签

 · 领域:AI 开发者工具

## 证据(README 行号)

> L28: - **Launch mode** (`aweswitch <profile>`) — starts a new agent session with isolated env. Each session gets its own
> L29: - **Write mode** (`aweswitch apply <profile>`) — makes a profile the agent's persistent default: Claude env into `~

## 星数曲线

```mermaid
xychart-beta
    title "Wehuman01/aweswitch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-29 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `23cc66602466` · [字段定义](../../DATASET.md)*
