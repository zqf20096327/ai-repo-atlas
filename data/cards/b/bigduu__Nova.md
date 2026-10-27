# bigduu/Nova

⭐ 22 · Rust · MIT · 推送 2026-10-16 · [GitHub](https://github.com/bigduu/Nova) · [官网](https://bodhi-ai.vercel.app) · 个人维护 · 中文 README

**让 MCP agent 控制真实 macOS/Windows 桌面的 Rust MCP 服务器**

单个 Rust 二进制的 computer-use MCP 服务器，无 Python 运行时，向 Claude Desktop、Cursor、Codex、Claude Code 等 MCP 客户端提供屏幕截图、原生 OCR（Apple Vision / Windows OCR）、鼠标键盘输入（含中日韩与 emoji 全 Unicode 文本）、剪贴板、窗口/应用控制及 Accessibility/UIA 操作。支持 stdio 与 HTTP 传输，macOS 上可由 Nova.app（开发预览版）托管权限。限制：Linux 不支持桌面控制（仅无头协议检查）；Windows 二进制未做 Authenticode 签名；batch_actions 上限 64 步。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 截图像素空间与屏幕坐标映射，先读取（AX/UIA/OCR）再点击
- 全 Unicode 键盘输入，支持中日韩与 emoji
- AX 优先的 ax_read/ax_activate 与 64 步 batch_actions 结构化失败报告
- 可选 Chrome DevTools MCP sidecar，支持 URL 白名单与隔离浏览器配置

## 适用场景

- 让 Claude Desktop / Cursor 等 MCP 客户端操作我的真实桌面应用
- 通过截图与 OCR 让 agent 读取并点击界面元素
- 配合 Chrome DevTools sidecar 做浏览器页面自动化

## 场景标签

`GUI 自动化` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: **Let any MCP agent use your real Mac or Windows apps.** Nova is a single Rust
> L6: binary, with no Python runtime, that gives Claude Desktop, Cursor, Codex, Claude
> L7: Code and other MCP clients screenshots, native OCR, keyboard and mouse input,

## 星数曲线

```mermaid
xychart-beta
    title "bigduu/Nova 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `cffd785522a9` · [字段定义](../../DATASET.md)*
