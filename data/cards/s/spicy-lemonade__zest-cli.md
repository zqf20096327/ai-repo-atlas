# spicy-lemonade/zest-cli

⭐ 27 · Python · 推送 2026-10-10 · [GitHub](https://github.com/spicy-lemonade/zest-cli) · [官网](http://www.zestcli.com) · 组织维护

**本地离线小模型驱动的自然语言转 CLI 命令工具（macOS）**

面向 macOS 用户的命令行助手：输入自然语言（涉及文件管理、网络、Docker、Git、系统等场景），由本地运行的微调小语言模型翻译为 shell 命令。模型为 Qwen3.5-9B（SFT 约 7.4 万条真实样本后 DPO 对齐），量化为 Q5_K_M GGUF（约 6.6GB），内嵌 llama.cpp 推理引擎，通过 Metal 使用 Mac 内置 GPU（自动回退 CPU）。推理完全离线、无 API key、无遥测；训练流程另使用 GCS/Colab。README 提示对单一请求效果更好，仅在 zestcli.com 提供更多信息，未在本 README 中给出安装命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言翻译为 shell 命令，覆盖文件/网络/Docker/Git/系统等场景
- Qwen3.5-9B 经 SFT+DPO 微调，量化为 Q5_K_M GGUF（约 6.6GB）
- 内嵌 llama.cpp 引擎，Metal GPU 加速并自动 CPU 回退，无需额外安装
- 推理完全离线，无云依赖、无 API key、零遥测

## 适用场景

- 不记得具体命令语法时用自然语言生成 shell 命令
- 在无网络或注重隐私的环境下做本地命令行操作
- 快速执行 Docker、Git、磁盘检查等常见终端任务

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: Zest CLI translates natural language into shell commands using a local small language model. MacOS only. Learn more 
> L31: Zest CLI runs a single model, Qwen3.5-9B, fine-tuned for natural language to CLI translation with supervised fine-t

## 星数曲线

```mermaid
xychart-beta
    title "spicy-lemonade/zest-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `4c2d48f881a2` · [字段定义](../../DATASET.md)*
