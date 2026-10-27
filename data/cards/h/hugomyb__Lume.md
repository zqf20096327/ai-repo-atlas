# hugomyb/Lume

⭐ 22 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/hugomyb/Lume) · [官网](https://uselume.dev) · 个人维护

**带内联 AI 的本地优先开源终端模拟器，可用手机远程控制**

用 Rust + Tauri 2 + SolidJS + xterm.js 编写的终端模拟器，功能包括命令块（命令+输出为可导航块）、分屏、工作区（YAML 可分享）、富历史记录（本地 JSONL）、SSH 管理器、自动补全与文件树。内联 AI 可解释命令块或从自然语言生成命令，支持本地 Claude/Codex CLI 或任意 OpenAI 兼容 API（含 Ollama）。支持手机经 LAN 或隧道远程控制，端到端加密；完全本地、无账户无遥测。提供 Linux/macOS/Windows 三平台安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 命令块（OSC 133）隔离展示命令与输出，含退出码徽章
- 内联 AI：解释命令块或自然语言生成命令，多 provider 可选（Claude/Codex CLI、OpenAI 兼容 API、Ollama）
- 手机远程控制终端，单次 QR 配对、可逐个撤销、端到端加密
- 几 MB 原生二进制，完全本地、无账户无遥测

## 适用场景

- 用带命令块和分屏的终端做日常开发
- 在手机上远程接管电脑里的终端会话
- 让 AI 解释报错输出或直接生成要执行的命令

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L9: An **open-source terminal emulator** with command blocks, inline AI and split
> L49: - **Inline AI** — explain a block or generate a command from natural language,

## 星数曲线

```mermaid
xychart-beta
    title "hugomyb/Lume 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `95a88b683b90` · [字段定义](../../DATASET.md)*
