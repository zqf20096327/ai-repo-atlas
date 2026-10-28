# ruslanlap/PowerToysRun-QuickAi

⭐ 21 · C# · MIT · 推送 2026-10-20 · [GitHub](https://github.com/ruslanlap/PowerToysRun-QuickAi) · [官网](https://ruslanlap.github.io/ruslanlap_buymeacoffe/) · 个人维护

**Windows PowerToys Run 的 AI 问答插件：快捷键即时获取多供应商 AI 回答**

以 C#/.NET 9.0 WPF 编写的 PowerToys Run 插件，用户按 Alt+Space 输入 `ai <问题>` 即可从多家 AI 供应商获得流式回答，无需切换到浏览器。支持 Groq、Together、Fireworks、OpenRouter、Cohere、Google、Ollama（本地）等供应商，v1.4.1 新增 Anthropic、xAI、智谱等 13 个预设。提供专用结果窗口、Markdown 渲染、自定义系统提示、剪贴板文本/图像附件、快捷命令（/explain、/translate 等）与双 API Key 回退。安装方式为下载 x64/ARM64 发行包解压至 PowerToys 插件目录，仅支持 Windows 10/11。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多供应商支持含 Ollama 本地离线运行
- 流式 token 输出与 Markdown 结果窗口
- 剪贴板图像附件用于视觉模型，剪贴板文本自动读取
- 内置与自定义快捷命令（/read、/explain、/translate 等）

## 适用场景

- 在 Windows 工作流中快捷键即时提问 AI，省去切换浏览器
- 通过 Ollama 在本机离线运行模型，零 API 费用
- 读取剪贴板截图文字或对剪贴板代码做解释/修复

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L82: **QuickAI** brings the power of multiple AI providers directly into PowerToys Run. Get instant, streaming responses
> L167: - 🏠 **Local AI Support**: Run AI models completely offline on your own machine with **zero API costs**

## 星数曲线

```mermaid
xychart-beta
    title "ruslanlap/PowerToysRun-QuickAi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f126a61ce10a` · [字段定义](../../DATASET.md)*
