# leemiracle/dsh-android

⭐ 5 · Kotlin · MIT · 推送 2026-11-05 · [GitHub](https://github.com/leemiracle/dsh-android) · 个人维护 · 中文 README

**把 DeepSeek Agent 运行环境装进 Android 手机的第三方封装**

基于 DeepSeek Harness（dsh）的第三方 Android 封装，将 Node.js 桌面/服务器端的 Agent 运行环境打包为单个 APK：内嵌 Termux Node.js 24 运行时与完整 dsh 依赖树、Termux bootstrap rootfs（bash/apt/python）。界面为对话、终端、浏览器三面板结构，agent 可通过 browser-use 语义工具操控 WebView 页面并支持人工接管。免 Root、免 Termux，安装即用；模型请求由用户自行配置的提供方处理（默认局域网 vLLM，可填 OpenAI 兼容 key）。当前仅发布 arm64 包，出网依赖宿主机 adb 隧道。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- APK 内嵌 Termux Node.js 24.22.1 与完整 dsh npm 依赖树，安装即用无需 Root
- 对话/终端/浏览器三面板，agent 驱动与用户所见同一界面
- browser-use 工具面：web_open/web_dom/web_click 等含截图视觉与人工接管
- skillnet 技能商店与按 SkillX 三层格式固化的经验蒸馏

## 适用场景

- 在手机上直接运行 DeepSeek Harness 的对话与多面板 Agent 环境
- 让 agent 代为打开网页、读取 DOM、点击输入完成浏览器操作
- 在移动设备上用内置终端执行 bash/apt 命令与工具链任务

## 场景标签

`AI 助手` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7:  DeepSeek Harness 的 Android 本体。免 Root、免 Termux，一个 APK 装进完整的 Agent 运行环境——对话、终端、浏览器三面一体。
> L41: dsh-android 是基于 DeepSeek Harness（dsh）的第三方 Android 封装，把原本运行在 Node.js 桌面/服务器端的 AI Agent 运行环境完整「搬」进手机：
> L51: 模型请求仍由你配置的提供方处理（默认预置局域网 vLLM `qwen3.5-35b`，也可在设置里填 DeepSeek 官方 key）。

## 星数曲线

```mermaid
xychart-beta
    title "leemiracle/dsh-android 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-16", "2026-11-28"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-11-08 4 → 2026-11-28 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `bd2d37aca69e` · [字段定义](../../DATASET.md)*
