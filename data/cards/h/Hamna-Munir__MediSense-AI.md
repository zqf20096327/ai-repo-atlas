# Hamna-Munir/MediSense-AI

⭐ 24 · HTML · 推送 2026-05-16 · [GitHub](https://github.com/Hamna-Munir/MediSense-AI) · [官网](https://medisenseai27.netlify.app/) · 个人维护

**面向基层卫生员的浏览器 AI 症状分诊工具（单一 HTML 文件）**

MediSense AI 是一个单文件 HTML 应用，供社区卫生工作者（CHW）在浏览器中完成健康分诊：通过 14 个快捷症状标签、自由文本与严重度滑块采集信息，调用 Groq API 上的 LLaMA 3.3 70B 输出 LOW/MODERATE/HIGH/EMERGENCY 四级紧急度及处理建议，支持追问对话。运行需自行填入 Groq API key，可本地打开或部署到 Netlify，另附 Kaggle/Jupyter 演示笔记本。声明非医疗器械、不存储患者数据、目前仅英文，离线模式与多语言为规划项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 HTML 文件零安装，任意浏览器可运行
- LLaMA 3.3 70B 经 Groq API 输出四级分诊与严格 JSON 结构
- 提示词采用保守升级偏置与明确分级定义
- 无状态运行，不存储患者数据

## 适用场景

- 社区卫生工作者现场快速判断症状紧急程度
- 缺乏诊所资源地区初步判断是否需前往医院
- 围绕患者症状进行追问式对话咨询

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L37: |🤖 **AI Triage**|LLaMA 3.3 70B assigns urgency: LOW / MODERATE / HIGH / EMERGENCY|
> L64: |**Inference**|Groq API|~750 tokens/sec, sub-3s latency|

## 星数曲线

```mermaid
xychart-beta
    title "Hamna-Munir/MediSense-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `89871fa8c711` · [字段定义](../../DATASET.md)*
