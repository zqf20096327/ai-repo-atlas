# zhaolianghz/clawbox

⭐ 17 · Rust · MIT · 推送 2026-10-14 · [GitHub](https://github.com/zhaolianghz/clawbox) · [官网](https://clawbox.51topai.xyz) · 个人维护 · 中文 README

**AI 编码代理的统一配置中心桌面应用**

基于 Tauri v2（Rust + Svelte 5）的桌面应用（macOS/Windows/Linux），为 Claude Code、Codex、Hermes、OpenCode、Kimi 等 13 种 AI CLI 代理提供统一管理面板：配置 OpenAI/Anthropic 兼容 provider（内置 78 个）、可视化编辑 MCP server、统一技能库与 MEMORY.md 注入，一次配置同步到所有代理。含配置漂移检测与恢复机制，Hermes 代理支持 provider 回退链。macOS 提供 dmg 下载，也可从源码构建（需 Node.js ≥ 18、Rust ≥ 1.77）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一管理 provider、MCP、skills 与 memory，一键同步到多个代理
- 内置 78 个 OpenAI/Anthropic 兼容 provider，双端点配置
- 配置漂移以自然语言呈现，提供 Restore / Keep current 一键处理
- Hermes 支持 provider 有序回退链（无需网关）

## 适用场景

- 同时使用多个 AI 编码代理时避免逐个改配置文件
- 集中管理 API key 与 MCP server 并同步到各代理
- 接管手工配置过的代理（Adopt from agent）

## 场景标签

 · 领域:开发者工具/AI 基础设施

## 证据(README 行号)

> L3:  Unified configuration center for AI agents
> L14: ClawBox is a desktop app (macOS · Windows · Linux) that gives you a single control panel for all your AI coding age
> L32: |**Providers**|Add API keys and endpoints for any OpenAI- or Anthropic-compatible provider (78 built-in, dual-endpo

## 星数曲线

```mermaid
xychart-beta
    title "zhaolianghz/clawbox 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-29 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `7cabaf63c408` · [字段定义](../../DATASET.md)*
