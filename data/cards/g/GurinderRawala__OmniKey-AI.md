# GurinderRawala/OmniKey-AI

⭐ 15 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/GurinderRawala/OmniKey-AI) · [官网](https://omnikeyai.ca) · 个人维护

**选中文本快捷键触发 AI 改写的桌面效率工具（macOS/Windows）**

面向 macOS（菜单栏）与 Windows（系统托盘）的桌面应用加 CLI：在任意应用中选中文本后按快捷键，调用 LLM 原地改写，覆盖提示词增强（⌘E）、语法清理（⌘G）与自定义任务（⌘T）。可配置 OpenAI、Anthropic、Google Gemini 或 OpenAI 兼容开源模型作为后端，支持 Web 搜索、认证浏览器会话、MCP 服务器接入与 Telegram 远程控制；@omniAgent 前缀可交给可执行 shell 命令、读取浏览器标签页的自主 agent。CLI 经 Homebrew 或 npm 安装，桌面应用需另行下载，MIT 许可。

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

- 任意应用内选中文本快捷键触发 AI 原地改写
- 多 LLM 后端：OpenAI/Anthropic/Gemini/OpenAI 兼容开源模型
- @omniAgent 自主 agent：shell 命令、读取已登录浏览器标签页、MCP 工具
- Telegram 远程运行任务与定时任务调度

## 适用场景

- 写作时随手修正语法或增强提示词，无需切换窗口
- 把常用文本处理流程存为自定义任务一键执行
- 通过 Telegram 在其他设备上发起并跟踪 AI 任务

## 场景标签

`AI 写作` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5:  Select text anywhere. Press a shortcut. AI rewrites it in place.
> L59: - **Multiple LLM providers** — switch between OpenAI, Anthropic, Google Gemini, and OpenAI-compatible open models d

## 星数曲线

```mermaid
xychart-beta
    title "GurinderRawala/OmniKey-AI 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-22 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `bd0627d264b3` · [字段定义](../../DATASET.md)*
