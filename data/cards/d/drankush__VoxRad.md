# drankush/VoxRad

⭐ 35 · Python · GPL-3.0 · 推送 2026-02-28 · [GitHub](https://github.com/drankush/VoxRad) · [官网](https://voxrad.gitbook.io/voxrad) · 组织维护

**面向放射科医师的语音转录与报告结构化桌面应用**

VOXRAD 是供放射科医师及住院医师使用的语音转录应用：录制口述音频后，经语音转录模型转写，再由大语言模型按预定义指令模板（如 HRCT_Thorax.txt）与指南（BIRADS/TIRADS 等）重排为结构化报告，成品自动写入剪贴板。支持两种工作流：转录+LLM 重排，或多模态模型直接处理音频（实验性）。模型接入采用 OpenAI 兼容 Base URL/API Key，可用本地部署端点，API key 可加密存储。提供 macOS .app 与 Windows .exe。仓库已停止活跃开发，开发转向 VOXRAD2（计划 2026 年中发布）；声明为演示性应用，不用于诊断与临床用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语音转录 + LLM 指令模板重排生成结构化放射报告
- OpenAI 兼容 API 接入，支持本地部署模型端点
- API key 密码加密存储，报告自动写入剪贴板
- 多模态模型直接音频输入工作流（实验性）

## 适用场景

- 放射科医师口述后自动生成结构化影像报告并粘贴到 PACS 或文档
- 按检查类型（HRCT、CT 头颅等）套用自定义模板与指南
- 敏感数据场景下配合本地部署模型完成转录与重排

## 场景标签

`语音识别` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L21: VOXRAD is a voice transcription application for radiologists leveraging voice transcription and large language mode
> L25: This application leverages the power of generative AI to efficiently transcribe and format radiology reports from a
> L58: - Use a combination of using a transcription model to first transcribe audio and then format and restructure the tr

## 星数曲线

```mermaid
xychart-beta
    title "drankush/VoxRad 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-25 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0ca4fb7da8ec` · [字段定义](../../DATASET.md)*
