# mp-web3/jarvis-v3

⭐ 35 · Python · 推送 2026-03-24 · [GitHub](https://github.com/mp-web3/jarvis-v3) · 个人维护

**Apple Silicon 本地语音界面：用说话方式操作 Claude Code**

面向 Apple Silicon Mac 的全本地语音交互工具：麦克风输入经 Parakeet TDT 0.6B 转写、Qwen 1.5B 润色后注入运行 Claude Code 的 tmux 窗格，待回复完成后由 Kokoro 82M 朗读输出。采用 4 状态 VAD 状态机、SmartTurn ML 断句预测、说话人验证 VAD 与智能打断机制，全部推理经 MLX 跑在 Metal 上，语音链路无需云端 API 与联网。tmux 注入方式使其兼容任意 CLI 工具。已知限制：打断功能需戴耳机，打断后的文本片段处理尚不完善。

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

- 全本地语音链路：Parakeet STT + Kokoro TTS，MLX/Metal 推理，无需云端语音 API
- SmartTurn ML 断句预测替代固定静音计时器
- Qwen 1.5B 转写润色：去填充词、修复语法、去重
- tmux 注入机制兼容任意 CLI 工具，不限于 Claude Code

## 适用场景

- 在终端用语音与 Claude Code 对话并听回复
- 不依赖云端 API 的本地语音交互
- 通过打断机制随时插话控制语音输出

## 场景标签

`语音 Agent` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: Fully local voice interface for Claude Code on Apple Silicon. Talk to Claude through your terminal, no cloud APIs fo
> L5: Mic → Parakeet TDT 0.6B (STT) → Qwen 1.5B (transcript polish) → tmux injection → Claude Code → Kokoro 82M (TTS) → sp
> L24: All inference runs on Metal via MLX. No cloud APIs, no internet required for speech.

## 星数曲线

```mermaid
xychart-beta
    title "mp-web3/jarvis-v3 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-30 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `13d5f2b5c004` · [字段定义](../../DATASET.md)*
