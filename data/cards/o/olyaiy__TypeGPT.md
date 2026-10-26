# olyaiy/TypeGPT

⭐ 149 · Python · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/olyaiy/TypeGPT) · [官网](https://discord.gg/Vfxeb2U2Ay) · 个人维护

**在系统任意文本框通过快捷键调用 LLM 的桌面工具**

Python 编写的桌面应用：通过键盘监听与快捷键，在任何应用（聊天、文档、代码编辑器）的文本输入框中调用 ChatGPT、Gemini、Claude 或经 Ollama 本地运行的 Llama3，回复直接输入到当前文本框。支持图片粘贴、截图视觉查询（/see）、剪贴板集成与 O1 模型。提供 Tkinter GUI 管理器用于 API key 配置与启停。需 Python 3.x 与 Tkinter，macOS 需授予辅助功能权限，Windows/Linux/macOS 均需管理员权限用于键盘监听。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 任意文本输入框全局调用多模型（ChatGPT/Gemini/Claude/Llama3/O1）
- 截图与剪贴板图片的多模态查询（/see 命令）
- Tkinter GUI 管理器管理 API key 与程序状态
- Llama3 通过本地 Ollama 实例推理

## 适用场景

- 在写作或聊天应用中不切换窗口直接调用 AI 补全/回答
- 用截图向多模态模型发起视觉提问
- 本地通过 Ollama 运行 Llama3 完成查询

## 场景标签

`AI 助手` `多模态` · 领域:对话与助手

## 证据(README 行号)

> L5: TypeGPT is a Python application that allows you to invoke various AI's and LLM's from any text field in your operati
> L11: - **Global Accessibility**: Invoke AI models from any text input field across your system.

## 星数曲线

```mermaid
xychart-beta
    title "olyaiy/TypeGPT 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-10-26"]
    y-axis "stars" 148 --> 150
    line [149, 149]
```

2026-10-22 149 → 2026-10-26 149（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `b3264dec10ad` · [字段定义](../../DATASET.md)*
