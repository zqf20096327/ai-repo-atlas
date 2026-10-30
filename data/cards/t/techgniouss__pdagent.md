# techgniouss/pdagent

⭐ 15 · HTML · MIT · 推送 2026-10-19 · [GitHub](https://github.com/techgniouss/pdagent) · [官网](https://pypi.org/project/pocket-desk-agent/) · 个人维护 · 中文 README

**自托管的 Telegram 机器人：远程控制 Windows PC，可选 Gemini AI**

运行在 Windows PC 上的本地进程，通过 Telegram 出站长轮询接收指令，实现文件浏览（沙箱限定目录）、截屏、快捷键、剪贴板、OCR 文本点击（Tesseract）与元素检测（OpenCV）、宏录制、任务调度、React Native APK 构建，以及经 cloudflared 隧道的浏览器实时远程桌面。零 AI 配置即可运行；添加 Google Gemini 凭据后解锁多轮对话与 agentic 计算机操作（破坏性操作需 Telegram 按钮确认）。macOS/Linux 仅支持文件、AI 聊天与调度功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 出站长轮询连接 Telegram，无需开放入站端口或路由器配置
- OCR 点击、元素检测、宏录制与宏回放的 UI 自动化
- 浏览器实时远程桌面（cloudflared 隧道自动安装）
- 可选 Gemini agentic 计算机操作，破坏性操作需人工确认

## 适用场景

- 出差时用手机远程操作家中或办公 PC，无需配置端口转发
- 远程触发构建、取回 APK、驱动 Claude Desktop 或 VS Code
- 用截屏+OCR+宏自动化无 API 的桌面操作

## 场景标签

`GUI 自动化` `聊天机器人` · 领域:效率与自动化

## 证据(README 行号)

> L35: Out of the box, with zero AI setup:
> L44: Add **Google Gemini** credentials to unlock:
> L72: - **AI Chat & Computer Use**: Google Gemini with multi-turn conversation, image analysis, and full agentic tool-cal

## 星数曲线

```mermaid
xychart-beta
    title "techgniouss/pdagent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ccfb935be03d` · [字段定义](../../DATASET.md)*
