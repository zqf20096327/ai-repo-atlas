# Saganaki22/Moss_TTS-ComfyUI

⭐ 31 · Python · 推送 2026-06-28 · [GitHub](https://github.com/Saganaki22/Moss_TTS-ComfyUI) · [官网](https://github.com/OpenMOSS/MOSS-TTS) · 个人维护 · 中文 README

**MOSS-TTS v1.5 的 ComfyUI 节点包：本地 48kHz 立体声语音生成与克隆**

为 MOSS-TTS-Local-Transformer-v1.5（48kHz 立体声本地 Transformer TTS 模型）提供的 ComfyUI 自定义节点包，面向 ComfyUI 工作流用户。包含模型加载、免参考音频直接生成、零样本语音克隆（无需参考转录文本）、基于前缀音频+转录的语音续写、可选 Whisper 转录辅助节点，支持 31 种语言、中英混合、拼音/IPA 发音标注、时长控制。小体积配置文件内置于节点目录，大模型文件存放于 ComfyUI/models/mosstts/ 并可按需下载；提供 dtype 与 attention 后端选择及 AIMDO 动态显存集成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零样本语音克隆，本地 v1.5 路径无需参考转录文本
- 语音续写（前缀音频+转录）与可选 Whisper 转录辅助节点
- 31 种语言标签、内联停顿标记、拼音/IPA 发音控制
- dtype（auto/bf16/fp16）与 attention（auto/sdpa/flash_attention/eager）选择，AIMDO 动态显存集成

## 适用场景

- 在 ComfyUI 工作流中直接生成 48kHz 立体声语音
- 用自己拥有的参考音频做零样本音色克隆
- 从已有音频前缀续写或补全一句话
- 多语言与中英混合（code-switching）语音合成

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L43:  a 48 kHz stereo local Transformer TTS model with direct generation, zero-shot voice cloning,
> L148: |`MOSS-TTS Voice Clone`|Zero-shot voice cloning from a ComfyUI `AUDIO` reference. No reference transcript is requi

## 星数曲线

```mermaid
xychart-beta
    title "Saganaki22/Moss_TTS-ComfyUI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 29 --> 32
    line [30, 31]
```

2026-10-18 30 → 2026-10-31 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `fea358cdcd37` · [字段定义](../../DATASET.md)*
