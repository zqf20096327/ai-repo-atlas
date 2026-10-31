# anslwy/openduck

⭐ 14 · Svelte · MIT · 推送 2026-05-16 · [GitHub](https://github.com/anslwy/openduck) · 个人维护 · 中文 README

**macOS 实时语音对话应用：8 语言聊天+字幕+屏幕感知**

基于 Rust/Tauri/Svelte 的原生 macOS 应用，将 OpenAI 兼容模型转为实时语音对话：支持随时打断、实时转录与双语字幕、8 种语言（英/日/中/西/法/印/意/葡，由 Kokoro 与 Whisper Large V3 驱动）。支持截屏区域让 AI 查看屏幕内容，可挂载 Live2D Cubism 模型（含表情映射）并通过 .openduck 文件分享角色。模型来源为内置 MLX 优化模型或连接 Ollama、LM Studio 及 OpenAI 兼容端点。要求 Apple Silicon（M1 及以上），以 dmg 发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 8 语言实时语音对话，支持随时打断，亚秒级响应
- 实时转录与字幕，Whisper Large V3 + Kokoro
- 屏幕感知视觉：快捷键截取区域供 AI 查看
- 内置 MLX 模型或连接 Ollama/LM Studio/OpenAI 兼容端点

## 适用场景

- 在 Mac 上与本地或远端模型进行免手操作的语音对话
- 跨语言对话时查看实时字幕与翻译
- 让 AI 查看屏幕指定区域辅助当前任务

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L5: Turn any OpenAI-compatible model into a real-time voice chat app in 8 languages (English, Japanese, Mandarin Chinese
> L38: - **Flexible Model Support**: Built-in MLX-optimized models or connect to Ollama, LM Studio, and OpenAI-compatible 

## 星数曲线

```mermaid
xychart-beta
    title "anslwy/openduck 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `7a0e4e097c69` · [字段定义](../../DATASET.md)*
