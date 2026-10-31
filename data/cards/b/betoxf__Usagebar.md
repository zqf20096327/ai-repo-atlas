# betoxf/Usagebar

⭐ 14 · Swift · MIT · 推送 2026-10-29 · [GitHub](https://github.com/betoxf/Usagebar) · [官网](https://bullfighterstudio.com/usagebar) · 个人维护

**macOS 菜单栏应用：显示 Claude/Codex/Cursor 等 AI 编程工具的用量限额**

原生 Swift 编写的 macOS 菜单栏应用，面向使用多个 AI 编程工具的开发者：在一个状态图标中显示 Claude Code、Codex、Cursor、Kimi Code、z.ai 与 Grok 的 5 小时滚动窗口与每周额度百分比及重置时间。通过本地复用各提供商 CLI 已保存的凭据（Keychain、auth.json 等）直接向提供商 API 请求用量，无需账号、无遥测、无中间后端；默认每 2 分钟刷新，休眠时暂停轮询。要求 macOS 14+，提供 Homebrew cask 安装与源码构建，发布产物未公证。

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

- 一个状态项追踪 6 家提供商（Claude/Codex/Cursor/Kimi Code/z.ai/Grok）的用量限额
- 本地凭据自动发现，复用各 CLI 已有登录，无需粘贴 API key
- 无账号、无遥测、无中间后端，用量数据直连各提供商
- 浏览器会话凭据以 AES-256-GCM 加密存储于本地

## 适用场景

- 开发中随时查看 Claude Code/Codex 的 5 小时窗口与每周额度还剩多少
- 多 AI 工具订阅用户在一处对比各家用量与重置时间
- 根据焦点应用自动切换菜单栏显示的提供商

## 场景标签

 · 领域:开发者工具/桌面应用

## 证据(README 行号)

> L140: Usagebar is a local status-bar client. It discovers credentials already stored by provider tools, requests usage d
> L26: Usage limits matter most while you are working. Usagebar keeps your Claude Code, Codex, and Cursor limits (the curr

## 星数曲线

```mermaid
xychart-beta
    title "betoxf/Usagebar 星数(近 3 点)"
    x-axis ["2026-10-26", "2026-10-30", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-26 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `47383b33605f` · [字段定义](../../DATASET.md)*
