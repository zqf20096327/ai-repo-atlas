# chjm-ai/vococo

⭐ 42 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/chjm-ai/vococo) · 个人维护 · 中文 README

**基于 Claude 订阅的单用户常驻个人 AI 助理**

Python 实现的单用户、常驻进程、语音优先的个人 AI 助理，基于 Claude Agent SDK 运行，依赖 Claude Pro/Max 订阅令牌或任意 Anthropic 兼容第三方端点。功能覆盖 TUI/CLI/Web（自建 PWA）多渠道共用主会话、按住说话与 Omni 实时语音通话、语音派活/cron 定时任务后台引擎、Agent 分层委托、基于 Markdown 的长期记忆、DeepSeek/Kimi 等多供应商热切换、三档安全闸与手机审批、业务文件隔离沙箱。平台以 macOS/Linux 验证为主，Windows 未测；常驻脚本假设 macOS+zsh。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TUI/CLI/Web 多渠道共享同一主会话，Web 为自建 PWA
- 语音优先：按住说话 STT、TTS 朗读、Omni 实时免提通话
- 后台任务引擎统一承载语音派活、cron、独立会话，代码任务跑独立 git worktree
- 危险操作三档安全闸、手机审批、Bash 文件沙箱与业务目录隔离

## 适用场景

- 个人用 Claude 订阅搭建常驻私人助理，手机浏览器访问
- 语音通话中给助理派活，由后台任务引擎执行定时或长时任务
- 多个 Agent 分层委托处理项目任务，成果写入 iCloud 等仓库外目录

## 场景标签

`AI 助手` `语音 Agent` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5:  基于 Claude 订阅 的个人 AI 助理，单用户、常驻、语音优先、多渠道共用一个大脑。
> L25: - **语音优先** — 按住说话（STT）、TTS 朗读、Omni 实时免提通话（可打断）
> L170: **前置**:Python ≥ 3.11、uv、一份 Claude Pro/Max 订阅

## 星数曲线

```mermaid
xychart-beta
    title "chjm-ai/vococo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-27 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `f561f2c304e5` · [字段定义](../../DATASET.md)*
