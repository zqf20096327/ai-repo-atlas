# NoPainNullGain/LocalEyes

⭐ 28 · Python · MIT · 推送 2026-07-07 · [GitHub](https://github.com/NoPainNullGain/LocalEyes) · 个人维护

**给 Claude Code 中的纯文本 LLM 接入本地视觉能力**

面向 Claude Code 用户的本地视觉桥接工具：文本模型（如 DeepSeek、CodeLlama、Qwen-Coder）自身无视觉能力，LocalEyes 通过脚本截取屏幕、读取剪贴板或图像文件，经 base64 编码后调用本地 Ollama 视觉模型（默认 qwen2.5vl:7b）生成文字描述，供原模型推理使用。全程本地运行，无云端上传与 API key。以 git clone + install.py 安装为 Claude Code 技能；Windows 10/11 已测试，macOS/Linux 未测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 截屏/剪贴板/图像文件三种输入，经本地 Ollama 视觉模型生成文字描述
- 支持 agentic 模式：模型可在工作流中自主调用截屏
- 可通过 config.json 与环境变量切换视觉模型与超时等参数
- 全程本地，无云端上传、无 API key

## 适用场景

- 让 DeepSeek 等无视觉模型在编程代理中查看截图与 UI 报错
- 调试或照 mockup 实现 UI 时代理自行截屏获取视觉上下文
- 隐私敏感环境下本地描述屏幕与图像内容

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: **Vision for text-only LLMs in Claude Code.** Many flagship models like DeepSeek, CodeLlama, Qwen-Coder, and many ot
> L100: 3. Sent to Ollama's local API at `localhost:11434`

## 星数曲线

```mermaid
xychart-beta
    title "NoPainNullGain/LocalEyes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `15f4e105b0ff` · [字段定义](../../DATASET.md)*
