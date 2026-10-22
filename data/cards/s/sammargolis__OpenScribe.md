# sammargolis/OpenScribe

⭐ 222 · TypeScript · MIT · 推送 2026-10-04 · [GitHub](https://github.com/sammargolis/OpenScribe) · [官网](https://openscribe.org) · 个人维护

**开源 AI 医疗病历助手：录音问诊并自动生成结构化病历**

面向临床医生的开源 AI 病历记录工具：录制患者接诊音频，经 Whisper 转写后由 LLM（默认 Anthropic Claude）生成结构化病历草稿，支持 Default/SOAP/自定义 markdown 模板。默认混合 Web 模式为本地 Whisper 转写 + 云端 Claude 生成；另有完全本地桌面路径（Whisper + Ollama 本地模型）。数据本地优先存储（AES-GCM 加密 localStorage），无遥测。README 明确声明尚未满足 HIPAA 合规，需用户自行完成合规清单；所有 AI 病历为需人工审核的草稿。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 录音→Whisper 转写→LLM 生成结构化病历（Default/SOAP/自定义模板）
- 三种运行模式：混合 Web（默认）、完全本地桌面（Whisper+Ollama）、云端回退
- 本地优先存储：AES-GCM 加密 localStorage，无遥测/云同步
- 桌面端提供 macOS/Windows/Linux 安装包，含首运行设置向导

## 适用场景

- 医生接诊时录音并自动生成病历草稿
- 在本地运行完整转写与生成流程以保护患者隐私
- 按科室自定义病历模板结构

## 场景标签

 · 领域:医疗信息化/临床文档

## 证据(README 行号)

> L21: OpenScribe is a free, MIT-licensed, open-source AI medical scribe that helps clinicians record patient encounters, 
> L318: - **Transcription (default web path)**: local Whisper server (`whisper.cpp` via `pywhispercpp`, model `tiny.en`)
> L322: - **Note Core**: Structured clinical note generation and validation

## 星数曲线

```mermaid
xychart-beta
    title "sammargolis/OpenScribe 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 218 --> 222
    line [219, 220, 221]
```

2026-10-18 219 → 2026-10-22 221（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `102043fa5311` · [字段定义](../../DATASET.md)*
