# Saganaki22/FireRedTTS3-ComfyUI

⭐ 23 · Python · MIT · 推送 2026-08-18 · [GitHub](https://github.com/Saganaki22/FireRedTTS3-ComfyUI) · 个人维护 · 中文 README

**ComfyUI 节点包：本地运行 FireRedTTS3 语音克隆、语音设计与编辑**

面向 ComfyUI 用户的 FireRedTTS3 推理节点包，提供零样本语音克隆（24 种语言+21 种中文方言）、自然语言语音设计、语义与声学语音编辑、Whisper 参考音频转写四个功能节点。Qwen3 主干、DiT 流头、RedAE 编解码器等在 ComfyUI 进程内原生运行，无外部服务与远程代码。提供 fp32/bf16/INT8 三种权重档位与 AIMDO DynamicVRAM 支持；instruct 变体的设计与编辑功能对语言支持有限（中文/英文为主），INT8 为实验性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零样本语音克隆覆盖 24 语言+21 中文方言（base 模型）
- 进程内原生推理，无外部服务与远程代码
- bf16/INT8 权重镜像，检查点 7.90 GiB 降至 3.07 GiB（INT8，实验性）
- Whisper 参考转写节点辅助提升克隆效果

## 适用场景

- 在 ComfyUI 工作流中用参考音频克隆声音合成语音
- 用文字描述生成定制音色
- 对已有语音做变速、变调、改词等编辑
- 显存受限时用 bf16/INT8 权重运行模型

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L9: ComfyUI nodes for FireRedTeam/FireRedTTS3: zero-shot voice cloning across 24 languages and 21 Chinese dialects, inst
> L20: - **Native in-process inference** - The Qwen3 backbone, PatchEncoder, DiT flow head, RedAE codec, and CAM++ speaker
> L31: - **INT8 ConvRot weights (experimental)** - the `FireRedTTS3-int8` mirror ships the core transformer linears pre-qu

## 星数曲线

```mermaid
xychart-beta
    title "Saganaki22/FireRedTTS3-ComfyUI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `647667ff884d` · [字段定义](../../DATASET.md)*
