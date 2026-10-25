# giusmarci/openwhisp

⭐ 152 · TypeScript · 推送 2026-04-11 · [GitHub](https://github.com/giusmarci/openwhisp) · 个人维护

**macOS 本地语音转文字听写工具：按住 Fn 说话即转写润色粘贴**

面向 macOS 用户的本地语音听写 Electron 应用：按住 Fn 说话、松开后由 Whisper 本地转写，再经 Ollama 运行的本地 LLM（默认 gemma4:e4b）润色，自动粘贴到当前应用的文本框；无文本框时复制到剪贴板。提供 Conversation/Vibe Coding 两种风格与四级润色档位，支持意图解析（取最终说法）。需 macOS，安装 Ollama 并拉取约 9.6GB 模型，源码运行需 npm 构建并编译 Swift 辅助程序。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按 Fn 说话→Whisper 转写→本地 LLM 润色→自动粘贴的完整管线
- 全程本地运行，数据不离开 Mac
- Conversation / Vibe Coding 两种风格与四级润色档位
- 支持 Ollama 兼容模型切换与首启动设置向导

## 适用场景

- 在邮件、聊天、编辑器里用语音输入并自动润色粘贴
- 开发者用口语描述自动生成工程化表述（Vibe Coding 模式）
- 需要离线、数据不出本机的语音听写

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L13: 3. **Release Fn** — Whisper transcribes your speech, a local LLM polishes the text, and the result is pasted into w
> L15: The entire pipeline runs locally via Whisper (speech-to-text) and Ollama (text enhancement).

## 星数曲线

```mermaid
xychart-beta
    title "giusmarci/openwhisp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 151 --> 153
    line [152, 152]
```

2026-10-18 152 → 2026-10-25 152（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `e8caa710cc04` · [字段定义](../../DATASET.md)*
