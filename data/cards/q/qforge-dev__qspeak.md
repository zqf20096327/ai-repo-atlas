# qforge-dev/qspeak

⭐ 61 · TypeScript · MIT · 推送 2025-11-21 · [GitHub](https://github.com/qforge-dev/qspeak) · [官网](https://qspeak.app) · 组织维护

**本地离线的语音转文字与 AI 助手桌面工具**

基于 Tauri（Rust+React）构建的跨平台桌面应用：通过快捷键（默认 F6）在任意接受文本输入的应用中实时将语音转写为文字，内置 AI 助手与按上下文自适应的交流风格，支持 MCP server 集成扩展工作流。全部语音处理在本地设备完成，使用本地模型，语音数据不离开设备。安装包从官网下载，支持 Windows 11、macOS 10.15+、Ubuntu 22.04+，也可用 Node.js、pnpm、Rust 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 快捷键触发的实时语音转文字，适用于任意文本输入框
- 本地离线处理，语音数据不上传设备
- AI 助手与上下文自适应 personas
- MCP server 集成支持自定义工作流

## 适用场景

- 打字时用语音快速输入到 Slack、邮件或文档
- 不联网环境下做语音转文字
- 通过 MCP server 把语音助手接入自定义工作流

## 场景标签

`语音识别` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L24: - **Real-time Voice Transcription**: Convert your speech to text instantly in any application
> L25: - **AI Assistant**: Get instant help and answers without switching contexts

## 星数曲线

```mermaid
xychart-beta
    title "qforge-dev/qspeak 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-26 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `4b0f74633888` · [字段定义](../../DATASET.md)*
