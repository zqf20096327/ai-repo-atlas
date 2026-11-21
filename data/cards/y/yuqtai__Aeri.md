# yuqtai/Aeri

⭐ 3 · Rust · MIT · 推送 2026-11-18 · [GitHub](https://github.com/yuqtai/Aeri) · 个人维护 · 中文 README

**Windows 免手语音助手：说 Hey Aeri 即执行操作**

Rust 编写的 Windows 桌面语音助手：唤醒词本地检测，识别后执行打开应用、重命名文件、改设置、设提醒等本地操作，并主动语音播报提醒与后台任务完成。语言模型通过设置页接入（OpenAI key 或其他 provider），语音识别本地离线运行，回复用 Windows 语音朗读。插件用英文短文描述即可组合内置能力，另有 13 个现成插件一键安装。下载约 27 MB，空闲内存约 60 MB，MIT 开源，无遥测。

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

- 唤醒词本地检测，未唤醒前音频不出本机
- 插件以纯英文描述组合内置能力，无需代码与重启
- 13 个现成插件一键安装，带插件市场
- 单个 Rust 进程，27 MB 下载，空闲约 60 MB 内存

## 适用场景

- 双手占用时用语音操作电脑
- 语音设置提醒并由助手准时播报
- 用英文插件把常用操作流程串成一句话
- 配合本地 Ollama 模型完全离线运行

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L18: Say "Hey Aeri" and what you need. It opens apps, renames files, changes settings and sets reminders. No clicks, no 
> L26: Open source (MIT). Bring any AI model, or run it fully offline with Ollama. The wake word is detected on your PC, a
> L77: Prefer another provider? Aeri also works with Anthropic, Google Gemini, OpenRouter, Groq, DeepSeek, a local Ollama 

## 星数曲线

```mermaid
xychart-beta
    title "yuqtai/Aeri 星数(近 2 点)"
    x-axis ["2026-11-15", "2026-11-21"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-15 3 → 2026-11-21 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `bd659283b99c` · [字段定义](../../DATASET.md)*
